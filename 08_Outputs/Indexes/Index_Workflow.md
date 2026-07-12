---
id: "Index_Workflow"
type: "index_note"
status: "active"
created: "2026-06-20"
updated: "2026-06-20"
tags:
  - "index"
  - "workflow"
---

# Workflow索引

このDBの基本作業は、読書メモをそのまま本文化せず、出典付きの小さな主張へ分解してからリンクで接続することです。

## 基本フロー

1. Source Noteを作る。
   - 場所: `01_Sources/Source_Notes/`
   - テンプレート: [[90_Templates/Source Note|Source Note]]
2. 読書中のメモをCapture Noteに入れる。
   - 場所: `00_Inbox/Captures/` または `01_Sources/Captures/`
   - テンプレート: [[90_Templates/Capture Note|Capture Note]]
3. 1主張ずつFact Cardに切り出す。
   - 場所: `02_Fact_Cards/`
   - テンプレート: [[90_Templates/Fact Card|Fact Card]]
4. 日付を持つ主張はTimeline Entryにも整理する。
   - 場所: `05_Timeline/`
   - テンプレート: [[90_Templates/Timeline Entry|Timeline Entry]]
5. 人物・事件・場所・組織・テーマへリンクする。
   - 場所: `03_Entities/` と `04_Events/`

## CSV投入

CSVテンプレートは `91_CSV_Templates/`、変換スクリプトは `92_Scripts/csv_to_md.py` にあります。

```powershell
python .\92_Scripts\csv_to_md.py --kind fact_cards --csv .\91_CSV_Templates\fact_cards_template.csv
python .\92_Scripts\csv_to_md.py --kind captures --csv .\91_CSV_Templates\capture_notes_template.csv
python .\92_Scripts\csv_to_md.py --kind timeline --csv .\91_CSV_Templates\timeline_template.csv
```

既存ファイルは既定でスキップします。上書きが必要なときだけ `--overwrite` を付けます。

## Hamnett投入の次フェーズ

1. 既存のHamnett Fact CardとTimelineをObsidian上で確認する。
2. 未投入範囲をCapture Noteに分ける。
3. Capture NoteからFact CardとTimeline Entryを生成する。
4. 生成後にSource Note、Entity、Eventへのリンクを確認する。

## 確認する索引

- [[08_Outputs/Indexes/Index_Fact_Cards|Fact Card索引]]
- [[08_Outputs/Indexes/Index_Sources|Source索引]]
- [[08_Outputs/Indexes/Index_Entities|Entity索引]]
- [[08_Outputs/Indexes/Index_Timeline|Timeline索引]]
