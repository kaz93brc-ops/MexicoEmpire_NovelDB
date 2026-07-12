---
id: NOVEL_CHARACTER_DESIGN_INDEX
type: novel_character_design_index
status: active
created: 2026-06-14
updated: 2026-06-14
tags:
  - novel-design
  - character-design
  - mexemp
  - ncd
ncd_range: NCD_MEXEMP_0001-NCD_MEXEMP_0031
source_handling: existing_db_linkage_only
rights_note: "Do not store Shawcross text, Hamnett text, NOTES text, screenshots, long quotations, or full transcriptions."
---

# Novel Character Design Index

## 1. Purpose

このDocは、MexicoEmpire_NovelDB 内の既存 Person / Fact / Timeline / Capture / Event / Place / Org / Theme / Source カードと、これまでの管理ファイルを、小説執筆用の人物設計へ接続するための集約インデックスである。

本工程では小説本文、台詞、心理描写本文、Fact Card、Timeline Entry、Capture Note、Person / Event / Place / Org / Theme / Sourceカードを新規作成しない。既存Personカードも全面改稿せず、人物ごとの史実根拠、創作利用、要検証点、史料偏りをNCD単位で整理する。

## 2. Method and Scope

- 同趣旨ファイル検索: `Character`, `Person`, `人物`, `人物設計`, `小説人物`, `Character Design`, `Novel Character`, `Viewpoint`, `POV`, `Arc`, `人物相関`, `関係性`, `NCD_MEXEMP_` を確認した。
- 同趣旨既存ファイル: 見つからなかったため、この `93_Docs/Novel_Character_Design_Index.md` を新規作成した。
- NCD採番: 既存 `NCD_MEXEMP_####` は検出されなかったため、`NCD_MEXEMP_0001` から開始する。
- ID使用ルール: `related_*_cards` には、既存ファイルまたは既存管理Docで実在確認済みとして扱われているカードIDのみを記載する。未実在・生成漏れ疑いのIDは関連カードとして扱わない。
- 範囲表記: `Novel_Chapter_Design_Linkage` と `Shawcross_ID_Audit` で実在確認済みとして整理済みの連続範囲だけを使う。人物ごとの全出現IDを網羅するものではない。
- 史実認定と創作利用は分ける。証言・回想録由来の場面素材、会話、内面、身ぶり、沈黙、噂は原則 `verification_needed: yes` または `creative_inference` として扱う。
- HamnettはJuárez側一次・準一次史料への出典探索ルートとして扱い、Hamnett本文・注をこのDocで本文Fact化しない。

## 3. Existing Person Card Coverage

確認できた既存Personカード:

| Person Card | ID | NCD |
|---|---|---|
| [[Maximilian]] | `PER-MAXIMILIAN` | `NCD_MEXEMP_0001` |
| [[Carlota]] | `PER-CARLOTA` | `NCD_MEXEMP_0002` |
| [[Benito_Juarez]] | `PER-BENITO-JUAREZ` | `NCD_MEXEMP_0003` |
| [[Napoleon_III]] | `PER-NAPOLEON-III` | `NCD_MEXEMP_0004` |
| [[Bazaine]] | `PER-BAZAINE` | `NCD_MEXEMP_0005` |
| [[Miguel_Miramon]] | `PER-MIGUEL-MIRAMON` | `NCD_MEXEMP_0007` |
| [[Leonardo_Marquez]] | `PER-LEONARDO-MARQUEZ` | `NCD_MEXEMP_0008` |
| [[Tomas_Mejia]] | `PER-TOMAS-MEJIA` | `NCD_MEXEMP_0009` |
| [[William H. Seward]] | `PER-WILLIAM-H-SEWARD` | `NCD_MEXEMP_0014` |
| [[Mariano_Escobedo]] | `PER-MARIANO-ESCOBEDO` | `NCD_MEXEMP_0024` |
| [[Porfirio_Diaz]] | `PER-PORFIRIO-DIAZ` | `NCD_MEXEMP_0025` |
| [[Franz_Joseph]] | `PER-FRANZ-JOSEPH` | `NCD_MEXEMP_0031` |

Phase 2で、Bazaine、Miramón、Márquez、Mejía、Seward、Escobedo、DíazのPersonカードを追加した。上記以外の人物は、引き続き `missing_person_card_candidate` またはPhase 2のB/C判定候補として扱う。

## 4. Source and Bias Caveats

- Shawcross由来DBは Maximilian / Carlota / Habsburg / French / loyal witness 側の素材が厚い。人物設計では、Juárez、共和派政府、共和派軍、裁判法理、自由主義改革、自由派新聞、戦後記憶を補強対象として明示する。
- Basch / Blasio / Felix Salm-Salm / Agnes Salm-Salm は場面価値が高いが、回想録・証言として `verification_needed: yes` を付ける。
- Agnes Salm-SalmのJuárez接触や助命嘆願は、共和派側記録なしに会話・身ぶり・心理へ固定しない。
- Mexican press は public opinion / propaganda / rumor source として扱い、事実認定の単独根拠にしない。
- Vigil / Zamacois / Arrangoiz / Romero de Terreros は記憶化・対抗叙述の材料として有効だが、一次史料の代替にしない。
- Juárezを単純な処刑者または完全な英雄として固定しない。Carlotaを悲劇的ヒロインだけに固定しない。Maximilianを殉教者だけに固定しない。

## 5. NCD Index Table

| NCD ID | Person | Existing Person Card | Coverage Group | Historical Role | Primary Novel Function | Viewpoint Potential | Related CDL | Related Fact | Related Timeline | Related Capture | Related Entity / Source Cards | Evidence Strength | Republican Balance Needed | Maximilian-centered Risk | Verification Needed | Manual Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `NCD_MEXEMP_0001` | Maximilian / Maximiliano | [[Maximilian]] `PER-MAXIMILIAN` | major | Emperor of Mexico | protagonist candidate | high | `CDL_MEXEMP_0001-0015` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `EVT-SECOND-MEXICAN-EMPIRE`; `PLC-MIRAMAR`; `PLC-QUERETARO`; `ORG-HABSBURG`; `THM-LEGITIMACY`; `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO` | moderate | yes | high | yes | yes |
| `NCD_MEXEMP_0002` | Carlota / Charlotte | [[Carlota]] `PER-CARLOTA` | major | Empress of Mexico | co-protagonist | high | `CDL_MEXEMP_0002`; `0004-0010`; `0014-0015` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `ORG-HABSBURG`; `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`; `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO` | moderate | yes | high | yes | yes |
| `NCD_MEXEMP_0003` | Benito Juárez | [[Benito_Juarez]] `PER-BENITO-JUAREZ` | major | President and republican legality carrier | political counterweight | high | `CDL_MEXEMP_0001`; `0003`; `0006`; `0008`; `0011-0016` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `ORG-MEXICAN-REPUBLICANS`; `THM-LIBERAL-REFORM`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`; RSG/HJI | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0004` | Napoleon III | [[Napoleon_III]] `PER-NAPOLEON-III` | major | French imperial sponsor | institutional actor | medium | `CDL_MEXEMP_0002-0004`; `0008-0010`; `0014` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `THM-FOREIGN-INTERVENTION`; AAE/400AP/FO routes | moderate | yes | high | yes | yes |
| `NCD_MEXEMP_0005` | Bazaine | [[Bazaine]] `PER-BAZAINE` | major | French military commander | institutional actor | medium | `CDL_MEXEMP_0003`; `0008-0011`; `0014` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `THM-FOREIGN-INTERVENTION`; `NSI/SRM/NRC_SHAWCROSS_0022`; `0043` | moderate | yes | high | yes | yes |
| `NCD_MEXEMP_0006` | Castelnau | none; `missing_person_card_candidate` | major | French late-stage envoy / military-diplomatic actor | mediator | medium | `CDL_MEXEMP_0009-0012` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `NSI/SRM/NRC_SHAWCROSS_0041`; 400AP route | mixed | yes | high | yes | yes |
| `NCD_MEXEMP_0007` | Miguel Miramón | [[Miguel_Miramon]] `PER-MIGUEL-MIRAMON` | major | Conservative general, Querétaro co-defendant | antagonist function | medium | `CDL_MEXEMP_0011-0013`; `0015` | `FACT_MEXEMP_0001-0006`; `2029-2365`; `2390-2438`; `2514` | `TIME_MEXEMP_0001-0002`; `0323-0375`; `0379-0386` | `CAP_MEXEMP_0001`; `0084-0102` | `ORG-MEXICAN-CONSERVATIVES`; `PLC-QUERETARO`; `NSI/SRM/NRC_SHAWCROSS_0009` | mixed | yes | high | yes | yes |
| `NCD_MEXEMP_0008` | Leonardo Márquez | [[Leonardo_Marquez]] `PER-LEONARDO-MARQUEZ` | major | Conservative general and imperial military actor | antagonist function | medium | `CDL_MEXEMP_0011`; `0013`; `0015` | `FACT_MEXEMP_2029-2365`; `2390-2438` | `TIME_MEXEMP_0323-0375`; `0379-0386` | `CAP_MEXEMP_0084-0095`; `0097-0102` | `ORG-MEXICAN-CONSERVATIVES`; `PLC-QUERETARO` | mixed | yes | high | yes | yes |
| `NCD_MEXEMP_0009` | Tomás Mejía | [[Tomas_Mejia]] `PER-TOMAS-MEJIA` | major | Imperial general, Querétaro co-defendant | tragic figure | medium | `CDL_MEXEMP_0011-0013`; `0015` | `FACT_MEXEMP_0001-0006`; `2029-2365`; `2390-2438`; `2514` | `TIME_MEXEMP_0001-0002`; `0323-0375`; `0379-0386` | `CAP_MEXEMP_0001`; `0084-0102` | `ORG-MEXICAN-CONSERVATIVES`; `PLC-QUERETARO` | mixed | yes | high | yes | yes |
| `NCD_MEXEMP_0010` | Samuel Basch | none; `missing_person_card_candidate` | witness | physician / loyal final-month witness | witness | high | `CDL_MEXEMP_0011-0015` | `FACT_MEXEMP_2029-2365`; `2390-2438`; `2514-2560` | `TIME_MEXEMP_0323-0375`; `0379-0386`; `0414-0422` | `CAP_MEXEMP_0084-0095`; `0097-0104` | `NSI/SRM/NRC_SHAWCROSS_0037`; `HJI_MEXEMP_0023` | mixed | yes | high | yes | yes |
| `NCD_MEXEMP_0011` | José Luis Blasio | none; `missing_person_card_candidate` | witness | private secretary / court-adjacent witness | source-bias carrier | medium | `CDL_MEXEMP_0010-0015` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `NSI/SRM/NRC_SHAWCROSS_0038`; `HJI_MEXEMP_0023` | mixed | yes | high | yes | yes |
| `NCD_MEXEMP_0012` | Felix Salm-Salm | none; `missing_person_card_candidate` | witness | military participant and memoir witness | witness | medium | `CDL_MEXEMP_0011-0015` | `FACT_MEXEMP_2029-2365`; `2390-2438`; `2514-2560` | `TIME_MEXEMP_0323-0375`; `0379-0386`; `0414-0422` | `CAP_MEXEMP_0084-0095`; `0097-0104` | `NSI/SRM/NRC_SHAWCROSS_0039`; `HJI_MEXEMP_0023` | mixed | yes | high | yes | yes |
| `NCD_MEXEMP_0013` | Agnes Salm-Salm | none; `missing_person_card_candidate` | witness | mercy-diplomacy participant and memoir witness | mediator | high | `CDL_MEXEMP_0012-0015` | `FACT_MEXEMP_2390-2438`; `2514-2560` | `TIME_MEXEMP_0379-0386`; `0414-0422` | `CAP_MEXEMP_0097-0104` | `NSI/SRM/NRC_SHAWCROSS_0040`; `RSG_MEXEMP_0021`; `HJI_MEXEMP_0017`; `0023` | mixed | yes | high | yes | yes |
| `NCD_MEXEMP_0014` | William H. Seward | [[William H. Seward]] `PER-WILLIAM-H-SEWARD` | secondary | U.S. diplomatic pressure actor | political counterweight | medium | `CDL_MEXEMP_0008`; `0012`; `0016` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `NSI/SRM/NRC_SHAWCROSS_0011`; `RSG_MEXEMP_0012`; `HJI_MEXEMP_0013` | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0015` | Andrew Johnson | none; `missing_person_card_candidate` | secondary | U.S. executive context after Lincoln | institutional actor | low | `CDL_MEXEMP_0008`; `0016` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `NSI/SRM/NRC_SHAWCROSS_0011`; `RSG_MEXEMP_0012`; `HJI_MEXEMP_0013` | weak | yes | medium | yes | yes |
| `NCD_MEXEMP_0016` | Abraham Lincoln | none; `missing_person_card_candidate` | secondary | U.S. Civil War / recognition background | symbolic figure | low | `CDL_MEXEMP_0003`; `0008`; `0016` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `NSI/SRM/NRC_SHAWCROSS_0011`; `RSG_MEXEMP_0012`; `HJI_MEXEMP_0013` | weak | yes | medium | yes | yes |
| `NCD_MEXEMP_0017` | Meglia | none; `missing_person_card_candidate` | secondary | Papal nuncio / church-state conflict actor | institutional actor | low | `CDL_MEXEMP_0006` | `FACT_MEXEMP_1137-1166`; `1262-1306`; `1327-1403` | `TIME_MEXEMP_0174-0178`; `0184-0189`; `0194-0204` | `CAP_MEXEMP_0046-0051`; `0053-0057` | `ORG-CATHOLIC-CHURCH`; `THM-LIBERAL-REFORM`; `NSI/SRM/NRC_SHAWCROSS_0030-0033` | weak | yes | medium | yes | yes |
| `NCD_MEXEMP_0018` | Iturbide関係者 | none; group-level `missing_person_card_candidate` | secondary | monarchy legitimacy / adoption-symbol cluster | symbolic figure | low | `CDL_MEXEMP_0002`; `0004-0005` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `ORG-MEXICAN-CONSERVATIVES`; `THM-LEGITIMACY` | weak | yes | medium | yes | yes |
| `NCD_MEXEMP_0019` | Alice Green | none; `missing_person_card_candidate` | secondary | 要確認: existing name matches, role not safely fixed here | witness | low | 要確認 | 要確認 | 要確認 | 要確認 | source trail to be identified before use | manual_review_needed | yes | high | yes | yes |
| `NCD_MEXEMP_0020` | Eloin | none; `missing_person_card_candidate` | secondary | 要確認: court/diplomatic-adjacent actor in existing mentions | mediator | low | 要確認 | 要確認 | 要確認 | 要確認 | source trail to be identified before use | manual_review_needed | yes | high | yes | yes |
| `NCD_MEXEMP_0021` | Faverney | none; `missing_person_card_candidate` | secondary | 要確認: existing name matches, role not safely fixed here | other | not_recommended | 要確認 | 要確認 | 要確認 | 要確認 | source trail to be identified before use | manual_review_needed | yes | high | yes | yes |
| `NCD_MEXEMP_0022` | John M. Schofield | none; `missing_person_card_candidate` | secondary | U.S. military memoir / policy observer | source-bias carrier | low | `CDL_MEXEMP_0008`; `0016` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | `NSI/SRM/NRC_SHAWCROSS_0035`; `RSG_MEXEMP_0012`; `HJI_MEXEMP_0013` | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0023` | Castagny | none; `missing_person_card_candidate` | secondary | French military actor; exact role requires review | institutional actor | low | `CDL_MEXEMP_0008-0011` | verified CDL ranges only | verified CDL ranges only | verified CDL ranges only | French military memoir / official routes | manual_review_needed | yes | high | yes | yes |
| `NCD_MEXEMP_0024` | Mariano Escobedo | [[Mariano_Escobedo]] `PER-MARIANO-ESCOBEDO` | secondary | Republican commander at Querétaro | institutional actor | medium | `CDL_MEXEMP_0011-0013`; `0016` | `FACT_MEXEMP_2029-2365`; `2390-2438`; `2514` | `TIME_MEXEMP_0323-0375`; `0379-0386` | `CAP_MEXEMP_0084-0095`; `0097-0102` | `ORG-MEXICAN-REPUBLICANS`; `PLC-QUERETARO`; `RSG_MEXEMP_0008-0009`; `HJI_MEXEMP_0010-0011`; `0016-0017` | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0025` | Porfirio Díaz | [[Porfirio_Diaz]] `PER-PORFIRIO-DIAZ` | secondary | Republican general and later memory/political horizon | symbolic figure | low | `CDL_MEXEMP_0014`; `0016` | `FACT_MEXEMP_2515-2560` | `TIME_MEXEMP_0414-0422` | `CAP_MEXEMP_0103-0106` | `ORG-MEXICAN-REPUBLICANS`; memory routes `RSG_MEXEMP_0013-0016`; `HJI_MEXEMP_0018-0019` | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0026` | Pedro Santacilia | none; `missing_person_card_candidate` | secondary | Juárez private/political correspondence route | mediator | low | `CDL_MEXEMP_0016` | 要確認 | 要確認 | 要確認 | `RSG_MEXEMP_0003`; `HJI_MEXEMP_0003`; `0017` | manual_review_needed | yes | medium | yes | yes |
| `NCD_MEXEMP_0027` | José María Vigil | none; `missing_person_card_candidate` | witness | liberal/republican memory and historiography | source-bias carrier | medium | `CDL_MEXEMP_0013-0016` | source trail only | source trail only | source trail only | `NSI/SRM/NRC_SHAWCROSS_0024`; `RSG_MEXEMP_0013`; `HJI_MEXEMP_0018-0019` | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0028` | Niceto de Zamacois | none; `missing_person_card_candidate` | witness | Mexican narrative / conservative counter-memory route | source-bias carrier | medium | `CDL_MEXEMP_0013-0016` | source trail only | source trail only | source trail only | `NSI/SRM/NRC_SHAWCROSS_0027`; `RSG_MEXEMP_0014`; `HJI_MEXEMP_0019` | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0029` | Arrangoiz y Berzábal | none; `missing_person_card_candidate` | witness | conservative participant-memory route | source-bias carrier | medium | `CDL_MEXEMP_0004-0005`; `0013-0016` | source trail only | source trail only | source trail only | `NSI/SRM/NRC_SHAWCROSS_0028`; `RSG_MEXEMP_0015`; `HJI_MEXEMP_0019` | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0030` | Romero de Terreros | none; `missing_person_card_candidate` | witness | edited contemporary correspondence route | source-bias carrier | medium | `CDL_MEXEMP_0013-0016` | source trail only | source trail only | source trail only | `NSI/SRM/NRC_SHAWCROSS_0029`; `RSG_MEXEMP_0016`; `HJI_MEXEMP_0019` | mixed | yes | medium | yes | yes |
| `NCD_MEXEMP_0031` | Franz Joseph | [[Franz_Joseph]] `PER-FRANZ-JOSEPH` | secondary | Habsburg dynastic actor | institutional actor | medium | `CDL_MEXEMP_0002`; `0004`; `0014` | `FACT_MEXEMP_0007-0260`; `0568-0786`; `2515-2560` | `TIME_MEXEMP_0003-0049`; `0095-0129`; `0414-0422` | `CAP_MEXEMP_0002-0012`; `0024-0034`; `0103-0106` | `ORG-HABSBURG`; `PLC-MIRAMAR`; `THM-LEGITIMACY`; HHStA/Ratz routes | moderate | yes | high | yes | yes |

## 6. Major Character Design Notes

### NCD_MEXEMP_0001 - Maximilian / Maximiliano

- person_name: Maximilian / Maximiliano
- existing_person_card: [[Maximilian]] (`PER-MAXIMILIAN`)
- historical_role: メキシコ皇帝。欧州君主制構想、Mexican Crown受諾、Liberal Empire、Black Decree、退位逡巡、Querétaro、裁判・処刑を貫く中心人物。
- novel_function: protagonist candidate; tragic figure; symbolic figure; source-bias carrier
- viewpoint_potential: high
- related_CDL: `CDL_MEXEMP_0001-0015`
- related_timeline_cards: `TIME_MEXEMP_0001-0002`; `0003-0049`; `0095-0129`; `0136-0168`; `0172-0178`; `0184-0189`; `0194-0204`; `0215-0250`; `0259-0268`; `0273-0291`; `0298-0301`; `0323-0375`; `0379-0386`; `0414-0422`
- related_fact_cards: `FACT_MEXEMP_0001-0006`; `0007-0260`; `0568-0786`; `0811-1087`; `1119-1166`; `1262-1306`; `1327-1403`; `1428-1673`; `1729-1775`; `1808-1880`; `1909-1936`; `2029-2365`; `2390-2438`; `2514-2560`
- related_capture_cards: `CAP_MEXEMP_0001-0043`; `0045-0051`; `0053-0095`; `0097-0106`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`
- related_place_cards: `PLC-MIRAMAR`; `PLC-QUERETARO`
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`; `THM-LIBERAL-REFORM`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`; `SRC_UNSET_001` only for `CAP/FACT/TIME_MEXEMP_0001-0006` attribution review
- related_NSI / SRM / NRC: `0004`; `0013`; `0015-0020`; `0037-0040`; `0048`
- related_RSG / HJI: `RSG_MEXEMP_0009`; `0021-0022`; `HJI_MEXEMP_0011`; `0017`; `0023`
- evidence_strength: moderate for broad chronology; mixed for final-month psychology and reported dialogue
- source_bias_notes: Shawcross-side, Habsburg-side, loyal-witness, and French official sources can over-center Maximilian as victim or martyr.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: idealist sovereign image -> constrained ruler dependent on French force -> liberal/conservative contradiction -> Black Decree and retreat options -> Querétaro enclosure -> legal defeat and memory contest. Inner motives require creative_inference unless supported by correspondence.
- relationship_conflicts: Carlota as partner and political actor; Juárez as legality counterweight; Napoleon III/Bazaine/Castelnau as support-withdrawal axis; Miramón/Márquez/Mejía as conservative-military trap; Basch/Blasio/Salm-Salm as loyal but biased narrators.
- usable_scene_types: Miramar decision, policy council, church-state conflict, correspondence reading, abdication debate, siege command, courtroom/prison, execution memory.
- factual_risk_notes: Do not use Basch / Blasio / Salm-Salm alone for exact words, emotional states, or last gestures. `FACT_MEXEMP_2561-2608` and `TIME_MEXEMP_0423-0448` are not used.
- missing_sources: court-martial record, republican government documents, BJDOCS/APBJPS/FJ, AAE/FO/400AP cross-checks.
- manual_review_needed: yes

### NCD_MEXEMP_0002 - Carlota / Charlotte

- person_name: Carlota / Charlotte
- existing_person_card: [[Carlota]] (`PER-CARLOTA`)
- historical_role: Empress of Mexico. 宮廷運営、外交交渉、Maximilianとの政治的協働、父Leopold I死去後の孤独、欧州への援助要請、後年の記憶化に関わる。
- novel_function: co-protagonist; political counterweight; tragic figure
- viewpoint_potential: high
- related_CDL: `CDL_MEXEMP_0002`; `0004-0010`; `0014-0015`
- related_timeline_cards: `TIME_MEXEMP_0003-0049`; `0095-0129`; `0136-0168`; `0174-0178`; `0184-0189`; `0194-0204`; `0215-0250`; `0256-0268`; `0273-0291`; `0298-0301`; `0414-0422`
- related_fact_cards: `FACT_MEXEMP_0007-0260`; `0568-0786`; `0811-1087`; `1119-1166`; `1262-1306`; `1327-1403`; `1428-1673`; `1707-1775`; `1808-1880`; `1909-1936`; `2390-2438`; `2514-2560`
- related_capture_cards: `CAP_MEXEMP_0002-0043`; `0045-0051`; `0053-0079`; `0097-0106`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-MIRAMAR`; `PLC-QUERETARO` as late-memory / indirect connection
- related_org_cards: `ORG-HABSBURG`; `ORG-CATHOLIC-CHURCH`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`; `THM-LIBERAL-REFORM`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0013`; `0016-0020`; `0038`; `0048`
- related_RSG / HJI: `RSG_MEXEMP_0013-0016`; `HJI_MEXEMP_0018-0019`
- evidence_strength: moderate for European/court chronology; mixed for breakdown, private words, and later memory.
- source_bias_notes: Habsburg, edited correspondence, Corti/Ratz/Foussemagne/Weckmann, and Blasio can make Carlota a tragic court figure while underplaying Mexican republican perception.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: politically active consort -> court-builder and policy participant -> diplomatic actor in Europe -> isolated figure in imperial collapse -> memory carrier. Avoid reducing this to private madness or pure romance.
- relationship_conflicts: Maximilian as partner and sovereign; Napoleon III as necessary but unreliable patron; Papacy/Church via Meglia; Juárez/Republicans mostly absent from Carlota-side sources and therefore requiring counterweight.
- usable_scene_types: Miramar domestic politics, court formation, church conflict, diplomatic audiences, letters, European refusal, epilogue/memory.
- factual_risk_notes: Her isolation and illness must not erase political agency. Juárez/republican-side view of Carlota is underdeveloped.
- missing_sources: HHStA originals/copies, Ratz editorial method, Belgian/French diplomatic records, Mexican republican press responses.
- manual_review_needed: yes

### NCD_MEXEMP_0003 - Benito Juárez

- person_name: Benito Juárez
- existing_person_card: [[Benito_Juarez]] (`PER-BENITO-JUAREZ`)
- historical_role: 共和国の合法性、移動政府、自由主義改革、対仏抵抗、米国関係、裁判・処刑判断を担う人物。
- novel_function: political counterweight; protagonist candidate; institutional actor
- viewpoint_potential: high
- related_CDL: `CDL_MEXEMP_0001`; `0003`; `0006`; `0008`; `0011-0016`
- related_timeline_cards: `TIME_MEXEMP_0001-0002`; `0050-0054`; `0064-0094`; `0174-0178`; `0184-0189`; `0194-0204`; `0228-0237`; `0259-0268`; `0273-0291`; `0298-0301`; `0323-0375`; `0379-0386`
- related_fact_cards: `FACT_MEXEMP_0001-0006`; `0261-0302`; `0331-0421`; `0446-0567`; `1127-1166`; `1262-1306`; `1327-1403`; `1546-1555`; `1732-1775`; `1808-1880`; `1909-1936`; `2029-2365`; `2390-2438`; `2514`
- related_capture_cards: `CAP_MEXEMP_0001`; `0013-0023`; `0045-0057`; `0065-0066`; `0072-0079`; `0084-0102`
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-CATHOLIC-CHURCH` for church-state conflict
- related_theme_cards: `THM-LIBERAL-REFORM`; `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`; `SRC_UNSET_001` attribution review
- related_NSI / SRM / NRC: `0011`; `0023-0024`; `0026`; `0033`; `0040`
- related_RSG: `RSG_MEXEMP_0001-0022`
- related_HJI: `HJI_MEXEMP_0001-0025`
- evidence_strength: mixed; direct Juárez/republican evidence is still a source-gap priority.
- source_bias_notes: Shawcross-side material can make Juárez visible only through imperial/french/witness reaction. Hamnett/RSG/HJI are source trails, not final proof.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: medium
- character_arc_candidate: reform/legal state builder -> mobile president under intervention -> diplomatic and military survivor -> decision-maker under trial/mercy pressure -> postwar legitimacy symbol. Inner life must remain controlled unless BJDOCS/APBJPS/FJ provide direct evidence.
- relationship_conflicts: Maximilian as rival sovereignty; Napoleon III/French intervention as foreign imposition; U.S. support/pressure as external necessity; Escobedo/republican generals as state-military link; Agnes Salm-Salm as risky witness-mediated contact.
- usable_scene_types: mobile government documents, legal councils, military dispatches, U.S. diplomacy, court-martial review, mercy appeals, liberal press reaction.
- factual_risk_notes: Do not portray Juárez as merely executioner or flawless hero. Trial and execution require BJDOCS, APBJPS, AGN, AGEO, FJ, court records, military reports, and press issue/date checks.
- missing_sources: BJDOCS document map, APBJPS/Santacilia correspondence, AGN/AGEO/FJ series, trial record, liberal press issue table.
- manual_review_needed: yes

### NCD_MEXEMP_0004 - Napoleon III

- person_name: Napoleon III
- existing_person_card: [[Napoleon_III]] (`PER-NAPOLEON-III`)
- historical_role: メキシコ帝政計画の後援者。欧州外交、フランス国内政治、議会批判、撤兵判断、責任転嫁・自己防衛の可能性を担う。
- novel_function: institutional actor; antagonist function; political counterweight
- viewpoint_potential: medium
- related_CDL: `CDL_MEXEMP_0002-0004`; `0008-0010`; `0014`
- related_timeline_cards: `TIME_MEXEMP_0003-0049`; `0050-0054`; `0064-0129`; `0205-0208`; `0215-0250`; `0256-0268`; `0273-0291`; `0298-0301`; `0414-0422`
- related_fact_cards: `FACT_MEXEMP_0007-0302`; `0331-0421`; `0446-0786`; `0811-0834`; `1404-1413`; `1428-1673`; `1707-1775`; `1808-1880`; `1909-1936`; `2515-2560`
- related_capture_cards: `CAP_MEXEMP_0002-0034`; `0058-0079`; `0103-0106`
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-MIRAMAR` for crown negotiations
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0001-0003`; `0008`; `0010-0012`; `0031`; `0041-0045`; `0047-0048`
- related_RSG / HJI: `RSG_MEXEMP_0018-0019`; `HJI_MEXEMP_0021-0022`
- evidence_strength: moderate for policy chronology; mixed for intention, blame, and private calculation.
- source_bias_notes: French official, legislative, and memoir records may protect French responsibility or reframe failure after the fact.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: architect/patron of intervention -> manager of diplomatic promise -> withdrawal decision-maker -> self-defensive imperial actor. Avoid making him the sole villain; domestic and international constraints matter.
- relationship_conflicts: Maximilian as dependent sovereign; Carlota as petitioner; Bazaine/Castelnau as implementation agents; Juárez/U.S. pressure as counterforce.
- usable_scene_types: cabinet/letter scenes, French legislative pressure, Saint-Cloud/audience context, withdrawal orders, blame displacement.
- factual_risk_notes: Responsibility claims require AAE, 400AP, FO, U.S. documents, French legislative material, and Mexican-side checks.
- missing_sources: sender-recipient-date table for AAE/400AP/FO references.
- manual_review_needed: yes

### NCD_MEXEMP_0005 - Bazaine

- person_name: Bazaine
- existing_person_card: [[Bazaine]] (`PER-BAZAINE`)
- historical_role: French military commander in Mexico; imperial support, military control, withdrawal, and responsibility questions connect him to Maximilian's dependence.
- novel_function: institutional actor; antagonist function; political counterweight
- viewpoint_potential: medium
- related_CDL: `CDL_MEXEMP_0003`; `0008-0011`; `0014`
- related_timeline_cards: verified French intervention / withdrawal / siege / epilogue CDL ranges only
- related_fact_cards: verified French intervention / withdrawal / siege / epilogue CDL ranges only
- related_capture_cards: verified French intervention / withdrawal / siege / epilogue CDL ranges only
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO` for late campaign context
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS` as conflict poles
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0022`; `0025`; `0034`; `0043`
- related_RSG / HJI: `RSG_MEXEMP_0008`; `0018-0019`; `HJI_MEXEMP_0010`; `0016`; `0021-0022`
- evidence_strength: moderate for presence and role; mixed for motive and blame.
- source_bias_notes: French military memoirs and later French histories can self-justify or shift responsibility.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: French power behind the throne -> unreliable protector -> withdrawal-era liability. Creative use should emphasize institution and command friction rather than private villainy.
- relationship_conflicts: Maximilian dependency; Napoleon III withdrawal; Castelnau mission; republican military pressure.
- usable_scene_types: military council, withdrawal notice, command friction, imperial court mistrust.
- factual_risk_notes: Bazaine-centered blame must be checked against AAE/400AP/FO, republican military reports, and Mexican-side records.
- missing_sources: French military reports, AAE/400AP file map, republican military counter-reports.
- manual_review_needed: yes

### NCD_MEXEMP_0006 - Castelnau

- person_name: Castelnau
- existing_person_card: none; `missing_person_card_candidate`
- historical_role: Late-stage French envoy / military-diplomatic actor tied to withdrawal, abdication pressure, and French responsibility management.
- novel_function: mediator; institutional actor; source-bias carrier
- viewpoint_potential: medium
- related_CDL: `CDL_MEXEMP_0009-0012`
- related_timeline_cards: `TIME_MEXEMP_0259-0268`; `0273-0291`; `0298-0301`; `0323-0375`; `0379-0386`
- related_fact_cards: `FACT_MEXEMP_1729-1775`; `1808-1880`; `1909-1936`; `2029-2365`; `2390-2438`; `2514`
- related_capture_cards: `CAP_MEXEMP_0072-0079`; `0084-0102`
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: none existing French army card; use event/theme only
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0041`; with `0001` 400AP route
- related_RSG / HJI: `RSG_MEXEMP_0018-0019`; `HJI_MEXEMP_0021-0022`
- evidence_strength: mixed
- source_bias_notes: Castelnau correspondence is primary-route material but must be placed in French state self-defense and withdrawal politics.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: messenger of narrowing options -> pressure point between French orders and Maximilian's self-image. Creative inference must stay tied to dated correspondence.
- relationship_conflicts: Napoleon III orders; Maximilian's refusal/hesitation; Bazaine command; republican advance.
- usable_scene_types: dispatch arrival, pressure meeting, withdrawal negotiation, contradiction between private advice and official stance.
- factual_risk_notes: Do not infer secret motive from mission outcome alone.
- missing_sources: 400AP/61 dossier, AAE/FO cross-check, Mexican-side reaction.
- manual_review_needed: yes

### NCD_MEXEMP_0007 - Miguel Miramón

- person_name: Miguel Miramón
- existing_person_card: [[Miguel_Miramon]] (`PER-MIGUEL-MIRAMON`)
- historical_role: Mexican conservative general, imperial military actor, Querétaro co-defendant and execution companion.
- novel_function: antagonist function; tragic figure; political counterweight
- viewpoint_potential: medium
- related_CDL: `CDL_MEXEMP_0011-0013`; `0015`
- related_timeline_cards: `TIME_MEXEMP_0001-0002`; `0323-0375`; `0379-0386`
- related_fact_cards: `FACT_MEXEMP_0001-0006`; `2029-2365`; `2390-2438`; `2514`
- related_capture_cards: `CAP_MEXEMP_0001`; `0084-0102`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`; `SRC_UNSET_001` attribution review for prologue IDs
- related_NSI / SRM / NRC: `0009`; `0022`; `0037-0040`
- related_RSG / HJI: `RSG_MEXEMP_0008-0009`; `HJI_MEXEMP_0010-0011`; `0016-0017`; `0023`
- evidence_strength: mixed
- source_bias_notes: Conservative family memory and witness accounts can defend or dramatize him.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: defeated conservative military ambition -> last imperial gamble -> co-defendant whose fate ties Mexican civil conflict to imperial collapse.
- relationship_conflicts: Maximilian command; Mejía parallel fate; Márquez operational tension; Escobedo/republicans; Juárez legal framework.
- usable_scene_types: siege command, military dispute, courtroom grouping, execution triad.
- factual_risk_notes: Avoid flattening him into loyal sidekick or villain. Trial records and conservative/republican memory comparison needed.
- missing_sources: trial records, republican military reports, Lombardo de Miramón memoir checks.
- manual_review_needed: yes

### NCD_MEXEMP_0008 - Leonardo Márquez

- person_name: Leonardo Márquez
- existing_person_card: [[Leonardo_Marquez]] (`PER-LEONARDO-MARQUEZ`)
- historical_role: Mexican conservative general and controversial imperial military actor, strongly connected to siege tension and blame narratives.
- novel_function: antagonist function; political counterweight
- viewpoint_potential: medium
- related_CDL: `CDL_MEXEMP_0011`; `0013`; `0015`
- related_timeline_cards: `TIME_MEXEMP_0323-0375`; `0379-0386`
- related_fact_cards: `FACT_MEXEMP_2029-2365`; `2390-2438`
- related_capture_cards: `CAP_MEXEMP_0084-0095`; `0097-0102`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0022`; `0037-0040`; Mexican conservative memory cluster `0027-0028`
- related_RSG / HJI: `RSG_MEXEMP_0008`; `0009`; `0014-0015`; `HJI_MEXEMP_0010-0011`; `0016-0019`
- evidence_strength: mixed
- source_bias_notes: Blame narratives around military failure are likely partisan.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: conservative hardline force -> operational fracture point -> memory scapegoat or defensive actor, depending on source standpoint.
- relationship_conflicts: Maximilian, Miramón, Mejía, Bazaine/Castelnau, Escobedo.
- usable_scene_types: command conflict, rumors of betrayal/failure, siege pressure, retrospective accusation.
- factual_risk_notes: Any claim about betrayal, cowardice, or cruelty requires multiple-source confirmation.
- missing_sources: republican reports, conservative memoirs, trial/military records.
- manual_review_needed: yes

### NCD_MEXEMP_0009 - Tomás Mejía

- person_name: Tomás Mejía
- existing_person_card: [[Tomas_Mejia]] (`PER-TOMAS-MEJIA`)
- historical_role: Imperial general and Querétaro co-defendant executed with Maximilian and Miramón.
- novel_function: tragic figure; witness-adjacent contrast; symbolic figure
- viewpoint_potential: medium
- related_CDL: `CDL_MEXEMP_0011-0013`; `0015`
- related_timeline_cards: `TIME_MEXEMP_0001-0002`; `0323-0375`; `0379-0386`
- related_fact_cards: `FACT_MEXEMP_0001-0006`; `2029-2365`; `2390-2438`; `2514`
- related_capture_cards: `CAP_MEXEMP_0001`; `0084-0102`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`; `SRC_UNSET_001` attribution review for prologue IDs
- related_NSI / SRM / NRC: `0022`; `0037-0040`
- related_RSG / HJI: `RSG_MEXEMP_0008-0009`; `HJI_MEXEMP_0010-0011`; `0016-0017`; `0023`
- evidence_strength: mixed
- source_bias_notes: Often subordinated to Maximilian's final image; need Mexican-side context for his own political/military standing.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: loyal imperial commander -> enclosed military actor -> co-defendant whose death complicates a purely European tragedy.
- relationship_conflicts: Maximilian/Miramón execution triad; Escobedo and court-martial; conservative/republican memory.
- usable_scene_types: siege, prison/court grouping, execution contrast, later memory.
- factual_risk_notes: Do not use him only as visual accompaniment to Maximilian.
- missing_sources: trial records, republican reports, Mexican conservative and liberal accounts.
- manual_review_needed: yes

### NCD_MEXEMP_0010 - Samuel Basch

- person_name: Samuel Basch
- existing_person_card: none; `missing_person_card_candidate`
- historical_role: Close medical/personal witness in final months; source for prison, mood, conduct, and final-crisis scenes.
- novel_function: witness; source-bias carrier
- viewpoint_potential: high
- related_CDL: `CDL_MEXEMP_0011-0015`
- related_timeline_cards: `TIME_MEXEMP_0323-0375`; `0379-0386`; `0414-0422`
- related_fact_cards: `FACT_MEXEMP_2029-2365`; `2390-2438`; `2514-2560`
- related_capture_cards: `CAP_MEXEMP_0084-0095`; `0097-0104`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0037`
- related_RSG / HJI: `RSG_MEXEMP_0021-0022`; `HJI_MEXEMP_0023`
- evidence_strength: mixed
- source_bias_notes: Loyal close witness; strong descriptive value but high risk for motive, dialogue, and final conduct.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: observer inside shrinking imperial world -> custodian of final image. Use as witness lens, not omniscient truth.
- relationship_conflicts: Maximilian dependence; Blasio/Salm-Salm testimony comparison; republican jail/court access.
- usable_scene_types: medical care, prison atmosphere, exhaustion, witness disagreement, post-execution memory.
- factual_risk_notes: Single-witness dialogue and mood claims are not settled fact.
- missing_sources: trial records, republican records, AAE/FO/400AP, press comparison.
- manual_review_needed: yes

### NCD_MEXEMP_0011 - José Luis Blasio

- person_name: José Luis Blasio
- existing_person_card: none; `missing_person_card_candidate`
- historical_role: Private secretary / court-adjacent witness; useful for court atmosphere, Carlota-adjacent material, and final months, but biased.
- novel_function: source-bias carrier; witness
- viewpoint_potential: medium
- related_CDL: `CDL_MEXEMP_0010-0015`
- related_timeline_cards: verified CDL ranges only
- related_fact_cards: verified CDL ranges only
- related_capture_cards: verified CDL ranges only
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0038`
- related_RSG / HJI: `RSG_MEXEMP_0021`; `HJI_MEXEMP_0023`
- evidence_strength: mixed
- source_bias_notes: Anecdotal proximity; private secretary perspective may intensify loyalty, self-defense, or court gossip.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: court insider -> recorder of collapse -> memory filter.
- relationship_conflicts: Carlota/Maximilian court world; Basch/Salm-Salm witness cluster; French and republican external realities.
- usable_scene_types: court rumor, El Olindo/Cuernavaca atmosphere, private correspondence handling, witness contradiction.
- factual_risk_notes: Do not turn rumor or retrospective court anecdote into direct fact.
- missing_sources: source edition check, court records, correspondence, Mexican-side confirmation.
- manual_review_needed: yes

### NCD_MEXEMP_0012 - Felix Salm-Salm

- person_name: Felix Salm-Salm
- existing_person_card: none; `missing_person_card_candidate`
- historical_role: Military participant and memoir witness in 1867 campaign, rescue/mercy effort context, and memory of Maximilian's final crisis.
- novel_function: witness; source-bias carrier
- viewpoint_potential: medium
- related_CDL: `CDL_MEXEMP_0011-0015`
- related_timeline_cards: `TIME_MEXEMP_0323-0375`; `0379-0386`; `0414-0422`
- related_fact_cards: `FACT_MEXEMP_2029-2365`; `2390-2438`; `2514-2560`
- related_capture_cards: `CAP_MEXEMP_0084-0095`; `0097-0104`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0039`
- related_RSG / HJI: `RSG_MEXEMP_0008-0009`; `0021`; `HJI_MEXEMP_0010-0011`; `0016-0017`; `0023`
- evidence_strength: mixed
- source_bias_notes: Participant heroization and self-defense risk.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: soldier of a collapsing cause -> rescuer/self-narrator -> memory-maker.
- relationship_conflicts: Agnes Salm-Salm; Maximilian; Miramón/Mejía; republican jail/court system.
- usable_scene_types: siege action, escape/rescue plan, mercy effort, retrospective comparison.
- factual_risk_notes: Use against Basch, Blasio, official records, and republican accounts.
- missing_sources: diary edition check, court records, republican reports.
- manual_review_needed: yes

### NCD_MEXEMP_0013 - Agnes Salm-Salm

- person_name: Agnes Salm-Salm
- existing_person_card: none; `missing_person_card_candidate`
- historical_role: Mercy diplomacy participant and memoir witness, especially claims of contact with Juárez/republican authorities.
- novel_function: mediator; witness; source-bias carrier
- viewpoint_potential: high
- related_CDL: `CDL_MEXEMP_0012-0015`
- related_timeline_cards: `TIME_MEXEMP_0379-0386`; `0414-0422`
- related_fact_cards: `FACT_MEXEMP_2390-2438`; `2514-2560`
- related_capture_cards: `CAP_MEXEMP_0097-0104`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI / SRM / NRC: `0040`
- related_RSG / HJI: `RSG_MEXEMP_0021`; `HJI_MEXEMP_0017`; `0023`
- evidence_strength: mixed
- source_bias_notes: Memoir/testimony with language-barrier and reconstructed-dialogue risk.
- verification_needed: yes
- republican_balance_needed: yes
- maximilian_centered_risk: high
- character_arc_candidate: outsider/participant seeking mercy -> failed negotiator -> contested witness.
- relationship_conflicts: Juárez and republican officials; Felix Salm-Salm; Maximilian; court-martial machinery.
- usable_scene_types: petition, access negotiation, failed mercy appeal, later witness disagreement.
- factual_risk_notes: Her Juárez-contact claims require republican-side confirmation before any conversation, gesture, or motive is used.
- missing_sources: BJDOCS, APBJPS, FJ, AGN, trial records, liberal press issue/date table.
- manual_review_needed: yes

## 7. Character Relationship and Conflict Matrix

| Axis | Characters / NCD | Story Function | Evidence / Risk |
|---|---|---|---|
| Rival sovereignty | Maximilian `0001` vs Juárez `0003` | empire vs republic, legitimacy conflict | Must balance imperial witness sources with BJDOCS/APBJPS/AGN/AGEO/FJ and court records. |
| Marriage and political partnership | Maximilian `0001` / Carlota `0002` | intimate politics, court building, diplomacy | Avoid making Carlota only a tragic wife; use correspondence and political actions. |
| Patron and dependency | Napoleon III `0004`, Bazaine `0005`, Castelnau `0006`, Maximilian `0001` | French support, withdrawal, responsibility | French official records may self-protect. Cross-check AAE/400AP/FO/U.S. documents. |
| Conservative military trap | Miramón `0007`, Márquez `0008`, Mejía `0009`, Maximilian `0001` | imperial side internal pressure and final military enclosure | Conservative memory and witness accounts require republican military reports. |
| Republican command and law | Juárez `0003`, Escobedo `0024`, Seward/US actors `0014-0016`, Schofield `0022` | mobile government, military victory, U.S. pressure | Do not substitute U.S. official or memoir views for Mexican republican records. |
| Court witness cluster | Basch `0010`, Blasio `0011`, Felix `0012`, Agnes `0013` | final-month atmosphere and scene texture | High scene value; weak as single-source proof. |
| Memory conflict | Vigil `0027`, Zamacois `0028`, Arrangoiz `0029`, Romero `0030`, Porfirio Díaz `0025` | liberal, conservative, edited-correspondence, and later memory | Keep memory politics separate from event-level proof. |

## 7.1 Relationship Evidence Cards Added 2026-06-14

今回の追加は、人物像の確定ではなく、PersonカードとRelationshipカードから既存DB内の人物像検討材料・関係性材料へ入れるようにする最小追記である。

- [[REL_MEXEMP_0001_Maximilian_Carlota]] - Maximilian `NCD_MEXEMP_0001` / Carlota `NCD_MEXEMP_0002`; marriage, political partnership, disputed influence.
- [[REL_MEXEMP_0002_Maximilian_Napoleon_III]] - Maximilian `NCD_MEXEMP_0001` / Napoleon III `NCD_MEXEMP_0004`; patronage, dependency, withdrawal.
- [[REL_MEXEMP_0003_Maximilian_Benito_Juarez]] - Maximilian `NCD_MEXEMP_0001` / Juárez `NCD_MEXEMP_0003`; rival legitimacy, legal-political conflict.
- [[REL_MEXEMP_0004_Maximilian_Bazaine]] - Maximilian `NCD_MEXEMP_0001` / Bazaine `NCD_MEXEMP_0005`; military support, command tension, abdication pressure.
- [[REL_MEXEMP_0005_Carlota_Napoleon_III]] - Carlota `NCD_MEXEMP_0002` / Napoleon III `NCD_MEXEMP_0004`; trust, diplomatic appeal, disappointment.
- [[REL_MEXEMP_0006_Juarez_United_States_Seward]] - Juárez `NCD_MEXEMP_0003` / Seward-U.S. `NCD_MEXEMP_0014-0016`; non-recognition, diplomatic pressure, aid context.
- Updated Person cards: [[Maximilian]], [[Carlota]], [[Benito_Juarez]], [[Napoleon_III]].

## 7.2 Relationship and Person Evidence Cards Added 2026-06-14 Phase 2

Phase 2では、前工程の主要人物Relationshipを拡張し、次点人物のPersonカード作成可否を判定した。関連レポートは [[Character_Relationship_Evidence_Expansion_Report]], [[Character_Relationship_Phase2_Report]], [[Character_Relationship_Consistency_Check_Report]] を参照。

- [[REL_MEXEMP_0007_Maximilian_Mexican_Conservative_Elites]] - Maximilian `NCD_MEXEMP_0001` / Mexican conservative elites; support base, dependency, liberal-policy tension.
- [[REL_MEXEMP_0008_Maximilian_Mexican_Liberals]] - Maximilian `NCD_MEXEMP_0001` / Mexican liberals and republicans; outreach, ideological overlap, rival legitimacy.
- [[REL_MEXEMP_0009_Carlota_Imperial_Court_Project]] - Carlota `NCD_MEXEMP_0002` / imperial court and project; court work, diplomacy, practical support.
- [[REL_MEXEMP_0010_Bazaine_French_Command_Napoleon_III]] - Bazaine `NCD_MEXEMP_0005` / Napoleon III `NCD_MEXEMP_0004`; French command, Regency, withdrawal.
- [[REL_MEXEMP_0011_Juarez_Republican_Generals]] - Juárez `NCD_MEXEMP_0003` / Republican generals; political legitimacy and military execution.
- [[REL_MEXEMP_0012_Juarez_Porfirio_Diaz]] - Juárez `NCD_MEXEMP_0003` / Porfirio Díaz `NCD_MEXEMP_0025`; Oaxaca and Army of the East.
- [[REL_MEXEMP_0013_Juarez_Escobedo]] - Juárez `NCD_MEXEMP_0003` / Escobedo `NCD_MEXEMP_0024`; Army of the North and Querétaro.
- [[REL_MEXEMP_0014_Mexican_Conservative_Elites_French_Intervention]] - Mexican conservative elites / French intervention; local collaboration and representation risk.
- New A-judgement Person cards: [[Bazaine]], [[William H. Seward]], [[Miguel_Miramon]], [[Leonardo_Marquez]], [[Tomas_Mejia]], [[Mariano_Escobedo]], [[Porfirio_Diaz]], [[Juan_Nepomuceno_Almonte]].
- B-judgement candidates retained for later authority work: Andrew Johnson, Empress Eugénie, Leopold I, Alice Green / Agustín de Iturbide y Green.

## 8. Viewpoint Candidate Analysis

High viewpoint candidates:

- Maximilian `NCD_MEXEMP_0001`: central but highest risk of martyr-centered narration.
- Carlota `NCD_MEXEMP_0002`: politically useful, especially court and European diplomacy; avoid tragic-only framing.
- Benito Juárez `NCD_MEXEMP_0003`: essential counterweight, but direct source trail must be strengthened before close interiority.
- Samuel Basch `NCD_MEXEMP_0010`: strong final-month observer; use as witness-lens only.
- Agnes Salm-Salm `NCD_MEXEMP_0013`: strong mercy-appeal lens; high verification burden.

Medium viewpoint candidates:

- Napoleon III, Bazaine, Castelnau, Miramón, Márquez, Mejía, Blasio, Felix Salm-Salm, Seward, Escobedo, Vigil, Zamacois, Arrangoiz, Romero de Terreros, Franz Joseph.

Low or not recommended as viewpoint without more evidence:

- Andrew Johnson, Lincoln, Meglia, Iturbide関係者, Alice Green, Eloin, Faverney, Schofield, Castagny, Porfirio Díaz, Santacilia.

## 9. Chapter Linkage by Character

| NCD | Character | Viewpoint candidate chapters | Conflict / necessary appearance chapters | Creative-use caution |
|---|---|---|---|
| `0001` | Maximilian | `CDL_MEXEMP_0001-0002`; `0004-0015` | all imperial collapse chapters | High Maximilian-centered risk; every final-month scene needs republican balance. |
| `0002` | Carlota | `CDL_MEXEMP_0002`; `0004-0010`; `0014` | court, diplomacy, memory | Do not reduce to illness or romance. |
| `0003` | Juárez | `CDL_MEXEMP_0003`; `0008`; `0011-0016` | intervention, Black Decree, trial, execution | Do not infer inner life without BJDOCS/APBJPS/FJ. |
| `0004-0006` | Napoleon III / Bazaine / Castelnau | `CDL_MEXEMP_0003`; `0008-0010` | French intervention and withdrawal | French self-defense records need countercheck. |
| `0007-0009` | Miramón / Márquez / Mejía | `CDL_MEXEMP_0011-0013` | Querétaro, trial, execution | Avoid using them only as Maximilian accessories. |
| `0010-0013` | Basch / Blasio / Salm-Salm | `CDL_MEXEMP_0011-0015` | witness-control chapter | Treat scenes as witness-colored unless corroborated. |
| `0014-0016`; `0022` | Seward / Johnson / Lincoln / Schofield | `CDL_MEXEMP_0008`; `0016` | U.S. pressure and recognition | External viewpoint, not republican interiority. |
| `0017` | Meglia | `CDL_MEXEMP_0006` | Liberal Empire, church conflict | Needs Vatican/church-state source trail before close use. |
| `0018` | Iturbide関係者 | `CDL_MEXEMP_0004-0005` | legitimacy theatre | Symbolic use only until individual identities are mapped. |
| `0019-0021`; `0023`; `0026` | Alice Green / Eloin / Faverney / Castagny / Santacilia | 要確認 | use only after role/source check | Missing Person cards and insufficient safe design basis. |
| `0024` | Escobedo | `CDL_MEXEMP_0011-0013`; `0016` | siege, capture, trial machinery | Strong candidate for republican military counterweight after reports are located. |
| `0025` | Porfirio Díaz | `CDL_MEXEMP_0014`; `0016` | memory and later political horizon | Avoid anachronistic Porfiriato teleology in 1867 scenes. |
| `0027-0030` | Vigil / Zamacois / Arrangoiz / Romero | `CDL_MEXEMP_0014-0016` | memory, historiography, counter-narrative | Source voices, not direct scene witnesses unless specific dated material is confirmed. |
| `0031` | Franz Joseph | `CDL_MEXEMP_0002`; `0004`; `0014` | Habsburg family and memory | Habsburg frame can over-Europeanize the novel. |

## 10. Source Trail Linkage: NSI / SRM / NRC / RSG / HJI / CDL

| Source Trail Cluster | IDs | Character Use |
|---|---|---|
| French official / diplomatic | `NSI/SRM/NRC_SHAWCROSS_0001-0003`; `0008`; `0031`; `0041-0045` | Napoleon III, Bazaine, Castelnau, withdrawal, trial diplomacy |
| Habsburg / Maximilian-Carlota | `NSI/SRM/NRC_SHAWCROSS_0004`; `0013`; `0016-0020` | Maximilian, Carlota, Franz Joseph, Miramar, court politics |
| U.S. official / policy | `NSI/SRM/NRC_SHAWCROSS_0011`; `0035`; `RSG_MEXEMP_0012`; `HJI_MEXEMP_0013` | Seward, Johnson, Lincoln, Schofield, U.S. pressure |
| Mexican political voices | `NSI/SRM/NRC_SHAWCROSS_0006`; `0023-0029`; `0033` | Mexican conservatives, liberal/republican memory, press, documentary trails |
| Final-month witness cluster | `NSI/SRM/NRC_SHAWCROSS_0037-0040`; `HJI_MEXEMP_0023` | Basch, Blasio, Felix Salm-Salm, Agnes Salm-Salm |
| Republican source gap | `RSG_MEXEMP_0001-0022` | Juárez, Escobedo, trial/court-martial, military reports, press, legal framework |
| Hamnett Juárez source trail | `HJI_MEXEMP_0001-0025` | BJDOCS, APBJPS, AGN, AGEO, FJ mapping; use as guide only |
| Chapter design linkage | `CDL_MEXEMP_0001-0016` | all NCD records; especially `0011-0016` for republican balance and witness control |

## 11. Novel Use Notes

- Best close viewpoint candidates: Maximilian, Carlota, Juárez, Basch, Agnes Salm-Salm. The last two must be framed as witness accounts, not omniscient truth.
- Best institutional counterweights: Napoleon III, Bazaine, Castelnau, Meglia, Escobedo, Seward.
- Best conflict figures inside the imperial camp: Miramón, Márquez, Mejía, Blasio, Basch, Felix Salm-Salm.
- Best memory-layer figures: Vigil, Zamacois, Arrangoiz, Romero de Terreros, Porfirio Díaz, Franz Joseph.
- Characters with strong scene potential but high factual risk: Basch, Blasio, Felix Salm-Salm, Agnes Salm-Salm, Alice Green, Eloin, Faverney.
- Characters whose appearance is useful but not yet safe for close interiority: Seward, Johnson, Lincoln, Meglia, Iturbide関係者, Schofield, Castagny, Santacilia.

## 12. Factual Risk and Verification Notes

- Known missing CAPs: `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096`.
- Known non-existing post-max Fact IDs: `FACT_MEXEMP_2561-2608`.
- Known non-existing post-max Timeline IDs: `TIME_MEXEMP_0423-0448`.
- Trial and epilogue generation-gap dependencies: `FACT_MEXEMP_2439-2513`, `TIME_MEXEMP_0387-0413`, `TIME_MEXEMP_0413`.
- Prologue source issue: `SRC_UNSET_001` remains separate from `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- Witness risk: Basch / Blasio / Felix Salm-Salm / Agnes Salm-Salm are scene-rich but require court-martial records, Juárez-side documents, official diplomatic records, and press comparison.
- Republican gap: RSG/HJI must be resolved before future Fact/Timeline creation about Juárez decision-making, republican military reporting, court martial, Liberal Reform, and liberal press.
- Missing Person card risk: Phase 2で主要な軍事・外交アクターの一部はPersonカード化したが、witness cluster、U.S.周辺、Iturbide cluster、source-bias carrierは未作成が残る。

## 13. Missing Person Card Candidates

Personカード未作成候補:

- Castelnau
- Samuel Basch
- José Luis Blasio
- Felix Salm-Salm
- Agnes Salm-Salm
- Andrew Johnson
- Abraham Lincoln
- Meglia
- Iturbide関係者
- Alice Green
- Eloin
- Faverney
- John M. Schofield
- Castagny
- Pedro Santacilia
- José María Vigil
- Niceto de Zamacois
- Arrangoiz y Berzábal
- Romero de Terreros

Phase 2でBazaine、Miramón、Márquez、Mejía、William H. Seward、Mariano Escobedo、Porfirio Díaz、Juan Nepomuceno AlmonteはPersonカード化した。残る候補を将来作成する場合は、人物同定、典拠、aliases、source trail、史料種別を確認してから別工程で行う。

## 14. Manual Review / Dependency List

| Dependency | Related NCD | Required Before Future Use |
|---|---|---|
| BJDOCS / APBJPS / AGN / AGEO / FJ document-level map | `0003`; `0013`; `0024`; `0026` | Juárez decision-making, mercy appeals, execution decision, republican government operation |
| Trial and court-martial records | `0001`; `0003`; `0007-0013`; `0024` | charges, procedure, sentence, appeals, execution order |
| Republican military reports | `0003`; `0007-0009`; `0024`; `0025` | Querétaro siege, capture, victory-side command |
| Witness cluster comparison | `0010-0013` | Basch/Blasio/Felix/Agnes contradictions, language and self-fashioning risk |
| French official / FO / 400AP / AAE table | `0004-0006`; `0014-0016`; `0023` | withdrawal chronology, blame shifting, diplomatic pressure |
| Church-state / Meglia source trail | `0002`; `0003`; `0017` | Liberal Empire, Catholic Church, papal diplomacy |
| Mexican memory comparison | `0025`; `0027-0030`; `0031` | liberal, conservative, edited correspondence, European memory separation |
| Role identification for Alice Green / Eloin / Faverney / Castagny | `0019-0021`; `0023` | prevent overuse of under-specified figures |
| Person card authority work | all missing candidates | only after source identity and aliases are verified |

## 15. Next Recommended Step

次工程候補:

1. `NCD_MEXEMP_0003`, `0013`, `0024` を起点に、BJDOCS / APBJPS / AGN / AGEO / FJ と裁判・軍法会議記録の文書単位チェックリストを作る。
2. `NCD_MEXEMP_0010-0013` の witness cluster を、Basch / Blasio / Felix Salm-Salm / Agnes Salm-Salm の比較表として整理する。ただし新規Fact/Timeline化は、共和派側・公文書側の照合後に限定する。
3. 残るPersonカード未作成候補のうち、Castelnau、Basch、Blasio、Salm-Salm夫妻、Andrew Johnson、Empress Eugénie、Leopold I、Alice Green / Iturbide clusterを優先し、将来の人物カード作成可否を典拠単位で判定する。

## 16. Work Log and Stats

- Created: 2026-06-14.
- Same-purpose existing file: not found.
- Existing NCD ID: not found; started at `NCD_MEXEMP_0001`.
- NCD count: 31.
- NCD range: `NCD_MEXEMP_0001-NCD_MEXEMP_0031`.
- Existing NCD-linked Person card coverage: 12 existing; 19 missing person card candidates. Phase 2 also created [[Juan_Nepomuceno_Almonte]], which was not assigned a distinct NCD row in the original index.
- Coverage group counts: major 9; secondary 14; witness/source-recording group 8.
- Primary novel_function counts: protagonist candidate 1; co-protagonist 1; political counterweight 2; institutional actor 7; mediator 4; antagonist function 2; tragic figure 1; witness 3; source-bias carrier 6; symbolic figure 3; other 1.
- viewpoint_potential counts: high 5; medium 15; low 10; not_recommended 1.
- evidence_strength counts: strong 0; moderate 5; mixed 17; weak 4; manual_review_needed 5.
- republican_balance_needed yes: 31.
- maximilian_centered_risk counts: high 17; medium 14; low 0.
- verification_needed yes: 31.
- manual_review_needed yes: 31.
- 2026-06-14 relationship expansion: created `REL_MEXEMP_0001-REL_MEXEMP_0006`; updated [[Maximilian]], [[Carlota]], [[Benito_Juarez]], [[Napoleon_III]] with Character Evidence / 人物像検討材料 sections and relationship links.
- 2026-06-14 Phase 2 relationship expansion: created `REL_MEXEMP_0007-REL_MEXEMP_0014`; created A-judgement Person cards for Bazaine, Seward, Miramón, Márquez, Mejía, Escobedo, Díaz, and Almonte; updated major Person cards with new relationship links.
- No new Fact Card, Timeline Entry, Capture Note, individual NCD Markdown, character Markdown, chapter Markdown, event/place/org/theme/source card, novel prose, dialogue, psychological prose, long quotation, full transcription, renumbering, deletion, or gap filling was created.
- `FACT_MEXEMP_2561-2608` and `TIME_MEXEMP_0423-0448` were not used as existing related cards.
