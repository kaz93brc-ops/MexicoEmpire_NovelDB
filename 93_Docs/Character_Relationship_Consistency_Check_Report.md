---
id: CHARACTER_RELATIONSHIP_CONSISTENCY_CHECK_REPORT
type: operation_report
status: complete
created: 2026-06-14
updated: 2026-06-14
tags:
  - report
  - consistency-check
  - character-evidence
  - relationship
  - mexemp
rights_note: "No long quotations, translations, screenshots, or full text reproduction; this pass checked metadata, aliases, links, IDs, and index routes."
---

# Character Relationship Consistency Check Report

## 作業目的

人物・関係性カードの軽い整合性チェック。追加分析ではなく、aliases、frontmatter、リンク、ID重複、Index導線を確認した。

## 確認対象

- Personカード: [[Maximilian]], [[Carlota]], [[Benito_Juarez]], [[Napoleon_III]], [[Bazaine]], [[William H. Seward]], [[Miguel_Miramon]], [[Leonardo_Marquez]], [[Tomas_Mejia]], [[Mariano_Escobedo]], [[Porfirio_Diaz]], [[Juan_Nepomuceno_Almonte]]
- Relationshipカード: `REL_MEXEMP_0001-REL_MEXEMP_0014`
- Index / Report: [[Novel_Character_Design_Index]], [[Character_Relationship_Evidence_Expansion_Report]], [[Character_Relationship_Phase2_Report]]

## 実施した修正

- aliases: 主要4名とPhase 2人物8名に、アクセント有無、英西表記、短縮名、称号付き表記を最小追記した。
- frontmatter: 対象Personカードに `name`, `role`, `confidence` を補った。既存の `id`, `canonical_name`, `roles` は変更していない。`type: person` は既存形式を尊重して維持した。
- links: [[REL_MEXEMP_0006_Juarez_United_States_Seward]] のfrontmatter内 `[[United_States|United States]]` は、対応Orgカード未作成のため `"United States"` のプレーンテキストに変更した。
- reciprocal links: 指定されたRelationship間に `related_relationships` を最小追記した。
- index: [[Novel_Character_Design_Index]] にPhase 1 / Phase 2 / 本レポートへの導線を追記した。

## ID確認結果

- Person ID: 対象Personを含むPeople配下で重複なし。
- Relationship ID: `REL_MEXEMP_0001-REL_MEXEMP_0014` のfrontmatter IDは各1件。
- 重複の有無: Person ID / Relationship IDとも重複なし。
- Relationship IDとファイル名番号: 一致確認済み。

## リンク確認結果

- Person → Relationship: 対象Personカードからの `REL_MEXEMP_####` リンクは実在Relationshipカードに解決。
- Relationship → Person: Relationship frontmatter内の対象Personリンクは実在Personカードに解決。
- Relationship → Relationship: [[REL_MEXEMP_0001_Maximilian_Carlota]] / [[REL_MEXEMP_0002_Maximilian_Napoleon_III]] / [[REL_MEXEMP_0003_Maximilian_Benito_Juarez]] / [[REL_MEXEMP_0004_Maximilian_Bazaine]] / [[REL_MEXEMP_0008_Maximilian_Mexican_Liberals]] / [[REL_MEXEMP_0009_Carlota_Imperial_Court_Project]] / [[REL_MEXEMP_0010_Bazaine_French_Command_Napoleon_III]] / [[REL_MEXEMP_0011_Juarez_Republican_Generals]] の相互導線を確認。
- Index → Person / Relationship: [[Novel_Character_Design_Index]] から主要4名、Phase 2人物8名、`REL_MEXEMP_0001-REL_MEXEMP_0014`、Phase 1 / Phase 2 / 本レポートへ到達可能。

## ファイル名・表記ゆれ

| 対象 | 状況 | 対応 | 要検討 |
|---|---|---|---|
| Maximilian | aliases不足 | `Maximilian I`, `Maximiliano`, `Archduke Ferdinand Maximilian` などを追記 | なし |
| Carlota | aliases不足 | `Charlotte`, `Empress Carlota`, `Empress Charlotte` などを追記 | なし |
| Benito Juárez | accent有無・短縮名不足 | `Benito Juarez`, `Juárez`, `Juarez` を追記 | canonical_nameは既存のまま |
| Napoleon III | aliases空 | `Napoléon III`, `Louis-Napoléon`, `Louis Napoleon`, `Louis-Napoleon Bonaparte` を追記 | なし |
| Bazaine | 称号付き表記不足 | `Marshal Bazaine`, `Maréchal Bazaine` を追記 | なし |
| William H. Seward | 短縮名不足 | `William Seward`, `Seward` を追記 | ファイル名のスペースとピリオドは維持 |
| Miramón / Márquez / Mejía / Díaz | accent有無・短縮名不足 | アクセント付き、アクセントなし、姓のみを追記 | ファイル名はASCII寄りの既存名を維持 |
| United States | Orgカード未作成 | REL0006 frontmatterではリンク化せずプレーンテキスト化 | 将来Orgカード作成を検討 |

## リネーム保留事項

なし。既存ファイル名は変更していない。`William H. Seward.md` は実在ファイル名として維持した。

## 未修正・要確認

- `type: person` は既存Personカード形式として維持した。将来、Vault全体の型表記を `Person` に統一する場合は別工程で行う。
- United States Orgカードは未作成。今回は新規Orgカードを作らず、REL0006のfrontmatter上のリンクだけ外した。
- 本工程外の既存カードにある非対象リンクは網羅修正していない。
- Hamnett略語・共和派側一次資料のsource trailは今回の対象外。

## 次工程案

- Hamnett本の読解・DB化に戻る。
- Juárez側・共和派側一次資料の補強を進める。
- Carlota書簡 / Maximilian書簡 / Basch / Salm-Salm / Blasioによる人物関係の補強を行う。
