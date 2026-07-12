from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

KIND_DIRS = {
    "event": ROOT / "04_Events",
    "organization": ROOT / "03_Entities" / "Organizations",
    "place": ROOT / "03_Entities" / "Places",
    "theme": ROOT / "03_Entities" / "Themes",
}

ID_PREFIX = {
    "event": "EVT",
    "organization": "ORG",
    "place": "PLC",
    "theme": "THM",
}

OLD_KIND_TAGS = {"person", "organization", "place", "theme", "event"}

RECLASSIFY = {
    # People -> events
    "American_Civil_War": "event",
    "Austro_Prussian_War": "event",
    "Crimean_War": "event",
    "Execution_Of_Maximilian_Miramon_And_Mejia": "event",
    "First_World_War": "event",
    "Franco_Prussian_War": "event",
    "Italian_War": "event",
    "Marquez_Vidaurri_Mexico_City": "event",
    "Mexican_American_War": "event",
    "North_American_Revolution": "event",
    "Spanish_American_War": "event",
    "US_Mexican_War": "event",
    "U_S_Mexican_War": "event",
    # People -> organizations / polities / institutions
    "Aztec_Empire": "organization",
    "Brazilian_Empire": "organization",
    "British_Legation": "organization",
    "Central_American_Federation": "organization",
    "Confederate_States": "organization",
    "Early_Mexican_Empire": "organization",
    "El_Monitor_Republicano": "organization",
    "Empress_Regiment": "organization",
    "First_Federal_Republic": "organization",
    "Frances_Third_Republic": "organization",
    "Mexican_Republic": "organization",
    "Ottoman_Empire": "organization",
    "Restored_Republic": "organization",
    "Russian_Empire": "organization",
    "Second_French_Empire": "organization",
    "Venetian_Republic": "organization",
    # People -> places
    "Bouchout_Castle": "place",
    "Central_America": "place",
    "Chapultepec_Castle": "place",
    "Fort_Guadalupe": "place",
    "Fort_Loreto": "place",
    "Latin_America": "place",
    "North_America": "place",
    "South_America": "place",
    "Spanish_North_America": "place",
    "Tervuren_Castle": "place",
    # People -> themes
    "Colonial_Economy": "theme",
    "Constitutional_Restructuring": "theme",
    "Early_Liberalism": "theme",
    "External_Pressure": "theme",
    "Latin_American_Liberalism": "theme",
    "Mining_Economy": "theme",
    "Political_Economy": "theme",
    "Spanish_American_Political_Tradition": "theme",
    "Unitary_State": "theme",
    "Written_Constitution": "theme",
    # Organizations -> events/processes
    "Belgian_Monarchy_Establishment": "event",
    "Conservative_Ministry_Resignation_Crisis": "event",
    "Court_Crisis": "event",
    "Court_Etiquette_Incident": "event",
    "Drafting_Of_Imperial_Court_Etiquette": "event",
    "Formation_Of_Maximilians_Government": "event",
    # Organizations -> themes
    "Absolute_Monarchy": "theme",
    "Alternative_Monarchy": "theme",
    "Army_Reform": "theme",
    "Carlotas_Early_Court_Etiquette_Conflicts": "theme",
    "Catholic_Monarchy": "theme",
    "Ceremonial_Monarchy": "theme",
    "Confederate_Service_In_Maximilians_Government": "theme",
    "Conservative_Monarchy": "theme",
    "Court_Culture": "theme",
    "Court_Diplomacy": "theme",
    "Court_Etiquette": "theme",
    "Court_Ritual": "theme",
    "European_Court_Culture": "theme",
    "European_Monarchy": "theme",
    "Exile_Monarchy": "theme",
    "Foreign_Court_Culture": "theme",
    "Foreign_Monarchy": "theme",
    "French_Court_Culture": "theme",
    "French_Criticism_Of_Maximilians_Government": "theme",
    "French_Former_Monarchy": "theme",
    "Greek_Monarchy_Comparison": "theme",
    "Informal_Monarchy": "theme",
    "Liberal_Monarchy": "theme",
    "Luxury_Versus_Government": "theme",
    "Maximilian_Monarchy_Project": "theme",
    "Misgovernment": "theme",
    "Monarchy_And_Nationalism": "theme",
    "Monarchy_And_Subjects": "theme",
    "Monarchy_Building": "theme",
    "Monarchy_In_The_Americas": "theme",
    "Monarchy_Project": "theme",
    "Monarchy_Propaganda": "theme",
    "Monarchy_Rhetoric": "theme",
    "Monarchy_Spectacle": "theme",
    "Monarchy_Support": "theme",
    "Monarchy_Vs_Republic": "theme",
    "Multiethnic_Monarchy": "theme",
    "New_Monarchy": "theme",
    "Opposition_To_European_Monarchy_In_America": "theme",
    "Parvenu_Monarchy": "theme",
    "Paternal_Monarchy": "theme",
    "Planned_Rupture_With_Juarez_Government": "theme",
    "US_Non_Recognition_Of_Maximilians_Government": "theme",
    "Volunteer_Legion_Planning": "theme",
    # Places -> corrected kinds
    "Agriculture": "theme",
    "Republicans": "organization",
}


def find_note(stem: str) -> Path | None:
    matches = [p for p in ROOT.rglob(f"{stem}.md") if ".obsidian" not in p.parts]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        return None
    raise RuntimeError(f"Ambiguous source for {stem}: {matches}")


def split_frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---"):
        return None
    marker = "\n---"
    end = text.find(marker, 3)
    if end == -1:
        return None
    return text[4:end], text[end + len(marker) :]


def update_tags(lines: list[str], new_kind: str) -> list[str]:
    out: list[str] = []
    i = 0
    handled = False
    while i < len(lines):
        line = lines[i]
        if line.startswith("tags:"):
            handled = True
            out.append("tags:")
            i += 1
            tags: list[str] = []
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].strip() == ""):
                stripped = lines[i].strip()
                if stripped.startswith("- "):
                    value = stripped[2:].strip().strip('"').strip("'")
                    if value and value not in OLD_KIND_TAGS and value not in tags:
                        tags.append(value)
                i += 1
            out.append(f"  - {new_kind}")
            for tag in tags:
                if tag != new_kind:
                    out.append(f"  - {tag}")
            continue
        out.append(line)
        i += 1
    if not handled:
        insert_at = 0
        for idx, line in enumerate(out):
            if line.startswith("type:"):
                insert_at = idx + 1
                break
        out[insert_at:insert_at] = ["tags:", f"  - {new_kind}"]
    return out


def update_frontmatter(text: str, stem: str, new_kind: str) -> str:
    prefix = ID_PREFIX[new_kind]
    parts = split_frontmatter(text)
    if parts is None:
        fm_lines = [
            f"id: {prefix}-{stem.upper()}",
            f"type: {new_kind}",
            "status: draft",
            "tags:",
            f"  - {new_kind}",
        ]
        return "---\n" + "\n".join(fm_lines) + "\n---\n\n" + text

    frontmatter, body = parts
    lines = frontmatter.splitlines()
    seen_id = False
    seen_type = False
    updated: list[str] = []
    for line in lines:
        if line.startswith("id:"):
            updated.append(f"id: {prefix}-{stem.upper()}")
            seen_id = True
        elif line.startswith("type:"):
            updated.append(f"type: {new_kind}")
            seen_type = True
        else:
            updated.append(line)
    if not seen_id:
        updated.insert(0, f"id: {prefix}-{stem.upper()}")
    if not seen_type:
        updated.insert(1, f"type: {new_kind}")
    updated = update_tags(updated, new_kind)
    return "---\n" + "\n".join(updated).rstrip() + "\n---" + body


def reclassify(dry_run: bool) -> tuple[list[tuple[str, str, str]], list[tuple[str, str]]]:
    moved: list[tuple[str, str, str]] = []
    skipped: list[tuple[str, str]] = []
    for stem, new_kind in sorted(RECLASSIFY.items()):
        try:
            source = find_note(stem)
        except RuntimeError as exc:
            skipped.append((stem, str(exc)))
            continue
        if source is None:
            skipped.append((stem, "source not found"))
            continue
        destination = KIND_DIRS[new_kind] / source.name
        if source.resolve() == destination.resolve():
            text = source.read_text(encoding="utf-8")
            updated = update_frontmatter(text, stem, new_kind)
            if text != updated and not dry_run:
                source.write_text(updated, encoding="utf-8", newline="\n")
            moved.append((stem, str(source.relative_to(ROOT)), "frontmatter only"))
            continue
        if destination.exists():
            skipped.append((stem, f"destination exists: {destination.relative_to(ROOT)}"))
            continue
        moved.append((stem, str(source.relative_to(ROOT)), str(destination.relative_to(ROOT))))
        if dry_run:
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8")
        updated = update_frontmatter(text, stem, new_kind)
        source.write_text(updated, encoding="utf-8", newline="\n")
        shutil.move(str(source), str(destination))
    return moved, skipped


def write_report(moved: list[tuple[str, str, str]], skipped: list[tuple[str, str]], dry_run: bool) -> Path:
    report_dir = ROOT / "08_Outputs" / "Link_Resolution"
    report_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    mode = "dry_run" if dry_run else "apply"
    report = report_dir / f"Reclassification_{stamp}_{mode}.md"
    lines = [
        "---",
        "id: RECLASSIFICATION-REPORT",
        "type: report",
        "status: active",
        f"created: {datetime.now().date().isoformat()}",
        "tags:",
        "  - link-resolution",
        "  - reclassification",
        "---",
        "",
        f"# Reclassification Report ({mode})",
        "",
        "## Summary",
        "",
        f"- Planned/applied moves: {len(moved)}",
        f"- Skipped: {len(skipped)}",
        "",
        "## Moves",
        "",
        "| Stem | From | To |",
        "| --- | --- | --- |",
    ]
    for stem, src, dst in moved:
        lines.append(f"| `{stem}` | `{src}` | `{dst}` |")
    if skipped:
        lines.extend(["", "## Skipped", "", "| Stem | Reason |", "| --- | --- |"])
        for stem, reason in skipped:
            lines.append(f"| `{stem}` | {reason} |")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return report


def run(args: argparse.Namespace) -> int:
    dry_run = not args.apply
    moved, skipped = reclassify(dry_run=dry_run)
    report: Path | str
    if args.no_report:
        report = "(disabled)"
    else:
        report = write_report(moved, skipped, dry_run=dry_run)
    print(f"mode: {'apply' if args.apply else 'dry-run'}")
    print(f"report: {report}")
    print(f"moves: {len(moved)}")
    print(f"skipped: {len(skipped)}")
    for stem, reason in skipped[:20]:
        print(f"skipped: {stem}: {reason}")
    return 1 if args.check and skipped else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="apply reclassification changes")
    parser.add_argument("--no-report", action="store_true", help="do not write a Markdown report")
    parser.add_argument("--check", action="store_true", help="return non-zero if any item would be skipped")
    return run(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
