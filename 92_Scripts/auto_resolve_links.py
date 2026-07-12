#!/usr/bin/env python3
"""
Analyze and resolve unresolved Obsidian wiki links in MexicoEmpire_NovelDB.

Modes:
  analyze: write a Markdown report with candidates only.
  apply: create entry notes, rewrite selected wiki links, and write a report.

The script only rewrites wiki links. It does not modify ordinary prose.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WIKI_LINK_RE = re.compile(r"(?<![!\\])\[\[([^\]\n]+?)\]\]")
FENCED_CODE_RE = re.compile(r"^```.*?^```", re.M | re.S)

KIND_PATHS = {
    "person": Path("03_Entities/People"),
    "place": Path("03_Entities/Places"),
    "organization": Path("03_Entities/Organizations"),
    "theme": Path("03_Entities/Themes"),
    "event": Path("04_Events"),
}

KIND_TAGS = {
    "person": "person",
    "place": "place",
    "organization": "organization",
    "theme": "theme",
    "event": "event",
}

DEFAULT_RULES = {
    "min_count": 15,
    "exclude_terms": [],
    "explicit_mappings": {},
    "place_terms": [],
    "person_terms": [],
    "organization_keywords": [],
    "event_keywords": [],
    "theme_keywords": [],
}


@dataclass(frozen=True)
class LinkOccurrence:
    file: Path
    target: str


@dataclass(frozen=True)
class Candidate:
    source: str
    target: str
    kind: str
    count: int
    action: str
    reason: str


@dataclass(frozen=True)
class UnlinkCandidate:
    source: str
    count: int
    reason: str


def load_rules(path: Path) -> dict[str, Any]:
    if not path.exists():
        return DEFAULT_RULES.copy()
    data = json.loads(path.read_text(encoding="utf-8"))
    merged = DEFAULT_RULES.copy()
    merged.update(data)
    return merged


def vault_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def iter_markdown_files(root: Path) -> list[Path]:
    return [
        path
        for path in root.rglob("*.md")
        if ".obsidian" not in path.parts
        and not (
            "08_Outputs" in path.parts
            and "Link_Resolution" in path.parts
        )
    ]


def split_wiki_inner(inner: str) -> tuple[str, str, str | None]:
    pipe_index = inner.find("|")
    if pipe_index >= 0:
        left = inner[:pipe_index]
        alias = inner[pipe_index + 1 :]
    else:
        left = inner
        alias = None
    hash_index = left.find("#")
    if hash_index >= 0:
        target = left[:hash_index].strip()
        anchor = left[hash_index:]
    else:
        target = left.strip()
        anchor = ""
    return target, anchor, alias


def iter_wiki_matches(text: str) -> list[re.Match[str]]:
    matches: list[re.Match[str]] = []
    last = 0
    for fence in FENCED_CODE_RE.finditer(text):
        matches.extend(WIKI_LINK_RE.finditer(text, last, fence.start()))
        last = fence.end()
    matches.extend(WIKI_LINK_RE.finditer(text, last))
    return matches


def replace_wiki_links(text: str, replacement: Any) -> str:
    parts: list[str] = []
    last = 0
    for fence in FENCED_CODE_RE.finditer(text):
        parts.append(WIKI_LINK_RE.sub(replacement, text[last : fence.start()]))
        parts.append(text[fence.start() : fence.end()])
        last = fence.end()
    parts.append(WIKI_LINK_RE.sub(replacement, text[last:]))
    return "".join(parts)


def existing_note_names(files: list[Path]) -> set[str]:
    return {path.stem for path in files}


def link_exists(root: Path, names: set[str], target: str) -> bool:
    if "/" in target:
        return (root / f"{target}.md").exists()
    return target in names


def collect_unresolved(root: Path) -> tuple[Counter[str], dict[str, list[Path]]]:
    files = iter_markdown_files(root)
    names = existing_note_names(files)
    counts: Counter[str] = Counter()
    locations: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in iter_wiki_matches(text):
            target, _anchor, _alias = split_wiki_inner(match.group(1))
            if not target:
                continue
            if not link_exists(root, names, target):
                counts[target] += 1
                if len(locations[target]) < 5:
                    locations[target].append(path)
    return counts, locations


def ascii_fold(value: str) -> str:
    replacements = {
        "ł": "l",
        "Ł": "L",
        "đ": "d",
        "Đ": "D",
        "ß": "ss",
        "æ": "ae",
        "Æ": "AE",
        "œ": "oe",
        "Œ": "OE",
    }
    for source, replacement in replacements.items():
        value = value.replace(source, replacement)
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(char for char in normalized if not unicodedata.combining(char))


def normalize_target(label: str) -> str:
    value = ascii_fold(label.strip())
    value = value.replace("&", " and ")
    value = value.replace("'", "")
    value = value.replace("’", "")
    value = value.replace("`", "")
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    if not value:
        value = "Untitled_Link"
    value = "_".join(part[:1].upper() + part[1:] for part in value.split("_") if part)
    if value[0].isdigit():
        value = "N_" + value
    return value


def title_for(label: str) -> str:
    return label.replace("_", " ").strip()


def infer_kind(label: str, rules: dict[str, Any]) -> tuple[str | None, str]:
    if label in set(rules.get("place_terms", [])):
        return "place", "place_terms"
    if label in set(rules.get("person_terms", [])):
        return "person", "person_terms"

    label_lower = label.lower()
    for keyword in rules.get("organization_keywords", []):
        if keyword.lower() in label_lower:
            return "organization", f"organization keyword: {keyword}"
    for keyword in rules.get("event_keywords", []):
        if keyword.lower() in label_lower:
            return "event", f"event keyword: {keyword}"
    for keyword in rules.get("theme_keywords", []):
        if keyword.lower() in label_lower:
            return "theme", f"theme keyword: {keyword}"

    if "," in label:
        return "person", "comma-form personal name"
    words = [word for word in re.split(r"\s+", label.replace("_", " ")) if word]
    if 2 <= len(words) <= 4 and all(word[:1].isupper() for word in words if word[:1].isalpha()):
        return "person", "title-case name heuristic"
    if len(words) <= 3 and all(word[:1].isupper() for word in words if word[:1].isalpha()):
        return "place", "title-case place heuristic"
    return None, "no confident rule"


def is_lowercase_generic(label: str) -> bool:
    words = [word for word in re.split(r"\s+", label.replace("_", " ")) if word]
    if not words:
        return True
    has_letter = any(any(char.isalpha() for char in word) for word in words)
    if not has_letter:
        return True
    return not any(word[:1].isupper() for word in words if word[:1].isalpha())


def build_candidates(
    root: Path,
    counts: Counter[str],
    rules: dict[str, Any],
    limit: int,
) -> tuple[list[Candidate], list[tuple[str, int, str]]]:
    files = iter_markdown_files(root)
    names = existing_note_names(files)
    excluded = {term.casefold() for term in rules.get("exclude_terms", [])}
    explicit = rules.get("explicit_mappings", {})
    min_count = int(rules.get("min_count", 1))
    candidates: list[Candidate] = []
    skipped: list[tuple[str, int, str]] = []

    for source, count in sorted(counts.items(), key=lambda item: (-item[1], item[0].casefold())):
        if len(candidates) >= limit:
            break
        if count < min_count:
            skipped.append((source, count, f"below min_count {min_count}"))
            continue
        if source.casefold() in excluded:
            skipped.append((source, count, "excluded by rules"))
            continue

        if source in explicit:
            entry = explicit[source]
            target = entry["target"]
            kind = entry.get("kind")
            if not kind:
                kind, reason = infer_kind(source, rules)
            else:
                reason = "explicit mapping"
        else:
            target = normalize_target(source)
            kind, reason = infer_kind(source, rules)

        if not kind or kind not in KIND_PATHS:
            skipped.append((source, count, reason))
            continue

        action = "map_existing" if target in names or (root / f"{target}.md").exists() else "create_and_map"
        candidates.append(Candidate(source, target, kind, count, action, reason))

    return candidates, skipped


def build_finalize_candidates(
    root: Path,
    counts: Counter[str],
    rules: dict[str, Any],
) -> tuple[list[Candidate], list[UnlinkCandidate], list[tuple[str, int, str]]]:
    files = iter_markdown_files(root)
    names = existing_note_names(files)
    excluded = {term.casefold() for term in rules.get("exclude_terms", [])}
    explicit = rules.get("explicit_mappings", {})
    candidates: list[Candidate] = []
    unlink: list[UnlinkCandidate] = []
    skipped: list[tuple[str, int, str]] = []

    for source, count in sorted(counts.items(), key=lambda item: (-item[1], item[0].casefold())):
        if source.casefold() in excluded:
            if rules.get("unlink_generics"):
                unlink.append(UnlinkCandidate(source, count, "excluded classification/general term"))
            else:
                skipped.append((source, count, "excluded by rules; pass --unlink-generics to unlink"))
            continue

        if source in explicit:
            entry = explicit[source]
            target = entry["target"]
            kind = entry.get("kind")
            reason = "explicit mapping"
        else:
            target = normalize_target(source)
            kind, reason = infer_kind(source, rules)

        if not kind or kind not in KIND_PATHS:
            if is_lowercase_generic(source):
                if rules.get("unlink_generics"):
                    unlink.append(UnlinkCandidate(source, count, "lowercase generic phrase"))
                else:
                    skipped.append((source, count, "lowercase generic phrase; pass --unlink-generics to unlink"))
                continue
            kind = "theme"
            reason = f"fallback theme after {reason}"

        action = "map_existing" if target in names or (root / f"{target}.md").exists() else "create_and_map"
        candidates.append(Candidate(source, target, kind, count, action, reason))

    return candidates, unlink, skipped


def frontmatter_id(kind: str, target: str) -> str:
    prefixes = {
        "person": "PER",
        "place": "PLC",
        "organization": "ORG",
        "theme": "THM",
        "event": "EVT",
    }
    return f"{prefixes[kind]}-{target.upper()}"


def note_path(root: Path, candidate: Candidate) -> Path:
    return root / KIND_PATHS[candidate.kind] / f"{candidate.target}.md"


def note_body(candidate: Candidate, today: str) -> str:
    label = title_for(candidate.source)
    tag = KIND_TAGS[candidate.kind]
    note_id = frontmatter_id(candidate.kind, candidate.target)

    common = [
        "---",
        f"id: {note_id}",
        f"type: {tag}",
        "status: draft",
        f"created: {today}",
        f"updated: {today}",
        "tags:",
        f"  - {tag}",
        'source_id: ""',
        'chapter: ""',
        'page: ""',
        'kindle_location: ""',
        'screenshot_file: ""',
    ]

    if candidate.kind == "person":
        common += [
            f'canonical_name: "{label}"',
            "aliases:",
            f'  - "{candidate.source}"',
            'birth_date: ""',
            'death_date: ""',
            "roles: []",
            "---",
            "",
            f"# {label}",
            "",
            "## Overview",
            "",
            f"Entry note for {label}. Verify details in linked Fact Cards and Timeline Entries.",
            "",
            "## Relationships",
            "",
            "- People:",
            "- Organizations:",
            "- Places:",
            "- Events:",
            "- Themes:",
            "",
            "## Fact Cards",
            "",
            "-",
            "",
            "## Source Notes",
            "",
            "-",
        ]
    elif candidate.kind == "place":
        common += [
            f'canonical_name: "{label}"',
            "aliases:",
            f'  - "{candidate.source}"',
            'modern_country: ""',
            'coordinates: ""',
            "---",
            "",
            f"# {label}",
            "",
            "## Overview",
            "",
            f"Entry note for {label}. Verify details in linked Fact Cards and Timeline Entries.",
            "",
            "## Linked Items",
            "",
            "- People:",
            "- Events:",
            "- Organizations:",
            "- Themes:",
            "- Fact Cards:",
            "- Timeline Entries:",
            "",
            "## Source Notes",
            "",
            "-",
        ]
    elif candidate.kind == "organization":
        common += [
            f'canonical_name: "{label}"',
            "aliases:",
            f'  - "{candidate.source}"',
            'organization_kind: ""',
            'date_start: ""',
            'date_end: ""',
            "---",
            "",
            f"# {label}",
            "",
            "## Overview",
            "",
            f"Entry note for {label}. Verify details in linked Fact Cards and Timeline Entries.",
            "",
            "## Linked Items",
            "",
            "- People:",
            "- Events:",
            "- Places:",
            "- Themes:",
            "- Fact Cards:",
            "",
            "## Source Notes",
            "",
            "-",
        ]
    elif candidate.kind == "event":
        common += [
            'date_start: ""',
            'date_end: ""',
            'date_precision: ""',
            "places: []",
            "people: []",
            "organizations: []",
            "themes: []",
            "---",
            "",
            f"# {label}",
            "",
            "## Summary",
            "",
            f"Entry note for {label}. Verify chronology and actors in linked Fact Cards and Timeline Entries.",
            "",
            "## Actors",
            "",
            "- People:",
            "- Organizations:",
            "",
            "## Places",
            "",
            "-",
            "",
            "## Themes",
            "",
            "-",
            "",
            "## Fact Cards",
            "",
            "-",
            "",
            "## Timeline Entries",
            "",
            "-",
        ]
    else:
        common += [
            'theme_kind: ""',
            "---",
            "",
            f"# {label}",
            "",
            "## Definition",
            "",
            f"Entry note for {label}. Keep historical evidence, interpretation, and creative use separate.",
            "",
            "## Linked Items",
            "",
            "- People:",
            "- Events:",
            "- Places:",
            "- Organizations:",
            "- Fact Cards:",
            "",
            "## Source Notes",
            "",
            "-",
        ]

    return "\n".join(common) + "\n"


def create_notes(root: Path, candidates: list[Candidate]) -> list[Path]:
    today = dt.date.today().isoformat()
    created: list[Path] = []
    for candidate in candidates:
        path = note_path(root, candidate)
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(note_body(candidate, today), encoding="utf-8", newline="\n")
        created.append(path)
    return created


def rewrite_links(
    root: Path,
    candidates: list[Candidate],
    unlink_sources: list[UnlinkCandidate] | None = None,
) -> tuple[int, int, Counter[str], Counter[str]]:
    mapping = {candidate.source: candidate.target for candidate in candidates}
    unlink_set = {candidate.source for candidate in unlink_sources or []}
    counts: Counter[str] = Counter()
    unlink_counts: Counter[str] = Counter()
    files_changed = 0
    links_changed = 0

    def replace_match(match: re.Match[str]) -> str:
        nonlocal links_changed
        target, anchor, alias = split_wiki_inner(match.group(1))
        if target not in mapping:
            if target not in unlink_set:
                return match.group(0)
            unlink_counts[target] += 1
            links_changed += 1
            return alias if alias is not None else target
        new_target = mapping[target]
        counts[target] += 1
        links_changed += 1
        if alias is not None:
            return f"[[{new_target}{anchor}|{alias}]]"
        if new_target == target:
            return f"[[{new_target}{anchor}]]"
        return f"[[{new_target}{anchor}|{target}]]"

    for path in iter_markdown_files(root):
        text = path.read_text(encoding="utf-8")
        new_text = replace_wiki_links(text, replace_match)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            files_changed += 1

    return files_changed, links_changed, counts, unlink_counts


def unresolved_stats(root: Path) -> dict[str, Any]:
    counts, _locations = collect_unresolved(root)
    total = sum(counts.values())
    return {
        "total_occurrences": total,
        "unique_targets": len(counts),
        "top": sorted(counts.items(), key=lambda item: (-item[1], item[0].casefold()))[:50],
    }


def check_new_note_links(root: Path, paths: list[Path]) -> list[tuple[Path, str]]:
    files = iter_markdown_files(root)
    names = existing_note_names(files)
    missing: list[tuple[Path, str]] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for match in iter_wiki_matches(text):
            target, _anchor, _alias = split_wiki_inner(match.group(1))
            if not link_exists(root, names, target):
                missing.append((path, target))
    return missing


def report_path(root: Path, mode: str) -> Path:
    out_dir = root / "08_Outputs" / "Link_Resolution"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    return out_dir / f"Link_Resolution_{stamp}_{mode}.md"


def write_report(
    root: Path,
    mode: str,
    before: dict[str, Any],
    after: dict[str, Any] | None,
    candidates: list[Candidate],
    skipped: list[tuple[str, int, str]],
    created: list[Path],
    rewrite_counts: Counter[str],
    unlink_counts: Counter[str],
    files_changed: int,
    links_changed: int,
    new_note_missing: list[tuple[Path, str]],
) -> Path:
    lines: list[str] = []
    lines += [
        "---",
        "id: LINK-RESOLUTION-REPORT",
        "type: report",
        "status: active",
        f"created: {dt.date.today().isoformat()}",
        "tags:",
        "  - link-resolution",
        "  - report",
        "---",
        "",
        f"# Link Resolution Report ({mode})",
        "",
        "## Summary",
        "",
        f"- Before unresolved occurrences: {before['total_occurrences']}",
        f"- Before unique unresolved targets: {before['unique_targets']}",
    ]
    if after is not None:
        lines += [
            f"- After unresolved occurrences: {after['total_occurrences']}",
            f"- After unique unresolved targets: {after['unique_targets']}",
        ]
    lines += [
        f"- Candidates selected: {len(candidates)}",
        f"- Notes created: {len(created)}",
        f"- Files changed: {files_changed}",
        f"- Links changed: {links_changed}",
        "",
        "## Selected Candidates",
        "",
        "| Count | Source | Target | Kind | Action | Reason |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for candidate in candidates:
        lines.append(
            f"| {candidate.count} | `{candidate.source}` | `{candidate.target}` | "
            f"`{candidate.kind}` | `{candidate.action}` | {candidate.reason} |"
        )
    lines += ["", "## Created Notes", ""]
    if created:
        for path in created:
            rel = path.relative_to(root).as_posix()
            lines.append(f"- [[{rel[:-3]}]]")
    else:
        lines.append("- None")
    lines += ["", "## Replacement Counts", ""]
    if rewrite_counts:
        for source, count in rewrite_counts.most_common():
            lines.append(f"- `{source}`: {count}")
    else:
        lines.append("- None")
    lines += ["", "## Unlinked Counts", ""]
    if unlink_counts:
        for source, count in unlink_counts.most_common():
            lines.append(f"- `{source}`: {count}")
    else:
        lines.append("- None")
    lines += ["", "## Skipped Examples", ""]
    for source, count, reason in skipped[:50]:
        lines.append(f"- `{source}` ({count}): {reason}")
    if new_note_missing:
        lines += ["", "## New Note Link Problems", ""]
        for path, target in new_note_missing:
            rel = path.relative_to(root).as_posix()
            lines.append(f"- `{rel}` -> `{target}`")
    lines += ["", "## Remaining Top Unresolved", ""]
    top = (after or before)["top"]
    for source, count in top:
        lines.append(f"- `{source}`: {count}")

    path = report_path(root, mode)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def run(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else vault_root_from_script()
    rules_path = Path(args.rules).resolve() if args.rules else root / "92_Scripts" / "link_resolution_rules.json"
    rules = load_rules(rules_path)

    before = unresolved_stats(root)
    counts, _locations = collect_unresolved(root)
    unlink_sources: list[UnlinkCandidate] = []
    if args.mode == "finalize":
        rules_for_finalize = dict(rules)
        rules_for_finalize["unlink_generics"] = args.unlink_generics
        candidates, unlink_sources, skipped = build_finalize_candidates(root, counts, rules_for_finalize)
    else:
        candidates, skipped = build_candidates(root, counts, rules, args.limit)

    created: list[Path] = []
    rewrite_counts: Counter[str] = Counter()
    unlink_counts: Counter[str] = Counter()
    files_changed = 0
    links_changed = 0
    new_note_missing: list[tuple[Path, str]] = []
    after: dict[str, Any] | None = None

    if args.mode in {"apply", "finalize"}:
        created = create_notes(root, candidates)
        files_changed, links_changed, rewrite_counts, unlink_counts = rewrite_links(
            root,
            candidates,
            unlink_sources,
        )
        new_note_missing = check_new_note_links(root, created)
        after = unresolved_stats(root)

    report: Path | str
    if args.no_report:
        report = "(disabled)"
    else:
        report = write_report(
            root=root,
            mode=args.mode,
            before=before,
            after=after,
            candidates=candidates,
            skipped=skipped,
            created=created,
            rewrite_counts=rewrite_counts,
            unlink_counts=unlink_counts,
            files_changed=files_changed,
            links_changed=links_changed,
            new_note_missing=new_note_missing,
        )

    print(f"mode: {args.mode}")
    print(f"report: {report}")
    print(f"before_unresolved_occurrences: {before['total_occurrences']}")
    print(f"before_unique_unresolved: {before['unique_targets']}")
    print(f"candidates: {len(candidates)}")
    if after is not None:
        print(f"after_unresolved_occurrences: {after['total_occurrences']}")
        print(f"after_unique_unresolved: {after['unique_targets']}")
        print(f"notes_created: {len(created)}")
        print(f"files_changed: {files_changed}")
        print(f"links_changed: {links_changed}")
        print(f"new_note_link_problems: {len(new_note_missing)}")
    return 1 if new_note_missing else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["analyze", "apply", "finalize"], required=True)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--root", default="")
    parser.add_argument("--rules", default="")
    parser.add_argument("--no-report", action="store_true", help="do not write a Markdown report")
    parser.add_argument(
        "--unlink-generics",
        action="store_true",
        help="in finalize mode, convert excluded/lowercase generic wiki links to plain text",
    )
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(run(parse_args()))
