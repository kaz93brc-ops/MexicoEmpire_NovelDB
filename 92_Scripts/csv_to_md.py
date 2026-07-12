#!/usr/bin/env python3
"""
Convert CSV rows into Obsidian Markdown notes for MexicoEmpire_NovelDB.

The script never overwrites existing files unless --overwrite is given.
CSV list fields use semicolon-separated values, for example:
people = Maximilian;Carlota
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from pathlib import Path


LIST_FIELDS = {
    "tags",
    "people",
    "events",
    "places",
    "organizations",
    "themes",
    "related_fact_cards",
    "related_questions",
    "questions",
}

BASE_FIELDS = [
    "id",
    "type",
    "status",
    "created",
    "updated",
    "tags",
    "source_id",
    "chapter",
    "page",
    "kindle_location",
    "screenshot_file",
]

EVIDENCE_CATEGORY_VALUES = {
    "historical_fact",
    "primary_testimony",
    "author_interpretation",
    "rumor_hearsay",
    "variant_disputed",
    "creative_inference",
}

CONFIDENCE_VALUES = {
    "confirmed",
    "probable",
    "uncertain",
    "disputed",
    "fictionalized",
}

REQUIRED_COLUMNS = {
    "fact_cards": {
        "id",
        "title",
        "status",
        "created",
        "updated",
        "tags",
        "source_id",
        "chapter",
        "page",
        "kindle_location",
        "screenshot_file",
        "evidence_category",
        "confidence",
        "claim",
        "summary",
        "evidence_note",
        "limitations",
        "creative_use",
        "people",
        "events",
        "places",
        "organizations",
        "themes",
        "related_fact_cards",
        "related_questions",
    },
    "captures": {
        "id",
        "title",
        "status",
        "created",
        "updated",
        "tags",
        "source_id",
        "source_title",
        "chapter",
        "page",
        "kindle_location",
        "screenshot_file",
        "capture_date",
        "capture_type",
        "summary",
        "extracted_claims",
        "direct_quote_short",
        "people",
        "events",
        "places",
        "organizations",
        "themes",
        "questions",
        "creative_notes",
        "next_action",
    },
    "timeline": {
        "id",
        "title",
        "status",
        "created",
        "updated",
        "tags",
        "date_start",
        "date_end",
        "date_precision",
        "calendar",
        "evidence_category",
        "confidence",
        "summary",
        "source_id",
        "chapter",
        "page",
        "kindle_location",
        "screenshot_file",
        "people",
        "events",
        "places",
        "organizations",
        "themes",
        "related_fact_cards",
        "notes",
    },
}

ENUM_COLUMNS = {
    "fact_cards": {
        "evidence_category": EVIDENCE_CATEGORY_VALUES,
        "confidence": CONFIDENCE_VALUES,
    },
    "timeline": {
        "evidence_category": EVIDENCE_CATEGORY_VALUES,
        "confidence": CONFIDENCE_VALUES,
    },
}


def today() -> str:
    return dt.date.today().isoformat()


def split_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.replace("|", ";").split(";") if item.strip()]


def linkify(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if value.startswith("[[") and value.endswith("]]"):
        return value
    if value.startswith("FC-") or value.startswith("TL-") or value.startswith("CAP-"):
        return f"[[{value}]]"
    if value.startswith("FACT_") or value.startswith("TIME_") or value.startswith("SRC_"):
        return f"[[{value}]]"
    target = link_target(value)
    if target and target != value:
        return f"[[{target}|{value}]]"
    return f"[[{value}]]"


def link_list(row: dict[str, str], field: str) -> str:
    items = [linkify(item) for item in split_list(row.get(field, ""))]
    return ", ".join(items) if items else ""


SOURCE_TITLE_BY_ID = {
    "SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO": "The Last Emperor of Mexico: A Disaster in the New World",
    "SRC_HAMNETT_1994_JUAREZ": "Juárez",
}

AUTHOR_BY_ID = {
    "SRC_HAMNETT_1994_JUAREZ": "Brian R. Hamnett",
}

DEFAULT_TAGS_BY_KIND = {
    "fact_cards": "fact-card;mexemp",
    "captures": "capture;mexemp",
    "timeline": "timeline;mexemp",
}

DEFAULT_TAGS_BY_SOURCE = {
    "SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO": {
        "fact_cards": "fact-card;mexemp;shawcross",
        "captures": "capture;mexemp;shawcross",
        "timeline": "timeline;mexemp;shawcross",
    },
    "SRC_HAMNETT_1994_JUAREZ": {
        "fact_cards": "fact-card;hamnett;juarez",
        "captures": "capture;hamnett;juarez",
        "timeline": "timeline;hamnett;juarez",
    },
}

LINK_TARGET_BY_LABEL = {
    "Benito Juárez": "Benito_Juarez",
    "Benito Juarez": "Benito_Juarez",
    "Juárez": "Benito_Juarez",
    "Maximilian": "Maximilian",
    "Napoleon III": "Napoleon_III",
    "Mexico City": "Mexico_City",
    "Guadalajara": "Guadalajara",
    "New Spain": "New_Spain",
    "Mexico": "Mexico",
    "United States": "United_States",
    "Texas": "Texas",
    "Guatemala": "Guatemala",
    "Central American Federation": "Central_American_Federation",
    "Poland": "Poland",
    "Imperial Russia": "Imperial_Russia",
    "Prussia": "Prussia",
    "Europe": "Europe",
    "Viceroyalty of New Spain": "Viceroyalty_of_New_Spain",
    "First Federal Republic": "First_Federal_Republic",
    "Mexican Republic": "Mexican_Republicans",
    "Mexican army": "Mexican_Army",
    "Catholic Church": "Catholic_Church",
    "archdiocese of Mexico City": "Archdiocese_of_Mexico_City",
    "dioceses": "Dioceses",
    "audiencias": "Audiencias_New_Spain",
    "mercantile guild": "Mercantile_Guild_New_Spain",
    "Spanish monarchy": "Spanish_Monarchy",
    "Liberal Party": "Liberal_Party_Mexico",
    "Conservative Party": "Mexican_Conservatives",
    "Juárez government": "Mexican_Republicans",
    "Bourbon reforms": "Bourbon_Reforms",
    "Bourbon centralization": "Bourbon_Reforms",
    "Independence": "Wars_of_Independence_Mexico",
    "Independence from Iberian rule": "Wars_of_Independence_Mexico",
    "Spanish colonial era": "Spanish_Colonial_Era",
    "loss of Texas": "Loss_of_Texas_1836",
    "War of 1846–47": "War_of_1846_1847",
    "defeat of 1847": "Defeat_of_1847",
    "Reform War": "Reform_War",
    "French Intervention": "French_Intervention_in_Mexico",
    "Central American Federation disintegration": "Dissolution_of_Central_American_Federation",
    "establishment of the First Federal Republic": "First_Federal_Republic",
    "rise of the United States": "Rise_of_the_United_States",
    "Juárez presidency": "Juarez_Presidency",
    "early Mexican Republic": "First_Federal_Republic",
    "economic unity": "Economic_Unity",
    "national cohesion": "National_Cohesion",
    "colonial legacy": "Colonial_Legacy",
    "merchant-financiers": "Merchant_Financiers",
    "colonial economy": "Colonial_Economy",
    "mining economy": "Mining_Economy",
    "agriculture": "Agriculture",
    "administrative structure": "Administrative_Structure",
    "Church-state relations": "Church_State_Relations_Mexico",
    "Church structure": "Church_Structure",
    "political economy": "Political_Economy",
    "regionalism": "Regionalism",
    "personalism": "Personalism",
    "regionalism and personalism": "Regionalism_and_Personalism",
    "constitutional government": "Constitutional_Government",
    "representative republican government": "Representative_Republican_Government",
    "US-Mexico relations": "US_Mexico_Relations",
    "domestic politics": "Domestic_Politics",
    "external pressure": "External_Pressure",
    "national humiliation": "National_Humiliation",
    "territorial loss": "Territorial_Loss",
    "national survival": "National_Survival",
    "geopolitical comparison": "Geopolitical_Comparison",
    "national politics": "National_Politics",
    "political culture": "Political_Culture",
    "centrifugal elements": "Centrifugal_Elements",
    "Liberalism": "Mexican_Liberalism_and_Nationalism",
    "state formation": "State_Formation",
    "economic development": "Economic_Development",
    "foreign relations": "Foreign_Relations",
    "race": "Race",
    "Juárez leadership": "Juarez_Political_Power",
    "Mexican Constitutionalism": "Mexican_Constitutionalism",
    "nineteenth-century Mexican history": "Comparative_Nineteenth_Century_Mexico",
    "infrastructure": "Infrastructure",
    "federalism": "Mexican_Federalism",
    "comparative history": "Comparative_Nineteenth_Century_Mexico",
    "Liberal Reform": "Liberal_Reform",
    "Valentín Gómez Farías": "Valentin_Gomez_Farias",
    "Antonio López de Santa Anna": "Antonio_Lopez_de_Santa_Anna",
    "Ramón Ramírez de Aguilar": "Ramon_Ramirez_de_Aguilar",
    "López Ortigoza": "Jose_Lopez_Ortigoza",
    "Tiburcio Cañas": "Tiburcio_Canas",
    "Vicente Guerrero": "Vicente_Guerrero",
    "Juan Álvarez": "Juan_Alvarez",
    "Anastasio Bustamante": "Anastasio_Bustamante",
    "Francisco Bulnes": "Francisco_Bulnes",
    "Melchor Ocampo": "Melchor_Ocampo",
    "Mariano Paredes Arrillaga": "Mariano_Paredes_y_Arrillaga",
    "Mariano Paredes y Arrillaga": "Mariano_Paredes_y_Arrillaga",
    "Florencio del Castillo": "Florencio_del_Castillo",
    "José María Morelos": "Jose_Maria_Morelos",
    "Miguel Hidalgo": "Miguel_Hidalgo",
    "Cuilapan": "Cuilapan",
    "Ciudad Guerrero": "Ciudad_Guerrero",
    "New Orleans": "New_Orleans",
    "Costa Rica": "Costa_Rica",
    "Cádiz": "Cadiz",
    "Dominican convent in Oaxaca": "Dominican_Convent_Oaxaca",
    "Rosary Chapel": "Rosary_Chapel_Oaxaca",
    "Oaxaca city council": "Oaxaca_City_Council",
    "Oaxaca state legislature": "Oaxaca_State_Legislature",
    "State Court of Justice": "State_Court_Of_Justice_Oaxaca",
    "State Court of Justice of Oaxaca": "State_Court_Of_Justice_Oaxaca",
    "Chamber of Deputies": "Chamber_Of_Deputies_Oaxaca",
    "Cádiz Cortes": "Cadiz_Cortes",
    "Inquisition": "Inquisition",
    "Institute of Sciences and Arts of Oaxaca": "Institute_Of_Sciences_And_Arts_Of_Oaxaca",
    "Institute of Sciences and Arts of the State of Oaxaca": "Institute_Of_Sciences_And_Arts_Of_Oaxaca",
    "Catholic clergy": "Catholic_Clergy",
    "Oaxaca Liberal Party": "Oaxaca_Liberal_Party",
    "Guerrero rehabilitation campaign": "Guerrero_Rehabilitation_Campaign",
    "Juárez final law examination 1834": "Juarez_Final_Law_Examination_1834",
    "Transfer of Guerrero remains 1834": "Transfer_Of_Guerrero_Remains_1834",
    "Gómez Farías reforms": "Gomez_Farias_Reforms",
    "Liberal Experiment of 1833-34": "Gomez_Farias_Liberal_Experiment",
    "Liberal Experiment of 1833–34": "Gomez_Farias_Liberal_Experiment",
    "Juárez legal career formation": "Juarez_Legal_Career_Formation",
    "Juárez early political career": "Juarez_Early_Political_Career",
    "Juárez and Liberalism": "Juarez_And_Liberalism",
    "Oaxaca provincial liberalism": "Oaxaca_Provincial_Liberalism",
    "Reform prehistory": "Reform_Prehistory_1833_1834",
    "Church and State": "Church_State_Relations_Mexico",
    "secular education": "Secular_Education_And_Liberalism",
    "symbolic politics and Guerrero": "Symbolic_Politics_And_Guerrero",
    "Morelos revolutionary legacy": "Morelos_Revolutionary_Legacy",
    "Liberal-Conservative fluidity": "Liberal_Conservative_Fluidity",
    "personal clientelism in Mexican politics": "Patron_Client_Politics",
    "Liberalism and Catholicism": "Liberalism_And_Catholicism",
}


def split_chapter_section(row: dict[str, str]) -> tuple[str, str]:
    chapter = row.get("chapter", "").strip()
    section_value = row.get("section", "").strip()
    if " / " in chapter and not section_value:
        chapter, section_value = [part.strip() for part in chapter.split(" / ", 1)]
    return chapter, section_value


def combined_section(chapter: str, section_value: str) -> str:
    if chapter and section_value:
        return f"{chapter} / {section_value}"
    return chapter or section_value


def source_title(row: dict[str, str]) -> str:
    return row.get("source_title", "").strip() or SOURCE_TITLE_BY_ID.get(row.get("source_id", ""), "")


def author(row: dict[str, str]) -> str:
    return row.get("author", "").strip() or AUTHOR_BY_ID.get(row.get("source_id", ""), "")


def default_tags(row: dict[str, str], kind_name: str) -> str:
    explicit = row.get("tags", "").strip()
    if explicit:
        return explicit
    source_id = row.get("source_id", "").strip()
    source_defaults = DEFAULT_TAGS_BY_SOURCE.get(source_id, {})
    return source_defaults.get(kind_name, DEFAULT_TAGS_BY_KIND.get(kind_name, ""))


def display_page(row: dict[str, str]) -> str:
    return row.get("printed_page", "").strip() or row.get("page", "").strip()


def archive_page(row: dict[str, str]) -> str:
    return row.get("archive_page", "").strip()


def link_target(value: str) -> str:
    mapped = LINK_TARGET_BY_LABEL.get(value)
    if mapped:
        return mapped
    return clean_filename_part(value)


def extract_between(text: str, label: str, end_labels: list[str]) -> str:
    if not text or label not in text:
        return ""
    start = text.find(label) + len(label)
    end = len(text)
    for end_label in end_labels:
        candidate = text.find(end_label, start)
        if candidate != -1:
            end = min(end, candidate)
    return text[start:end].strip(" .")


def fact_source_note(row: dict[str, str]) -> str:
    return row.get("source_note", "").strip() or extract_between(
        row.get("evidence_note", ""), "Source note:", ["Japanese note:"]
    )


def fact_japanese_note(row: dict[str, str]) -> str:
    return row.get("japanese_note", "").strip() or extract_between(
        row.get("evidence_note", ""), "Japanese note:", []
    )


def fact_cautions(row: dict[str, str]) -> str:
    return row.get("cautions", "").strip() or extract_between(
        row.get("limitations", ""), "Cautions:", ["Verification needed:"]
    )


def verification_needed(row: dict[str, str]) -> str:
    value = row.get("verification_needed", "").strip()
    if value:
        return value
    match = re.search(r"Verification needed:\s*(yes|no|true|false)", row.get("limitations", ""), re.I)
    if match:
        return match.group(1).lower()
    match = re.search(r"Verification needed:\s*(yes|no|true|false)", row.get("notes", ""), re.I)
    if match:
        return match.group(1).lower()
    return ""


def timeline_creative_use(row: dict[str, str]) -> str:
    return row.get("creative_use", "").strip() or extract_between(
        row.get("notes", ""), "Creative use:", ["Verification needed:"]
    )


def yaml_field(lines: list[str], field: str, value: str | None, list_value: bool = False) -> None:
    if list_value:
        lines.append(f"{field}: {yaml_value(field, value)}")
    else:
        lines.append(f"{field}: {scalar(value)}")


def rich_frontmatter(scalar_fields: list[tuple[str, str | None]], list_fields: list[tuple[str, str | None]]) -> str:
    lines = ["---"]
    for field, value in scalar_fields:
        yaml_field(lines, field, value)
    for field, value in list_fields:
        yaml_field(lines, field, value, list_value=True)
    lines.append("---")
    return "\n".join(lines)


def scalar(value: str | None) -> str:
    if value is None or value == "":
        return '""'
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def yaml_value(field: str, value: str | None) -> str:
    if field in LIST_FIELDS:
        items = split_list(value)
        if not items:
            return "[]"
        return "\n" + "\n".join(f"  - {scalar(item)}" for item in items)
    return scalar(value)


def frontmatter(row: dict[str, str], fields: list[str], note_type: str, kind_name: str = "") -> str:
    data = dict(row)
    defaults = {
        "id": "",
        "status": "draft",
        "created": today(),
        "updated": today(),
        "tags": default_tags(data, kind_name),
    }
    for key, value in defaults.items():
        if not data.get(key):
            data[key] = value
    data["type"] = note_type

    lines = ["---"]
    for field in fields:
        lines.append(f"{field}: {yaml_value(field, data.get(field, ''))}")
    lines.append("---")
    return "\n".join(lines)


def clean_filename_part(value: str) -> str:
    value = value.replace("[[", "").replace("]]", "")
    value = re.sub(r'[<>:"/\\|?*]', "", value)
    value = re.sub(r"\s+", "_", value.strip())
    value = re.sub(r"_+", "_", value)
    return value[:90].strip("._ ") or "untitled"


def note_path(out_dir: Path, row: dict[str, str], fallback_title: str) -> Path:
    note_id = clean_filename_part(row.get("id", ""))
    title = clean_filename_part(row.get("title", "") or fallback_title)
    filename = f"{note_id}.md" if note_id else f"{title}.md"
    return out_dir / filename


def section(title: str, content: str | None) -> str:
    content = (content or "").strip()
    return f"## {title}\n\n{content if content else ''}\n"


def render_fact_card(row: dict[str, str]) -> tuple[str, str]:
    title = row.get("title") or row.get("claim") or row.get("id") or "Fact Card"
    chapter, section_value = split_chapter_section(row)
    section_label = combined_section(chapter, section_value)
    statement = row.get("statement") or row.get("claim") or row.get("summary") or ""
    source_note = fact_source_note(row)
    japanese_note = fact_japanese_note(row)
    cautions = fact_cautions(row)
    verification = verification_needed(row)
    fm = rich_frontmatter(
        [
            ("id", row.get("id", "")),
            ("type", "fact_card"),
            ("status", row.get("status") or "draft"),
            ("created", row.get("created") or today()),
            ("updated", row.get("updated") or today()),
            ("tags", default_tags(row, "fact_cards")),
            ("source_id", row.get("source_id", "")),
            ("source_title", source_title(row)),
            ("author", author(row)),
            ("section", section_label),
            ("printed_page", display_page(row)),
            ("archive_page", archive_page(row)),
            ("page", row.get("page", "")),
            ("kindle_location", row.get("kindle_location", "")),
            ("screenshot_file", row.get("screenshot_file", "")),
            ("printed_page_status", row.get("printed_page_status", "")),
            ("title", title),
            ("statement", statement),
            ("evidence_category", row.get("evidence_category", "")),
            ("confidence", row.get("confidence", "")),
            ("verification_needed", verification),
            ("claim", statement),
            ("source_note", source_note),
            ("japanese_note", japanese_note),
            ("creative_use", row.get("creative_use", "")),
            ("cautions", cautions),
            ("related_capture", row.get("related_capture", "")),
        ],
        [
            ("people", row.get("people", "")),
            ("events", row.get("events", "")),
            ("places", row.get("places", "")),
            ("organizations", row.get("organizations", "")),
            ("themes", row.get("themes", "")),
        ],
    )
    body = [
        f"# {title}",
        section("Claim", statement),
        "## Evidence / Citation\n",
        f"- Category: {row.get('evidence_category', '')}",
        f"- Confidence: {row.get('confidence', '')}",
        f"- Verification needed: {verification}",
        f"- Source: {linkify(row.get('source_id', '')) if row.get('source_id') else ''}",
        f"- Source title: {source_title(row)}",
        f"- Author: {author(row)}",
        f"- Section: {section_label}",
        f"- Printed page: {display_page(row)}",
        f"- Archive page: {archive_page(row)}",
        f"- Page: {row.get('page', '')}",
        f"- Kindle location: {row.get('kindle_location', '')}",
        f"- Screenshot file: {row.get('screenshot_file', '')}",
        "",
        "## Notes\n",
        f"- Source note: {source_note}",
        f"- Japanese note: {japanese_note}",
        f"- Cautions: {cautions}",
        f"- Creative use: {row.get('creative_use', '')}",
        "",
        "## Links\n",
        f"- People: {link_list(row, 'people')}",
        f"- Events: {link_list(row, 'events')}",
        f"- Places: {link_list(row, 'places')}",
        f"- Organizations: {link_list(row, 'organizations')}",
        f"- Themes: {link_list(row, 'themes')}",
        f"- Related Fact Cards: {link_list(row, 'related_fact_cards')}",
        f"- Related Capture: {linkify(row.get('related_capture', '')) if row.get('related_capture') else ''}",
        "",
    ]
    return f"{fm}\n\n" + "\n".join(body), title


def render_capture(row: dict[str, str]) -> tuple[str, str]:
    fields = BASE_FIELDS + [
        "capture_date",
        "capture_type",
        "people",
        "events",
        "places",
        "organizations",
        "themes",
    ]
    fm = frontmatter(row, fields, "capture_note", "captures")
    title = row.get("title") or row.get("id") or "Capture Note"
    body = [
        f"# {title}",
        "## Source Position\n",
        f"- Source: {linkify(row.get('source_id', '')) if row.get('source_id') else ''}",
        f"- Source title: {row.get('source_title', '')}",
        f"- Chapter: {row.get('chapter', '')}",
        f"- Page: {row.get('page', '')}",
        f"- Kindle location: {row.get('kindle_location', '')}",
        f"- Screenshot file: {row.get('screenshot_file', '')}",
        "",
        section("Summary", row.get("summary")),
        section("Extracted Claim Candidates", row.get("extracted_claims")),
        section("Short Quote If Needed", row.get("direct_quote_short")),
        "## Links\n",
        f"- People: {link_list(row, 'people')}",
        f"- Events: {link_list(row, 'events')}",
        f"- Places: {link_list(row, 'places')}",
        f"- Organizations: {link_list(row, 'organizations')}",
        f"- Themes: {link_list(row, 'themes')}",
        section("Questions", row.get("questions")),
        section("Creative Notes", row.get("creative_notes")),
        section("Next Action", row.get("next_action")),
    ]
    return f"{fm}\n\n" + "\n".join(body), title


def render_timeline(row: dict[str, str]) -> tuple[str, str]:
    title = row.get("title") or row.get("summary") or row.get("id") or "Timeline Entry"
    chapter, section_value = split_chapter_section(row)
    section_label = combined_section(chapter, section_value)
    summary = row.get("event_summary") or row.get("summary") or ""
    date_label = row.get("date") or row.get("date_start") or ""
    date_start = row.get("date_start") or date_label
    creative_use = timeline_creative_use(row)
    verification = verification_needed(row)
    fm = rich_frontmatter(
        [
            ("id", row.get("id", "")),
            ("type", "timeline_entry"),
            ("status", row.get("status") or "draft"),
            ("created", row.get("created") or today()),
            ("updated", row.get("updated") or today()),
            ("tags", default_tags(row, "timeline")),
            ("source_id", row.get("source_id", "")),
            ("source_title", source_title(row)),
            ("author", author(row)),
            ("section", section_label),
            ("printed_page", display_page(row)),
            ("archive_page", archive_page(row)),
            ("page", row.get("page", "")),
            ("kindle_location", row.get("kindle_location", "")),
            ("screenshot_file", row.get("screenshot_file", "")),
            ("date", date_label),
            ("date_start", date_start),
            ("date_end", row.get("date_end", "")),
            ("date_precision", row.get("date_precision", "")),
            ("calendar", row.get("calendar", "") or "Gregorian"),
            ("evidence_category", row.get("evidence_category", "")),
            ("confidence", row.get("confidence", "")),
            ("verification_needed", verification),
            ("event_summary", summary),
            ("creative_use", creative_use),
            ("related_capture", row.get("related_capture", "")),
        ],
        [
            ("people", row.get("people", "")),
            ("events", row.get("events", "")),
            ("places", row.get("places", "")),
            ("organizations", row.get("organizations", "")),
            ("themes", row.get("themes", "")),
            ("related_fact_cards", row.get("related_fact_cards", "")),
        ],
    )
    body = [
        f"# {title}",
        "## Date\n",
        f"- Start: {date_start}",
        f"- End: {row.get('date_end', '')}",
        f"- Precision: {row.get('date_precision', '')}",
        f"- Calendar: {row.get('calendar', '') or 'Gregorian'}",
        "",
        section("Summary", summary),
        "## Citation\n",
        f"- Source: {linkify(row.get('source_id', '')) if row.get('source_id') else ''}",
        f"- Source title: {source_title(row)}",
        f"- Author: {author(row)}",
        f"- Section: {section_label}",
        f"- Printed page: {display_page(row)}",
        f"- Archive page: {archive_page(row)}",
        f"- Page: {row.get('page', '')}",
        f"- Kindle location: {row.get('kindle_location', '')}",
        f"- Screenshot file: {row.get('screenshot_file', '')}",
        "",
        "## Evidence Notes\n",
        f"- Evidence category: {row.get('evidence_category', '')}",
        f"- Confidence: {row.get('confidence', '')}",
        f"- Verification needed: {verification}",
        "",
        section("Creative Use", creative_use),
        "## Links\n",
        f"- People: {link_list(row, 'people')}",
        f"- Events: {link_list(row, 'events')}",
        f"- Places: {link_list(row, 'places')}",
        f"- Organizations: {link_list(row, 'organizations')}",
        f"- Themes: {link_list(row, 'themes')}",
        f"- Related Fact Cards: {link_list(row, 'related_fact_cards')}",
        f"- Related Capture: {linkify(row.get('related_capture', '')) if row.get('related_capture') else ''}",
    ]
    return f"{fm}\n\n" + "\n".join(body), title


KINDS = {
    "fact_cards": {
        "out_dir": "02_Fact_Cards",
        "renderer": render_fact_card,
    },
    "captures": {
        "out_dir": "01_Sources/Captures",
        "renderer": render_capture,
    },
    "timeline": {
        "out_dir": "05_Timeline",
        "renderer": render_timeline,
    },
}


def validate_header(kind_name: str, path: Path, fieldnames: list[str] | None) -> None:
    header = set(fieldnames or [])
    missing = sorted(REQUIRED_COLUMNS[kind_name] - header)
    if missing:
        raise SystemExit(
            f"Missing required columns for {kind_name}: {', '.join(missing)}\n"
            f"CSV: {path}"
        )


def validate_enums(kind_name: str, path: Path, rows: list[dict[str, str]]) -> None:
    enum_columns = ENUM_COLUMNS.get(kind_name, {})
    errors = []

    for line_number, row in enumerate(rows, start=2):
        if not any(row.values()):
            continue
        for column, allowed_values in enum_columns.items():
            value = row.get(column, "")
            if value not in allowed_values:
                allowed = ", ".join(sorted(allowed_values))
                errors.append(
                    f"{path} line {line_number} column {column}: "
                    f'invalid value "{value}". Allowed: {allowed}'
                )

    if errors:
        raise SystemExit("CSV enum validation failed:\n" + "\n".join(errors))


def read_csv(path: Path, kind_name: str) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        validate_header(kind_name, path, reader.fieldnames)
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
        validate_enums(kind_name, path, rows)
        return rows


def convert(args: argparse.Namespace) -> int:
    vault = Path(args.vault).resolve()
    csv_path = Path(args.csv).resolve()
    kind = KINDS[args.kind]
    out_dir = vault / kind["out_dir"]

    rows = read_csv(csv_path, args.kind)
    written = 0
    skipped = 0
    if not args.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    for index, row in enumerate(rows, start=1):
        if not any(row.values()):
            continue
        content, title = kind["renderer"](row)
        path = note_path(out_dir, row, title or f"row-{index}")

        if path.exists() and not args.overwrite:
            print(f"SKIP existing: {path}")
            skipped += 1
            continue

        if args.dry_run:
            action = "WOULD OVERWRITE" if path.exists() else "WOULD WRITE"
            print(f"{action}: {path}")
            continue

        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"WROTE: {path}")
        written += 1

    print(f"Done. written={written} skipped={skipped} dry_run={args.dry_run}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    script_path = Path(__file__).resolve()
    default_vault = script_path.parents[1]
    parser = argparse.ArgumentParser(description="Convert CSV rows to Obsidian Markdown notes.")
    parser.add_argument("--kind", required=True, choices=sorted(KINDS.keys()))
    parser.add_argument("--csv", required=True, help="Input CSV path.")
    parser.add_argument("--vault", default=str(default_vault), help="Vault root path.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing Markdown files.")
    parser.add_argument("--dry-run", action="store_true", help="Print output paths without writing files.")
    return parser


def main() -> int:
    return convert(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
