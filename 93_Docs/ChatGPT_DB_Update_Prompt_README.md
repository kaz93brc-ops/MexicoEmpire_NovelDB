---
id: DOC_CHATGPT_DB_UPDATE_PROMPT_README
type: documentation
status: active
created: 2026-06-23
updated: 2026-07-13
tags:
  - docs
  - chatgpt
  - prompt
  - workflow
source_id: ""
chapter: ""
page: ""
kindle_location: ""
screenshot_file: ""
---

# ChatGPT DB Update Prompt README

このファイルは、ChatGPTに `MexicoEmpire_NovelDB` 更新用プロンプトを作らせるときに渡す単一READMEです。

統合元だった `ChatGPT_Sharing_Memo.md` と `ChatGPT_Hamnett_Prompt_Transfer.md` の内容は、このファイルへ吸収しました。古い日付固定の進捗、古いHamnett件数、古い `next_required_page` は使わず、作業時に監査ファイルから最新値を確認する前提に更新しています。

## 目的

`MexicoEmpire_NovelDB` は、メキシコ第二帝政、Maximilian、Carlota、Benito Juarez、メキシコ共和派を扱う歴史小説執筆用のObsidian vaultです。

保存するのは、出典付き要約、Fact Card、Timeline Entry、Entity Note、創作利用メモ、Open Questionsです。市販書籍、史料本文、OCR全文、全文翻訳、スクリーンショット全文転記、長文引用の保存場所ではありません。

ChatGPTに作らせるプロンプトの目的は、Codexや別エージェントがこのvaultを壊さず、出典・ID・リンク・検証手順を守って更新できる作業依頼文を作ることです。

## Vault前提

- vault root: `MexicoEmpire_NovelDB/`
- Obsidian標準Markdown、YAML frontmatter、wiki linkで運用する。
- Dataviewなどのコミュニティプラグイン前提の記法にしない。
- 既存Markdownは理由なく上書き・削除しない。
- CSV変換や一括生成を使う場合も、既存ノートは既定で上書きしない。
- スクリーンショットは検証用参照であり、本文保存の代替ではない。
- 紙面ページ未確認の `printed_page_status: "not_verified"` は構造エラーではない。

## 主要フォルダ

```text
MexicoEmpire_NovelDB/
  00_Inbox/                  一時メモ、未整理capture
  01_Sources/                Source NoteとCapture Note
    Captures/                整理済みCapture Note
  02_Fact_Cards/             1カード1主張のFact Card
  03_Entities/               People / Places / Organizations / Themes
  04_Events/                 事件・政治過程
  05_Timeline/               Timeline Entry
  06_Scenes/                 小説用Scene Note
  07_Questions/              未確認事項
  08_Outputs/                索引、監査、執筆用まとめ
  09_Attachments/            検証用スクリーンショット等
  90_Templates/              Obsidian用テンプレート
  91_CSV_Templates/          CSV入力テンプレート
  92_Scripts/                保守・変換スクリプト
  93_Docs/                   運用ドキュメント
```

## 作業前に読ませるファイル

一般のDB更新プロンプトでは、最低限次を確認する指示を入れてください。

- `README.md`
- `AGENTS.md`
- 関連Source Note
- `08_Outputs/Audits/Fact_Card_Metadata_Review.md`
- `08_Outputs/Audits/Printed_Page_Verification_Candidates.md`

Hamnett `Juarez` 取り込みでは追加で次を確認させます。

- `01_Sources/Source_Notes/SRC_HAMNETT_1994_JUAREZ.md`
- `93_Docs/Hamnett_Juarez_Progress_Master.md`
- `08_Outputs/Audits/Hamnett_Ingestion_Readiness.md`

Hamnett作業では `Hamnett_Ingestion_Readiness.md` の `next_required_page` を通常の入口にします。ただし、ユーザーが対象ページやスクリーンショットを明示した場合はユーザー指定を優先し、Readinessとの矛盾を最終報告に残します。

## プロンプトに必ず含める情報

ChatGPTが作るDB更新プロンプトは、渡す相手に応じて通常モードと短縮モードを使い分けます。

通常モードは、初回作業者、別環境、または恒久ルールを読めない相手へ渡す場合に使います。次を具体的に含めてください。

- 対象vault: `MexicoEmpire_NovelDB/`
- Source ID、source title、author、publisher、publication year、edition
- URL、archive page、printed page、section、chapter、screenshot_file
- 作成予定のCapture / Fact / Timeline ID
- 既存IDがあれば上書きせず、次の未使用IDへずらす指示
- 本文全文、全文翻訳、長文引用、スクリーンショット全文転記を禁止する指示
- 史実、一次証言、著者解釈、伝聞、異説、創作用推測を分ける指示
- Fact Cardは1カード1主張にする指示
- 新規Entity作成前に既存basename、title、aliasesを確認する指示
- Relationshipカードは命名規則が明確でない場合、新規作成せず候補に留める指示
- 作業後の検証コマンドと最終報告項目

短縮モードは、このリポジトリのCodex環境で、`AGENTS.md` とこのREADMEを読める前提のHamnett継続作業に使います。恒久ルールの再掲は避け、ページ固有情報だけを渡してください。

- 再掲しない: 禁止事項、証拠分類一覧、`confidence` 一覧、標準YAML項目、Entity確認ルール、Relationship保留方針、検証コマンド、標準最終報告項目、一般的な描写注意。
- 必ず渡す: 対象ページ、スクリーンショット名、archive page、printed page、予定ID、前後ページ接続、ページ大意、Fact候補、Timeline候補、Entity候補、ページ固有の照合観点・創作利用・要確認事項。
- Fact候補は `ID: statement / evidence_category / confidence / printed_page / source_note任意 / caution任意` の1行形式にします。
- Entity候補は `existing_connect`、`new_stub_consider`、`candidate_only` に分けます。
- 最終報告は標準チェックリストを適用させ、ページ固有で必ず報告してほしい点だけ `extra_final_report` に書きます。

## 証拠分類

`evidence_category` は次から選びます。

- `historical_fact`: このDB上で史実として扱う情報。
- `primary_testimony`: 書簡、日記、回想、証言、新聞、議会発言、公文書など一次証言に由来する情報。
- `author_interpretation`: 研究者や著者による評価、整理、因果説明。
- `rumor_hearsay`: 噂、伝聞、同時代の評判。
- `variant_disputed`: 異説、史料間の食い違い。
- `creative_inference`: 小説用推測。史実として扱わない。

`confidence` は次から選びます。

- `confirmed`
- `probable`
- `uncertain`
- `disputed`
- `fictionalized`

注意点:

- 著者の評価、整理、因果説明は原則 `author_interpretation`。
- 未クロスチェックの史実整理は `historical_fact / probable / verification_needed: yes` を基本にする。
- 一次史料に由来しそうだが原典未確認の情報は `primary_testimony / probable / verification_needed: yes` を基本にする。
- `confirmed` は紙面ページ、注、原典、別文献などで実際に確認できた場合だけ慎重に使う。
- 創作用推測は史実カードと混ぜず、`creative_inference` やScene Note側へ分ける。

## Fact Card仕様

Fact Cardは `02_Fact_Cards/` に置き、1カード1主張にします。プロンプトでは最低限、次のYAML項目を要求してください。

```yaml
id:
type: "fact_card"
status:
source_id:
source_title:
author:
section:
printed_page:
archive_page:
page:
screenshot_file:
printed_page_status:
title:
statement:
evidence_category:
confidence:
verification_needed:
source_note:
japanese_note:
creative_use:
cautions:
related_capture:
people: []
events: []
places: []
organizations: []
themes: []
```

本文側には最低限、次を置かせます。

- `## Claim`
- `## Evidence / Citation`
- `## Notes`
- `## Links`

`statement` と `## Claim` は同じ主張にし、複数の史実や人物評価を1カードへ詰め込ませないでください。

## Capture Note仕様

Capture Noteは `01_Sources/Captures/` に置きます。詳細な作業ログではなく、出典付き大意、重要ポイント、作成ID、創作利用、要確認事項を中心にします。

入れる内容:

- frontmatter: `id`, `type: capture`, `source_id`, `source_title`, `author`, `chapter`, `section`, `printed_page`, `archive_page`, `screenshot_file`, `printed_page_status`, `reading_accuracy`
- 大意
- 重要ポイント
- Factリンク
- Timelineリンク
- Person / Event / Place / Organization / Theme接続
- Relationship候補
- 他文献照合観点
- 創作利用メモ
- 要確認事項
- 必要最小限の短い原文メモ

長文引用は禁止します。短い原文メモは、固有名詞、概念語、表記確認に必要な語句だけにしてください。

## Timeline Entry仕様

Timeline Entryは、日付または期間を持つ情報だけ `05_Timeline/` に作ります。

- 出典、証拠分類、確度、検証要否、関連Fact Cardへのリンクを入れる。
- 日付が曖昧な場合は `date_precision: approximate_period` などで表現する。
- 年表化できても日付がないものは、Fact CardやCapture Noteの要確認事項に留める。
- 無理に正確な日付へ変換しない。

## Entityとリンク

プロンプトには、Entity作成前の確認を必ず入れてください。

- 既存ノートのbasename、title、aliasesを確認する。
- 同じbasenameのMarkdownを増やさない。
- リンクは既存stemを指すObsidian wiki linkにする。
- 表示名が必要な場合は、stemと表示名をパイプで分ける通常形式を使う。
- 抽象Themeと実体Organizationを混同しない。
- 重要Entityだけ最小stubを作る。軽微な対象はCapture Note内の候補に留めてよい。
- stubには最低限 `type`, `status`, `source_id`, `Historical Role`, `Creative Use`, `Open Questions`, `Linked Items` を入れる。
- Relationshipカードは既存命名規則が明確でない場合、新規作成せず候補に留める。

説明用の未実在wiki link例をプロンプト内に置くと監査で未解決リンク扱いになることがあります。例示が必要な場合は、実在stemだけを使うか、二重角括弧の実記法を避けた説明文にしてください。

## ID運用

プロンプトでは、既存ID確認を明示してください。

- Capture Note: source別規則に従う。Hamnettなら `CAP_HAMNETT_JUAREZ_NNNN.md`。
- Fact Card: source別規則に従う。Hamnettなら `FACT_HAMNETT_JUAREZ_NNNN.md`。
- Timeline Entry: source別規則に従う。Hamnettなら `TIME_HAMNETT_JUAREZ_NNNN.md`。
- 既存IDを上書きしない。
- ユーザー提示IDが衝突した場合は、既存DBを優先して次の未使用IDへずらす。
- ID変更が発生したら、Capture Noteと最終報告に「予定ID -> 実使用ID」を明記する。

## Hamnett Juarez専用注意

Hamnett `Juarez` は二次文献として扱います。

- Source IDは `SRC_HAMNETT_1994_JUAREZ`。
- Hamnett自身の評価、整理、因果説明は原則 `author_interpretation / probable`。
- Hamnett本文だけを根拠にした史実整理は安易に `confirmed` にしない。
- 注、出典、一次史料に由来しそうな情報は、未確認なら `verification_needed: yes` にする。
- `90_Templates/Hamnett Compact Capture Note.md`、`Hamnett Compact Fact Card.md`、`Hamnett Compact Timeline Entry.md` を優先する。
- `Hamnett_Ingestion_Readiness.md` の `next_required_page` と `Hamnett_Juarez_Progress_Master.md` の最新ID範囲を確認する。
- ユーザーが今回対象を明示した場合は、その指定を優先し、Readinessとの差分を報告する。

描写上の注意:

- Juarezを単純な英雄にしない。
- Maximilianを単純な愚者、侵略者、悲劇的人物にしない。
- Liberal / Conservativeを善悪二分法で処理しない。
- Church対立を「近代化対迷信」に固定しない。
- Juchitan、Isthmus、村落、非エリート集団を犯罪者化しない。
- `caste`, `puro`, `pintos` などの語は現代語へ単純化せず、要確認事項に残す。

## ローカル探索コマンド

Hamnett取り込みプロンプトでは、作業者にPowerShell探索を使わせる指示を入れてください。

- ファイル列挙: `Get-ChildItem -Recurse -Filter *.md`
- 内容検索: `Get-ChildItem ... | Select-String -Pattern ...`
- ID確認: `01_Sources/Captures/`, `02_Fact_Cards/`, `05_Timeline/` を直接確認
- 空wiki link確認: 正規表現 `\[\[\s*\]\]`

`rg` が使えない環境があるため、Hamnett作業では最初からPowerShell探索に寄せるのが安全です。

## 検証コマンド

更新作業後は、可能な範囲で次を実行させます。

```powershell
python .\MexicoEmpire_NovelDB\92_Scripts\auto_resolve_links.py --mode analyze --limit 20
python .\MexicoEmpire_NovelDB\92_Scripts\vault_maintenance.py --phase all
```

索引・監査レポート再生成が必要な作業では、次も含めます。

```powershell
python .\MexicoEmpire_NovelDB\92_Scripts\vault_maintenance.py --phase all --apply
```

期待する結果:

- unresolved wiki links: `0`
- empty wiki links: `0`
- Fact Card `statement` 欠落: `0`
- `source_id_review`: `0`
- locator missing: `0`
- 実ノートのbasename重複: `0`
- 紙面ページ未確認だけは残ってよい

## 最終報告チェックリスト

プロンプトの最後には、作業者に以下を報告させてください。

- 作成・更新したCapture / Fact / Timeline ID
- ID変更の有無と変更前後
- 既存Person / Event / Place / Organization / Theme接続先
- 新規Entityを作成したか、候補に留めたか
- Relationshipカードを作成したか、候補に留めたか
- 重要な未完論点、注、要確認事項を残したか
- 他文献照合観点と創作利用メモを残したか
- 検証結果: unresolved wiki links, empty wiki links, basename重複, statement欠落, locator missing, source_id_review
- 長文引用、全文保存、全文翻訳、スクリーンショット全文転記が発生していないこと
- branch名、commit SHA、PR URL、PR種別、auto-merge設定、merge状態

## ページ用プロンプト末尾のGitHub反映指示

各ページ・見開きのDB更新プロンプト末尾には、次の短縮版を付けてください。詳細条件は`AGENTS.md`と`93_Docs/GitHub_Workflow.md`から読ませ、プロンプト側へ重複掲載しません。

```text
github_publish:
- ローカルDB更新だけで完了とせず、専用branchで対象ファイルだけをstageし、commit、push、Pull Request作成まで行う。
- 通常取込はGitHub_Workflow.mdの安全条件をすべて満たす場合だけ通常PRとし、safety成功後のsquash auto-mergeを設定する。
- 地図、Index、不確実性、検証失敗、競合、保護対象変更、50件超、削除・移動・改名、またはレビュー指定がある場合はDraft PRで停止し、auto-mergeを設定しない。
- 最終報告に変更箇所、branch名、commit SHA、PR URL、PR種別、auto-merge設定、検証結果、merge状態を記載する。
- branch名、commit SHA、PR URLのいずれかがない場合は「GitHub反映完了」とせず、「ローカルDB更新完了・GitHub反映未完了」と報告する。
```

## ChatGPTへ渡す短縮指示

短く渡す場合は、以下を貼り付ければ足ります。

```text
MexicoEmpire_NovelDB更新用プロンプトを作るときは、このvaultが歴史小説執筆用Obsidian DBであり、本文全文・全文OCR・全文翻訳・長文引用を保存しないことを前提にしてください。保存するのは出典付き要約、Fact Card、Timeline Entry、Entity接続、創作利用メモ、Open Questionsだけです。

Fact Cardは1カード1主張。史実、一次証言、著者解釈、伝聞、異説、創作用推測を必ず分けてください。著者の評価や因果説明は author_interpretation、未クロスチェックの史実は historical_fact / probable / verification_needed: yes を基本にしてください。

プロンプトには、作業前に README.md、AGENTS.md、関連Source Note、進捗管理ファイル、監査レポートを確認する指示、新規Entity作成前に既存basename・aliasesを確認する指示、既存IDを上書きしない指示、作業後に auto_resolve_links.py と vault_maintenance.py を実行する指示を入れてください。

Hamnett Juarez取り込みでは、SRC_HAMNETT_1994_JUAREZ、Hamnett_Juarez_Progress_Master.md、Hamnett_Ingestion_Readiness.md を確認させ、Readinessの next_required_page を通常入口にしてください。ユーザーが対象ページを明示した場合はユーザー指定を優先し、矛盾は最終報告に残してください。

最終報告には、作成・更新ID、ID変更、Entity接続、Relationship候補、Open Questions、検証結果、長文引用等が発生していないことを含めてください。
```

## Hamnett短縮プロンプトテンプレート

このCodex環境でHamnett `Juarez` の次ページを処理させる場合は、以下の形を優先してください。恒久ルールは `AGENTS.md` とこのREADMEから読ませ、依頼文ではページ固有情報だけを渡します。

```text
MexicoEmpire_NovelDB の Hamnett, Juárez 取込を続けてください。
恒久ルールは AGENTS.md と 93_Docs/ChatGPT_DB_Update_Prompt_README.md に従い、本文全文・長文引用・全文翻訳・全文OCRは保存しないでください。

target:
- screenshot_no:
- screenshot_file:
- chapter:
- section:
- printed_page:
- archive_page:
- screen_display:
- content_type:

ids:
- capture:
- fact_start:
- timeline_start:

continuity:
- previous:
- next:

page_summary:
- 大意を箇条書きで記載。全文翻訳にしない。

fact_candidates:
- FACT_...: statement / evidence_category / confidence / printed_page / source_note任意 / caution任意

timeline_candidates:
- TIME_...: date or period / summary / related_fact / caution任意
- 作成しない候補がある場合は理由を書く。

entities:
- existing_connect:
- new_stub_consider:
- candidate_only:

relationship_candidates:
- 候補のみ。命名規則が明確でなければ作成しない。

cross_check:
- Shawcross等との照合観点だけ記載。

creative_use:
- historical_use:
- creative_inference:

open_questions:
- ページ固有の要確認事項だけ記載。

extra_final_report:
- ページ固有で必ず報告してほしい点だけ記載。

github_publish:
- 専用branch、対象ファイルだけのstage、commit、push、PR作成まで行う。
- 安全条件をすべて満たす通常取込だけ通常PR＋safety成功後のsquash auto-mergeとする。
- Draft条件に該当する場合はDraft PRで停止し、auto-mergeを設定しない。
- branch名、commit SHA、PR URL、PR種別、検証結果、merge状態を最終報告する。3点のいずれかがなければ「ローカルDB更新完了・GitHub反映未完了」とする。
```
