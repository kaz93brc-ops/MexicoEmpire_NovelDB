---
id: NOVEL_CHAPTER_DESIGN_LINKAGE
type: chapter_design_linkage
status: active
created: 2026-06-14
updated: 2026-06-14
tags:
  - novel-design
  - chapter-linkage
  - mexemp
  - cdl
cdl_range: CDL_MEXEMP_0001-CDL_MEXEMP_0016
source_handling: existing_db_linkage_only
rights_note: "Do not store Shawcross text, Hamnett text, NOTES text, screenshots, long quotations, or full transcriptions."
---

# Novel Chapter Design Linkage

## 1. Purpose

このDocは、既存の MexicoEmpire_NovelDB を小説の仮章立て・場面設計・視点設計へ接続するためのDB利用設計表である。

本工程では、新しい本文カード、小説本文、Fact Card、Timeline Entry、Capture Note、Person / Event / Place / Org / Theme / Sourceカードを作成しない。既存カード群を、どの幕・章候補・場面候補に使えるかだけを整理する。

## 2. Method and Scope

- 既存同趣旨ファイル検索: `Chapter`, `Plot`, `Outline`, `Novel`, `Scene`, `Structure`, `Act`, `Arc`, `Chapter Design`, `Story Design`, `Scene Plan`, `仮章立て`, `章立て`, `構成`, `場面設計`, `小説設計`, `CDL_MEXEMP_` を確認した。同趣旨Docと既存CDL IDは見つからなかった。
- 採番: 既存 `CDL_MEXEMP_####` がなかったため、`CDL_MEXEMP_0001` から開始する。
- ID使用ルール: `related_*_cards` には実在確認済みIDのみを記載する。範囲表記は、[[Shawcross_ID_Audit]] と実在ファイル名で確認できた連続範囲だけを示す。
- 除外ルール: `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096` はファイル未発見として関連カード欄には入れない。`FACT_MEXEMP_2561-2608` と `TIME_MEXEMP_0423-0448` は実在IDとして扱わない。
- NOTES / Hamnett: [[Shawcross_Notes_Source_Index]], [[Shawcross_Source_Reliability_Matrix]], [[Shawcross_Next_Reading_Candidates]], [[Juarez_Republican_Source_Gap_Analysis]], [[Hamnett_Juarez_Source_Trail_Index]] は出典探索・信頼性・次読書計画として扱い、本文Fact化しない。
- 史実認定と創作利用は分ける。会話、内心、表情、沈黙、噂の広がり、証言由来の劇的場面は、原則 `verification_needed` または `creative_inference` として扱う。

## 3. Existing DB Coverage

確認済みの既存整理Doc:

- [[Shawcross_Progress_Master]]
- [[Shawcross_ID_Audit]]
- [[Shawcross_Notes_Source_Index]]
- [[Shawcross_Source_Reliability_Matrix]]
- [[Shawcross_Next_Reading_Candidates]]
- [[Juarez_Republican_Source_Gap_Analysis]]
- [[Hamnett_Juarez_Source_Trail_Index]]
- [[SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO]]
- [[SRC_UNSET_001]]

既存カードの実在確認概要:

| Card Type | Existing IDs / Files Confirmed | Use in This CDL |
|---|---|---|
| Capture | existing spans `CAP_MEXEMP_0001-0043`, `0045-0051`, `0053-0095`, `0097-0107`; 104 files | existing CAP only; missing CAPs are manual review |
| Fact | minimum `FACT_MEXEMP_0001`, maximum `FACT_MEXEMP_2560`; 2040 files with known gaps | verified continuous ranges only |
| Timeline | minimum `TIME_MEXEMP_0001`, maximum `TIME_MEXEMP_0422`; 323 files with known gaps | verified continuous ranges only |
| Person | `PER-MAXIMILIAN`, `PER-CARLOTA`, `PER-BENITO-JUAREZ`, `PER-NAPOLEON-III`, `PER-FRANZ-JOSEPH` | existing Person cards only |
| Event | `EVT-FRENCH-INTERVENTION-IN-MEXICO`, `EVT-SECOND-MEXICAN-EMPIRE` | existing Event cards only |
| Place | `PLC-MIRAMAR`, `PLC-QUERETARO` | existing Place cards only |
| Org | `ORG-HABSBURG`, `ORG-MEXICAN-CONSERVATIVES`, `ORG-MEXICAN-REPUBLICANS`, `ORG-CATHOLIC-CHURCH` | existing Org cards only |
| Theme | `THM-FOREIGN-INTERVENTION`, `THM-LEGITIMACY`, `THM-LIBERAL-REFORM` | existing Theme cards only |
| Source | `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`, `SRC_UNSET_001` | existing Source notes only |
| Source Trail Docs | `NSI_SHAWCROSS_0001-0048`, `SRM_SHAWCROSS_0001-0048`, `NRC_SHAWCROSS_0001-0048`, `RSG_MEXEMP_0001-0022`, `HJI_MEXEMP_0001-0025` | source-discovery and verification only |

## 4. Source and Bias Caveats

- Shawcross由来DBは Maximilian / Carlota / Habsburg / French / loyal witness 側が厚い。章設計では、Juarez本人、共和派政府、共和派軍、裁判法理、自由主義改革、戦後記憶化を意識的に補う。
- Basch / Blasio / Felix Salm-Salm / Agnes Salm-Salm は場面価値が高いが、回想録・証言として `verification_needed` を付ける。
- Mexican press は public opinion / propaganda / rumor source として扱い、事実認定の単独根拠にしない。
- Hamnettは本文証拠ではなく、BJDOCS / APBJPS / AGN / AGEO / FJ などへの出典探索ルートとして扱う。
- Juarezを単純な処刑者、Maximilianを単純な殉教者、Carlotaを悲劇的ヒロインだけに固定しない。

## 5. Chapter / Part Candidate Overview

| Part | Design Focus | Primary CDL |
|---|---|---|
| Part I | 帝国計画、欧州側構想、フランス介入、皇冠受諾 | `CDL_MEXEMP_0002-0004` |
| Part II | 到着、宮廷形成、帝国成立の矛盾 | `CDL_MEXEMP_0005-0006` |
| Part III | Liberal Empire、現地社会との距離、政策理想 | `CDL_MEXEMP_0006-0007` |
| Part IV | 米国圧力、国境、Black Decree、軍事的崩壊 | `CDL_MEXEMP_0008` |
| Part V | 撤兵決定、Carlota渡欧、退位危機、宮廷の亀裂 | `CDL_MEXEMP_0009-0010` |
| Part VI | Querétaro包囲、捕縛、軍法会議、助命交渉 | `CDL_MEXEMP_0011-0012` |
| Part VII | 処刑、証言検証、Carlota後年、記憶化 | `CDL_MEXEMP_0001`, `CDL_MEXEMP_0013-0015` |
| Cross-cutting | 共和派バランス、Juárez側出典探索 | `CDL_MEXEMP_0016` |

## 6. CDL Index Table

| CDL ID | Part | Chapter Candidate | Chronology | Narrative Function | Viewpoint Candidates | Related Timeline | Related Fact | Related Capture | Related Entity Cards | Related Source Docs | Evidence Strength | Republican Balance Needed | Maximilian-centered Risk | Verification Needed | Scene Potential | Manual Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CDL_MEXEMP_0001 | Part VII / Prologue option | Querétaro処刑前の倒叙導入 | 1867春-1867-06 | 導入 | Maximilian; 共和派関係者; 市民・噂 | `TIME_MEXEMP_0001-0002` | `FACT_MEXEMP_0001-0006` | `CAP_MEXEMP_0001` | `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`; `PLC-QUERETARO`; `EVT-SECOND-MEXICAN-EMPIRE` | `SRC_UNSET_001`; RSG/HJI trial routes | mixed | yes | high | yes | high | yes |
| CDL_MEXEMP_0002 | Part I | 欧州側の帝国計画と大公夫妻 | 1850s-1861頃 | 導入 | Maximilian; Carlota; Napoleon III; Habsburg | `TIME_MEXEMP_0003-0049` | `FACT_MEXEMP_0007-0260` | `CAP_MEXEMP_0002-0012` | `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`; `ORG-HABSBURG`; `THM-LEGITIMACY` | `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`; NSI/SRM/NRC Habsburg routes | moderate | yes | high | yes | medium | yes |
| CDL_MEXEMP_0003 | Part I | フランス介入とJuárez政府の継続抵抗 | 1861-1863頃 | 対立拡大 | Juárez; フランス軍・外交官; Mexican conservatives | `TIME_MEXEMP_0050-0054`; `TIME_MEXEMP_0064-0094` | `FACT_MEXEMP_0261-0302`; `FACT_MEXEMP_0331-0421`; `FACT_MEXEMP_0446-0567` | `CAP_MEXEMP_0013-0023` | `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `ORG-MEXICAN-REPUBLICANS` | NSI/SRM/NRC French/FO/U.S. routes; RSG/HJI republican routes | mixed | yes | medium | yes | high | yes |
| CDL_MEXEMP_0004 | Part I / II | Mexican Crown と Miramarの受諾条件 | 1863-1864 | 転換 | Maximilian; Carlota; Mexican conservatives; French diplomacy | `TIME_MEXEMP_0095-0129`; `TIME_MEXEMP_0136-0141` | `FACT_MEXEMP_0568-0786`; `FACT_MEXEMP_0811-0834` | `CAP_MEXEMP_0024-0034` | `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`; `PLC-MIRAMAR`; `ORG-MEXICAN-CONSERVATIVES`; `THM-LEGITIMACY` | NSI/SRM/NRC HHStA, Gutiérrez de Estrada, Ratz routes | moderate | yes | high | yes | high | yes |
| CDL_MEXEMP_0005 | Part II | 到着、宮廷形成、帝国初期統治 | 1864 | 導入 | Maximilian; Carlota; 宮廷関係者; 市民・新聞・噂 | `TIME_MEXEMP_0142-0168`; `TIME_MEXEMP_0172-0173` | `FACT_MEXEMP_0835-1087`; `FACT_MEXEMP_1119-1136` | `CAP_MEXEMP_0035-0043`; `CAP_MEXEMP_0045` | `PER-MAXIMILIAN`; `PER-CARLOTA`; `EVT-SECOND-MEXICAN-EMPIRE`; `ORG-MEXICAN-CONSERVATIVES`; `THM-LEGITIMACY` | NSI/SRM/NRC correspondence and press routes | moderate | yes | high | yes | high | yes |
| CDL_MEXEMP_0006 | Part II / III | Liberal Empire、教会政策、Megliaとの衝突 | 1864-1865 | 対立拡大 | Maximilian; Carlota; Juárez; Catholic Church; Papal nuncio | `TIME_MEXEMP_0174-0178`; `TIME_MEXEMP_0184-0189`; `TIME_MEXEMP_0194-0204` | `FACT_MEXEMP_1137-1166`; `FACT_MEXEMP_1262-1306`; `FACT_MEXEMP_1327-1403` | `CAP_MEXEMP_0046-0051`; `CAP_MEXEMP_0053-0057` | `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`; `ORG-CATHOLIC-CHURCH`; `THM-LIBERAL-REFORM` | NSI/SRM/NRC `0030-0033`; RSG `0020`; HJI `0014` | mixed | yes | medium | yes | high | yes |
| CDL_MEXEMP_0007 | Part III | 現地社会、先住民政策、文化的帝国像 | 1864-1865 | 対立拡大 | Maximilian; Carlota; 市民・新聞・噂; other | `TIME_MEXEMP_0142-0154`; `TIME_MEXEMP_0200`; `TIME_MEXEMP_0228` | `FACT_MEXEMP_0867`; `FACT_MEXEMP_0869-0870`; `FACT_MEXEMP_0883`; `FACT_MEXEMP_0892`; `FACT_MEXEMP_1367-1370`; `FACT_MEXEMP_1392-1393`; `FACT_MEXEMP_1531-1534` | `CAP_MEXEMP_0035-0038`; `CAP_MEXEMP_0054-0057`; `CAP_MEXEMP_0064-0065` | `PER-MAXIMILIAN`; `PER-CARLOTA`; `THM-LEGITIMACY`; `THM-LIBERAL-REFORM` | NSI/SRM/NRC press and correspondence routes; RSG/HJI press/legal routes | mixed | yes | medium | yes | medium | yes |
| CDL_MEXEMP_0008 | Part IV | 米国圧力、国境、Black Decree | 1864-1866 | 対立拡大 | Juárez; 共和派関係者; U.S. officials; French army | `TIME_MEXEMP_0172-0173`; `TIME_MEXEMP_0194-0204`; `TIME_MEXEMP_0228-0237`; `TIME_MEXEMP_0259-0268`; `TIME_MEXEMP_0273-0291`; `TIME_MEXEMP_0298-0301` | `FACT_MEXEMP_1127-1131`; `FACT_MEXEMP_1327-1370`; `FACT_MEXEMP_1546-1555`; `FACT_MEXEMP_1732-1775`; `FACT_MEXEMP_1808-1880`; `FACT_MEXEMP_1909-1936` | `CAP_MEXEMP_0045`; `CAP_MEXEMP_0053-0057`; `CAP_MEXEMP_0065-0066`; `CAP_MEXEMP_0072-0079` | `PER-BENITO-JUAREZ`; `ORG-MEXICAN-REPUBLICANS`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `THM-FOREIGN-INTERVENTION` | NSI/SRM/NRC U.S. docs and press; RSG `0008`, `0010`, `0012`; HJI `0010`, `0013`, `0015`, `0024` | mixed | yes | medium | yes | high | yes |
| CDL_MEXEMP_0009 | Part V | Napoleon III撤兵決定とCarlota渡欧 | 1866 | 破局準備 | Carlota; Napoleon III; French diplomacy; Maximilian | `TIME_MEXEMP_0205-0208`; `TIME_MEXEMP_0215-0250`; `TIME_MEXEMP_0256-0258` | `FACT_MEXEMP_1404-1413`; `FACT_MEXEMP_1428-1673`; `FACT_MEXEMP_1707-1728` | `CAP_MEXEMP_0058-0071` | `PER-CARLOTA`; `PER-MAXIMILIAN`; `PER-NAPOLEON-III`; `ORG-HABSBURG`; `THM-FOREIGN-INTERVENTION` | NSI/SRM/NRC AAE, 400AP, FO, Ratz/Foussemagne routes | mixed | yes | high | yes | high | yes |
| CDL_MEXEMP_0010 | Part V | Cuernavaca / El Olindo と退位危機 | 1865-1866 | 破局準備 | Maximilian; Carlota; 宮廷関係者; French officials | `TIME_MEXEMP_0215-0250`; `TIME_MEXEMP_0259-0268`; `TIME_MEXEMP_0273-0291`; `TIME_MEXEMP_0298-0301` | `FACT_MEXEMP_1437-1475`; `FACT_MEXEMP_1729-1775`; `FACT_MEXEMP_1808-1880`; `FACT_MEXEMP_1909-1936` | `CAP_MEXEMP_0060-0069`; `CAP_MEXEMP_0072-0079` | `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`; `EVT-SECOND-MEXICAN-EMPIRE`; `THM-LEGITIMACY` | NSI/SRM/NRC Blasio, Ratz, FO, AAE routes | mixed | yes | high | yes | high | yes |
| CDL_MEXEMP_0011 | Part VI | Querétaro包囲と共和派軍の前進 | 1867前半 | 包囲 | Maximilian; 共和派関係者; Miramón; Mejía; Márquez; Escobedo | `TIME_MEXEMP_0323-0375` | `FACT_MEXEMP_2029-2365` | `CAP_MEXEMP_0084-0095` | `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`; `PLC-QUERETARO`; `ORG-MEXICAN-REPUBLICANS`; `EVT-FRENCH-INTERVENTION-IN-MEXICO` | NSI/SRM/NRC military memoir and Castelnau routes; RSG `0008-0009`; HJI `0010`, `0016`, `0023` | mixed | yes | high | yes | high | yes |
| CDL_MEXEMP_0012 | Part VI | 捕縛、軍法会議、助命交渉 | 1867-05-1867-06 | 裁判 | Juárez; Maximilian; 共和派関係者; Salm-Salm; French diplomats | `TIME_MEXEMP_0379-0386` | `FACT_MEXEMP_2390-2438`; `FACT_MEXEMP_2514` | `CAP_MEXEMP_0097-0102` | `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`; `PLC-QUERETARO`; `ORG-MEXICAN-REPUBLICANS`; `THM-LEGITIMACY` | NSI/SRM/NRC `0037-0040`, `0045-0046`; RSG `0009`, `0021-0022`; HJI `0011`, `0017`, `0023` | mixed | yes | high | yes | high | yes |
| CDL_MEXEMP_0013 | Part VII | 処刑場面と三者の最終像 | 1867-06 | 処刑 | Maximilian; 共和派関係者; 市民・新聞・噂; witness cluster | `TIME_MEXEMP_0001-0002`; `TIME_MEXEMP_0379-0386` | `FACT_MEXEMP_0001-0006`; `FACT_MEXEMP_2390-2438`; `FACT_MEXEMP_2514` | `CAP_MEXEMP_0001`; `CAP_MEXEMP_0097-0102` | `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`; `PLC-QUERETARO`; `THM-LEGITIMACY` | `SRC_UNSET_001`; NSI/SRM/NRC witness cluster; RSG/HJI trial and execution routes | mixed | yes | high | yes | high | yes |
| CDL_MEXEMP_0014 | Part VII | 遺体返還、Carlota後年、記憶化 | 1867後-20世紀初頭 | 記憶化 | Carlota; Habsburg; French/European memory; Mexican memory | `TIME_MEXEMP_0414-0422` | `FACT_MEXEMP_2515-2560` | `CAP_MEXEMP_0103-0106` | `PER-CARLOTA`; `PER-MAXIMILIAN`; `PER-FRANZ-JOSEPH`; `ORG-HABSBURG`; `THM-LEGITIMACY` | NSI/SRM/NRC `0047-0048`; RSG/HJI memory routes | mixed | yes | high | yes | medium | yes |
| CDL_MEXEMP_0015 | Part VI / VII | Basch / Blasio / Salm-Salm証言の制御 | 1866-1867; later memoir | 裁判 | 宮廷関係者; witness cluster; Juárez; Maximilian | `TIME_MEXEMP_0379-0386`; `TIME_MEXEMP_0414-0422` | `FACT_MEXEMP_2390-2438`; `FACT_MEXEMP_2514-2560` | `CAP_MEXEMP_0097-0104` | `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`; `PLC-QUERETARO` | NSI/SRM/NRC `0037-0040`; RSG `0021`; HJI `0023` | weak | yes | high | yes | high | yes |
| CDL_MEXEMP_0016 | Cross-cutting | Juárez / 共和派側補強設計 | 1857-1867 and postwar | other | Juárez; 共和派関係者; liberal press; U.S. diplomacy | 要確認 | 要確認 | existing Shawcross CAP ranges as context only | `PER-BENITO-JUAREZ`; `ORG-MEXICAN-REPUBLICANS`; `THM-LIBERAL-REFORM`; `EVT-FRENCH-INTERVENTION-IN-MEXICO` | RSG `0001-0022`; HJI `0001-0025`; NSI/SRM/NRC republican bridges | manual_review_needed | yes | medium | yes | medium | yes |

## 7. Part-by-Part DB Linkage Notes

### CDL_MEXEMP_0001 - Querétaro処刑前の倒叙導入

- act_or_part_candidate: Part VII / Prologue option
- chapter_candidate: Querétaro処刑前の倒叙導入
- chronological_range: 1867春-1867年6月
- core_historical_question: 三人の処刑待機を、Maximilian殉教譚だけでなく保守派敗北、共和派法理、外国干渉の帰結としてどう置くか。
- narrative_function: 導入
- viewpoint_candidates: Maximilian; 共和派関係者; 市民・新聞・噂の視点
- related_timeline_cards: `TIME_MEXEMP_0001-0002`
- related_fact_cards: `FACT_MEXEMP_0001-0006`
- related_capture_cards: `CAP_MEXEMP_0001`
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_UNSET_001`
- related_NSI: `NSI_SHAWCROSS_0037-0040`
- related_SRM: `SRM_SHAWCROSS_0037-0040`
- related_NRC: `NRC_SHAWCROSS_0037-0040`
- related_RSG: `RSG_MEXEMP_0009`; `RSG_MEXEMP_0021`
- related_HJI: `HJI_MEXEMP_0011`; `HJI_MEXEMP_0017`; `HJI_MEXEMP_0023`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: 冒頭で使いやすいが、処刑前の会話・身ぶり・表情は証言由来になりやすい。処刑場面は後半へ回し、冒頭では問いだけを提示する構成も可。
- factual_risk_notes: `SRC_UNSET_001` はPrologue source_id未統合。裁判法、収監場所、処刑日程はRSG/HJI側で再確認する。
- additional_source_needed: 裁判・軍法会議記録、BJDOCS、liberal press、Basch / Blasio / Salm-Salm照合。
- manual_review_needed: yes; exact Kindle location and source_id harmonization.

### CDL_MEXEMP_0002 - 欧州側の帝国計画と大公夫妻

- act_or_part_candidate: Part I
- chapter_candidate: 欧州側の帝国計画と大公夫妻
- chronological_range: 1850s-1861頃
- core_historical_question: MaximilianとCarlotaの自己像、Habsburg家の位置、Napoleon IIIの構想は、メキシコ国内政治とどうずれるか。
- narrative_function: 導入
- viewpoint_candidates: Maximilian; Carlota; Napoleon III; Habsburg
- related_timeline_cards: `TIME_MEXEMP_0003-0049`
- related_fact_cards: `FACT_MEXEMP_0007-0260`
- related_capture_cards: `CAP_MEXEMP_0002-0012`
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`; `PER-FRANZ-JOSEPH`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-MIRAMAR`
- related_org_cards: `ORG-HABSBURG`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0004`; `0013`; `0015-0020`
- related_SRM: `SRM_SHAWCROSS_0004`; `0013`; `0015-0020`
- related_NRC: `NRC_SHAWCROSS_0004`; `0013`; `0015-0020`
- related_RSG: `RSG_MEXEMP_0001`; `RSG_MEXEMP_0012`
- related_HJI: `HJI_MEXEMP_0001`; `HJI_MEXEMP_0013`
- evidence_strength: moderate
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: medium
- novel_use_notes: 欧州宮廷・家族・理想主義の導入に使える。ここだけで読者に同情の重心を置きすぎない。
- factual_risk_notes: Habsburg・Maximilian自己表象が強い。Juárez側の存在はまだ薄い。
- additional_source_needed: HHStA、Ratz、Foussemagne、Weckmann、BJDOCS側の同時期反応。
- manual_review_needed: yes; correspondence original location and editorial mediation.

### CDL_MEXEMP_0003 - フランス介入とJuárez政府の継続抵抗

- act_or_part_candidate: Part I
- chapter_candidate: フランス介入とJuárez政府の継続抵抗
- chronological_range: 1861-1863頃
- core_historical_question: フランス介入は、債務・外交・帝国構想・共和派抵抗のどの結節点で戦争化したか。
- narrative_function: 対立拡大
- viewpoint_candidates: Juárez; 共和派関係者; フランス軍・外交官; Mexican conservatives
- related_timeline_cards: `TIME_MEXEMP_0050-0054`; `TIME_MEXEMP_0064-0094`
- related_fact_cards: `FACT_MEXEMP_0261-0302`; `FACT_MEXEMP_0331-0421`; `FACT_MEXEMP_0446-0567`
- related_capture_cards: `CAP_MEXEMP_0013-0023`
- related_person_cards: `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`; `PER-MAXIMILIAN`
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO` as later destination only
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0002`; `0003`; `0008`; `0011`; `0021`; `0025-0026`
- related_SRM: `SRM_SHAWCROSS_0002`; `0003`; `0008`; `0011`; `0021`; `0025-0026`
- related_NRC: `NRC_SHAWCROSS_0002`; `0003`; `0008`; `0011`; `0021`; `0025-0026`
- related_RSG: `RSG_MEXEMP_0007`; `RSG_MEXEMP_0012`; `RSG_MEXEMP_0018-0019`
- related_HJI: `HJI_MEXEMP_0009`; `HJI_MEXEMP_0013`; `HJI_MEXEMP_0021-0022`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: medium
- verification_needed: yes
- scene_potential: high
- novel_use_notes: 戦争開始、La Soledad、Puebla、外交の不信、Juárez側移動政府の持続を並行させる章候補。
- factual_risk_notes: `FACT_MEXEMP_0303-0330`, `0422-0445`, `TIME_MEXEMP_0055-0063` は欠番。介入側資料だけでJuárezの意図を決めない。
- additional_source_needed: FO / AAE、U.S. official documents、BJDOCS、共和派政府文書。
- manual_review_needed: yes; missing range and Mexican-side government records.

### CDL_MEXEMP_0004 - Mexican Crown と Miramarの受諾条件

- act_or_part_candidate: Part I / II
- chapter_candidate: Mexican Crown と Miramarの受諾条件
- chronological_range: 1863-1864
- core_historical_question: 「メキシコ皇冠」の正統性は、誰の同意・保証・幻想で支えられたのか。
- narrative_function: 転換
- viewpoint_candidates: Maximilian; Carlota; メキシコ保守派; フランス外交官
- related_timeline_cards: `TIME_MEXEMP_0095-0129`; `TIME_MEXEMP_0136-0141`
- related_fact_cards: `FACT_MEXEMP_0568-0786`; `FACT_MEXEMP_0811-0834`
- related_capture_cards: `CAP_MEXEMP_0024-0034`
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-MIRAMAR`
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0004`; `0006`; `0016`; `0020`
- related_SRM: `SRM_SHAWCROSS_0004`; `0006`; `0016`; `0020`
- related_NRC: `NRC_SHAWCROSS_0004`; `0006`; `0016`; `0020`
- related_RSG: `RSG_MEXEMP_0014-0016`
- related_HJI: `HJI_MEXEMP_0019`
- evidence_strength: moderate
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: Miramarの儀礼、条件交渉、家族・国家・野心の交差を場面化できる。
- factual_risk_notes: Mexican consent と plebiscite 的演出は保守派・フランス・Habsburg側資料に寄りやすい。
- additional_source_needed: Gutiérrez de Estrada、Mexican conservative sources、Juárez側反応、Vigilとの対比。
- manual_review_needed: yes; `FACT_MEXEMP_0787-0810`, `TIME_MEXEMP_0130-0135` 欠番。

### CDL_MEXEMP_0005 - 到着、宮廷形成、帝国初期統治

- act_or_part_candidate: Part II
- chapter_candidate: 到着、宮廷形成、帝国初期統治
- chronological_range: 1864
- core_historical_question: 到着と宮廷形成は、統治の実質なのか、正統性演出なのか。
- narrative_function: 導入
- viewpoint_candidates: Maximilian; Carlota; 宮廷関係者; 市民・新聞・噂の視点
- related_timeline_cards: `TIME_MEXEMP_0142-0168`; `TIME_MEXEMP_0172-0173`
- related_fact_cards: `FACT_MEXEMP_0835-1087`; `FACT_MEXEMP_1119-1136`
- related_capture_cards: `CAP_MEXEMP_0035-0043`; `CAP_MEXEMP_0045`
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-MIRAMAR`; `PLC-QUERETARO` as endpoint contrast
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0013`; `0016-0019`; `0023`
- related_SRM: `SRM_SHAWCROSS_0013`; `0016-0019`; `0023`
- related_NRC: `NRC_SHAWCROSS_0013`; `0016-0019`; `0023`
- related_RSG: `RSG_MEXEMP_0010-0011`
- related_HJI: `HJI_MEXEMP_0012`
- evidence_strength: moderate
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: Veracruz到着、Mexico City、Chapultepec、宮廷儀礼、新聞・噂を情景化できる。
- factual_risk_notes: Labastida, Bazaineなどの人物カードが未作成。噂や歓迎描写を国民感情に拡張しない。
- additional_source_needed: Mexican press issue/date、liberal press、共和派政府文書。
- manual_review_needed: yes; `CAP_MEXEMP_0044`, `FACT_MEXEMP_1088-1118`, `TIME_MEXEMP_0169-0171` 欠番。

### CDL_MEXEMP_0006 - Liberal Empire、教会政策、Megliaとの衝突

- act_or_part_candidate: Part II / III
- chapter_candidate: Liberal Empire、教会政策、Megliaとの衝突
- chronological_range: 1864-1865
- core_historical_question: Maximilianの自由主義的帝国は、教会・保守派・共和派のどの線で矛盾を露呈したか。
- narrative_function: 対立拡大
- viewpoint_candidates: Maximilian; Carlota; Juárez; Catholic Church; Papal nuncio Meglia
- related_timeline_cards: `TIME_MEXEMP_0174-0178`; `TIME_MEXEMP_0184-0189`; `TIME_MEXEMP_0194-0204`
- related_fact_cards: `FACT_MEXEMP_1137-1166`; `FACT_MEXEMP_1262-1306`; `FACT_MEXEMP_1327-1403`
- related_capture_cards: `CAP_MEXEMP_0046-0051`; `CAP_MEXEMP_0053-0057`
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: none existing specific card beyond general Mexico; use `PLC-MIRAMAR` only for earlier contrast
- related_org_cards: `ORG-CATHOLIC-CHURCH`; `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LIBERAL-REFORM`; `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0030-0033`
- related_SRM: `SRM_SHAWCROSS_0030-0033`
- related_NRC: `NRC_SHAWCROSS_0030-0033`
- related_RSG: `RSG_MEXEMP_0020`
- related_HJI: `HJI_MEXEMP_0014`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: medium
- verification_needed: yes
- scene_potential: high
- novel_use_notes: Meglia、Syllabus of Errors、1864年12月27日布告、教会政策を、理念と政治実務の衝突として場面化できる。
- factual_risk_notes: 教会政策をMaximilianの人格問題だけにしない。Reformaの法制度と共和派政策との接続が必要。
- additional_source_needed: Reforma law records、BJDOCS、AGN、AGEO、FJ、Church-side documents。
- manual_review_needed: yes; `CAP_MEXEMP_0052`, `FACT_MEXEMP_1167-1261`, `1307-1326`, `TIME_MEXEMP_0179-0183`, `0190-0193` 欠番。

### CDL_MEXEMP_0007 - 現地社会、先住民政策、文化的帝国像

- act_or_part_candidate: Part III
- chapter_candidate: 現地社会、先住民政策、文化的帝国像
- chronological_range: 1864-1865
- core_historical_question: Maximilianの現地社会への接近は政策実体だったのか、象徴政治だったのか。
- narrative_function: 対立拡大
- viewpoint_candidates: Maximilian; Carlota; 市民・新聞・噂の視点; other
- related_timeline_cards: `TIME_MEXEMP_0142-0154`; `TIME_MEXEMP_0200`; `TIME_MEXEMP_0228`
- related_fact_cards: `FACT_MEXEMP_0867`; `FACT_MEXEMP_0869-0870`; `FACT_MEXEMP_0883`; `FACT_MEXEMP_0892`; `FACT_MEXEMP_1367-1370`; `FACT_MEXEMP_1392-1393`; `FACT_MEXEMP_1531-1534`
- related_capture_cards: `CAP_MEXEMP_0035-0038`; `CAP_MEXEMP_0054-0057`; `CAP_MEXEMP_0064-0065`
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: none existing specific card
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`; `THM-LIBERAL-REFORM`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0023`; `0033`
- related_SRM: `SRM_SHAWCROSS_0023`; `0033`
- related_NRC: `NRC_SHAWCROSS_0023`; `0033`
- related_RSG: `RSG_MEXEMP_0010-0011`; `RSG_MEXEMP_0017`
- related_HJI: `HJI_MEXEMP_0012`; `HJI_MEXEMP_0020`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: medium
- verification_needed: yes
- scene_potential: medium
- novel_use_notes: Nahuatl布告、先住民政策、儀礼、アカデミー的文化事業、paper empire的な空疎さを扱う補助章候補。
- factual_risk_notes: Shawcross側の観察だけで先住民社会の反応を確定しない。象徴描写と政策効果を分ける。
- additional_source_needed: Mexican documentary collections、local/indigenous-side evidence、press issue/date。
- manual_review_needed: yes; individual policy documents and local reception.

### CDL_MEXEMP_0008 - 米国圧力、国境、Black Decree

- act_or_part_candidate: Part IV
- chapter_candidate: 米国圧力、国境、Black Decree
- chronological_range: 1864-1866
- core_historical_question: 米国の非承認・国境支援・武器流入は、帝国の軍事的崩壊とBlack Decreeにどう接続するか。
- narrative_function: 対立拡大
- viewpoint_candidates: Juárez; 共和派関係者; U.S. officials; フランス軍・外交官
- related_timeline_cards: `TIME_MEXEMP_0172-0173`; `TIME_MEXEMP_0194-0204`; `TIME_MEXEMP_0228-0237`; `TIME_MEXEMP_0259-0268`; `TIME_MEXEMP_0273-0291`; `TIME_MEXEMP_0298-0301`
- related_fact_cards: `FACT_MEXEMP_1127-1131`; `FACT_MEXEMP_1327-1370`; `FACT_MEXEMP_1546-1555`; `FACT_MEXEMP_1732-1775`; `FACT_MEXEMP_1808-1880`; `FACT_MEXEMP_1909-1936`
- related_capture_cards: `CAP_MEXEMP_0045`; `CAP_MEXEMP_0053-0057`; `CAP_MEXEMP_0065-0066`; `CAP_MEXEMP_0072-0079`
- related_person_cards: `PER-BENITO-JUAREZ`; `PER-MAXIMILIAN`; `PER-NAPOLEON-III`
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO` as later endpoint
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LIBERAL-REFORM`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0011`; `0023`; `0026`; `0035`
- related_SRM: `SRM_SHAWCROSS_0011`; `0023`; `0026`; `0035`
- related_NRC: `NRC_SHAWCROSS_0011`; `0023`; `0026`; `0035`
- related_RSG: `RSG_MEXEMP_0008`; `0010`; `0012`; `0020`
- related_HJI: `HJI_MEXEMP_0010`; `0013`; `0015`; `0024`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: medium
- verification_needed: yes
- scene_potential: high
- novel_use_notes: Brownsville / Matamoros、武器流入、国境の酒場・亡命者・軍事報告、Black Decreeの法的・感情的衝撃を章候補化できる。
- factual_risk_notes: U.S.資料は自己正当化を含む。Black DecreeはMaximilian悲劇かJuárez報復の単純図式にしない。
- additional_source_needed: U.S. official documents、BJDOCS、republican military reports、liberal press。
- manual_review_needed: yes; Black Decree original text and republican response route.

### CDL_MEXEMP_0009 - Napoleon III撤兵決定とCarlota渡欧

- act_or_part_candidate: Part V
- chapter_candidate: Napoleon III撤兵決定とCarlota渡欧
- chronological_range: 1866
- core_historical_question: Carlotaの渡欧は政治交渉だったのか、崩壊する同盟への最後の訴えだったのか。
- narrative_function: 破局準備
- viewpoint_candidates: Carlota; Napoleon III; フランス軍・外交官; Maximilian
- related_timeline_cards: `TIME_MEXEMP_0205-0208`; `TIME_MEXEMP_0215-0250`; `TIME_MEXEMP_0256-0258`
- related_fact_cards: `FACT_MEXEMP_1404-1413`; `FACT_MEXEMP_1428-1673`; `FACT_MEXEMP_1707-1728`
- related_capture_cards: `CAP_MEXEMP_0058-0071`
- related_person_cards: `PER-CARLOTA`; `PER-MAXIMILIAN`; `PER-NAPOLEON-III`
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: none existing specific Paris/Rome cards
- related_org_cards: `ORG-HABSBURG`; `ORG-CATHOLIC-CHURCH`
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0001-0004`; `0031`; `0041-0045`
- related_SRM: `SRM_SHAWCROSS_0001-0004`; `0031`; `0041-0045`
- related_NRC: `NRC_SHAWCROSS_0001-0004`; `0031`; `0041-0045`
- related_RSG: `RSG_MEXEMP_0018-0019`
- related_HJI: `HJI_MEXEMP_0021-0022`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: Saint-Cloud、Grand Hotel、Rome/Vatican、Pius IXとの距離など場面性が強い。
- factual_risk_notes: Carlotaの心理を後年の悲劇へ直線化しない。外交文書と私信の差を分ける。
- additional_source_needed: AAE, 400AP, FO, Ratz, Foussemagne, Weckmann, Belgian-side material。
- manual_review_needed: yes; `FACT_MEXEMP_1414-1427`, `1674-1706`, `TIME_MEXEMP_0209-0214`, `0251-0255` 欠番。

### CDL_MEXEMP_0010 - Cuernavaca / El Olindo と退位危機

- act_or_part_candidate: Part V
- chapter_candidate: Cuernavaca / El Olindo と退位危機
- chronological_range: 1865-1866
- core_historical_question: 私的空間、噂、フランスの撤兵通告は、Maximilianの退位逡巡にどう作用したか。
- narrative_function: 破局準備
- viewpoint_candidates: Maximilian; Carlota; 宮廷関係者; フランス軍・外交官
- related_timeline_cards: `TIME_MEXEMP_0215-0250`; `TIME_MEXEMP_0259-0268`; `TIME_MEXEMP_0273-0291`; `TIME_MEXEMP_0298-0301`
- related_fact_cards: `FACT_MEXEMP_1437-1475`; `FACT_MEXEMP_1729-1775`; `FACT_MEXEMP_1808-1880`; `FACT_MEXEMP_1909-1936`
- related_capture_cards: `CAP_MEXEMP_0060-0069`; `CAP_MEXEMP_0072-0079`
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`
- related_place_cards: none existing Cuernavaca/El Olindo card
- related_org_cards: `ORG-HABSBURG`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0016`; `0037-0038`; `0041-0043`
- related_SRM: `SRM_SHAWCROSS_0016`; `0037-0038`; `0041-0043`
- related_NRC: `NRC_SHAWCROSS_0016`; `0037-0038`; `0041-0043`
- related_RSG: `RSG_MEXEMP_0008`; `0018`
- related_HJI: `HJI_MEXEMP_0010`; `0016`; `0021`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: Cuernavacaの親密な宮廷、El Olindoの噂、撤兵書簡到着を宮廷崩壊の転調として使える。
- factual_risk_notes: 性的噂や私生活描写はBlasio等の証言・噂の層を分ける。French officialsの不信と現実の統治能力を混同しない。
- additional_source_needed: Blasio bias profile, correspondence, AAE/FO, Mexican-side military records。
- manual_review_needed: yes; Abdication Crisis中盤のFACT/TIME欠番。

### CDL_MEXEMP_0011 - Querétaro包囲と共和派軍の前進

- act_or_part_candidate: Part VI
- chapter_candidate: Querétaro包囲と共和派軍の前進
- chronological_range: 1867前半
- core_historical_question: 包囲戦は帝政側の閉塞だけでなく、共和派軍の作戦・統制・内部問題としてどう見えるか。
- narrative_function: 包囲
- viewpoint_candidates: Maximilian; 共和派関係者; Miramón; Mejía; Márquez; Escobedo
- related_timeline_cards: `TIME_MEXEMP_0323-0375`
- related_fact_cards: `FACT_MEXEMP_2029-2365`
- related_capture_cards: `CAP_MEXEMP_0084-0095`
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0022`; `0037`; `0039`; `0041`
- related_SRM: `SRM_SHAWCROSS_0022`; `0037`; `0039`; `0041`
- related_NRC: `NRC_SHAWCROSS_0022`; `0037`; `0039`; `0041`
- related_RSG: `RSG_MEXEMP_0008-0009`; `RSG_MEXEMP_0011`
- related_HJI: `HJI_MEXEMP_0010`; `0016`; `0023`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: 包囲の物理的圧迫、Escobedo側の軍事報告、帝政側の疲労・疑心暗鬼を複眼化する。
- factual_risk_notes: 包囲戦をBasch/Salm-Salmの内側だけで構成しない。Republican military reportsが必要。
- additional_source_needed: republican military reports, trial records, Mexican press, French military memoir cluster comparison。
- manual_review_needed: yes; `CAP_MEXEMP_0096`, `FACT_MEXEMP_2366-2389`, `TIME_MEXEMP_0376-0378` 欠番。

### CDL_MEXEMP_0012 - 捕縛、軍法会議、助命交渉

- act_or_part_candidate: Part VI
- chapter_candidate: 捕縛、軍法会議、助命交渉
- chronological_range: 1867年5月-6月
- core_historical_question: Juárezの処刑判断は、戦時法理、国家正統性、国際圧力、復讐感情のどの組み合わせで説明できるか。
- narrative_function: 裁判
- viewpoint_candidates: Juárez; Maximilian; 共和派関係者; Salm-Salm; French diplomats
- related_timeline_cards: `TIME_MEXEMP_0379-0386`
- related_fact_cards: `FACT_MEXEMP_2390-2438`; `FACT_MEXEMP_2514`
- related_capture_cards: `CAP_MEXEMP_0097-0102`
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-LEGITIMACY`; `THM-LIBERAL-REFORM`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0037-0040`; `0045-0046`
- related_SRM: `SRM_SHAWCROSS_0037-0040`; `0045-0046`
- related_NRC: `NRC_SHAWCROSS_0037-0040`; `0045-0046`
- related_RSG: `RSG_MEXEMP_0009`; `0021-0022`
- related_HJI: `HJI_MEXEMP_0011`; `0017`; `0023`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: 軍法会議、書類、助命嘆願、外交電報を交互に置くと、感情劇だけでない裁判章にできる。
- factual_risk_notes: `FACT_MEXEMP_2439-2513`, `TIME_MEXEMP_0387-0413` は生成漏れ疑い。Agnes Salm-Salmの会話・身ぶりは証言単独で使わない。
- additional_source_needed: court-martial records, BJDOCS, APBJPS, FJ, AAE Forest correspondence, U.S. official documents。
- manual_review_needed: yes; late trial generation-gap ranges and Chynoweth identity.

### CDL_MEXEMP_0013 - 処刑場面と三者の最終像

- act_or_part_candidate: Part VII
- chapter_candidate: 処刑場面と三者の最終像
- chronological_range: 1867年6月
- core_historical_question: 処刑を、帝政側殉教譚、共和派法理、メキシコ内戦の終局、欧州側記憶のどれとして読ませるか。
- narrative_function: 処刑
- viewpoint_candidates: Maximilian; 共和派関係者; 市民・新聞・噂の視点; witness cluster
- related_timeline_cards: `TIME_MEXEMP_0001-0002`; `TIME_MEXEMP_0379-0386`
- related_fact_cards: `FACT_MEXEMP_0001-0006`; `FACT_MEXEMP_2390-2438`; `FACT_MEXEMP_2514`
- related_capture_cards: `CAP_MEXEMP_0001`; `CAP_MEXEMP_0097-0102`
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_UNSET_001`; `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0037-0040`; `0045-0048`
- related_SRM: `SRM_SHAWCROSS_0037-0040`; `0045-0048`
- related_NRC: `NRC_SHAWCROSS_0037-0040`; `0045-0048`
- related_RSG: `RSG_MEXEMP_0009`; `0010-0015`; `0021-0022`
- related_HJI: `HJI_MEXEMP_0011`; `0017-0019`; `0023`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: 最終場面は強いが、逐語の最後の言葉や情緒は証言・記憶化の層を明示してから扱う。
- factual_risk_notes: 処刑場面は後年の英雄化・殉教化・党派的記憶が入りやすい。
- additional_source_needed: trial/court-martial record, liberal press issue/date, Vigil/Zamacois/Arrangoiz比較。
- manual_review_needed: yes; execution-specific claims and witness divergences.

### CDL_MEXEMP_0014 - 遺体返還、Carlota後年、記憶化

- act_or_part_candidate: Part VII
- chapter_candidate: 遺体返還、Carlota後年、記憶化
- chronological_range: 1867後-20世紀初頭
- core_historical_question: 死後のMaximilianとCarlotaは、どの政治的記憶の中で再構成されたか。
- narrative_function: 記憶化
- viewpoint_candidates: Carlota; Habsburg; フランス軍・外交官; Mexican memory; European memory
- related_timeline_cards: `TIME_MEXEMP_0414-0422`
- related_fact_cards: `FACT_MEXEMP_2515-2560`
- related_capture_cards: `CAP_MEXEMP_0103-0106`
- related_person_cards: `PER-CARLOTA`; `PER-MAXIMILIAN`; `PER-FRANZ-JOSEPH`; `PER-NAPOLEON-III`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: none existing Belgium/France/Metz cards
- related_org_cards: `ORG-HABSBURG`
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0047-0048`; `0013`; `0038`
- related_SRM: `SRM_SHAWCROSS_0047-0048`; `0013`; `0038`
- related_NRC: `NRC_SHAWCROSS_0047-0048`; `0013`; `0038`
- related_RSG: `RSG_MEXEMP_0013-0016`
- related_HJI: `HJI_MEXEMP_0018-0019`; `0025`
- evidence_strength: mixed
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: medium
- novel_use_notes: 終幕候補。Carlotaの長い余生、Habsburg崩壊、Porfiriato、欧州側記憶とメキシコ側記憶の距離を示す。
- factual_risk_notes: Carlotaを悲劇的ヒロインだけに固定しない。自由派記憶と保守派・欧州記憶を分ける。
- additional_source_needed: Vigil, Zamacois, Arrangoiz, Romero de Terreros, French legislative material, Habsburg records。
- manual_review_needed: yes; `FACT_MEXEMP_2561-2608`, `TIME_MEXEMP_0423-0448` are not existing IDs.

### CDL_MEXEMP_0015 - Basch / Blasio / Salm-Salm証言の制御

- act_or_part_candidate: Part VI / VII
- chapter_candidate: Basch / Blasio / Salm-Salm証言の制御
- chronological_range: 1866-1867; later memoir
- core_historical_question: 忠誠証言は、どこまで事実認定に使え、どこから場面素材・記憶化資料に留めるべきか。
- narrative_function: 裁判
- viewpoint_candidates: 宮廷関係者; witness cluster; Juárez; Maximilian
- related_timeline_cards: `TIME_MEXEMP_0379-0386`; `TIME_MEXEMP_0414-0422`
- related_fact_cards: `FACT_MEXEMP_2390-2438`; `FACT_MEXEMP_2514-2560`
- related_capture_cards: `CAP_MEXEMP_0097-0104`
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-LEGITIMACY`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- related_NSI: `NSI_SHAWCROSS_0037-0040`
- related_SRM: `SRM_SHAWCROSS_0037-0040`
- related_NRC: `NRC_SHAWCROSS_0037-0040`
- related_RSG: `RSG_MEXEMP_0021`
- related_HJI: `HJI_MEXEMP_0023`
- evidence_strength: weak
- republican_balance_needed: yes
- maximilian_centered_risk: high
- verification_needed: yes
- scene_potential: high
- novel_use_notes: prison, mercy mission, escape plan, execution aftermathの場面素材。複数証言を並べて不一致を活かすこともできる。
- factual_risk_notes: 単一証言の台詞・動機・身ぶりは史実認定しない。Agnes Salm-Salmは言語障壁の注記あり。
- additional_source_needed: court-martial records, BJDOCS, liberal press, AAE/FO, Mexican-side confirmation。
- manual_review_needed: yes; witness cluster bias profile.

### CDL_MEXEMP_0016 - Juárez / 共和派側補強設計

- act_or_part_candidate: Cross-cutting
- chapter_candidate: Juárez / 共和派側補強設計
- chronological_range: 1857-1867 and postwar
- core_historical_question: 小説全体で共和派を、単なる外圧・処刑者・抽象的共和国ではなく、行政・軍事・法理・記憶を持つ主体としてどう配置するか。
- narrative_function: other
- viewpoint_candidates: Juárez; 共和派関係者; liberal press; U.S. diplomacy; 市民・新聞・噂の視点
- related_timeline_cards: 要確認; future use must select verified existing IDs only
- related_fact_cards: 要確認; future use must select verified existing IDs only
- related_capture_cards: existing Shawcross CAP ranges as context only; no new CAP
- related_person_cards: `PER-BENITO-JUAREZ`
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`
- related_place_cards: `PLC-QUERETARO`
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`
- related_theme_cards: `THM-LIBERAL-REFORM`; `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO` as imbalance source; Hamnett source trail is not a Source card here
- related_NSI: `NSI_SHAWCROSS_0024`; `0026`; `0033`; `0040`
- related_SRM: `SRM_SHAWCROSS_0024`; `0026`; `0033`; `0040`
- related_NRC: `NRC_SHAWCROSS_0024`; `0026`; `0033`; `0040`
- related_RSG: `RSG_MEXEMP_0001-0022`
- related_HJI: `HJI_MEXEMP_0001-0025`
- evidence_strength: manual_review_needed
- republican_balance_needed: yes
- maximilian_centered_risk: medium
- verification_needed: yes
- scene_potential: medium
- novel_use_notes: Juárez移動政府、共和派軍報告、裁判法理、自由主義改革、戦後記憶化を各Partへ差し込むための横断設計。
- factual_risk_notes: Hamnett本文を最終証拠にしない。BJDOCS / APBJPS / AGN / AGEO / FJ の文書単位確認が必要。
- additional_source_needed: BJDOCS, APBJPS, AGN, AGEO, FJ, trial records, republican military reports, liberal press issue/date table。
- manual_review_needed: yes; all HJI rows require document-level review before future Fact/Timeline use.

## 8. Character / Viewpoint Linkage

| Viewpoint | Existing Cards | Strong Use | Balance / Risk |
|---|---|---|---|
| Maximilian | `PER-MAXIMILIAN`; many Shawcross Fact/Timeline ranges | inner conflict, legitimacy, Liberal Empire, abdication, final months | high risk of martyr-centered narrative |
| Carlota | `PER-CARLOTA`; `CAP_MEXEMP_0058-0071`; `CAP_MEXEMP_0103-0106` | diplomacy, court politics, isolation, memory | avoid tragic heroine reduction |
| Juárez | `PER-BENITO-JUAREZ`; RSG/HJI source trails | legal decision, mobile government, republican continuity | direct source gap; do not infer inner life from enemy/witness accounts |
| 共和派関係者 | `ORG-MEXICAN-REPUBLICANS`; RSG/HJI military and trial routes | siege, military reports, court martial, press | currently under-carded; use source trails before scene claims |
| フランス軍・外交官 | `PER-NAPOLEON-III`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`; NSI/SRM/NRC AAE/400AP/FO | policy, withdrawal, blame, external pressure | official records are not neutral |
| メキシコ保守派 | `ORG-MEXICAN-CONSERVATIVES`; Gutiérrez, Zamacois, Arrangoiz routes | monarchy project, legitimacy claims, defeated memory | partisan self-defense |
| 宮廷関係者 | no individual cards for Basch/Blasio/Salm-Salm | high scene value for final months | memoir/testimony verification required |
| 市民・新聞・噂 | `THM-LEGITIMACY`; press source trails | atmosphere, rumor, propaganda, ceremony | press cannot certify facts alone |

## 9. Event / Place / Organization Linkage

- `EVT-FRENCH-INTERVENTION-IN-MEXICO`: `CDL_MEXEMP_0003`, `0008`, `0009`, `0011`.
- `EVT-SECOND-MEXICAN-EMPIRE`: `CDL_MEXEMP_0004-0015`.
- `PLC-MIRAMAR`: `CDL_MEXEMP_0002-0004`.
- `PLC-QUERETARO`: `CDL_MEXEMP_0001`, `0011-0015`.
- `ORG-HABSBURG`: `CDL_MEXEMP_0002`, `0004`, `0009`, `0014`.
- `ORG-MEXICAN-CONSERVATIVES`: `CDL_MEXEMP_0003-0005`, `0011`, `0013`.
- `ORG-MEXICAN-REPUBLICANS`: `CDL_MEXEMP_0003`, `0006`, `0008`, `0011-0016`.
- `ORG-CATHOLIC-CHURCH`: `CDL_MEXEMP_0006`, `0009`.

## 10. Theme Linkage

- `THM-FOREIGN-INTERVENTION`: Part I, Part IV, Part V, and diplomatic aftermath.
- `THM-LEGITIMACY`: Miramar, imperial arrival, court martial, execution, and memory.
- `THM-LIBERAL-REFORM`: Liberal Empire, church-state conflict, Black Decree response, Juárez/republican legal routes.

## 11. Source Trail Linkage: NSI / SRM / NRC / RSG / HJI

| Source Trail Cluster | IDs | CDL Use |
|---|---|---|
| French official / diplomatic | `NSI/SRM/NRC_SHAWCROSS_0001-0003`, `0031`, `0041-0045` | `CDL_MEXEMP_0003`, `0009-0012` |
| Habsburg / Maximilian-Carlota | `NSI/SRM/NRC_SHAWCROSS_0004`, `0013`, `0016-0020` | `CDL_MEXEMP_0002`, `0004`, `0009-0010`, `0014` |
| Mexican political voices | `NSI/SRM/NRC_SHAWCROSS_0006`, `0023-0029`, `0033` | `CDL_MEXEMP_0003-0008`, `0013-0016` |
| Witness cluster | `NSI/SRM/NRC_SHAWCROSS_0037-0040` | `CDL_MEXEMP_0011-0015` |
| Republican source gap | `RSG_MEXEMP_0001-0022` | especially `CDL_MEXEMP_0008`, `0011-0016` |
| Hamnett Juárez source trail | `HJI_MEXEMP_0001-0025` | especially `CDL_MEXEMP_0008`, `0011-0016` |

## 12. Scene Potential Notes

High scene potential:

- `CDL_MEXEMP_0001`: inverted Querétaro opening.
- `CDL_MEXEMP_0003`: French intervention, La Soledad/Puebla, Juárez resistance.
- `CDL_MEXEMP_0004`: Miramar negotiations and crown acceptance.
- `CDL_MEXEMP_0005`: arrival, court formation, public ceremony.
- `CDL_MEXEMP_0006`: church-state confrontation.
- `CDL_MEXEMP_0008`: Brownsville / Matamoros and Black Decree.
- `CDL_MEXEMP_0009`: Carlota in Europe, Saint-Cloud/Rome.
- `CDL_MEXEMP_0010`: Cuernavaca / El Olindo and withdrawal letter.
- `CDL_MEXEMP_0011`: Querétaro siege.
- `CDL_MEXEMP_0012`: court martial and mercy appeals.
- `CDL_MEXEMP_0013`: execution.
- `CDL_MEXEMP_0015`: witness-cluster comparison.

Medium scene potential:

- `CDL_MEXEMP_0002`: European planning and dynastic framing.
- `CDL_MEXEMP_0007`: policy symbolism and local reception.
- `CDL_MEXEMP_0014`: epilogue and memory.
- `CDL_MEXEMP_0016`: republican balance design.

## 13. Factual Risk and Verification Notes

- Known missing CAPs: `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096`.
- Known non-existing post-max Fact IDs: `FACT_MEXEMP_2561-2608`.
- Known non-existing post-max Timeline IDs: `TIME_MEXEMP_0423-0448`.
- Trial and epilogue generation-gap dependencies: `FACT_MEXEMP_2439-2513`, `TIME_MEXEMP_0387-0413`, `TIME_MEXEMP_0413`.
- Prologue source issue: `SRC_UNSET_001` remains separate from `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- Witness risk: Basch / Blasio / Felix Salm-Salm / Agnes Salm-Salm are scene-rich but require court-martial records, Juárez-side documents, official diplomatic records, and press comparison.
- Republican gap: RSG/HJI must be resolved before future Fact/Timeline creation about Juárez decision-making, republican military reporting, court martial, Liberal Reform, and liberal press.

## 14. Manual Review / Dependency List

| Dependency | Related CDL | Required Before Future Fact / Timeline Work |
|---|---|---|
| `SRC_UNSET_001` source harmonization | `CDL_MEXEMP_0001`, `0013` | exact Kindle/source attribution check |
| Missing CAPs `0044`, `0052`, `0096` | `CDL_MEXEMP_0005-0006`, `0011` | do not create speculative files; check screenshots/CSV only if later requested |
| Known missing Fact/Timeline ranges | many CDLs | never cite as existing; use only manual_review notes |
| BJDOCS / APBJPS / AGN / AGEO / FJ mapping | `CDL_MEXEMP_0008`, `0011-0016` | document-level citation map |
| Trial/court-martial records | `CDL_MEXEMP_0012-0013`, `0015-0016` | charges, procedure, sentence, appeals, execution order |
| Liberal press issue/date table | `CDL_MEXEMP_0008`, `0012-0016` | paper title, issue date, alignment, article type |
| Witness cluster bias profile | `CDL_MEXEMP_0011-0015` | compare Basch, Blasio, Felix Salm-Salm, Agnes Salm-Salm |
| French official / FO / U.S. official cross-checks | `CDL_MEXEMP_0003`, `0008-0012` | sender-recipient-date and policy chronology |
| Memory source comparison | `CDL_MEXEMP_0014` | Vigil, Zamacois, Arrangoiz, Romero de Terreros separation |

## 15. Next Recommended Step

次工程候補:

1. `CDL_MEXEMP_0016` を起点に、BJDOCS / APBJPS / AGN / AGEO / FJ の文書単位探索表を作る。
2. `CDL_MEXEMP_0012-0013` を優先し、裁判・軍法会議・処刑判断の共和派側証拠を整理する。
3. `CDL_MEXEMP_0015` の witness cluster を、Basch / Blasio / Felix Salm-Salm / Agnes Salm-Salm の比較表として読む。ただし新規Fact/Timeline化は、共和派側・公文書側の照合後に限定する。

## 16. Work Log and Stats

- Created: 2026-06-14.
- Same-purpose existing file: not found.
- Existing CDL ID: not found; started at `CDL_MEXEMP_0001`.
- CDL count: 16.
- Part / chapter candidate count: 16 chapter candidates across 7 Parts plus cross-cutting design.
- narrative_function counts: 導入 3; 対立拡大 4; 転換 1; 破局準備 2; 包囲 1; 裁判 2; 処刑 1; 記憶化 1; other 1.
- evidence_strength counts: moderate 3; mixed 11; weak 1; manual_review_needed 1.
- republican_balance_needed yes: 16.
- maximilian_centered_risk: high 11; medium 5; low 0.
- verification_needed yes: 16.
- manual_review_needed yes: 16.
- No new Fact Card, Timeline Entry, Capture Note, individual CDL Markdown, chapter Markdown, person/event/place/org/theme/source card, novel prose, long quotation, full transcription, renumbering, deletion, or gap filling was created.
