---
id: JUAREZ_REPUBLICAN_SOURCE_GAP_ANALYSIS
type: source_gap_analysis
status: active
created: 2026-06-13
updated: 2026-06-14
tags:
  - source-gap
  - juarez
  - republican
  - shawcross
  - mexemp
source_id: SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO
---

# Juárez / Republican Source Gap Analysis

## 1. Purpose

このファイルは、Edward Shawcross, *The Last Emperor of Mexico: A Disaster in the New World* 由来DBの Maximilian / Habsburg / French / loyal witness 側への偏りを補正するため、Juárez・共和派・自由主義改革・対仏抵抗・帝政崩壊後の記憶化を補強する史料候補を整理する。

本工程では追加読解、本文カード化、Fact Card / Timeline Entry / Capture Note の新規作成は行わない。NOTESは本文Factではなく、既存の `NSI_SHAWCROSS_0001-0048`、`SRM_SHAWCROSS_0001-0048`、`NRC_SHAWCROSS_0001-0048` と同じく出典探索インデックスとして扱う。

RSG採番確認: Vault内検索で既存 `RSG_MEXEMP_####` は検出されなかったため、本工程は `RSG_MEXEMP_0001` から開始する。

## 2. Source Scope and Method

確認済みの既存整理ファイル:

- [[Shawcross_Progress_Master]]
- [[Shawcross_ID_Audit]]
- [[Shawcross_Notes_Source_Index]]
- [[Shawcross_Source_Reliability_Matrix]]
- [[Shawcross_Next_Reading_Candidates]]
- [[SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO]]

同趣旨ファイル確認:

- `93_Docs/Juarez_Republican_Source_Gap_Analysis.md` は既存なし。
- 関連ファイル名検索で確認できた既存カードは `Benito_Juarez.md`、`Mexican_Republicans.md`、`Liberal_Reform.md` のみ。
- 新規ファイルは本ファイルのみ。RSG個別Markdown、人物別Markdown、史料別Markdownは作成しない。

実在確認済みの関連既存カードID:

- `PER-BENITO-JUAREZ`
- `ORG-MEXICAN-REPUBLICANS`
- `THM-LIBERAL-REFORM`
- `EVT-FRENCH-INTERVENTION-IN-MEXICO`
- `EVT-SECOND-MEXICAN-EMPIRE`
- `PLC-QUERETARO`

今回の扱い:

- `FACT_MEXEMP_2561-2608` と `TIME_MEXEMP_0423-0448` は、`Shawcross_ID_Audit` 上で generation_gap_suspected とされているため、実在IDとして扱わない。
- RSG表の `related_existing_cards` には実在確認済みの上記IDのみを記載する。
- 回想録・証言は原則 `verification_needed: yes` とする。
- 二次史料は、史実確定ではなく一次・準一次史料への案内役、または記憶化の対象として扱う。

Hamnett関連略語は次の展開名と併記して扱う:

- AGEO = Archivo del Estado de Oaxaca
- AGN = Archivo General de la Nación (Mexico City)
- APBJPS = Archivo Privado de D. Benito Juárez y D. Pedro Santacilia, ed. J. Puig Casauranc, Mexico, 1928
- BBSHCP = Boletín Bibliográfico de la Secretaría de Hacienda y Crédito Público
- BEO CMMG = Biblioteca del Estado de Oaxaca, Colección Manuel Martínez Gracida
- BJDOCS = Benito Juárez. Documentos, discursos y correspondencia, ed. Jorge L. Tamayo, 15 vols, Mexico, 1964-71
- FJ = Fondo Juárez, Archivo General del Estado, Oaxaca
- HAHR = Hispanic American Historical Review
- UNAM = Universidad Nacional Autónoma de México

## 3. Bias Diagnosis: Shawcross-derived DB

Shawcross由来DBは、既存整理上、本文105枚、ACKNOWLEDGMENTS 1枚、NOTES 8枚に対応し、Shawcross source_id限定で Capture 103件、Fact 2034件、Timeline 321件が確認済みである。単一のShawcross本文から生成された大きなカード群であるため、叙述の重心は必然的にShawcrossの史料選択に強く依存する。

`Shawcross_Source_Reliability_Matrix` と `Shawcross_Next_Reading_Candidates` では、Shawcross NOTES由来の高優先候補が HHStA、Ratz、Foussemagne、Weckmann、Corti、Basch、Blasio、Felix Salm-Salm、Agnes Salm-Salm、AAE、400AP、FO、French military memoirs に厚く寄っていることが確認されている。これは Maximilian / Carlota / Habsburg / French policy / court witness / loyal witness の声を豊かにする一方で、Juárez政府内部、共和派軍、移動政府、自由主義改革の政策論理を直接には補強しない。

共和派側直接史料が不足している主な領域:

- Juárez本人の政治判断、助命拒否、合法性主張。
- 共和派政府の亡命・移動政府運営、行政継続、財政・通信・軍事指揮。
- Liberal Reform と教会政策の制度的背景。
- 共和派軍の作戦報告、Escobedo、Díaz、Corona らの動向。
- Black Decreeへの共和派側反応。
- Querétaro包囲戦を共和派がどう把握したか。
- Maximilian裁判・軍法会議・処刑判断の共和派法理。
- 第二帝政崩壊後の自由派記憶、国民史化、保守派記憶との対抗関係。

小説利用上危険な箇所:

- Agnes Salm-SalmのJuárez接触や助命嘆願を、共和派側記録なしに会話場面として固定すること。
- Basch / Blasio / Felix Salm-Salmの最終期描写を、忠誠・名誉回復・自己弁護のフィルターなしに史実認定へ転用すること。
- French withdrawal / Bazaine / Castelnau / Napoleon III の責任叙述を、フランス公文書と帝政側証言だけで閉じること。
- Black Decreeや軍法会議をMaximilian側の悲劇、またはJuárez側の冷酷さだけで描くこと。
- Mexican pressを世論そのものとして扱うこと。pressは public opinion / propaganda / rumor source として扱う。

既存DBで補強可能な箇所:

- 年表骨格、人物関係、Querétaro・裁判・処刑のShawcross側叙述位置。
- NSI/SRM/NRCによる出典候補の所在、バイアス、照合順。
- `PER-BENITO-JUAREZ`、`ORG-MEXICAN-REPUBLICANS`、`THM-LIBERAL-REFORM` などの実在エンティティへの接続。

追加読解が必要な箇所:

- BJDOCS / APBJPS / AGN / AGEO / FJ に基づくJuárez側一次・準一次史料。
- 共和派政府文書、軍事報告、裁判・軍法会議記録、自由派新聞の issue/date 単位確認。
- Hamnettの注を使った一次史料探索。Hamnett本文を最終証拠にせず、略語付き典拠表として使う。

## 4. Republican / Juárez-side Gap Summary

共和派側の不足は、単に「Juárezの人物像が薄い」ことではなく、Shawcross由来DBの事件説明が帝政側の体験、フランス側の政策、Habsburg側の家族・宮廷文脈、最終期の忠臣証言に引っ張られる点にある。特に裁判・処刑・Querétaro包囲は、読者にとってMaximilian悲劇として強く見えやすい。ここにJuárez側の法的連続性、共和国の存続主張、占領下での行政実務、軍事的消耗、国際承認戦略を入れないと、物語上も史料上もバランスを欠く。

優先補強線:

1. Hamnettを案内役に、BJDOCS、APBJPS、AGN、AGEO、FJのどこにJuárez側一次・準一次史料があるかを抽出する。
2. 裁判・軍法会議・処刑判断は、共和派政府文書、軍事報告、裁判記録、自由派新聞、U.S. official documentsを照合する。
3. Basch / Blasio / Salm-Salm証言は、BJDOCS、APBJPS、共和派軍事・司法記録、press issue/date で検証する。
4. Vigil、Zamacois、Arrangoiz、Romero de Terrerosは、記憶化・対抗叙述の材料として使い、一次史料の代替にしない。

## 5. RSG Index Table

| RSG ID | Candidate | Abbreviation | Expanded Name | Source Type | Republican Relevance | Related NSI | Related SRM | Related NRC | Priority | Verification Needed | Manual Review |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RSG_MEXEMP_0001 | Hamnett, *Juárez* | Hamnett | Brian R. Hamnett, *Juárez* | secondary | Juárez研究の現代的案内役。略語から一次・準一次史料へ入るための地図。 | NSI_SHAWCROSS_0026 | SRM_SHAWCROSS_0026 | NRC_SHAWCROSS_0026 | first | no | yes |
| RSG_MEXEMP_0002 | Benito Juárez documents collection | BJDOCS | Benito Juárez. Documentos, discursos y correspondencia, ed. Jorge L. Tamayo, 15 vols, Mexico, 1964-71 | quasi_primary | Juárez発言、書簡、布告、政府文書を追う本体候補。 | NSI_SHAWCROSS_0024; NSI_SHAWCROSS_0026; NSI_SHAWCROSS_0040 | SRM_SHAWCROSS_0024; SRM_SHAWCROSS_0026; SRM_SHAWCROSS_0040 | NRC_SHAWCROSS_0024; NRC_SHAWCROSS_0026; NRC_SHAWCROSS_0040 | first | yes | yes |
| RSG_MEXEMP_0003 | Juárez and Santacilia private archive edition | APBJPS | Archivo Privado de D. Benito Juárez y D. Pedro Santacilia, ed. J. Puig Casauranc, Mexico, 1928 | quasi_primary | Juárez私信・Santacilia経由の政治判断と家族・亡命政府文脈の候補。 | NSI_SHAWCROSS_0026; NSI_SHAWCROSS_0040 | SRM_SHAWCROSS_0026; SRM_SHAWCROSS_0040 | NRC_SHAWCROSS_0026; NRC_SHAWCROSS_0040 | second | yes | yes |
| RSG_MEXEMP_0004 | Archivo General de la Nación | AGN | Archivo General de la Nación (Mexico City) | archive_or_collection | 共和派政府、裁判、軍事、外交文書探索の中核候補。 | NSI_SHAWCROSS_0026; NSI_SHAWCROSS_0033 | SRM_SHAWCROSS_0026; SRM_SHAWCROSS_0033 | NRC_SHAWCROSS_0026; NRC_SHAWCROSS_0033 | first | yes | yes |
| RSG_MEXEMP_0005 | Oaxaca state archive | AGEO | Archivo del Estado de Oaxaca | archive_or_collection | Juárezの地域基盤、Oaxaca人脈、州行政・自由主義改革文脈の候補。 | NSI_SHAWCROSS_0026 | SRM_SHAWCROSS_0026 | NRC_SHAWCROSS_0026 | second | yes | yes |
| RSG_MEXEMP_0006 | Fondo Juárez, Oaxaca | FJ | Fondo Juárez, Archivo General del Estado, Oaxaca | archive_or_collection | Juárez本人・Oaxaca側の書簡、行政継続、個人ネットワークの候補。 | NSI_SHAWCROSS_0026 | SRM_SHAWCROSS_0026 | NRC_SHAWCROSS_0026 | first | yes | yes |
| RSG_MEXEMP_0007 | Republican government documents | - | 共和派政府文書、布告、回状、閣議・省庁文書 | primary | 移動政府、合法性主張、対仏抵抗、処刑判断の直接根拠候補。 | NSI_SHAWCROSS_0011; NSI_SHAWCROSS_0026; NSI_SHAWCROSS_0033 | SRM_SHAWCROSS_0011; SRM_SHAWCROSS_0026; SRM_SHAWCROSS_0033 | NRC_SHAWCROSS_0011; NRC_SHAWCROSS_0026; NRC_SHAWCROSS_0033 | first | yes | yes |
| RSG_MEXEMP_0008 | Republican military reports | - | 共和派軍事報告、作戦通信、将軍報告 | primary | Querétaro包囲、対仏抵抗、将軍間の判断を帝政側証言から切り離して検証する候補。 | NSI_SHAWCROSS_0022; NSI_SHAWCROSS_0026; NSI_SHAWCROSS_0033; NSI_SHAWCROSS_0039 | SRM_SHAWCROSS_0022; SRM_SHAWCROSS_0026; SRM_SHAWCROSS_0033; SRM_SHAWCROSS_0039 | NRC_SHAWCROSS_0022; NRC_SHAWCROSS_0026; NRC_SHAWCROSS_0033; NRC_SHAWCROSS_0039 | first | yes | yes |
| RSG_MEXEMP_0009 | Trial and court-martial records | - | Maximilian, Miramón, Mejía裁判・軍法会議記録 | primary | 軍法会議、罪状、判決、助命拒否、処刑判断の共和派法理を確認する候補。 | NSI_SHAWCROSS_0037; NSI_SHAWCROSS_0038; NSI_SHAWCROSS_0039; NSI_SHAWCROSS_0040; NSI_SHAWCROSS_0046 | SRM_SHAWCROSS_0037; SRM_SHAWCROSS_0038; SRM_SHAWCROSS_0039; SRM_SHAWCROSS_0040; SRM_SHAWCROSS_0046 | NRC_SHAWCROSS_0037; NRC_SHAWCROSS_0038; NRC_SHAWCROSS_0039; NRC_SHAWCROSS_0040; NRC_SHAWCROSS_0046 | first | yes | yes |
| RSG_MEXEMP_0010 | Liberal press issue list | - | 自由派新聞、共和派新聞、issue/date単位の新聞群 | press | 共和派世論、正統化、裁判・処刑・対仏抵抗の public rhetoric を補う候補。 | NSI_SHAWCROSS_0023; NSI_SHAWCROSS_0024 | SRM_SHAWCROSS_0023; SRM_SHAWCROSS_0024 | NRC_SHAWCROSS_0023; NRC_SHAWCROSS_0024 | second | yes | yes |
| RSG_MEXEMP_0011 | Mexican press from Shawcross cluster | Mexican press | La Sociedad, El Siglo, Mexican Times などShawcross由来press cluster | press | 共和派・帝政派・保守派・外国読者向け報道を分離して世論形成を読む候補。 | NSI_SHAWCROSS_0023 | SRM_SHAWCROSS_0023 | NRC_SHAWCROSS_0023 | second | yes | yes |
| RSG_MEXEMP_0012 | U.S. official documents | U.S. official documents | U.S. presidential and congressional documents | primary | Juárez政権承認、米国圧力、国境・武器・Monroe Doctrine文脈の外部公文書候補。 | NSI_SHAWCROSS_0011 | SRM_SHAWCROSS_0011 | NRC_SHAWCROSS_0011 | first | yes | yes |
| RSG_MEXEMP_0013 | José María Vigil | Vigil | José María Vigil / *México a través de los siglos* | secondary | 自由派・共和派記憶、国民史化、反帝政叙述の代表的counterweight。 | NSI_SHAWCROSS_0024 | SRM_SHAWCROSS_0024 | NRC_SHAWCROSS_0024 | second | no | yes |
| RSG_MEXEMP_0014 | Niceto de Zamacois | Zamacois | Niceto de Zamacois / *Historia de Méjico* | secondary | 保守寄り記憶と自由派記憶の対照。共和派側そのものではなく対抗記憶の照合先。 | NSI_SHAWCROSS_0027 | SRM_SHAWCROSS_0027 | NRC_SHAWCROSS_0027 | third | no | yes |
| RSG_MEXEMP_0015 | Arrangoiz y Berzábal | Arrangoiz | Francisco de Paula Arrangoiz y Berzábal / *Méjico desde 1808 hasta 1867* | memoir_or_testimony | 保守派参加者の自己弁護。共和派叙述を逆照射する対抗記憶候補。 | NSI_SHAWCROSS_0028 | SRM_SHAWCROSS_0028 | NRC_SHAWCROSS_0028 | third | yes | yes |
| RSG_MEXEMP_0016 | Romero de Terreros correspondence | Romero de Terreros | *Correspondencias contemporáneas* / Romero de Terreros, editor/source | quasi_primary | Mexico City elite reactions and political atmosphere の同時代性候補。 | NSI_SHAWCROSS_0029 | SRM_SHAWCROSS_0029 | NRC_SHAWCROSS_0029 | second | yes | yes |
| RSG_MEXEMP_0017 | García and Pereyra documentary collection | García/Pereyra | *Documentos inéditos o muy raros* / García and Pereyra, editors | quasi_primary | Shawcross由来で見えるMexican documentary trail。共和派側一次史料探索の入口候補。 | NSI_SHAWCROSS_0033 | SRM_SHAWCROSS_0033 | NRC_SHAWCROSS_0033 | second | yes | yes |
| RSG_MEXEMP_0018 | French official archives for cross-check | AAE / 400AP | Archives des Affaires Étrangères, CP Mexique; Archives nationales, Fonds Napoléon | archive_or_collection | 共和派側史料ではないが、French withdrawal、trial diplomacy、Castelnau/Bazaine責任を照合する外部軸。 | NSI_SHAWCROSS_0001; NSI_SHAWCROSS_0002; NSI_SHAWCROSS_0041; NSI_SHAWCROSS_0045 | SRM_SHAWCROSS_0001; SRM_SHAWCROSS_0002; SRM_SHAWCROSS_0041; SRM_SHAWCROSS_0045 | NRC_SHAWCROSS_0001; NRC_SHAWCROSS_0002; NRC_SHAWCROSS_0041; NRC_SHAWCROSS_0045 | third | yes | yes |
| RSG_MEXEMP_0019 | British Foreign Office reporting | FO | Foreign Office, National Archives, London | archive_or_collection | French・帝政・共和派の主張を外部外交報告で照合する候補。 | NSI_SHAWCROSS_0003; NSI_SHAWCROSS_0042 | SRM_SHAWCROSS_0003; SRM_SHAWCROSS_0042 | NRC_SHAWCROSS_0003; NRC_SHAWCROSS_0042 | third | yes | yes |
| RSG_MEXEMP_0020 | Reforma and church-state legal records | - | Leyes de Reforma、共和派法令、教会財産・聖職者政策文書 | primary | 自由主義改革、教会政策、Maximilianの教会政策評価を共和派法制から補強する候補。 | NSI_SHAWCROSS_0030; NSI_SHAWCROSS_0026 | SRM_SHAWCROSS_0030; SRM_SHAWCROSS_0026 | NRC_SHAWCROSS_0030; NRC_SHAWCROSS_0026 | first | yes | yes |
| RSG_MEXEMP_0021 | Agnes Salm-Salm Juárez-contact claims | Agnes Salm-Salm | Agnes Salm-Salm testimony/memoir references | memoir_or_testimony | Juárez接触・助命嘆願の高ドラマ領域。共和派側で検証すべき対象。 | NSI_SHAWCROSS_0040 | SRM_SHAWCROSS_0040 | NRC_SHAWCROSS_0040 | second | yes | yes |
| RSG_MEXEMP_0022 | William Harris Chynoweth trial reference | Chynoweth | William Harris Chynoweth reference, title and genre unclear | unclear | 裁判・処刑周辺の未特定候補。共和派側裁判記録との関係は要確認。 | NSI_SHAWCROSS_0046 | SRM_SHAWCROSS_0046 | NRC_SHAWCROSS_0046 | later | yes | yes |

Counts:

- RSG range: `RSG_MEXEMP_0001-0022`
- RSG count: 22
- source_type counts: `primary` 5, `quasi_primary` 4, `memoir_or_testimony` 2, `secondary` 3, `archive_or_collection` 5, `press` 2, `unclear` 1
- reading_priority counts: `first` 9, `second` 8, `third` 4, `later` 1
- verification_needed counts: `yes` 19, `no` 3

### RSG Candidate Detail Matrix

| RSG ID | related_shawcross_gap | related_existing_cards | expected_use_for_fact_check | expected_use_for_novel | bias_or_limitations | cross_check_targets |
|---|---|---|---|---|---|---|
| RSG_MEXEMP_0001 | Shawcross/NRCではJuárez側一次史料の入口が未展開。 | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS; THM-LIBERAL-REFORM | Hamnett注からBJDOCS, APBJPS, AGN, AGEO, FJへの導線を抽出。 | Juárez側場面の論点地図。移動政府、合法性、自由主義改革の背景整理。 | secondary。本文主張を最終証拠にしない。 | BJDOCS; APBJPS; AGN; AGEO; FJ; U.S. official documents |
| RSG_MEXEMP_0002 | Juárez本人の発言・書簡・政府判断が不足。 | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS | 助命拒否、裁判、移動政府、対仏抵抗、対米関係のJuárez側根拠。 | Juárezの沈黙、判断、書簡の間合いを場面化する基礎。 | edited collection。巻・日付・宛先・編集方針確認が必要。 | APBJPS; AGN; FJ; U.S. official documents; court-martial records |
| RSG_MEXEMP_0003 | 公的Juárez像だけでは私的・亡命政府の緊張が不足。 | PER-BENITO-JUAREZ | JuárezとSantacilia周辺の書簡、家族・政治ネットワークの確認。 | 移動政府の孤立、個人的負担、通信の遅延を描く材料。 | edited private archive。私信選択と編集意図に注意。 | BJDOCS; FJ; AGEO; Hamnett |
| RSG_MEXEMP_0004 | Mexican-side official record の探索基盤が不足。 | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS; EVT-SECOND-MEXICAN-EMPIRE | 政府・司法・軍事・外交文書の所在確認。 | 公文書の硬い声、行政継続、裁判制度の質感。 | finding aidとseries確認が必要。所蔵名だけで claim use しない。 | BJDOCS; court-martial records; military reports; press |
| RSG_MEXEMP_0005 | Oaxaca側の地域基盤とJuárez以前からの政治形成が薄い。 | PER-BENITO-JUAREZ; THM-LIBERAL-REFORM | Oaxaca行政・政治人脈・地域自由主義の確認。 | 首都外の政治世界、地方からの正統性を描く背景。 | 第二帝政期との直接接続は要確認。 | FJ; Hamnett; BJDOCS |
| RSG_MEXEMP_0006 | JuárezのOaxaca系書簡・個人史料の直接性が不足。 | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS | Juárez書簡、移動政府、Oaxacaネットワークの直接確認。 | Juárez側の非宮廷的な政治空間を描く材料。 | Fondo範囲とデジタル可用性は要確認。 | BJDOCS; APBJPS; AGEO |
| RSG_MEXEMP_0007 | 共和国政府の行政継続と合法性主張がShawcross側叙述で薄い。 | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS; EVT-FRENCH-INTERVENTION-IN-MEXICO | 政府布告、命令、閣僚通信、法令の確認。 | 移動政府の執務、布告作成、軍・外交への指示。 | 公文書は自己正当化を含む。日付・発行主体・配布先確認。 | BJDOCS; AGN; U.S. official documents; liberal press |
| RSG_MEXEMP_0008 | Republican armyの作戦認識が帝政側・French側証言に依存。 | ORG-MEXICAN-REPUBLICANS; EVT-FRENCH-INTERVENTION-IN-MEXICO; PLC-QUERETARO | Querétaro包囲、将軍間の命令、降伏・捕縛の照合。 | 野営、補給、軍議、勝利側の緊張を描く材料。 | 勝者側の報告は功績主張や責任回避を含む。 | court-martial records; BJDOCS; Mexican press; French memoirs |
| RSG_MEXEMP_0009 | 裁判・処刑の共和派法理が証言側の悲劇叙述に埋もれる。 | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS; PLC-QUERETARO | 起訴、弁護、判決、助命嘆願、処刑命令の一次確認。 | 法廷、文書、審理手続きの緊張を描く基礎。 | 記録の完全性、刊本・写本の差、後年編集に注意。 | BJDOCS; AGN; military reports; Basch; Salm-Salm; press |
| RSG_MEXEMP_0010 | 共和派世論形成と自由派新聞のissue/date対応が不足。 | ORG-MEXICAN-REPUBLICANS; THM-LIBERAL-REFORM | 記事日付、政治線、検閲・占領状況、報道と布告の対応確認。 | 街頭・読者・噂・正統化の空気。 | pressは中立証拠ではない。記事タイトル、紙名、政治的位置を必ず記録。 | government documents; rival press; Vigil; U.S. documents |
| RSG_MEXEMP_0011 | Shawcross press clusterが一括で、liberal/conservative/foreignの切り分け不足。 | EVT-FRENCH-INTERVENTION-IN-MEXICO; EVT-SECOND-MEXICAN-EMPIRE | Mexican pressをpublic opinion、propaganda、rumorに分類。 | 報道の声、噂の速度、儀礼・処刑報道の温度差。 | 紙名ごとの立場、発行地、発行日、外国読者向け編集に注意。 | official records; liberal press; Mexican conservative histories |
| RSG_MEXEMP_0012 | Juárez承認、米国圧力、国境・武器問題が外部文書に偏在。 | ORG-MEXICAN-REPUBLICANS; EVT-FRENCH-INTERVENTION-IN-MEXICO | U.S. recognition, Monroe Doctrine, Johnson administration, Congress文書の確認。 | 国境の圧力、外交文書の硬さ、戦後米国の存在感。 | U.S.国内政治と自己正当化を含む。Mexican republican recordsで照合。 | BJDOCS; Republican government documents; FO; AAE; Schofield |
| RSG_MEXEMP_0013 | 自由派記憶はあるが一次史料化されていない。 | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS; THM-LIBERAL-REFORM | 自由派・国民史叙述の論点抽出。一次史料探索の問いを作る。 | 帝政崩壊後の記憶化、共和派の自己像。 | later secondary。自由派国民史の政治性を切り分ける。 | Zamacois; Arrangoiz; Romero de Terreros; BJDOCS |
| RSG_MEXEMP_0014 | 保守派記憶との対照設計が必要。 | EVT-SECOND-MEXICAN-EMPIRE | Vigilと対置し、保守寄り叙述の論点を抽出。 | 保守派人物の自己理解、敗北後の苦味。 | later secondary。旧綴り、巻、立場、反自由派傾向に注意。 | Vigil; Arrangoiz; Mexican press; official records |
| RSG_MEXEMP_0015 | conservative participant memoryの自己弁護を整理する必要。 | EVT-SECOND-MEXICAN-EMPIRE | 保守派が共和派をどう描いたか、帝政崩壊をどう弁明したかを確認。 | 保守派内部の焦り、怨恨、正統性観を描く材料。 | memoir_or_testimony。反自由派・自己弁護が強い。verification_needed。 | Vigil; Zamacois; government documents; press |
| RSG_MEXEMP_0016 | 同時代Mexico City elite reactionが不足。 | EVT-SECOND-MEXICAN-EMPIRE | 書簡の日時・差出人・受取人・編集方針を確認。 | 都市の空気、政治的沈黙、私信の緊張。 | edited correspondence。選択と匿名性、政治的位置に注意。 | press; Vigil; Zamacois; official records |
| RSG_MEXEMP_0017 | Mexican documentary trailが未特定。 | EVT-SECOND-MEXICAN-EMPIRE; THM-LIBERAL-REFORM | rare documentsの原史料、巻、文書番号、真偽を確認。 | 失われた文書や知られにくいメキシコ側声の入口。 | editorial criteria unclear。原文書への遡及が必要。 | AGN; BJDOCS; Vigil; press |
| RSG_MEXEMP_0018 | French self-protective recordを共和派側から照合する必要。 | EVT-FRENCH-INTERVENTION-IN-MEXICO; PLC-QUERETARO | French withdrawal、trial diplomacy、Castelnau/Bazaineの説明をメキシコ側で検証。 | フランス側の責任回避、官僚文体、距離感。 | French official viewpoint。共和派側史料ではない。 | BJDOCS; Republican government documents; U.S. documents; FO; press |
| RSG_MEXEMP_0019 | 外交外部視点はあるが共和派内部ではない。 | EVT-FRENCH-INTERVENTION-IN-MEXICO | British reportsでFrench/Mexican claims、press rumorを照合。 | 外国公使館から見た不確実性と噂。 | British interests and limited access。 | AAE; U.S. documents; Mexican press; republican records |
| RSG_MEXEMP_0020 | Liberal Reformが背景語に留まり、法制度として不足。 | THM-LIBERAL-REFORM; PER-BENITO-JUAREZ | Leyes de Reforma、教会財産、聖職者政策、Maximilianとの政策差を確認。 | 教会政策を善悪でなく制度対立として描く基礎。 | 法令だけでは実施状況はわからない。地方記録・pressで照合。 | BJDOCS; AGN; AGEO; FJ; church records |
| RSG_MEXEMP_0021 | AgnesのJuárez接触が劇的すぎ、共和派側確認が不足。 | PER-BENITO-JUAREZ; PLC-QUERETARO | 面会の有無、同席者、日付、伝達内容を共和派側記録で確認。 | 助命嘆願場面の扱いを制御する。 | language barrier and reconstruction risk。dialogue literalization禁止。 | BJDOCS; court-martial records; press; Basch; Felix Salm-Salm |
| RSG_MEXEMP_0022 | trial/execution周辺の未特定ソースが残る。 | PLC-QUERETARO | bibliographic identity、genre、date、trial recordsとの関係を確認。 | 使えるか不明。現時点では場面素材にしない。 | unclear。要確認まで claim use 不可。 | Shawcross note image; library catalogue; court-martial records |

## 6. High Priority Reading Candidates

First priority:

- `RSG_MEXEMP_0001` Hamnett: まずHamnett注と略語を使い、BJDOCS、APBJPS、AGN、AGEO、FJ、U.S. official documentsへの索引を作る。Hamnett本文をFact化しない。
- `RSG_MEXEMP_0002` BJDOCS: Juárez本人の発言・文書・通信の中心候補。裁判、移動政府、対米外交、自由主義改革を優先。
- `RSG_MEXEMP_0004` AGN: 共和派政府・司法・軍事記録の探索基盤。
- `RSG_MEXEMP_0006` FJ: Juárez本人・Oaxaca系ネットワークの直接候補。
- `RSG_MEXEMP_0007` 共和派政府文書: 合法性、行政継続、処刑判断の直接根拠。
- `RSG_MEXEMP_0008` 共和派軍事報告: Querétaro包囲、将軍たちの動向、勝者側記録。
- `RSG_MEXEMP_0009` 裁判・軍法会議記録: Maximilian裁判・処刑判断の検証基盤。
- `RSG_MEXEMP_0012` U.S. official documents: Juárez承認、米国圧力、武器・国境問題の外部公文書。
- `RSG_MEXEMP_0020` Reforma and church-state legal records: 自由主義改革と教会政策の制度的根拠。

Second priority:

- `RSG_MEXEMP_0003` APBJPS、`RSG_MEXEMP_0005` AGEO、`RSG_MEXEMP_0010` Liberal press、`RSG_MEXEMP_0011` Mexican press、`RSG_MEXEMP_0013` Vigil、`RSG_MEXEMP_0016` Romero de Terreros、`RSG_MEXEMP_0017` García/Pereyra、`RSG_MEXEMP_0021` Agnes Salm-Salm verification target。

Third or later:

- `RSG_MEXEMP_0014` Zamacois、`RSG_MEXEMP_0015` Arrangoiz、`RSG_MEXEMP_0018` AAE/400AP、`RSG_MEXEMP_0019` FO、`RSG_MEXEMP_0022` Chynoweth。

## 7. Cross-check Design

### 7.1 Basch / Blasio / Salm-Salm witness cluster

Target witness IDs in existing SRM/NRC:

- Basch: `NSI/SRM/NRC_SHAWCROSS_0037`
- Blasio: `NSI/SRM/NRC_SHAWCROSS_0038`
- Felix Salm-Salm: `NSI/SRM/NRC_SHAWCROSS_0039`
- Agnes Salm-Salm: `NSI/SRM/NRC_SHAWCROSS_0040`

共和派側照合先:

- Juárezの助命判断、面会、通信: `RSG_MEXEMP_0002` BJDOCS、`RSG_MEXEMP_0003` APBJPS、`RSG_MEXEMP_0006` FJ。
- 裁判・軍法会議: `RSG_MEXEMP_0009`。
- 捕縛・包囲・軍事行動: `RSG_MEXEMP_0008`。
- 公的発表・世論反応: `RSG_MEXEMP_0010`、`RSG_MEXEMP_0011`。
- 外交的外圧: `RSG_MEXEMP_0012`、必要に応じて `RSG_MEXEMP_0018` と `RSG_MEXEMP_0019`。

運用ルール:

- 会話・身ぶり・泣訴・英雄的行動は、証言だけで史実認定しない。
- scene value と fact certification を分ける。
- Agnes Salm-SalmのJuárez接触は、共和派記録で面会の有無・日時・同席者を確認するまで `verification_needed`。

### 7.2 French diplomatic and military documents

French-side sources:

- AAE / CP Mexique: `NSI/SRM/NRC_SHAWCROSS_0002`, `0031`, `0045`
- 400AP / Fonds Napoléon / Castelnau: `NSI/SRM/NRC_SHAWCROSS_0001`, `0041`
- French military memoirs and later histories: `NSI/SRM/NRC_SHAWCROSS_0022`, `0025`, `0034`

Mexican-side cross-check:

- 共和派政府文書: `RSG_MEXEMP_0007`
- 共和派軍事報告: `RSG_MEXEMP_0008`
- BJDOCS / APBJPS / FJ: `RSG_MEXEMP_0002`, `0003`, `0006`
- U.S. official documents: `RSG_MEXEMP_0012`
- press issue/date: `RSG_MEXEMP_0010`, `0011`

照合対象:

- French withdrawalを「裏切り」だけで読む危険。
- Bazaine / Castelnau / Napoleon III の責任転嫁。
- Querétaro包囲時の軍事的選択肢。
- trial diplomacy と処刑後のフランス側自己防衛。

### 7.3 Mexican press

Pressは次に分ける:

- liberal/republican press
- conservative/imperial press
- foreign-language press in Mexico
- French, British, Belgian, U.S. press

最低限必要なメタデータ:

- paper title
- issue date
- publication place
- article title or section
- political alignment
- censorship or occupation context
- whether it is report, editorial, rumor, official notice, translation, or reprint

照合先:

- 共和派政府文書、裁判記録、軍事報告、BJDOCS。
- Vigil / Zamacois / Arrangoiz / Romero de Terreros。
- U.S. official documents and FO for foreign reception.

### 7.4 Vigil / Zamacois / Arrangoiz / Romero de Terreros

扱い分け:

- Vigil: liberal/republican national memory。共和派側のcounterweightだが、一次史料ではない。
- Zamacois: broad Mexican narrative, conservative-leaning or anti-liberal framing likely。
- Arrangoiz: conservative participant, retrospective self-defense。
- Romero de Terreros: edited contemporary correspondence。日付・差出人・編集方針が確認できれば、空気感とelite reactionに有用。

照合順:

1. 同一事件をVigilとZamacoisで比較し、自由派記憶と保守派記憶の叙述差を抽出。
2. Arrangoizで保守派自己弁護と責任配分を確認。
3. Romero de Terrerosで同時代書簡の日時・人物・都市空気を確認。
4. 最後にBJDOCS、共和派政府文書、press issue/date、裁判記録で事実面を固定する。

### 7.5 Hamnett as Guide

Hamnettは、Juárez側一次・準一次史料への索引として使う。本文カード化や長文引用はしない。

Hamnett注で略語が出た場合:

- 略語と展開名を併記する。
- 巻、ページ、文書番号、所蔵、日付を取る。
- BJDOCS / APBJPS / AGN / AGEO / FJ のどれに接続するかをRSG単位で記録する。
- 出典特定に不確実性がある場合は `要確認` または `manual_review_needed` とする。

## 8. Theme-by-Theme Gap Notes

| Theme | Main Gap | Priority RSG | Fact-check Use | Novel Risk if Unchecked |
|---|---|---|---|---|
| Juárez本人の政治判断 | 助命拒否、法理、外交判断がShawcross側では外部から見えがち。 | RSG_MEXEMP_0002; 0003; 0006; 0007; 0009 | Juárez発言、通信、布告、裁判記録で確認。 | Juárezを冷酷な対立軸か抽象的共和国記号として描く危険。 |
| 共和派政府の亡命・移動政府運営 | 行政継続、通信、財政、軍指揮が不足。 | RSG_MEXEMP_0002; 0004; 0007; 0012 | 政府文書、米国文書、Juárez書簡で移動政府の実務を確認。 | 宮廷ドラマだけが政治空間になる危険。 |
| 自由主義改革と教会政策 | Reformaが背景語に留まり制度史が薄い。 | RSG_MEXEMP_0001; 0002; 0020; 0005 | 法令・教会財産・共和派政策の時系列化。 | 教会問題をMaximilian個人の理想や妥協だけで描く危険。 |
| 対仏抵抗の軍事・政治過程 | Republican military reportsが不足。 | RSG_MEXEMP_0008; 0007; 0012; 0018 | 共和派軍報告とFrench documentsを照合。 | フランス軍撤退と帝政側視点だけで戦争が進む危険。 |
| 共和派将軍たちの動向 | Escobedo, Díaz, Corona等の判断がShawcross側証言に従属。 | RSG_MEXEMP_0008; 0004; 0010 | 軍事報告、政府指令、pressで確認。 | 勝者側が無人格な軍事圧力になる危険。 |
| 米国との関係 | recognition, weapons, border, pressure の細部不足。 | RSG_MEXEMP_0012; 0007; 0002 | U.S. official documentsとJuárez側記録を照合。 | 米国を都合のよい外圧装置として扱う危険。 |
| Black Decreeへの共和派側反応 | 共和派の法的・軍事的受け止め不足。 | RSG_MEXEMP_0002; 0007; 0010; 0020 | 布告、press、法律論で反応を確認。 | Maximilian悲劇かJuárez報復に単純化する危険。 |
| Querétaro包囲戦 | Republican perception and commandが不足。 | RSG_MEXEMP_0008; 0009; 0011 | 共和派軍報告、裁判記録、pressで捕縛・降伏を確認。 | Basch/Salm-Salmの内側だけで包囲戦が構成される危険。 |
| Maximilian裁判・処刑判断 | 軍法会議と政府判断の一次根拠不足。 | RSG_MEXEMP_0009; 0002; 0007; 0012 | 起訴、判決、助命嘆願、処刑命令を照合。 | 処刑を感情劇だけで描く危険。 |
| 第二帝政崩壊後の記憶化 | 自由派記憶と保守派記憶の分離不足。 | RSG_MEXEMP_0013; 0014; 0015; 0016 | Vigil, Zamacois, Arrangoiz, Romeroを相互照合。 | どちらか一方の国民史・殉教史に寄る危険。 |
| 自由派新聞・世論形成 | paper alignment and issue datesが不足。 | RSG_MEXEMP_0010; 0011 | issue/date tableで報道と公文書を照合。 | pressを市民全体の声として過大評価する危険。 |
| 保守派・帝政派記憶との対抗 | conservative memoryの役割整理不足。 | RSG_MEXEMP_0014; 0015; 0016 | liberal/conservative/elite correspondenceを比較。 | 善玉共和派と悪玉帝政派、またはその逆に寄る危険。 |

## 9. Novel Use Notes

史実認定と創作利用は分ける。

Juárez側視点を入れることで補強できる場面:

- 移動政府の執務、通信、軍事報告受領、外交文書処理。
- Black Decreeを受けた共和国側の怒り、法理、軍事的判断。
- Querétaro包囲戦を包囲する側から見る場面。
- 助命嘆願が届く場面、返答を検討する場面。ただし会話や身ぶりは史料確認まで創作推定。
- 処刑判断後の共和派内部の緊張、国際反応への警戒。
- 帝政崩壊後、自由派が勝利をどう記憶化し、保守派記憶とぶつかるか。

Maximilian中心叙述だけでは平板・偏向になりやすい場面:

- Miramarからの正統性演出。
- French withdrawalをめぐる責任論。
- Querétaroでの最終抵抗と捕縛。
- Agnes Salm-Salmの嘆願。
- 軍法会議と処刑。
- CarlotaとMaximilianの悲劇を、メキシコ国内政治の犠牲者としてだけ描く場面。

共和派側の政治的緊張を描くために必要な史料:

- BJDOCS / APBJPS / FJ によるJuárez側書簡。
- 共和派政府文書と法令。
- 共和派軍事報告。
- 裁判・軍法会議記録。
- liberal press issue/date table。
- U.S. official documents and Mexican republican records の相互照合。

敵役化・善玉化を避ける注意点:

- Juárez側を単純な勝者・冷酷な法執行者・民族正義の象徴だけにしない。
- Maximilian側を単純な無垢の犠牲者・高潔な理想家だけにしない。
- Conservative Mexican actorsを単なる反動派にせず、ただし自己弁護史料を事実認定に直結しない。
- French official recordsを「客観公文書」としてではなく、政策説明と責任管理の文書として読む。
- Pressは空気を描く材料として強いが、出来事認定には公文書・書簡・裁判記録との照合が必要。

創作推定として扱うべき領域:

- Juárezの内心、沈黙、表情。
- 助命嘆願時の逐語会話。
- 軍議の細かい感情の流れ。
- 新聞読者の反応を一人の市民の声に集約する場面。
- 未確認の伝聞・噂が街でどう広まったか。

## 10. Manual Review / Dependency List

Manual review needed:

- Hamnett版・ページ・注番号の確認。略語は展開名併記。
- BJDOCSの巻、ページ、文書番号、日付、発信者、宛先の確認。
- APBJPSの編集方針、対象範囲、Santacilia関係文書の性質確認。
- AGN / AGEO / FJ のseries、finding aid、利用可能性確認。
- 共和派政府文書、軍事報告、裁判・軍法会議記録の所在確認。
- liberal press と Mexican press の紙名・issue date・political alignment・article title確認。
- Vigil / Zamacois / Arrangoiz / Romero de Terreros の巻・版・編集方針・立場確認。
- García/Pereyraの正確な巻・文書番号・原史料確認。
- Chynoweth reference の書誌同定。
- `notes_translation_0109.md` 未発見に由来する `NSI/SRM/NRC_SHAWCROSS_0044` の未同定source names。
- `FACT_MEXEMP_2561-2608` と `TIME_MEXEMP_0423-0448` は実在IDとして扱わず、ID監査側の generation_gap_suspected に留める。

## 11. Next Recommended Step

工程7成果物:

- [[Hamnett_Juarez_Source_Trail_Index]]: Hamnett *Juárez* を本文Fact化せず、`HJI_MEXEMP_0001-0025` として BJDOCS / APBJPS / AGN / AGEO / FJ / 共和派政府文書 / 裁判記録 / liberal press / U.S. official documents への探索表に整理済み。

次工程候補:

1. [[Hamnett_Juarez_Source_Trail_Index]] をもとに、Hamnett現物の章・ページ・注番号と BJDOCS / APBJPS / AGN / AGEO / FJ の文書単位を確認する。
2. BJDOCSを最初に読み、Juárez本人の裁判・処刑・対仏抵抗・対米外交関連文書をRSG別に抽出する。
3. その後、裁判・軍法会議記録、共和派軍事報告、liberal press issue/date tableを作る。

この工程では、市販書籍本文、Shawcross本文、NOTES本文、Hamnett本文・注の長文引用、全文転記、本文Fact化、Timeline生成、CAP / FACT / TIME 再採番、削除、欠番補完は行っていない。
