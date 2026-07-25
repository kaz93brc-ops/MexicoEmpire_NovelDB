from __future__ import annotations

import argparse
import ast
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.now().date().isoformat()
WIKI_RE = re.compile(r"(?<![!\\])\[\[([^\]\n]+?)\]\]")
FENCED_CODE_RE = re.compile(r"^```.*?^```", re.M | re.S)
REPLACEMENT_CHAR = "\ufffd"
CHAPTER_SUMMARY_REQUIRED_FIELDS = (
    "id",
    "type",
    "source_id",
    "chapter_number",
    "chapter_order",
    "chapter_title",
    "chapter_title_ja",
    "printed_pages",
    "capture_start",
    "capture_end",
    "coverage_status",
    "coverage_notes",
)
CHAPTER_SUMMARY_COVERAGE_STATUSES = {"complete", "partial", "not_started"}

AUDIT_DIR = ROOT / "08_Outputs" / "Audits"
INDEX_DIR = ROOT / "08_Outputs" / "Indexes"

CONTENT_DIRS = {
    "sources": ROOT / "01_Sources",
    "fact_cards": ROOT / "02_Fact_Cards",
    "entities": ROOT / "03_Entities",
    "events": ROOT / "04_Events",
    "timeline": ROOT / "05_Timeline",
    "scenes": ROOT / "06_Scenes",
    "questions": ROOT / "07_Questions",
}

ENTITY_FOLDERS = {
    "People": ROOT / "03_Entities" / "People",
    "Organizations": ROOT / "03_Entities" / "Organizations",
    "Places": ROOT / "03_Entities" / "Places",
    "Themes": ROOT / "03_Entities" / "Themes",
}


@dataclass
class Note:
    path: Path
    text: str
    frontmatter: dict[str, object]

    @property
    def stem(self) -> str:
        return self.path.stem

    @property
    def rel(self) -> str:
        return str(self.path.relative_to(ROOT)).replace("\\", "/")

    @property
    def title(self) -> str:
        for line in self.text.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        value = self.frontmatter.get("title") or self.frontmatter.get("canonical_name") or self.stem
        return str(value).strip('"')

    @property
    def type(self) -> str:
        return str(self.frontmatter.get("type", "")).strip('"')


def markdown_files(include_outputs: bool = False) -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if ".obsidian" in path.parts:
            continue
        if not include_outputs and "08_Outputs" in path.parts:
            continue
        files.append(path)
    return files


def split_frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[4:end], text[end + 4 :]


def parse_scalar(raw_value: str) -> object:
    value = raw_value.strip()
    if not value:
        return ""
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]") and not (value.startswith("[[") and value.endswith("]]")):
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            inner = value[1:-1].strip()
            if "," in inner:
                return [
                    str(parse_scalar(item.strip())).strip()
                    for item in inner.split(",")
                    if item.strip()
                ]
            return value
        if isinstance(parsed, (list, tuple)):
            return [str(item).strip().strip('"') for item in parsed if str(item).strip()]
    if (
        (value.startswith('"') and value.endswith('"'))
        or (value.startswith("'") and value.endswith("'"))
    ):
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
        return str(parsed)
    return value


def parse_frontmatter(text: str) -> dict[str, object]:
    parts = split_frontmatter(text)
    if parts is None:
        return {}
    lines = parts[0].splitlines()
    result: dict[str, object] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.startswith("  ") or ":" not in line:
            index += 1
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if raw_value:
            result[key] = parse_scalar(raw_value)
            index += 1
            continue
        values: list[str] = []
        probe = index + 1
        while probe < len(lines) and lines[probe].startswith("  "):
            stripped = lines[probe].strip()
            if stripped.startswith("- "):
                parsed = parse_scalar(stripped[2:])
                if isinstance(parsed, list):
                    values.extend(str(item) for item in parsed)
                elif str(parsed).strip():
                    values.append(str(parsed))
            probe += 1
        result[key] = values
        index = probe
    return result


def read_note(path: Path) -> Note:
    text = path.read_text(encoding="utf-8", errors="replace")
    return Note(path=path, text=text, frontmatter=parse_frontmatter(text))


def note_map(include_outputs: bool = False) -> dict[str, Note]:
    notes: dict[str, Note] = {}
    for path in markdown_files(include_outputs=include_outputs):
        if path.stem in notes and path.stem != "README":
            continue
        notes[path.stem] = read_note(path)
    return notes


def split_wiki_target(inner: str) -> str:
    target = inner.split("|", 1)[0].split("#", 1)[0].strip()
    return Path(target).name


def iter_wiki_matches(text: str) -> list[re.Match[str]]:
    matches: list[re.Match[str]] = []
    last = 0
    for fence in FENCED_CODE_RE.finditer(text):
        matches.extend(WIKI_RE.finditer(text, last, fence.start()))
        last = fence.end()
    matches.extend(WIKI_RE.finditer(text, last))
    return matches


def wiki_link(note: Note, alias: str | None = None) -> str:
    if alias and alias != note.stem:
        return f"[[{note.stem}|{alias}]]"
    title = note.title
    if title and title != note.stem:
        return f"[[{note.stem}|{title}]]"
    return f"[[{note.stem}]]"


def source_link(source_id: str, notes_by_stem: dict[str, Note]) -> str:
    if not source_id:
        return ""
    candidates = [source_id, source_id.replace("-", "_")]
    for candidate in candidates:
        if candidate in notes_by_stem:
            note = notes_by_stem[candidate]
            return wiki_link(note, alias=source_id)
    return f"`{source_id}`"


def path_category(path: Path) -> str:
    parts = set(path.relative_to(ROOT).parts)
    if "02_Fact_Cards" in parts:
        return "Fact Cards"
    if "05_Timeline" in parts:
        return "Timeline Entries"
    if "04_Events" in parts:
        return "Events"
    if "People" in parts:
        return "People"
    if "Organizations" in parts:
        return "Organizations"
    if "Places" in parts:
        return "Places"
    if "Themes" in parts:
        return "Themes"
    if "01_Sources" in parts:
        return "Source Notes"
    if "06_Scenes" in parts:
        return "Scenes"
    if "07_Questions" in parts:
        return "Questions"
    return "Other Notes"


def collect_backlinks(notes: dict[str, Note]) -> dict[str, list[Path]]:
    backlinks: dict[str, list[Path]] = defaultdict(list)
    for note in notes.values():
        for match in iter_wiki_matches(note.text):
            target = split_wiki_target(match.group(1))
            if target:
                backlinks[target].append(note.path)
    return backlinks


def collect_outlinks(text: str) -> set[str]:
    return {split_wiki_target(match.group(1)) for match in iter_wiki_matches(text) if split_wiki_target(match.group(1))}


def is_generated_stub(note: Note) -> bool:
    phrases = (
        "Entry note for ",
        "Verify details in linked Fact Cards and Timeline Entries.",
        "Keep historical evidence, interpretation, and creative use separate.",
    )
    return any(phrase in note.text for phrase in phrases)


def has_section(text: str, heading: str) -> bool:
    return re.search(rf"^## {re.escape(heading)}\n", text, re.M) is not None


def has_quality_sections(note: Note) -> bool:
    return all(
        has_section(note.text, heading)
        for heading in ("Historical Role", "Creative Use", "Open Questions")
    )


def is_example_note(note: Note) -> bool:
    tags = frontmatter_list(note, "tags")
    source_id = str(note.frontmatter.get("source_id", "")).strip()
    return (
        str(note.frontmatter.get("status", "")).strip() == "example"
        or "example" in tags
        or source_id == "SRC-EXAMPLE-001"
    )


def upsert_section(text: str, heading: str, content: str) -> str:
    pattern = re.compile(rf"(^## {re.escape(heading)}\n)(.*?)(?=^## |\Z)", re.M | re.S)
    replacement = f"## {heading}\n\n{content.rstrip()}\n\n"
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1).rstrip() + "\n"
    return text.rstrip() + "\n\n" + replacement


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def insert_frontmatter_key(text: str, key: str, value: str, after: tuple[str, ...]) -> str:
    parts = split_frontmatter(text)
    if parts is None:
        return text
    frontmatter, body = parts
    lines = frontmatter.splitlines()
    if any(line.startswith(f"{key}:") for line in lines):
        return text
    line_to_insert = f"{key}: {yaml_quote(value)}"
    insert_at = len(lines)
    for preferred in after:
        for index, line in enumerate(lines):
            if line.startswith(f"{preferred}:"):
                insert_at = index + 1
    lines.insert(insert_at, line_to_insert)
    return "---\n" + "\n".join(lines).rstrip() + "\n---" + body


def set_frontmatter_key(text: str, key: str, value: str, after: tuple[str, ...] = ()) -> str:
    parts = split_frontmatter(text)
    if parts is None:
        return text
    frontmatter, body = parts
    lines = frontmatter.splitlines()
    replacement = f"{key}: {yaml_quote(value)}"
    for index, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            if line == replacement:
                return text
            lines[index] = replacement
            return "---\n" + "\n".join(lines).rstrip() + "\n---" + body
    return insert_frontmatter_key(text, key, value, after=after)


def flatten_frontmatter_values(value: object) -> list[str]:
    values: list[str] = []

    def visit(item: object) -> None:
        if isinstance(item, (list, tuple)):
            for child in item:
                visit(child)
            return
        if item is None:
            return
        text = str(item).strip().strip('"')
        if text and text != "[]":
            values.append(text)

    visit(value)
    return values


def frontmatter_list(note: Note, key: str) -> list[str]:
    value = note.frontmatter.get(key, [])
    if isinstance(value, str):
        text = value.strip()
        if not text or text == "[]":
            return []
        if text.startswith("[") and text.endswith("]"):
            try:
                parsed = ast.literal_eval(text)
            except (SyntaxError, ValueError):
                return [text]
            if isinstance(parsed, (list, tuple)):
                return flatten_frontmatter_values(parsed)
        return [text]
    return flatten_frontmatter_values(value)


def locator_bucket(note: Note) -> str:
    printed_page = str(note.frontmatter.get("printed_page", "")).strip()
    page = str(note.frontmatter.get("page", "")).strip()
    kindle = str(note.frontmatter.get("kindle_location", "")).strip()
    screenshot = str(note.frontmatter.get("screenshot_file", "")).strip()
    if printed_page:
        return "printed_page_confirmed"
    if page and kindle:
        return "kindle_page_locator_available"
    if page:
        return "page_locator_available"
    if kindle:
        return "kindle_locator_available"
    if screenshot:
        return "screenshot_only"
    return "locator_missing"


def printed_page_status_value(note: Note) -> str:
    bucket = locator_bucket(note)
    if bucket == "locator_missing":
        return "missing_locator"
    return "not_verified"


def render_links(notes_by_stem: dict[str, Note], paths: list[Path], limit: int = 60) -> str:
    links: list[str] = []
    seen: set[str] = set()
    for path in sorted(paths, key=lambda item: item.stem.casefold()):
        stem = path.stem
        if stem in seen:
            continue
        seen.add(stem)
        note = notes_by_stem.get(stem)
        if note:
            links.append(wiki_link(note))
        else:
            links.append(f"[[{stem}]]")
    suffix = ""
    if len(links) > limit:
        suffix = f" (+{len(links) - limit} more)"
    return ", ".join(links[:limit]) + suffix


def build_linked_items(note: Note, backlinks: dict[str, list[Path]], notes_by_stem: dict[str, Note]) -> str:
    grouped: dict[str, list[Path]] = defaultdict(list)
    for source in backlinks.get(note.stem, []):
        if source == note.path:
            continue
        grouped[path_category(source)].append(source)

    order = [
        "People",
        "Organizations",
        "Places",
        "Events",
        "Themes",
        "Fact Cards",
        "Timeline Entries",
        "Source Notes",
        "Scenes",
        "Questions",
    ]
    lines: list[str] = []
    for category in order:
        paths = grouped.get(category, [])
        if paths:
            lines.append(f"- {category}: {render_links(notes_by_stem, paths)}")
        else:
            lines.append(f"- {category}:")
    return "\n".join(lines)


def enrich_generated_stubs(notes_by_stem: dict[str, Note], dry_run: bool) -> tuple[int, int]:
    backlinks = collect_backlinks(notes_by_stem)
    checked = 0
    changed = 0
    for note in list(notes_by_stem.values()):
        rel = note.rel
        if not (rel.startswith("03_Entities/") or rel.startswith("04_Events/")):
            continue
        if not is_generated_stub(note):
            continue
        checked += 1
        content = build_linked_items(note, backlinks, notes_by_stem)
        updated = upsert_section(note.text, "Linked Items", content)
        if updated != note.text:
            changed += 1
            if not dry_run:
                note.path.write_text(updated, encoding="utf-8", newline="\n")
    return checked, changed


def enrich_top_stubs(notes_by_stem: dict[str, Note], dry_run: bool, limit: int = 50) -> tuple[int, int]:
    backlinks = collect_backlinks(notes_by_stem)
    candidates = [
        note
        for note in notes_by_stem.values()
        if (note.rel.startswith("03_Entities/") or note.rel.startswith("04_Events/"))
        and is_generated_stub(note)
    ]
    selected = sorted(
        candidates,
        key=lambda item: (-len(backlinks.get(item.stem, [])), item.stem.casefold()),
    )[:limit]

    changed = 0
    for note in selected:
        sources = [path for path in backlinks.get(note.stem, []) if path != note.path]
        fact_paths = [path for path in sources if "02_Fact_Cards" in path.parts]
        timeline_paths = [path for path in sources if "05_Timeline" in path.parts]
        fact_links = render_links(notes_by_stem, fact_paths, limit=12) or "No direct Fact Cards yet."
        timeline_links = render_links(notes_by_stem, timeline_paths, limit=12) or "No direct Timeline Entries yet."
        historical_role = "\n".join(
            [
                f"Evidence hub for **{note.title}**. Treat this section as an index into linked evidence, not as a final historical summary.",
                "",
                f"- Key Fact Cards: {fact_links}",
                f"- Timeline Entries: {timeline_links}",
            ]
        )
        creative_use = "\n".join(
            [
                "Use this note as a scene/research entry point after checking the linked Fact Cards.",
                "",
                "- Convert only verified claims into narrative beats.",
                "- Keep author interpretation and creative inference separate from historical fact.",
            ]
        )
        open_questions = "\n".join(
            [
                "- Which linked claims are strong enough for scene design?",
                "- Which source passages still need page-level verification?",
            ]
        )
        updated = upsert_section(note.text, "Historical Role", historical_role)
        updated = upsert_section(updated, "Creative Use", creative_use)
        updated = upsert_section(updated, "Open Questions", open_questions)
        if updated != note.text:
            changed += 1
            if not dry_run:
                note.path.write_text(updated, encoding="utf-8", newline="\n")
    return len(selected), changed


def enrich_high_link_stubs(notes_by_stem: dict[str, Note], dry_run: bool, min_backlinks: int = 10) -> tuple[int, int]:
    backlinks = collect_backlinks(notes_by_stem)
    candidates = [
        note
        for note in notes_by_stem.values()
        if (note.rel.startswith("03_Entities/") or note.rel.startswith("04_Events/"))
        and is_generated_stub(note)
        and not has_quality_sections(note)
        and len(backlinks.get(note.stem, [])) >= min_backlinks
    ]
    selected = sorted(
        candidates,
        key=lambda item: (-len(backlinks.get(item.stem, [])), item.stem.casefold()),
    )

    changed = 0
    for note in selected:
        sources = [path for path in backlinks.get(note.stem, []) if path != note.path]
        fact_paths = [path for path in sources if "02_Fact_Cards" in path.parts]
        timeline_paths = [path for path in sources if "05_Timeline" in path.parts]
        fact_links = render_links(notes_by_stem, fact_paths, limit=12) or "No direct Fact Cards yet."
        timeline_links = render_links(notes_by_stem, timeline_paths, limit=12) or "No direct Timeline Entries yet."
        historical_role = "\n".join(
            [
                f"Evidence hub for **{note.title}**. Treat this section as an index into linked evidence, not as a final historical summary.",
                "",
                f"- Key Fact Cards: {fact_links}",
                f"- Timeline Entries: {timeline_links}",
            ]
        )
        creative_use = "\n".join(
            [
                "Use this note as a scene/research entry point after checking the linked Fact Cards.",
                "",
                "- Convert only verified claims into narrative beats.",
                "- Keep author interpretation and creative inference separate from historical fact.",
            ]
        )
        open_questions = "\n".join(
            [
                "- Which linked claims are strong enough for scene design?",
                "- Which source passages still need page-level verification?",
            ]
        )
        updated = upsert_section(note.text, "Historical Role", historical_role)
        updated = upsert_section(updated, "Creative Use", creative_use)
        updated = upsert_section(updated, "Open Questions", open_questions)
        if updated != note.text:
            changed += 1
            if not dry_run:
                note.path.write_text(updated, encoding="utf-8", newline="\n")
    return len(selected), changed


def merge_wiki_links(existing_line: str, additions: list[str]) -> str:
    found = [match.group(0) for match in iter_wiki_matches(existing_line)]
    merged: list[str] = []
    for link in found + additions:
        if link not in merged:
            merged.append(link)
    return ", ".join(merged)


def upsert_links_line(text: str, label: str, additions: list[str]) -> str:
    if not additions:
        return text
    pattern = re.compile(r"(^## Links\n)(.*?)(?=^## |\Z)", re.M | re.S)
    match = pattern.search(text)
    line_prefix = f"- {label}:"
    if not match:
        content = f"{line_prefix} {', '.join(additions)}"
        return upsert_section(text, "Links", content)

    section = match.group(2).rstrip()
    lines = section.splitlines() if section else []
    replaced = False
    new_lines: list[str] = []
    for line in lines:
        if line.startswith(line_prefix):
            merged = merge_wiki_links(line, additions)
            new_lines.append(f"{line_prefix} {merged}".rstrip())
            replaced = True
        else:
            new_lines.append(line)
    if not replaced:
        new_lines.append(f"{line_prefix} {', '.join(additions)}")
    replacement = match.group(1) + "\n".join(new_lines).rstrip() + "\n\n"
    return text[: match.start()] + replacement + text[match.end() :]


def normalize_known_source_records(dry_run: bool) -> tuple[int, int, int]:
    shawcross_source = "SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO"
    shawcross_link = "[[SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO|The Last Emperor of Mexico: A Disaster in the New World]]"
    source_normalized = 0
    examples_marked = 0
    touched: set[Path] = set()

    for name in [f"FACT_MEXEMP_{number:04d}.md" for number in range(1, 7)]:
        path = ROOT / "02_Fact_Cards" / name
        if not path.exists():
            continue
        note = read_note(path)
        updated = set_frontmatter_key(note.text, "source_id", shawcross_source, after=("tags",))
        updated = updated.replace("[[SRC_UNSET_001]]", shawcross_link)
        updated = updated.replace("[[SRC_UNSET_001|The Last Emperor of Mexico: A Disaster in the New World]]", shawcross_link)
        if updated != note.text:
            source_normalized += 1
            touched.add(path)
            if not dry_run:
                path.write_text(updated, encoding="utf-8", newline="\n")

    for name in ("TIME_MEXEMP_0001.md", "TIME_MEXEMP_0002.md"):
        path = ROOT / "05_Timeline" / name
        if not path.exists():
            continue
        note = read_note(path)
        updated = set_frontmatter_key(note.text, "source_id", shawcross_source, after=("tags",))
        updated = updated.replace("[[SRC_UNSET_001]]", shawcross_link)
        updated = updated.replace("[[SRC_UNSET_001|The Last Emperor of Mexico: A Disaster in the New World]]", shawcross_link)
        if updated != note.text:
            source_normalized += 1
            touched.add(path)
            if not dry_run:
                path.write_text(updated, encoding="utf-8", newline="\n")

    for path in (
        ROOT / "02_Fact_Cards" / "FC-1864-001.md",
        ROOT / "05_Timeline" / "TL-18640528-001.md",
        ROOT / "01_Sources" / "Source_Notes" / "SRC_EXAMPLE_001.md",
    ):
        if not path.exists():
            continue
        note = read_note(path)
        updated = set_frontmatter_key(note.text, "status", "example", after=("type",))
        if updated != note.text:
            examples_marked += 1
            touched.add(path)
            if not dry_run:
                path.write_text(updated, encoding="utf-8", newline="\n")

    return len(touched), source_normalized, examples_marked


def repair_fact_cards(notes_by_stem: dict[str, Note], dry_run: bool) -> tuple[int, int, int, int]:
    statement_added = 0
    printed_candidate_added = 0
    printed_status_added = 0
    fact_cards_touched: set[Path] = set()

    for path in sorted((ROOT / "02_Fact_Cards").glob("*.md")):
        note = read_note(path)
        if note.type != "fact_card":
            continue
        if is_example_note(note):
            continue
        updated = note.text
        claim = str(note.frontmatter.get("claim", "")).strip()
        if not note.frontmatter.get("statement") and claim:
            updated = insert_frontmatter_key(updated, "statement", claim, after=("title", "claim"))
            if updated != note.text:
                statement_added += 1
        note_after_statement = Note(path=path, text=updated, frontmatter=parse_frontmatter(updated))
        archive_page = str(note_after_statement.frontmatter.get("archive_page", "")).strip()
        if (
            not note_after_statement.frontmatter.get("printed_page")
            and archive_page
            and not note_after_statement.frontmatter.get("printed_page_candidate")
        ):
            newer = insert_frontmatter_key(updated, "printed_page_candidate", archive_page, after=("archive_page",))
            if newer != updated:
                printed_candidate_added += 1
                updated = newer
        note_after_printed_candidate = Note(path=path, text=updated, frontmatter=parse_frontmatter(updated))
        if not note_after_printed_candidate.frontmatter.get("printed_page_status"):
            status = printed_page_status_value(note_after_printed_candidate)
            newer = insert_frontmatter_key(
                updated,
                "printed_page_status",
                status,
                after=("printed_page", "page", "kindle_location", "screenshot_file"),
            )
            if newer != updated:
                printed_status_added += 1
                updated = newer
        if updated != note.text:
            fact_cards_touched.add(path)
            if not dry_run:
                path.write_text(updated, encoding="utf-8", newline="\n")

    return len(fact_cards_touched), statement_added, printed_candidate_added, printed_status_added


def timeline_related_fact_cards(note: Note) -> list[str]:
    related = frontmatter_list(note, "related_fact_cards")
    outlinks = collect_outlinks(note.text)
    for target in sorted(outlinks):
        if target.startswith("FACT_") and target not in related:
            related.append(target)
    return related


def strengthen_timeline_links(notes_by_stem: dict[str, Note], dry_run: bool) -> tuple[int, int]:
    timeline_touched = 0
    fact_cards_touched = 0
    fact_to_timeline: dict[str, list[str]] = defaultdict(list)

    for path in sorted((ROOT / "05_Timeline").glob("*.md")):
        note = read_note(path)
        if note.type != "timeline_entry":
            continue
        related = timeline_related_fact_cards(note)
        for fact in related:
            if fact in notes_by_stem:
                fact_to_timeline[fact].append(note.stem)
        source = str(note.frontmatter.get("source_id", "")).strip()
        source_line = f"- Source: {source_link(source, notes_by_stem)}" if source else "- Source:"
        fact_line = "- Related Fact Cards: " + (
            ", ".join(f"[[{fact}]]" for fact in related) if related else ""
        )
        evidence = "\n".join(
            [
                source_line,
                fact_line,
                f"- Evidence category: {note.frontmatter.get('evidence_category', '')}",
                f"- Confidence: {note.frontmatter.get('confidence', '')}",
                f"- Screenshot file: {note.frontmatter.get('screenshot_file', '')}",
            ]
        )
        updated = upsert_section(note.text, "Evidence / Source Links", evidence)
        if updated != note.text:
            timeline_touched += 1
            if not dry_run:
                path.write_text(updated, encoding="utf-8", newline="\n")

    for fact, timelines in sorted(fact_to_timeline.items()):
        note = notes_by_stem.get(fact)
        if not note:
            continue
        additions = [f"[[{timeline}]]" for timeline in sorted(set(timelines))]
        updated = upsert_links_line(note.text, "Related Timeline Entries", additions)
        if updated != note.text:
            fact_cards_touched += 1
            if not dry_run:
                note.path.write_text(updated, encoding="utf-8", newline="\n")
    return timeline_touched, fact_cards_touched


def source_id_counts(include_examples: bool = True) -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in (ROOT / "02_Fact_Cards").glob("*.md"):
        note = read_note(path)
        if note.type == "fact_card" and (include_examples or not is_example_note(note)):
            counts[str(note.frontmatter.get("source_id", "")).strip() or "(missing)"] += 1
    return counts


def missing_fact_metadata() -> dict[str, list[Path]]:
    missing: dict[str, list[Path]] = defaultdict(list)
    for path in (ROOT / "02_Fact_Cards").glob("*.md"):
        note = read_note(path)
        if note.type != "fact_card":
            continue
        if is_example_note(note):
            missing["example_fact_cards"].append(path)
            continue
        for key in ("statement", "source_id", "evidence_category", "confidence"):
            value = str(note.frontmatter.get(key, "")).strip()
            if not value:
                missing[key].append(path)
        missing[locator_bucket(note)].append(path)
        source_id = str(note.frontmatter.get("source_id", "")).strip()
        if source_id in {"", "SRC_UNSET_001", "SRC-EXAMPLE-001"}:
            missing["source_id_review"].append(path)
    return missing


def backlinks_counter(notes_by_stem: dict[str, Note]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for target, sources in collect_backlinks(notes_by_stem).items():
        counter[target] = len(sources)
    return counter


def render_path_list(paths: list[Path], limit: int = 80) -> list[str]:
    notes = note_map(include_outputs=True)
    lines: list[str] = []
    for path in paths[:limit]:
        note = notes.get(path.stem) or read_note(path)
        lines.append(f"- {wiki_link(note)}")
    if len(paths) > limit:
        lines.append(f"- ...and {len(paths) - limit} more")
    return lines


def write_fact_metadata_review(dry_run: bool) -> Path:
    missing = missing_fact_metadata()
    review_order = (
        "statement",
        "source_id",
        "evidence_category",
        "confidence",
        "source_id_review",
        "printed_page_confirmed",
        "kindle_page_locator_available",
        "page_locator_available",
        "kindle_locator_available",
        "screenshot_only",
        "locator_missing",
        "example_fact_cards",
    )
    lines = [
        "---",
        "id: FACT-CARD-METADATA-REVIEW",
        "type: report",
        "status: active",
        f"created: {TODAY}",
        "tags:",
        "  - audit",
        "  - fact-cards",
        "---",
        "",
        "# Fact Card Metadata Review",
        "",
        "## Summary",
        "",
    ]
    for key in review_order:
        lines.append(f"- {key}: {len(missing.get(key, []))}")
    for key in review_order:
        paths = missing.get(key, [])
        if not paths:
            continue
        lines.extend(["", f"## {key}", ""])
        lines.extend(render_path_list(sorted(paths), limit=120))
    path = AUDIT_DIR / "Fact_Card_Metadata_Review.md"
    if not dry_run:
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    return path


def table_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def note_locator_summary(note: Note) -> str:
    parts: list[str] = []
    for key in ("printed_page", "page", "kindle_location", "screenshot_file"):
        value = str(note.frontmatter.get(key, "")).strip()
        if value:
            parts.append(f"{key}: {value}")
    return "; ".join(parts)


def write_printed_page_candidates(notes_by_stem: dict[str, Note], dry_run: bool, limit: int = 200) -> Path:
    backlinks = backlinks_counter(notes_by_stem)
    candidates: list[Note] = []
    for path in (ROOT / "02_Fact_Cards").glob("*.md"):
        note = read_note(path)
        if note.type != "fact_card" or is_example_note(note):
            continue
        if str(note.frontmatter.get("printed_page_status", "")).strip() == "not_verified":
            candidates.append(note)

    selected = sorted(
        candidates,
        key=lambda item: (-backlinks[item.stem], str(item.frontmatter.get("source_id", "")), item.stem),
    )[:limit]

    lines = [
        "---",
        "id: PRINTED-PAGE-VERIFICATION-CANDIDATES",
        "type: report",
        "status: active",
        f"created: {TODAY}",
        "tags:",
        "  - audit",
        "  - printed-page",
        "---",
        "",
        "# Printed Page Verification Candidates",
        "",
        "## Summary",
        "",
        f"- total_not_verified: {len(candidates)}",
        f"- selected_for_review: {len(selected)}",
        "- selection_rule: highest backlink count, then source_id and Fact Card id",
        "",
        "## Candidates",
        "",
        "| Priority | Fact Card | Backlinks | Source | Locator |",
        "| ---: | --- | ---: | --- | --- |",
    ]
    for priority, note in enumerate(selected, 1):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(priority),
                    f"[[{note.stem}]]",
                    str(backlinks[note.stem]),
                    table_cell(note.frontmatter.get("source_id", "")),
                    table_cell(note_locator_summary(note)),
                ]
            )
            + " |"
        )

    path = AUDIT_DIR / "Printed_Page_Verification_Candidates.md"
    if not dry_run:
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def write_stub_priority_review(notes_by_stem: dict[str, Note], dry_run: bool) -> Path:
    backlinks = collect_backlinks(notes_by_stem)
    stubs = [
        note
        for note in notes_by_stem.values()
        if (note.rel.startswith("03_Entities/") or note.rel.startswith("04_Events/"))
        and is_generated_stub(note)
    ]
    buckets: dict[str, list[Note]] = {
        "10+": [],
        "5-9": [],
        "2-4": [],
        "1": [],
        "0": [],
    }
    for note in stubs:
        count = len(backlinks.get(note.stem, []))
        if count >= 10:
            buckets["10+"].append(note)
        elif count >= 5:
            buckets["5-9"].append(note)
        elif count >= 2:
            buckets["2-4"].append(note)
        elif count == 1:
            buckets["1"].append(note)
        else:
            buckets["0"].append(note)

    lines = [
        "---",
        "id: STUB-PRIORITY-REVIEW",
        "type: report",
        "status: active",
        f"created: {TODAY}",
        "tags:",
        "  - audit",
        "  - stubs",
        "---",
        "",
        "# Stub Priority Review",
        "",
        "## Summary",
        "",
        f"- generated_stubs: {len(stubs)}",
        f"- backlink_10_plus: {len(buckets['10+'])}",
        f"- backlink_5_9: {len(buckets['5-9'])}",
        f"- backlink_2_4: {len(buckets['2-4'])}",
        f"- backlink_1_low_priority: {len(buckets['1'])}",
        f"- backlink_0: {len(buckets['0'])}",
        "",
        "## Backlink 10+",
        "",
    ]
    for note in sorted(buckets["10+"], key=lambda item: (-len(backlinks[item.stem]), item.stem.casefold())):
        quality = "quality_sections: yes" if has_quality_sections(note) else "quality_sections: no"
        lines.append(f"- {wiki_link(note)} - backlinks: {len(backlinks[note.stem])}; {quality}")

    lines.extend(["", "## Stub Low Priority", ""])
    for note in sorted(buckets["1"], key=lambda item: item.stem.casefold()):
        lines.append(f"- {wiki_link(note)} - backlinks: 1")

    path = AUDIT_DIR / "Stub_Priority_Review.md"
    if not dry_run:
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def write_example_records_doc(notes_by_stem: dict[str, Note], dry_run: bool) -> Path:
    example_notes = [
        note
        for note in notes_by_stem.values()
        if is_example_note(note)
        and (
            note.rel.startswith("01_Sources/")
            or note.rel.startswith("02_Fact_Cards/")
            or note.rel.startswith("05_Timeline/")
        )
    ]
    lines = [
        "---",
        "id: EXAMPLE-RECORDS",
        "type: doc",
        "status: active",
        f"created: {TODAY}",
        "tags:",
        "  - examples",
        "  - maintenance",
        "---",
        "",
        "# Example Records",
        "",
        "These records are retained as examples and excluded from ordinary metadata review. Do not use them as historical evidence.",
        "",
        "## Records",
        "",
    ]
    for note in sorted(example_notes, key=lambda item: item.rel):
        lines.append(f"- {wiki_link(note)} - `{note.rel}`")

    path = ROOT / "93_Docs" / "Example_Records.md"
    if not dry_run:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def write_hamnett_readiness(notes_by_stem: dict[str, Note], dry_run: bool) -> Path:
    facts_by_section: Counter[str] = Counter()
    timeline_by_section: Counter[str] = Counter()
    for path in (ROOT / "02_Fact_Cards").glob("FACT_HAMNETT_JUAREZ_*.md"):
        note = read_note(path)
        facts_by_section[str(note.frontmatter.get("section", "(missing)")).strip() or "(missing)"] += 1
    for path in (ROOT / "05_Timeline").glob("TIME_HAMNETT_JUAREZ_*.md"):
        note = read_note(path)
        timeline_by_section[str(note.frontmatter.get("section", "(missing)")).strip() or "(missing)"] += 1

    progress = notes_by_stem.get("Hamnett_Juarez_Progress_Master")
    next_required_page = "unknown"
    next_checks: list[str] = []
    if progress:
        progress_next = str(progress.frontmatter.get("next_required_page", "")).strip()
        if progress_next:
            next_required_page = progress_next
        else:
            for line in progress.text.splitlines():
                if not line.startswith("| next_required_page |"):
                    continue
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) >= 2 and cells[1]:
                    next_required_page = cells[1].strip("`")
                break
        in_next = False
        for line in progress.text.splitlines():
            if line.startswith("## Next Checks"):
                in_next = True
                continue
            if in_next and line.startswith("## "):
                break
            if in_next and line.startswith("- "):
                next_checks.append(line)

    lines = [
        "---",
        "id: HAMNETT-INGESTION-READINESS",
        "type: report",
        "status: active",
        f"created: {TODAY}",
        "tags:",
        "  - hamnett",
        "  - ingestion",
        "  - readiness",
        "---",
        "",
        "# Hamnett Ingestion Readiness",
        "",
        "## Summary",
        "",
        f"- hamnett_fact_cards: {sum(facts_by_section.values())}",
        f"- hamnett_timeline_entries: {sum(timeline_by_section.values())}",
        f"- next_required_page: {next_required_page}",
        "",
        "## Fact Cards By Section",
        "",
    ]
    for section, amount in facts_by_section.most_common():
        lines.append(f"- {section}: {amount}")
    lines.extend(["", "## Timeline By Section", ""])
    for section, amount in timeline_by_section.most_common():
        lines.append(f"- {section}: {amount}")
    lines.extend(["", "## Next Checks From Progress Master", ""])
    lines.extend(next_checks[:40])

    path = AUDIT_DIR / "Hamnett_Ingestion_Readiness.md"
    if not dry_run:
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def evidence_summary_for(note: Note, notes_by_stem: dict[str, Note], backlinks: dict[str, list[Path]]) -> str:
    fact_paths = [path for path in backlinks.get(note.stem, []) if "02_Fact_Cards" in path.parts]
    timeline_paths = [path for path in backlinks.get(note.stem, []) if "05_Timeline" in path.parts]
    status_counts: Counter[str] = Counter()
    fact_notes: list[Note] = []
    for path in fact_paths:
        fact = notes_by_stem.get(path.stem) or read_note(path)
        if is_example_note(fact):
            continue
        fact_notes.append(fact)
        status_counts[str(fact.frontmatter.get("printed_page_status", "(missing)")).strip() or "(missing)"] += 1
    fact_links = ", ".join(wiki_link(fact) for fact in sorted(fact_notes, key=lambda item: item.stem)[:3])
    if len(fact_notes) > 3:
        fact_links += f" (+{len(fact_notes) - 3} more)"
    if not fact_links:
        fact_links = "none"
    return (
        f"Fact Cards: {len(fact_notes)}; Timeline: {len(timeline_paths)}; "
        f"printed confirmed/not_verified/missing: {status_counts['confirmed']}/"
        f"{status_counts['not_verified']}/{status_counts['(missing)']}; "
        f"direct facts: {fact_links}"
    )


def write_indexes(notes_by_stem: dict[str, Note], dry_run: bool) -> int:
    backlinks = backlinks_counter(notes_by_stem)
    if not dry_run:
        INDEX_DIR.mkdir(parents=True, exist_ok=True)
    count = 0

    entity_lines = [
        "---",
        'id: "Index_Entities"',
        'type: "index_note"',
        'status: "active"',
        f'created: "{TODAY}"',
        f'updated: "{TODAY}"',
        "tags:",
        '  - "index"',
        '  - "entities"',
        "---",
        "",
        "# Entity索引",
        "",
        "## Summary",
        "",
    ]
    for label, folder in ENTITY_FOLDERS.items():
        files = sorted(folder.glob("*.md"))
        entity_lines.append(f"- {label}: {len(files)}")
    entity_lines.append(f"- Events: {len(list((ROOT / '04_Events').glob('*.md'))) - 1}")
    entity_lines.extend(["", "## High-Link Entity Notes", ""])
    entity_notes = [read_note(p) for folder in ENTITY_FOLDERS.values() for p in folder.glob("*.md")]
    entity_notes += [read_note(p) for p in (ROOT / "04_Events").glob("*.md") if p.name != "README.md"]
    for note in sorted(entity_notes, key=lambda item: (-backlinks[item.stem], item.stem.casefold()))[:80]:
        entity_lines.append(f"- {wiki_link(note)} - backlinks: {backlinks[note.stem]}")
    for label, folder in ENTITY_FOLDERS.items():
        entity_lines.extend(["", f"## {label}", ""])
        for note in sorted((read_note(p) for p in folder.glob("*.md")), key=lambda item: item.stem.casefold()):
            entity_lines.append(f"- {wiki_link(note)}")
    entity_lines.extend(["", "## Events", ""])
    for note in sorted((read_note(p) for p in (ROOT / "04_Events").glob("*.md") if p.name != "README.md"), key=lambda item: item.stem.casefold()):
        entity_lines.append(f"- {wiki_link(note)}")
    if not dry_run:
        (INDEX_DIR / "Index_Entities.md").write_text("\n".join(entity_lines) + "\n", encoding="utf-8", newline="\n")
    count += 1

    missing = missing_fact_metadata()
    source_counts = source_id_counts(include_examples=False)
    fact_lines = [
        "---",
        'id: "Index_Fact_Cards"',
        'type: "index_note"',
        'status: "active"',
        f'created: "{TODAY}"',
        f'updated: "{TODAY}"',
        "tags:",
        '  - "index"',
        '  - "fact-cards"',
        "---",
        "",
        "# Fact Card索引",
        "",
        "## Summary",
        "",
        f"- Fact Cards: {sum(source_counts.values())}",
    ]
    for key in (
        "source_id_review",
        "printed_page_confirmed",
        "kindle_page_locator_available",
        "page_locator_available",
        "kindle_locator_available",
        "screenshot_only",
        "locator_missing",
    ):
        fact_lines.append(f"- {key} review count: {len(missing.get(key, []))}")
    fact_lines.extend(["", "## By Source", ""])
    for source, amount in source_counts.most_common():
        fact_lines.append(f"- {source_link(source, notes_by_stem)}: {amount}" if source != "(missing)" else f"- missing source_id: {amount}")
    fact_lines.extend(["", "## Metadata Review", "", "- [[Fact_Card_Metadata_Review]]"])
    if not dry_run:
        (INDEX_DIR / "Index_Fact_Cards.md").write_text("\n".join(fact_lines) + "\n", encoding="utf-8", newline="\n")
    count += 1

    timeline_notes = [read_note(p) for p in (ROOT / "05_Timeline").glob("*.md") if p.name != "README.md"]
    timeline_lines = [
        "---",
        'id: "Index_Timeline"',
        'type: "index_note"',
        'status: "active"',
        f'created: "{TODAY}"',
        f'updated: "{TODAY}"',
        "tags:",
        '  - "index"',
        '  - "timeline"',
        "---",
        "",
        "# Timeline索引",
        "",
        "## Summary",
        "",
        f"- Timeline Entries: {len(timeline_notes)}",
        f"- Entries with no backlinks: {sum(1 for note in timeline_notes if backlinks[note.stem] == 0)}",
        "",
        "## Entries",
        "",
    ]
    for note in sorted(timeline_notes, key=lambda item: str(item.frontmatter.get("date_start", item.stem))):
        date = note.frontmatter.get("date_start") or note.frontmatter.get("date") or ""
        timeline_lines.append(f"- {date}: {wiki_link(note)}")
    if not dry_run:
        (INDEX_DIR / "Index_Timeline.md").write_text("\n".join(timeline_lines) + "\n", encoding="utf-8", newline="\n")
    count += 1

    source_notes = [
        note
        for note in (read_note(p) for p in (ROOT / "01_Sources").rglob("*.md") if p.name != "README.md")
        if not is_example_note(note)
    ]
    source_records = [note for note in source_notes if note.type == "source_note"]
    chapter_summaries = [note for note in source_notes if note.type == "book_chapter_summary"]
    capture_records = [note for note in source_notes if note.type in {"capture", "capture_note"}]
    categorized_paths = {note.path for note in source_records + chapter_summaries + capture_records}
    other_source_records = [note for note in source_notes if note.path not in categorized_paths]
    source_lines = [
        "---",
        'id: "Index_Sources"',
        'type: "index_note"',
        'status: "active"',
        f'created: "{TODAY}"',
        f'updated: "{TODAY}"',
        "tags:",
        '  - "index"',
        '  - "sources"',
        "---",
        "",
        "# Source索引",
        "",
        "## Summary",
        "",
        f"- Source notes: {len(source_records)}",
        f"- Book chapter summaries: {len(chapter_summaries)}",
        f"- Capture notes: {len(capture_records)}",
        f"- Other source records: {len(other_source_records)}",
        "",
        "## Source Notes",
        "",
    ]
    for note in sorted(source_records, key=lambda item: (item.title.casefold(), item.stem.casefold())):
        source_lines.append(f"- {wiki_link(note)}")

    source_lines.extend(["", "## Book Chapter Summaries", ""])
    summaries_by_source: dict[str, list[Note]] = defaultdict(list)
    for note in chapter_summaries:
        source_id = str(note.frontmatter.get("source_id", "")).strip('"') or "(missing source_id)"
        summaries_by_source[source_id].append(note)
    for source_id in sorted(summaries_by_source, key=str.casefold):
        source_lines.append(f"### {source_link(source_id, notes_by_stem)}")
        source_lines.append("")
        ordered = sorted(
            summaries_by_source[source_id],
            key=lambda item: (
                int(str(item.frontmatter.get("chapter_order", "999999")).strip('"'))
                if str(item.frontmatter.get("chapter_order", "")).strip('"').isdigit()
                else 999999,
                item.stem.casefold(),
            ),
        )
        for note in ordered:
            pages = str(note.frontmatter.get("printed_pages", "")).strip('"')
            coverage = str(note.frontmatter.get("coverage_status", "")).strip('"')
            source_lines.append(f"- {wiki_link(note)} - pp. {pages} - `{coverage}`")
        source_lines.append("")

    source_lines.extend(["## Capture Notes", ""])
    for note in sorted(capture_records, key=lambda item: item.stem.casefold()):
        source_lines.append(f"- {wiki_link(note)}")

    source_lines.extend(["", "## Other Source Records", ""])
    for note in sorted(other_source_records, key=lambda item: item.stem.casefold()):
        source_lines.append(f"- {wiki_link(note)}")
    if not dry_run:
        (INDEX_DIR / "Index_Sources.md").write_text("\n".join(source_lines) + "\n", encoding="utf-8", newline="\n")
    count += 1
    return count


def write_writing_views(notes_by_stem: dict[str, Note], dry_run: bool) -> int:
    backlink_map = collect_backlinks(notes_by_stem)
    backlinks = backlinks_counter(notes_by_stem)
    fact_cards = [
        read_note(p)
        for p in (ROOT / "02_Fact_Cards").glob("*.md")
        if p.name != "README.md" and not is_example_note(read_note(p))
    ]
    high_use = [
        note for note in fact_cards
        if "creative_use" in note.frontmatter and str(note.frontmatter.get("creative_use", "")).strip()
    ][:80]
    themes = sorted((read_note(p) for p in (ROOT / "03_Entities" / "Themes").glob("*.md")), key=lambda item: (-backlinks[item.stem], item.stem.casefold()))[:40]
    events = sorted((read_note(p) for p in (ROOT / "04_Events").glob("*.md") if p.name != "README.md"), key=lambda item: (-backlinks[item.stem], item.stem.casefold()))[:40]
    people = sorted((read_note(p) for p in (ROOT / "03_Entities" / "People").glob("*.md")), key=lambda item: (-backlinks[item.stem], item.stem.casefold()))[:40]
    places = sorted((read_note(p) for p in (ROOT / "03_Entities" / "Places").glob("*.md")), key=lambda item: (-backlinks[item.stem], item.stem.casefold()))[:40]
    organizations = sorted((read_note(p) for p in (ROOT / "03_Entities" / "Organizations").glob("*.md")), key=lambda item: (-backlinks[item.stem], item.stem.casefold()))[:40]

    scene_lines = [
        "---",
        "id: SCENE-SEED-INDEX",
        "type: scene_note",
        "status: active",
        f"created: {TODAY}",
        "tags:",
        "  - scene-seeds",
        "  - writing-view",
        "---",
        "",
        "# Scene Seed Index",
        "",
        "DB内のFact Card、Event、Themeから小説場面の入口を作るための索引。本文創作ではなく、史料に戻るためのリンク集。",
        "",
        "## High-Use Fact Cards",
        "",
    ]
    scene_lines.extend(f"- {wiki_link(note)}" for note in high_use[:60])
    for heading, notes in (
        ("Major People", people),
        ("Major Events", events),
        ("Major Places", places),
        ("Major Organizations", organizations),
        ("Major Themes", themes),
    ):
        scene_lines.extend(["", f"## {heading}", ""])
        for note in notes:
            scene_lines.append(
                f"- {wiki_link(note)} - backlinks: {backlinks[note.stem]}; "
                f"{evidence_summary_for(note, notes_by_stem, backlink_map)}"
            )

    missing = missing_fact_metadata()
    review_lines = [
        "---",
        "id: OPEN-RESEARCH-QUESTIONS",
        "type: question_note",
        "status: active",
        f"created: {TODAY}",
        "tags:",
        "  - research-questions",
        "  - writing-view",
        "---",
        "",
        "# Open Research Questions",
        "",
        "未確認事項とDB補修対象の入口。判断が必要なものはFact Card本文を確認してから確定する。",
        "",
        "## Metadata Review",
        "",
        "- [[Fact_Card_Metadata_Review]]",
        "",
        "## Source ID Review",
        "",
    ]
    review_lines.extend(render_path_list(sorted(missing.get("source_id_review", [])), limit=80))
    review_lines.extend(["", "## Missing Statement", ""])
    review_lines.extend(render_path_list(sorted(missing.get("statement", [])), limit=80))
    locator_without_printed = []
    for key in (
        "kindle_page_locator_available",
        "page_locator_available",
        "kindle_locator_available",
        "screenshot_only",
    ):
        locator_without_printed.extend(missing.get(key, []))
    review_lines.extend(["", "## Printed Page Not Verified", ""])
    review_lines.extend(render_path_list(sorted(locator_without_printed), limit=80))
    review_lines.extend(["", "## Locator Missing", ""])
    review_lines.extend(render_path_list(sorted(missing.get("locator_missing", [])), limit=80))

    if not dry_run:
        (ROOT / "06_Scenes" / "Scene_Seed_Index.md").write_text("\n".join(scene_lines) + "\n", encoding="utf-8", newline="\n")
        (ROOT / "07_Questions" / "Open_Research_Questions.md").write_text("\n".join(review_lines) + "\n", encoding="utf-8", newline="\n")
    return 2


def files_with_replacement_char() -> list[Path]:
    paths: list[Path] = []
    for path in markdown_files(include_outputs=True):
        text = path.read_text(encoding="utf-8", errors="replace")
        if REPLACEMENT_CHAR in text:
            paths.append(path)
    return paths


def chapter_summary_metadata_issues() -> dict[str, list[str]]:
    issues: dict[str, list[str]] = defaultdict(list)
    chapter_dir = ROOT / "01_Sources" / "Chapter_Summaries"
    if not chapter_dir.exists():
        return issues

    notes: list[Note] = []
    for path in chapter_dir.glob("*.md"):
        if path.name == "README.md":
            continue
        note = read_note(path)
        notes.append(note)
    order_map: dict[tuple[str, str], list[Note]] = defaultdict(list)
    for note in notes:
        if note.type != "book_chapter_summary":
            issues["invalid_note_type"].append(f"{note.rel}: {note.type or '(missing)'}")
        for field in CHAPTER_SUMMARY_REQUIRED_FIELDS:
            value = note.frontmatter.get(field, "")
            if not str(value).strip().strip('"'):
                issues["missing_required"].append(f"{note.rel}: {field}")

        coverage = str(note.frontmatter.get("coverage_status", "")).strip('"')
        if coverage and coverage not in CHAPTER_SUMMARY_COVERAGE_STATUSES:
            issues["invalid_coverage_status"].append(f"{note.rel}: {coverage}")

        source_id = str(note.frontmatter.get("source_id", "")).strip('"')
        chapter_order = str(note.frontmatter.get("chapter_order", "")).strip('"')
        if source_id and chapter_order:
            order_map[(source_id, chapter_order)].append(note)

    for (source_id, chapter_order), grouped_notes in order_map.items():
        if len(grouped_notes) > 1:
            paths = ", ".join(note.rel for note in grouped_notes)
            issues["duplicate_source_chapter_order"].append(
                f"{source_id} / {chapter_order}: {paths}"
            )
    issues["notes_checked"] = [str(len(notes))]
    return issues


def write_chapter_summary_metadata_review(dry_run: bool) -> Path:
    issues = chapter_summary_metadata_issues()
    path = AUDIT_DIR / "Chapter_Summary_Metadata_Review.md"
    notes_checked = int(issues.get("notes_checked", ["0"])[0])
    lines = [
        "---",
        'id: "CHAPTER-SUMMARY-METADATA-REVIEW"',
        'type: "audit_report"',
        'status: "active"',
        f'created: "{TODAY}"',
        "tags:",
        '  - "audit"',
        '  - "chapter-summary"',
        "---",
        "",
        "# Chapter Summary Metadata Review",
        "",
        "## Summary",
        "",
        f"- Notes checked: {notes_checked}",
        f"- Missing required fields: {len(issues.get('missing_required', []))}",
        f"- Invalid note type: {len(issues.get('invalid_note_type', []))}",
        f"- Invalid coverage status: {len(issues.get('invalid_coverage_status', []))}",
        f"- Duplicate source/chapter order: {len(issues.get('duplicate_source_chapter_order', []))}",
        "",
    ]
    for key, heading in (
        ("missing_required", "Missing Required Fields"),
        ("invalid_note_type", "Invalid Note Type"),
        ("invalid_coverage_status", "Invalid Coverage Status"),
        ("duplicate_source_chapter_order", "Duplicate Source / Chapter Order"),
    ):
        lines.extend([f"## {heading}", ""])
        values = issues.get(key, [])
        lines.extend(f"- `{value}`" for value in values)
        if not values:
            lines.append("- None")
        lines.append("")
    while lines and not lines[-1]:
        lines.pop()
    if not dry_run:
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def validation_snapshot(notes_by_stem: dict[str, Note]) -> dict[str, int]:
    backlinks = collect_backlinks(notes_by_stem)
    entity_notes = [read_note(p) for p in (ROOT / "03_Entities").rglob("*.md")]
    timeline_notes = [read_note(p) for p in (ROOT / "05_Timeline").glob("*.md") if p.name != "README.md"]
    stubs = [note for note in entity_notes if is_generated_stub(note)]
    missing = missing_fact_metadata()
    chapter_issues = chapter_summary_metadata_issues()
    return {
        "markdown_files": len(markdown_files(include_outputs=True)),
        "entity_notes": len(entity_notes),
        "generated_entity_stubs": len(stubs),
        "entity_zero_backlinks": sum(1 for note in entity_notes if len(backlinks.get(note.stem, [])) == 0),
        "timeline_entries": len(timeline_notes),
        "timeline_zero_backlinks": sum(1 for note in timeline_notes if len(backlinks.get(note.stem, [])) == 0),
        "fact_missing_statement": len(missing.get("statement", [])),
        "fact_source_id_review": len(missing.get("source_id_review", [])),
        "fact_printed_page_confirmed": len(missing.get("printed_page_confirmed", [])),
        "fact_locator_available_without_printed_page": sum(
            len(missing.get(key, []))
            for key in (
                "kindle_page_locator_available",
                "page_locator_available",
                "kindle_locator_available",
                "screenshot_only",
            )
        ),
        "fact_locator_missing": len(missing.get("locator_missing", [])),
        "chapter_summaries": int(chapter_issues.get("notes_checked", ["0"])[0]),
        "chapter_summary_missing_required": len(chapter_issues.get("missing_required", [])),
        "chapter_summary_invalid_note_type": len(chapter_issues.get("invalid_note_type", [])),
        "chapter_summary_invalid_coverage_status": len(chapter_issues.get("invalid_coverage_status", [])),
        "chapter_summary_duplicate_source_chapter_order": len(
            chapter_issues.get("duplicate_source_chapter_order", [])
        ),
        "markdown_files_with_replacement_char": len(files_with_replacement_char()),
    }


def write_audit_report(summary: dict[str, int], actions: dict[str, int], dry_run: bool) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = AUDIT_DIR / f"Vault_Maintenance_Audit_{stamp}.md"
    lines = [
        "---",
        "id: VAULT-MAINTENANCE-AUDIT",
        "type: report",
        "status: active",
        f"created: {TODAY}",
        "tags:",
        "  - audit",
        "  - maintenance",
        "---",
        "",
        "# Vault Maintenance Audit",
        "",
        "## Actions",
        "",
    ]
    for key, value in actions.items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Snapshot", ""])
    for key, value in summary.items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Next Review Targets",
            "",
            "- Review `Fact_Card_Metadata_Review.md` for printed-page verification candidates.",
            "- Expand additional high-link generated stubs into narrative notes where they support scene design.",
            "- Continue Hamnett ingestion after confirming the Obsidian views are usable.",
        ]
    )
    if not dry_run:
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def run(dry_run: bool, phase: str = "all") -> dict[str, int | str]:
    notes = note_map(include_outputs=False)
    actions: dict[str, int] = {}

    if phase in {"all", "stub-expansion"}:
        checked, changed = enrich_generated_stubs(notes, dry_run=dry_run)
        actions["generated_stubs_checked"] = checked
        actions["generated_stubs_enriched"] = changed

        notes = note_map(include_outputs=False)
        selected, top_changed = enrich_top_stubs(notes, dry_run=dry_run, limit=50)
        actions["top_stubs_selected_for_quality_sections"] = selected
        actions["top_stubs_quality_sections_added"] = top_changed

        notes = note_map(include_outputs=False)
        high_selected, high_changed = enrich_high_link_stubs(notes, dry_run=dry_run, min_backlinks=10)
        actions["high_link_stubs_selected_for_quality_sections"] = high_selected
        actions["high_link_stubs_quality_sections_added"] = high_changed

    if phase in {"all", "printed-page-review"}:
        source_touched, source_normalized, examples_marked = normalize_known_source_records(dry_run=dry_run)
        actions["known_source_records_touched"] = source_touched
        actions["source_ids_normalized"] = source_normalized
        actions["example_records_marked"] = examples_marked

        notes = note_map(include_outputs=False)
        fact_touched, statement_added, printed_candidate_added, printed_status_added = repair_fact_cards(notes, dry_run=dry_run)
        actions["fact_cards_touched"] = fact_touched
        actions["statements_added_from_claim"] = statement_added
        actions["printed_page_candidates_added"] = printed_candidate_added
        actions["printed_page_status_added"] = printed_status_added

    if phase == "all":
        notes = note_map(include_outputs=False)
        timeline_touched, fact_timeline_touched = strengthen_timeline_links(notes, dry_run=dry_run)
        actions["timeline_entries_with_evidence_section"] = timeline_touched
        actions["fact_cards_with_timeline_backlinks"] = fact_timeline_touched

    notes = note_map(include_outputs=False)
    if phase in {"all", "printed-page-review"}:
        actions["indexes_written"] = write_indexes(notes, dry_run=dry_run)
        review_path = write_fact_metadata_review(dry_run=dry_run)
        printed_page_candidates_path = write_printed_page_candidates(notes, dry_run=dry_run, limit=200)
        chapter_summary_review_path = write_chapter_summary_metadata_review(dry_run=dry_run)
    else:
        review_path = AUDIT_DIR / "Fact_Card_Metadata_Review.md"
        printed_page_candidates_path = AUDIT_DIR / "Printed_Page_Verification_Candidates.md"
        chapter_summary_review_path = AUDIT_DIR / "Chapter_Summary_Metadata_Review.md"

    if phase in {"all", "stub-expansion"}:
        actions["writing_views_written"] = write_writing_views(notes, dry_run=dry_run)
        stub_review_path = write_stub_priority_review(notes, dry_run=dry_run)
    else:
        stub_review_path = AUDIT_DIR / "Stub_Priority_Review.md"

    if phase == "all":
        example_records_path = write_example_records_doc(notes, dry_run=dry_run)
        hamnett_readiness_path = write_hamnett_readiness(notes, dry_run=dry_run)
        actions["example_records_docs_written"] = 1
        actions["hamnett_readiness_reports_written"] = 1
    else:
        example_records_path = ROOT / "93_Docs" / "Example_Records.md"
        hamnett_readiness_path = AUDIT_DIR / "Hamnett_Ingestion_Readiness.md"

    notes = note_map(include_outputs=False)
    snapshot = validation_snapshot(notes)
    audit_path = write_audit_report(snapshot, actions, dry_run=dry_run)

    result: dict[str, int | str] = {**actions, **snapshot}
    result["fact_card_review"] = str(review_path)
    result["printed_page_candidates"] = str(printed_page_candidates_path)
    result["chapter_summary_review"] = str(chapter_summary_review_path)
    result["stub_priority_review"] = str(stub_review_path)
    result["example_records"] = str(example_records_path)
    result["hamnett_readiness"] = str(hamnett_readiness_path)
    result["audit_report"] = str(audit_path)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write maintenance changes")
    parser.add_argument(
        "--phase",
        choices=("all", "printed-page-review", "stub-expansion"),
        default="all",
        help="run only one maintenance phase",
    )
    args = parser.parse_args()
    result = run(dry_run=not args.apply, phase=args.phase)
    print(f"mode: {'apply' if args.apply else 'dry-run'}")
    print(f"phase: {args.phase}")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
