# MexicoEmpire_NovelDB

メキシコ皇帝マクシミリアンを題材にした歴史小説執筆用のObsidian vaultです。

このvaultは、史料本文や市販書籍の全文保存を目的にしません。保存する対象は、出典付きの要約、Fact Card、創作利用メモ、未確認事項、年表情報です。本文の長文引用、全文OCR、全文翻訳を前提にしない運用にしてください。

## Obsidianで開く

このフォルダ自体をObsidianのvaultとして開いてください。

- Vaultフォルダ: `C:\Users\kaz93\Documents\メキシコ帝国DB作成\MexicoEmpire_NovelDB`
- Obsidian本体: `C:\Users\kaz93\AppData\Local\Programs\Obsidian\Obsidian.exe`
- Obsidianでは `Open folder as vault` から上記のVaultフォルダを選びます。
- 既存の `C:\Users\kaz93\Documents\Obsidian Vault` へ移動・コピーする必要はありません。

初回確認では、次を開くと状態を把握しやすいです。

- [README](README.md)
- [[08_Outputs/Indexes/Index_Fact_Cards|Fact Card索引]]
- [[08_Outputs/Indexes/Index_Sources|Source索引]]
- [[08_Outputs/Indexes/Index_Entities|Entity索引]]
- [[08_Outputs/Indexes/Index_Timeline|Timeline索引]]
- [[08_Outputs/Indexes/Index_Workflow|Workflow索引]]
- [[SRC_HAMNETT_1994_JUAREZ]]
- [[FACT_HAMNETT_JUAREZ_0001]]
- `02_Fact_Cards/`
- `01_Sources/Captures/`
- `03_Entities/`
- `05_Timeline/`

標準機能だけで、検索、バックリンク、アウトリンク、グラフ、プロパティ表示、テンプレートを使えるようにしています。Dataviewなどのコミュニティプラグインはまだ入れていません。まず基本リンクとYAMLプロパティがObsidian上で読めることを確認してから追加してください。

Hamnett本の取り込み状況は、2026-06-20時点で `FACT_HAMNETT_JUAREZ_*.md` が134件、`CAP_HAMNETT_JUAREZ_*.md` が8件です。全投入は、Obsidian上で現在のカードを確認できるようにしてから進めます。

Hamnett本の取込作業ルールと短縮依頼フォーマットは、リポジトリ直下の `AGENTS.md` と `93_Docs/ChatGPT_DB_Update_Prompt_README.md` を参照してください。

## 基本方針

- 1つのFact Cardには、1つの主張だけを書く。
- 史実、一次証言、著者の解釈、噂・伝聞、異説、創作用推測を必ず区別する。
- 出典は `source_id`、章、ページ、Kindle位置、スクリーンショットファイル名で追跡する。
- スクリーンショットや史料本文そのものは、情報本体ではなく検証用の参照として扱う。
- 人物、事件、場所、組織、テーマはObsidianの内部リンクで接続する。
- CSVからMarkdownへ変換する場合も、既存ノートは既定で上書きしない。

## フォルダ構成

```text
MexicoEmpire_NovelDB/
  00_Inbox/                  一時メモ、未整理capture
  01_Sources/                Source Noteと整理済みCapture Noteの出典管理
    Captures/                整理済みCapture Note
    Chapter_Summaries/       書籍の章別論旨・内容構成・検証状況
  02_Fact_Cards/             1カード1主張のFact Card
  03_Entities/
    People/                  人物ノート
    Places/                  場所ノート
    Organizations/           組織ノート
    Themes/                  主題ノート
  04_Events/                 事件・時期・政治過程
  05_Timeline/               年表Markdown
  06_Scenes/                 小説用シーンメモ
  07_Questions/              未確認事項、調査課題
  08_Outputs/                草稿、抜き出し、執筆用まとめ
  09_Attachments/
    Screenshots/             検証用スクリーンショット
  90_Templates/              Obsidian用テンプレート
  91_CSV_Templates/          CSV入力テンプレート
  92_Scripts/                CSVからMarkdownへの変換スクリプト
  93_Docs/                   運用ルール
```

## ノート種別

| type | 用途 |
| --- | --- |
| `source_note` | 書籍、論文、史料集、アーカイブ資料などの出典単位 |
| `book_chapter_summary` | 書籍1章の論旨、内容の流れ、ページcoverage、検証状況 |
| `capture_note` | 読書・閲覧時に作った短い要約と抽出候補 |
| `fact_card` | 1つの主張、根拠、信頼度、創作利用メモ |
| `person` | 人物の概要、関係、登場シーン候補 |
| `event` | 事件、政治過程、時期 |
| `place` | 場所、建物、地理的舞台 |
| `organization` | 家門、政府、派閥、教会、軍など |
| `theme` | 正統性、改革、干渉などの抽象テーマ |
| `timeline_entry` | 年表の1行に相当する出来事 |
| `scene_note` | 小説の場面設計、史実との距離 |
| `question_note` | 未確認事項、異説、要調査メモ |

## 証拠分類

Fact CardとTimeline Entryでは、次のように分類してください。

| evidence_category | 意味 |
| --- | --- |
| `historical_fact` | このDB上で史実として扱う情報 |
| `primary_testimony` | 書簡、日記、回想、証言など一次証言 |
| `author_interpretation` | 研究者や著者による解釈 |
| `rumor_hearsay` | 噂、伝聞、同時代の評判 |
| `variant_disputed` | 異説、史料間の食い違い |
| `creative_inference` | 小説執筆のための推測。史実として扱わない |

`historical_fact` は、このDB上で史実として扱う情報を示します。ただし、未クロスチェックの場合があるため、確度は `confidence` で別途表現します。たとえば `evidence_category: historical_fact` と `confidence: probable` または `confidence: uncertain` の組み合わせを許容します。

`confidence` は `confirmed`、`probable`、`uncertain`、`disputed`、`fictionalized` から選びます。Timeline Entryでも `evidence_category` と `confidence` を併用します。

## 推奨ワークフロー

1. `01_Sources/Source_Notes/` にSource Noteを作る。
2. 書籍はSource NoteにBook OverviewとChapter Guideを置き、各章を`01_Sources/Chapter_Summaries/`の章別ノートへまとめる。
3. 読書中の未整理メモは `00_Inbox/Captures/` に一時保存する。
4. 出典位置を確認した整理済みCapture Noteは `01_Sources/Captures/` に保存する。
5. Capture Noteから、1主張ずつ `02_Fact_Cards/` にFact Cardを作る。
6. Fact Cardから `People`、`Events`、`Places`、`Organizations`、`Themes` へリンクする。
7. 日付を持つFact Cardは `05_Timeline/` にTimeline Entryとして整理する。
8. 創作用の仮説や場面案は `06_Scenes/` に分離し、史実と混ぜない。
9. 未確認事項は `07_Questions/` に残し、解決時にFact Cardへリンクする。

## CSV変換

CSVテンプレートは `91_CSV_Templates/` にあります。変換スクリプトは標準Pythonだけで動きます。

```powershell
python .\92_Scripts\csv_to_md.py --kind fact_cards --csv .\91_CSV_Templates\fact_cards_template.csv
python .\92_Scripts\csv_to_md.py --kind captures --csv .\91_CSV_Templates\capture_notes_template.csv
python .\92_Scripts\csv_to_md.py --kind timeline --csv .\91_CSV_Templates\timeline_template.csv
```

既存ファイルは既定でスキップします。上書きが必要な場合だけ `--overwrite` を付けてください。

CSVから生成するMarkdownは、`id` がある場合は `FC-...md`、`CAP-...md`、`TL-...md` のようにIDをファイル名にします。Obsidianリンクは `[[FC-1864-001]]` の形で解決しやすくなります。Source Noteも同じ理由で、ファイル名を `source_id` に合わせる運用を推奨します。

## 初期リンク対象

- [[Maximilian]]
- [[Carlota]]
- [[Benito_Juarez]]
- [[Napoleon_III]]
- [[Franz_Joseph]]
- [[Habsburg]]
- [[French_Intervention_in_Mexico]]
- [[Second_Mexican_Empire]]
- [[Queretaro]]
- [[Miramar]]
- [[Mexican_Conservatives]]
- [[Mexican_Republicans]]
- [[Catholic_Church]]
- [[Liberal_Reform]]
- [[Foreign_Intervention]]
- [[Legitimacy]]
