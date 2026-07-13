# Agent Operating Rules

このファイルは、今後 Brian R. Hamnett, *Juarez* の情報を `MexicoEmpire_NovelDB` に追加するエージェント向けの作業ルールです。対象 vault は `MexicoEmpire_NovelDB/` です。

## 基本方針

- CodexでHamnett *Juarez* 取込を行う場合は、まず `$hamnett-juarez-ingestion` skill を使用する。
- この vault は Obsidian 用の歴史小説執筆DBであり、書籍本文・全文OCR・長文引用・全文翻訳の保存場所ではない。
- Hamnett *Juarez* は二次文献として扱う。Hamnett自身の評価・整理・因果説明は原則 `evidence_category: "author_interpretation"` にする。
- 1つの Fact Card には1つの主張だけを書く。複数の主張、時系列、人物評価を1カードへ詰め込まない。
- 史実、著者解釈、一次証言、伝聞、異説、創作用推測を必ず分ける。
- 出典位置は `source_id`、`section`、`printed_page`、`archive_page` または `page`、`screenshot_file` で追跡する。
- Obsidian標準機能で動く Markdown と YAML frontmatter を維持する。Dataviewなどのコミュニティプラグイン前提の記法にしない。

## 作業前に読むファイル

Hamnett情報を追加する前に、最低限次を確認する。

- `MexicoEmpire_NovelDB/README.md`
- `MexicoEmpire_NovelDB/01_Sources/Source_Notes/SRC_HAMNETT_1994_JUAREZ.md`
- `MexicoEmpire_NovelDB/93_Docs/Hamnett_Juarez_Progress_Master.md`
- `MexicoEmpire_NovelDB/08_Outputs/Audits/Hamnett_Ingestion_Readiness.md`
- `MexicoEmpire_NovelDB/08_Outputs/Audits/Fact_Card_Metadata_Review.md`
- `MexicoEmpire_NovelDB/08_Outputs/Audits/Printed_Page_Verification_Candidates.md`

`Hamnett_Ingestion_Readiness.md` の `next_required_page` を次回処理の入口にする。固定日付の過去メモより、このレポートの最新値を優先する。進捗更新後は `SRC_HAMNETT_1994_JUAREZ.md` と `Hamnett_Juarez_Progress_Master.md` の次回確認事項も同じ入口に揃える。

## ローカル探索コマンド

- この作業環境では `rg` が実行権限の関係で拒否されることがあるため、Hamnett取り込み作業では最初から PowerShell で探索する。
- `rg` を試して失敗してから切り替える手順は不要。
- ファイル列挙は `Get-ChildItem -Recurse -Filter *.md` を使う。
- 内容検索は `Get-ChildItem ... | Select-String -Pattern ...` を使う。
- ID確認は `01_Sources/Captures/`、`02_Fact_Cards/`、`05_Timeline/` を PowerShell で直接確認する。
- 空wikiリンク確認は正規表現 `\[\[\s*\]\]` を使う。`Select-String -SimpleMatch '\[\[\]\]'` は説明文中のエスケープ表記も拾うため、実リンク確認には使わない。

## 省トークン運用

Hamnett取り込みでは、品質を落とさずトークン消費を抑えるため、次を優先する。

- 省トークン化で削ってよいのは、既存ルールの再掲、重複情報、定型文、冗長な説明だけとする。
- 対象ページ・見開きから得た新規情報は、原則すべて保存する。削らず、Capture Note、Fact Card、Timeline Entry、Entity追記、Open Questionsのいずれかへ振り分ける。
- 新規情報が多い場合は、情報を捨てずに文を短くし、1カード1主張のままFact Card数を増やす。
- 既存カードと実質重複する情報は新規カード化せず、既存カード・Capture Note・EntityのLinked Itemsへ接続する。
- ユーザー依頼文・作業報告では、このAGENTS.mdに既にある恒久ルールを再掲しない。
- 作業時は `90_Templates/Hamnett Compact Capture Note.md`、`90_Templates/Hamnett Compact Fact Card.md`、`90_Templates/Hamnett Compact Timeline Entry.md` を優先して使う。
- Capture Noteは詳細な作業ログではなく、出典付き大意、重要ポイント、創作利用、要確認事項、作成ID一覧を中心にする。
- Capture NoteのFact候補一覧は、原則 `ID: 短いstatement / evidence_category / confidence / verification_needed` 程度に圧縮する。
- Fact Card本文は必須見出しを維持しつつ、YAMLと本文で同じ説明を長く重複させない。
- `source_note`、`japanese_note`、`creative_use`、`cautions` は各1文を目安にする。
- Timeline Entry本文は年表として読める短い要約と出典・リンクに絞る。
- Entity追記は主要な既存Person / Event / Themeに絞り、軽微な接続はCapture NoteとFact Cardリンクで足りる場合は追記しない。
- 新規stubは未解決リンク0のために必要な重要Entityだけ作る。stub本文は `Historical Role`、`Creative Use`、`Open Questions`、`Linked Items` の短い構成にする。
- Relationshipカードは従来どおり、命名規則が明確でない場合は新規作成せず、Capture Note内の候補に留める。
- 最終報告は作成ID範囲、ID変更、主要接続先、検証結果、重要な注意点だけを簡潔に報告する。
- 長文引用禁止、Hamnett解釈と史実の分離、Juárezの単純英雄化回避、Juchitán / Isthmus側の犯罪者化回避は省略せず維持する。

## Hamnett短縮依頼フォーマット

同じCodex環境でHamnettページ取込を続ける場合、ユーザー依頼文はページ固有情報だけでよい。以下の恒久ルールはこのファイルを参照し、依頼文側で毎回再掲しない。

- 再掲不要: 禁止事項、証拠分類一覧、`confidence` 一覧、Fact Card / Capture Note / Timeline Entryの標準YAML項目、Entity作成前確認、Relationshipカード保留方針、検証コマンド、標準最終報告項目、一般的なJuárez / Maximilian / Liberal / Conservative描写注意。
- 再掲必要: 対象ページ、スクリーンショット名、archive page、printed page、画面表示、予定ID、前後ページ接続、ページ大意、Fact候補、Timeline候補、Entity候補、ページ固有の照合観点・創作利用・要確認事項。
- 恒久ルールと依頼文が衝突する場合はこのファイルを優先する。ただし、対象ページ・スクリーンショット・処理順についてはユーザーの明示指定を優先し、Readinessとの差分を最終報告に残す。
- ページ固有情報は、`target`、`ids`、`continuity`、`page_summary`、`fact_candidates`、`timeline_candidates`、`entities`、`relationship_candidates`、`cross_check`、`creative_use`、`open_questions`、`extra_final_report` の見出しに圧縮してよい。
- Fact候補は `ID: statement / evidence_category / confidence / printed_page / source_note任意 / caution任意` の1行形式でよい。詳細なfrontmatterはテンプレートと既存ルールから補完する。
- Entity候補は `existing_connect`、`new_stub_consider`、`candidate_only` の3分類でよい。軽微なThemeや未確定のRelationshipはCapture Note候補に留める。

## ID とファイル名

- Capture Note: `CAP_HAMNETT_JUAREZ_NNNN.md`
- Fact Card: `FACT_HAMNETT_JUAREZ_NNNN.md`
- Timeline Entry: `TIME_HAMNETT_JUAREZ_NNNN.md`
- Source ID: `SRC_HAMNETT_1994_JUAREZ`

既存IDを上書きしない。次の番号は既存ファイルを見て連番の未使用値を選ぶ。番号の空きが過去作業で発生していても、既存運用に合わせて安全な次番号を使う。

ユーザー提示IDが既存ファイルと重複する場合、既存DBを優先し、連続した次の未使用IDへずらす。ID変更が発生した場合は、Capture Note本文と最終報告に「予定ID → 実使用ID」を明記する。

## Capture Note 作成ルール

- `01_Sources/Captures/` に置く。
- 対象は1ページ、見開き、または読書単位ごとの短い要約にする。
- 本文の長文引用は避ける。必要な原文メモは短い語句だけにする。
- `reading_accuracy`、`section`、`printed_page`、`archive_page`、`screenshot_file` を入れる。
- 「大意」「重要ポイント」「創作利用メモ」「要確認事項」を分ける。
- 作成した Fact Card と Timeline Entry を Capture Note 末尾にリンクする。
- ユーザー提供の要約を元にしても、全文翻訳・全文OCR・長文引用へ拡張しない。
- 短い原文メモは、指定語句または固有名詞確認に必要な最小限に限定する。
- 次ページへ文が続く場合は `next_page_continuation: yes` とし、Capture Note と関連 Fact Card に継続確認を残す。

## Fact Card 作成ルール

Fact Card は `02_Fact_Cards/` に置き、次の情報を必ず持たせる。

- `id`
- `type: "fact_card"`
- `status`
- `source_id: "SRC_HAMNETT_1994_JUAREZ"`
- `source_title: "Juarez"`
- `author: "Brian R. Hamnett"`
- `section`
- `printed_page`
- `archive_page` または `page`
- `screenshot_file`
- `printed_page_status`
- `title`
- `statement`
- `evidence_category`
- `confidence`
- `verification_needed`
- `source_note`
- `japanese_note`
- `creative_use`
- `cautions`
- `related_capture`
- `people`
- `events`
- `places`
- `organizations`
- `themes`

本文側には最低限 `## Claim`、`## Evidence / Citation`、`## Notes`、`## Links` を置く。`statement` と `## Claim` が食い違わないようにする。

## 証拠分類

`evidence_category` は既存ルールに合わせて次から選ぶ。

- `historical_fact`
- `primary_testimony`
- `author_interpretation`
- `rumor_hearsay`
- `variant_disputed`
- `creative_inference`

`confidence` は次から選ぶ。

- `confirmed`
- `probable`
- `uncertain`
- `disputed`
- `fictionalized`

Hamnett本文だけを根拠にした事実整理は、安易に `confirmed` にしない。史料・注・別文献でまだ照合していないものは `probable` または `uncertain` を使う。

## 紙面ページ確認

- 紙面ページを実際に確認できた Fact Card だけ `printed_page_status: "confirmed"` にする。
- Kindle位置、archive表示位置、スクリーンショット名だけがある場合は `printed_page_status: "not_verified"` にする。
- ページ欄を推測で埋めない。推測が必要なら `cautions` または `verification_needed` に残す。
- 現在の大きな残作業は紙面ページ確認であり、`printed_page_status: "not_verified"` が残ること自体は構造エラーではない。

## Entity とリンク

- 新しい人物・場所・組織・事件・テーマを作る前に、既存ノートの basename、タイトル、alias を確認する。
- 同じ basename の Markdown ファイルを増やさない。Obsidianでリンク解決が曖昧になる。
- 抽象テーマと実体組織を混同しない。例: `French_Opposition` テーマと `French_Opposition_to_Napoleon_III` 組織は別物として扱う。
- リンクは原則、`File_Stem|表示名` を二重角括弧で囲む形式にし、既存ノートの stem に向ける。
- 生成stubを作る場合も、最低限 `type`、`status`、`source_id`、概要、関連リンクを入れる。
- 重要度の高いstubには `## Historical Role`、`## Creative Use`、`## Open Questions` を追加する。
- 未解決リンクを0にするため、重要な新規 Person / Event / Organization / Theme は最小stubを作成してよい。
- Relationshipカードは既存DBの命名規則が不明な場合、新規作成せず Capture Note 内の候補に留める。
- 人物の同一性やフルネームが不確かな場合は、既存候補へ無理に統合せず、`verification_needed`、`cautions`、`Open Questions` に残す。

## Timeline Entry

- 日付または期間を持つ情報だけ `05_Timeline/` に入れる。
- Timeline Entry も出典、証拠分類、確度、関連 Fact Card へのリンクを持たせる。
- 年表化できるが日付が曖昧なものは、無理に正確な日付へ変換せず、期間または要確認として扱う。

## 進捗更新

Hamnett情報を追加したら、次を更新または再生成する。

- `93_Docs/Hamnett_Juarez_Progress_Master.md`
- Capture Note の作成カード一覧
- 関連 Entity の Linked Items
- 必要な Timeline Entry
- `08_Outputs/Indexes/` の索引
- `08_Outputs/Audits/` の監査レポート

索引と監査は保守スクリプトで再生成する。

```powershell
python .\MexicoEmpire_NovelDB\92_Scripts\vault_maintenance.py --phase all --apply
```

## 検証コマンド

作業後は必ず次を実行する。

```powershell
python .\MexicoEmpire_NovelDB\92_Scripts\auto_resolve_links.py --mode analyze --limit 20
python .\MexicoEmpire_NovelDB\92_Scripts\vault_maintenance.py --phase all
```

期待する状態:

- unresolved wiki links: `0`
- empty wiki links: `0`
- Fact Card の `statement` 欠落: `0`
- `source_id_review`: `0`
- locator missing: `0`
- 紙面ページ未確認だけは残ってよい

`vault_maintenance.py --phase all` は dry-run のため、表示された `audit_report` パスが新規作成されない場合がある。実ファイル確認には直近の `--apply` 実行時レポートを使う。

必要なら、Obsidian互換性として `.obsidian/*.json` が JSON として読めること、frontmatter が閉じていること、basename重複がないことも確認する。

## 禁止事項

- 書籍本文の全文保存、長文引用、全文翻訳、スクリーンショット全文転記をしない。
- 既存ノートを理由なく上書き・削除しない。
- ユーザーが作った変更を巻き戻さない。
- `printed_page_status: "confirmed"` を確認なしに付けない。
- Hamnettの解釈を一次史料の証言や確定史実として扱わない。
- Juarezを単純な英雄、Maximilianを単純な愚者または悲劇的人物、Liberal/Conservativeを単純な善悪二分法で処理しない。

## GitHub workflow

- DB更新はローカル編集だけでは完了しない。専用branchを作り、依頼対象ファイルだけをstageしてcommit・pushし、Pull Requestを作成するまでを必須とする。
- 通常取込は、`93_Docs/GitHub_Workflow.md`の安全条件をすべて満たす場合だけ通常Pull Requestとし、必須check `safety`成功後のsquash auto-mergeを設定する。
- Draft条件に該当する作業はDraft Pull Requestで停止し、auto-mergeを設定しない。
- branch名、commit SHA、PR URLを確認できない場合は「GitHub反映完了」と報告せず、「ローカルDB更新完了・GitHub反映未完了」と報告する。
- 詳細な開始確認、安全条件、Draft条件、禁止事項、merge後確認、最終報告は`93_Docs/GitHub_Workflow.md`に従う。
