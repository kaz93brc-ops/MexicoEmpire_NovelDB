---
id: SHAWCROSS_NOTES_SOURCE_INDEX
type: source_index
status: active
created: 2026-06-13
updated: 2026-06-13
tags:
  - shawcross
  - notes
  - source-index
  - source-reliability
source_id: SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO
nsi_range: NSI_SHAWCROSS_0001-0048
---

# Shawcross Notes Source Index

## 1. Purpose

This file converts Shawcross NOTES pages into a source-discovery index for the Mexico Empire novel database. It is not a Fact Card set, not a Timeline set, and not a storage location for Shawcross's text or note text.

- Do not generate Fact / Timeline / Person / Event / Place / Org / Theme cards from this file automatically.
- Do not treat a cited source as proof of a historical claim until the cited source is checked directly.
- Use this index to decide which primary, quasi-primary, memoir/testimony, and secondary sources to inspect next.
- Keep Maximilian-centered and Shawcross-centered narrative bias visible during later source reliability work.

## 2. Scope

| Page | Kindle PC / Location | NOTES Range | Existing Log | Treatment |
|---:|---|---|---|---|
| 107 | 324/400 / No.4566/7062 | NOTES opening; abbreviations; Chapter 1 n.1-19; Chapter 2 n.1-7 | [[notes_translation_0107]] | source index only |
| 108 | 327/400 / No.4628/7062 | Chapter 2 n.8-25; Chapter 3 n.1-24 | [[notes_translation_0108]] | source index only |
| 109 | unverified | Chapter 3 n.25-41; Chapter 4 n.1-25 | `notes_translation_0109.md` not found | source index only; 要確認 |
| 110 | 332/400 / No.4764/7062 | Chapter 4 n.26-33; Chapter 5 n.1-23; Chapter 6 n.1-5 partial | [[notes_translation_0110]] | source index only |
| 111 | 335/400 / No.4828/7062 | Chapter 6 n.5 continued-39; Chapter 7 n.1-5 | [[notes_translation_0111]] | source index only |
| 112 | 338/400 / No.4895/7062 | Chapter 7 n.6-42; Chapter 8 n.1-8 | [[notes_translation_0112]] | source index only |
| 113 | 341/400 / No.4963/7062 | Chapter 8 n.9-31; Chapter 9 n.1-27 | [[notes_translation_0113]] | source index only |
| 114 | 344/400 / No.5036/7062 | Chapter 9 n.28-29; Chapter 10 n.1-23; EPILOGUE n.1-5 | [[SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO]] direct log | source index only; EPILOGUE n.5 complete |

## 3. Audit Preconditions

Confirmed from [[Shawcross_ID_Audit]]:

- CAP files exist across `CAP_MEXEMP_0001-0107`, but `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, and `CAP_MEXEMP_0096` are file-absent and remain manual review.
- Shawcross source_id CAP range is `CAP_MEXEMP_0002-0107`; `CAP_MEXEMP_0001` remains `SRC_UNSET_001`.
- FACT files exist only up to `FACT_MEXEMP_2560`. Do not treat `FACT_MEXEMP_2561-2608` as existing; they are `generation_gap_suspected`.
- TIME files exist only up to `TIME_MEXEMP_0422`. Do not treat `TIME_MEXEMP_0423-0448` as existing; they are `generation_gap_suspected`.
- `FACT_MEXEMP_2439-2513` and `TIME_MEXEMP_0387-0413` remain generation-gap/manual-review ranges.
- Broken existing references `FACT_MEXEMP_0489 -> FACT_MEXEMP_0431`, `FACT_MEXEMP_0638 -> FACT_MEXEMP_0439`, and `TIME_MEXEMP_0196 -> TIME_MEXEMP_0192` are not repaired here.
- `SRC_UNSET_001` remains on `CAP_MEXEMP_0001`, `FACT_MEXEMP_0001-0006`, and `TIME_MEXEMP_0001-0002`; no source_id rewrite is made here.
- Strict search found no NOTES-derived Fact conversion and no ACKNOWLEDGMENTS-derived body Fact/Timeline creation.

## 4. Abbreviations Index

| Abbrev. | Expanded Name / Holding | Type | Related Notes | Use | 要確認 |
|---|---|---|---|---|---|
| 400AP/61-400AP/63 | Campagne du Mexique, Archives nationales, Fonds Napoleon, Paris | archive_or_collection | Ch.8-9; Castelnau and French imperial papers | French imperial military/diplomatic correspondence | exact dossier and folio references |
| AAE, CP Mexique | Archives des Affaires Etrangeres, Correspondance Politique, Mexique, Paris | archive_or_collection | Ch.1, Ch.3, Ch.6-10 | French foreign ministry dispatches | accents, volume numbers, sender/recipient sequence |
| FO | Foreign Office, National Archives, London | archive_or_collection | Ch.1, Ch.7-8, trial-adjacent notes | British diplomatic reporting | FO series/volume/page verification |
| HHStA | Haus-, Hof- und Staatsarchiv, Archiv Kaiser Maximilian von Mexiko, Vienna | archive_or_collection | Ch.1-4 especially | Austrian/Habsburg and Maximilian correspondence | archive series and item numbering |

## 5. Source Index

| NSI ID | Page | Chapter / Notes | Source / Author | Source Type | Related Entities | Existing IDs | Use for Novel DB | Reliability / Bias Note | Verification | Priority | Manual Review |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| NSI_SHAWCROSS_0001 | 107, 113 | abbrev.; Ch.8-9 | 400AP/61-63, Archives nationales, Fonds Napoleon | archive_or_collection | Napoleon III; Castelnau; French army; Abdication Crisis; Under Siege | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO; THM-FOREIGN-INTERVENTION | trace French imperial command decisions and withdrawal policy | official archive; selection by Shawcross and dossier survival must be checked | yes | high | folio-level citation needed |
| NSI_SHAWCROSS_0002 | 107-114 | multiple notes | AAE, CP Mexique | archive_or_collection | French diplomats; Saligny; Dano; Drouyn de Lhuys; Forest; Mexico | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | reconstruct French diplomatic line, intervention policy, trial diplomacy | official dispatches but written for metropolitan readers; bureaucratic self-protection likely | yes | high | volume and folio references needed |
| NSI_SHAWCROSS_0003 | 107, 112-113 | Ch.1; Ch.7-8 | FO, National Archives, London | archive_or_collection | Wyke; Russell; Scarlett; Stanley; British legation | EVT-FRENCH-INTERVENTION-IN-MEXICO | independent diplomatic counterpoint to French and Mexican narratives | British interests and anti-French framing may shape reports | yes | high | exact FO volume checks |
| NSI_SHAWCROSS_0004 | 107-108 | abbrev.; Ch.1-4 | HHStA, Archiv Kaiser Maximilian von Mexiko | archive_or_collection | Maximilian; Carlota; Franz Joseph; Habsburg; Metternich | PER-MAXIMILIAN; PER-CARLOTA; PER-FRANZ-JOSEPH; ORG-HABSBURG; PLC-MIRAMAR | Habsburg correspondence, crown-offer negotiations, family pressure | strong Habsburg/imperial perspective; may privilege dynastic concerns | yes | high | item-level references required |
| NSI_SHAWCROSS_0005 | 107 | Ch.1 n.1 | Daniel Harvey Hill diary edition | quasi_primary | U.S.-Mexico War memory; U.S. expansion background | THM-FOREIGN-INTERVENTION | background atmosphere for U.S. military memory before intervention politics | edited diary; editor choices need review | yes | medium | check original diary context |
| NSI_SHAWCROSS_0006 | 107-108 | Ch.1; Ch.2 | Gutiérrez de Estrada pamphlet and letters | primary | Mexican Conservatives; monarchy project; Metternich; Maximilian | ORG-MEXICAN-CONSERVATIVES; THM-LEGITIMACY; EVT-SECOND-MEXICAN-EMPIRE | conservative argument for monarchy and early crown diplomacy | monarchist advocate; use as partisan source, not neutral Mexico-wide opinion | yes | high | title and letter locations |
| NSI_SHAWCROSS_0007 | 107 | Ch.1 n.3 | Frances Calderon de la Barca, Life in Mexico | memoir_or_testimony | Mexico; elite society; pre-intervention background | THM-LEGITIMACY | social texture and foreign observer voice before empire | foreign elite observer; gendered and class perspective | yes | medium | edition and passage context |
| NSI_SHAWCROSS_0008 | 107-108 | Ch.1; Ch.3 | Wyke/Russell; Saligny/Thouvenel dispatch clusters | primary | British and French diplomacy; Mexico debt crisis | EVT-FRENCH-INTERVENTION-IN-MEXICO | compare British and French motives before intervention | diplomatic dispatches are strategic documents | yes | high | separate FO and AAE citations |
| NSI_SHAWCROSS_0009 | 107 | Ch.1 n.8 | Concepcion Lombardo de Miramon, Memorias | memoir_or_testimony | Miramon; Mexican Conservatives; Carlota/Maximilian context | ORG-MEXICAN-CONSERVATIVES | conservative household and faction memory | retrospective self-justification likely; verify against documents | yes | medium | edition and chapter reference |
| NSI_SHAWCROSS_0010 | 107 | Ch.1 n.9-13 | Second Empire political context works | secondary | Napoleon III; French Second Empire; Bonapartism | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | ideological frame for Napoleon III and intervention imagination | interpretive secondary/classic political texts; not Mexico evidence alone | no | medium | split primary pamphlets later if needed |
| NSI_SHAWCROSS_0011 | 107, 112 | Ch.1 n.14; Ch.7 n.7; Ch.8 n.2 | U.S. presidential and congressional documents | primary | Buchanan; Andrew Johnson; U.S. Congress; Mexico policy | THM-FOREIGN-INTERVENTION; ORG-MEXICAN-REPUBLICANS | U.S. stance, Monroe Doctrine atmosphere, printed diplomatic material | official U.S. political framing; domestic agenda matters | yes | high | exact document title/page |
| NSI_SHAWCROSS_0012 | 107 | Ch.1 n.16-18 | Michel Chevalier and Charles du Pin texts | primary | French imperial policy; economic ideology; Mexico | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | French public-policy imagination of Mexico | imperial economic ideology; strong interventionist bias possible | yes | high | long French titles and archive location |
| NSI_SHAWCROSS_0013 | 107-114 | many notes | Egon Caesar Corti, Maximilian and Charlotte of Mexico | secondary | Maximilian; Carlota; Habsburg; trial and epilogue | PER-MAXIMILIAN; PER-CARLOTA; ORG-HABSBURG | roadmap to letters and court narrative | influential biography; often one step away from letters, must check originals | yes | high | publication-place oddities recur |
| NSI_SHAWCROSS_0014 | 107 | Ch.2 n.1 | Kendall and Sara Yorke Stevenson reminiscences | memoir_or_testimony | Maximilian; French Intervention; court observers | PER-MAXIMILIAN; EVT-FRENCH-INTERVENTION-IN-MEXICO | foreign witness texture and anecdotal court material | retrospective observer testimony; social memory bias | yes | medium | distinguish Kendall vs Stevenson |
| NSI_SHAWCROSS_0015 | 107 | Ch.2 n.4 | Maximilian, Recollections of My Life | memoir_or_testimony | Maximilian; Habsburg self-fashioning | PER-MAXIMILIAN; ORG-HABSBURG | Maximilian voice, ideals, self-image before Mexico | self-authored retrospective/self-fashioning; not neutral | yes | high | original publication and translation |
| NSI_SHAWCROSS_0016 | 108, 110-112 | Ch.2; Ch.5-8 | Konrad Ratz, Correspondencia inédita entre Maximiliano y Carlota | quasi_primary | Maximilian; Carlota; marriage; crisis | PER-MAXIMILIAN; PER-CARLOTA; PLC-MIRAMAR | private correspondence for emotion, politics, separation, crisis | edited/translated correspondence; editorial choices and omissions need review | yes | high | compare with archive originals if possible |
| NSI_SHAWCROSS_0017 | 108, 110, 112 | Ch.2; Ch.5; Ch.7 | Foussemagne, Charlotte de Belgique | quasi_primary | Carlota; Madame d'Hulst; Marie-Amelie; Belgium | PER-CARLOTA; PLC-MIRAMAR; ORG-HABSBURG | Carlota correspondence and Belgian court angle | edited biography/correspondence; pro-Carlota framing possible | yes | high | accents and letter dates |
| NSI_SHAWCROSS_0018 | 108 | Ch.2 n.11 | Letters of Queen Victoria | quasi_primary | Queen Victoria; Leopold; Carlota; Belgian/British court | PER-CARLOTA; ORG-HABSBURG | dynastic and court perception of marriage/politics | edited royal correspondence; court self-presentation | yes | medium | volume/page check |
| NSI_SHAWCROSS_0019 | 108 | Ch.2 n.20 | Luis Weckmann, Carlota de Belgica correspondence | quasi_primary | Carlota; Leopold II; European archives | PER-CARLOTA; ORG-HABSBURG | Carlota's Mexico-related writings from European archives | edited source collection; verify editorial scope | yes | high | collection scope and archive basis |
| NSI_SHAWCROSS_0020 | 108 | Ch.2-3 | HHStA reports and Maximilian correspondence cluster | primary | Maximilian; Metternich; Rechberg; Flahaut; Hidalgo | PER-MAXIMILIAN; PER-FRANZ-JOSEPH; ORG-HABSBURG | crown negotiations and French-Austrian diplomatic traffic | official/private documents; provenance and copy status matter | yes | high | some notes say copy/extract |
| NSI_SHAWCROSS_0021 | 108 | Ch.3 n.4 | Carl Bock, Prelude to Tragedy | secondary | Tripartite Convention; French invasion | EVT-FRENCH-INTERVENTION-IN-MEXICO | negotiation breakdown background | modern diplomatic history; use to orient primary checks | no | medium | identify cited primary basis |
| NSI_SHAWCROSS_0022 | 108, 110-114 | Ch.3; Ch.5; Ch.8-10 | French/imperial military memoir cluster | memoir_or_testimony | du Barail; Laurent; Keratry; Blanchot; Hans; Pitner | EVT-FRENCH-INTERVENTION-IN-MEXICO; PLC-QUERETARO | campaign texture, troop movements, siege atmosphere | participant memory and political grievance likely; verify with dispatches | yes | high | split by author in later reading |
| NSI_SHAWCROSS_0023 | 108, 110-113 | Ch.3; Ch.5-9 | Newspapers and periodicals: La Sociedad, El Siglo, Times, Journal des debats, Revue des deux mondes, Journal de Bruxelles, Mexican Times, Harper's Weekly | primary | Mexico City public sphere; French and British press; Republican/Imperial propaganda | EVT-FRENCH-INTERVENTION-IN-MEXICO; THM-LEGITIMACY | public rumor, propaganda, reportage, scene atmosphere | highly positional; newspaper politics must be mapped | yes | high | issue dates and article titles |
| NSI_SHAWCROSS_0024 | 108, 114 | Ch.3; Ch.10 | Jose Maria Vigil / Mexico a traves de los siglos | secondary | Liberal Reform; Republican memory; Juarez side | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS; THM-LIBERAL-REFORM | Republican/liberal historiographical counterweight | liberal national history; useful but partisan | no | medium | volume/title confirmation |
| NSI_SHAWCROSS_0025 | 108, 111 | Ch.3; Ch.6 | Gustave Niox, Expedition du Mexique | secondary | French army; Randon; Lorencez; intervention | EVT-FRENCH-INTERVENTION-IN-MEXICO | French military chronology and document trail | military history close to official French framing | no | medium | check quoted report source |
| NSI_SHAWCROSS_0026 | 108, 110 | Ch.3; Ch.5 | Cunningham, Hamnett, Taladoire, Schoonover | secondary | Napoleon III; Juarez; U.S.-Mexico relations; counter-guerrillas | PER-NAPOLEON-III; PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS | modern research scaffolding and historiographical checks | use to locate primary material; not final evidence alone | no | medium | assign by topic in matrix |
| NSI_SHAWCROSS_0027 | 110, 113-114 | Ch.5; Ch.8-10 | Niceto de Zamacois, Historia de Mejico | secondary | Mexican Empire; conservatives; trial/war narrative | EVT-SECOND-MEXICAN-EMPIRE; ORG-MEXICAN-CONSERVATIVES | broad nineteenth-century Mexican narrative | conservative-leaning framing possible; compare with Vigil/republican sources | no | medium | old spelling/title verification |
| NSI_SHAWCROSS_0028 | 110 | Ch.5 n.10-11 | Arrangoiz y Berzabal, Mejico desde 1808 hasta 1867 | memoir_or_testimony | Mexican Conservatives; imperial politics | ORG-MEXICAN-CONSERVATIVES; THM-LEGITIMACY | conservative participant interpretation | partisan and retrospective; verification_needed | yes | high | publication details and bias profile |
| NSI_SHAWCROSS_0029 | 110 | Ch.5 n.17 | Romero de Terreros, correspondencias contemporaneas | quasi_primary | Antonio Riba y Echeverria; Romero de Terreros; Mexico City | EVT-SECOND-MEXICAN-EMPIRE | contemporary correspondence for Mexico City political reactions | edited publication; selectivity unknown | yes | medium | exact letter and publication data |
| NSI_SHAWCROSS_0030 | 110 | Ch.6 n.1 | Pius IX, Syllabus of Errors | primary | Catholic Church; liberal empire; Rome | ORG-CATHOLIC-CHURCH; THM-LIBERAL-REFORM | church-state conflict context | doctrinal document; not Mexico-specific by itself | yes | medium | cite official text rather than web mirror |
| NSI_SHAWCROSS_0031 | 111-112 | Ch.6-7 | Dano / Drouyn de Lhuys diplomatic letters | primary | French Foreign Ministry; Maximilian; withdrawal pressure | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | French policy shift and pressure on Maximilian | official correspondence; strategic language | yes | high | AAE volume 66-67 checks |
| NSI_SHAWCROSS_0032 | 111 | Ch.6 | Brincourt, Lettres | quasi_primary | French military/diplomatic actors; Liberal Empire | EVT-FRENCH-INTERVENTION-IN-MEXICO | French side operational evidence | edited letters; authorship and addressee checks needed | yes | medium | incomplete note details in log |
| NSI_SHAWCROSS_0033 | 111 | Ch.6 | Garcia and Pereyra, Documentos ineditos o muy raros | quasi_primary | Mexican documentary evidence; imperial period | EVT-SECOND-MEXICAN-EMPIRE | source collection for rare Mexican documents | editorial criteria and authenticity need review | yes | medium | exact volume/document |
| NSI_SHAWCROSS_0034 | 111, 113 | Ch.6; Ch.8-9 | Paul Gaulot, L'Expedition du Mexique | secondary | French expedition; Castelnau; siege context | EVT-FRENCH-INTERVENTION-IN-MEXICO; PLC-QUERETARO | French narrative bridge for military/diplomatic episodes | later French narrative; may defend or critique imperial policy | no | medium | check cited primary references |
| NSI_SHAWCROSS_0035 | 112 | Ch.7 n.8 | John M. Schofield, Forty-Six Years in the Army | memoir_or_testimony | U.S. army; French withdrawal pressure | THM-FOREIGN-INTERVENTION | U.S. military perspective on post-Civil War pressure | memoir after the fact; self-positioning likely | yes | medium | compare with U.S. official documents |
| NSI_SHAWCROSS_0036 | 112 | Ch.7 n.13 | Carl von Malortie, Twixt Old Times and New | memoir_or_testimony | European court/military perspective; Maximilian | PER-MAXIMILIAN; ORG-HABSBURG | court atmosphere and late-imperial recollection | retrospective memoir; reliability uncertain | yes | medium | identity/context check |
| NSI_SHAWCROSS_0037 | 112-114 | Ch.8-10 | Samuel Basch, Memories of Mexico | memoir_or_testimony | Basch; Maximilian; Abdication Crisis; Querétaro; trial | PER-MAXIMILIAN; PLC-QUERETARO | close witness to final months and medical/personal detail | intimate witness but loyalist and retrospective; high verification need | yes | high | prioritize against trial records and other witnesses |
| NSI_SHAWCROSS_0038 | 110, 112-114 | Ch.5; Ch.7-10 | Jose Luis Blasio, memoirs/private secretary account | memoir_or_testimony | Blasio; Maximilian; Carlota; court life; trial | PER-MAXIMILIAN; PER-CARLOTA; EVT-SECOND-MEXICAN-EMPIRE | court anecdotes, Carlota observations, private secretary viewpoint | proximity valuable; role, politics, and later framing must be profiled | yes | high | create bias profile before using anecdotes |
| NSI_SHAWCROSS_0039 | 113-114 | Ch.9-10; Epilogue | Felix Salm-Salm, My Diary in Mexico in 1867 | memoir_or_testimony | Felix Salm-Salm; Maximilian; Querétaro; escape plans | PER-MAXIMILIAN; PLC-QUERETARO | siege action, escape plans, execution aftermath | participant self-defense and heroization likely | yes | high | compare with Basch, Blasio, court-martial sources |
| NSI_SHAWCROSS_0040 | 114 | Ch.10 | Agnes Salm-Salm testimony/memoir references | memoir_or_testimony | Agnes Salm-Salm; Juarez; Maximilian; mercy diplomacy | PER-BENITO-JUAREZ; PER-MAXIMILIAN; PLC-QUERETARO | dramatic mercy mission and prison/trial scenes | language barrier noted; gestures/reconstruction likely; verification_needed | yes | high | do not literalize dialogue without corroboration |
| NSI_SHAWCROSS_0041 | 113 | Ch.8-9 | Castelnau correspondence in 400AP/61, Dossier 3 | primary | Castelnau; Napoleon III; Bazaine; Maximilian | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | French mission, abdication pressure, late imperial orders | official report to emperor; may justify mission conduct | yes | high | exact dossier/pages |
| NSI_SHAWCROSS_0042 | 113 | Ch.8 | Scarlett / Stanley / Fischer correspondence, FO 50/397 | primary | Scarlett; Stanley; Fischer; Maximilian | EVT-FRENCH-INTERVENTION-IN-MEXICO | British external view of abdication crisis | diplomatic reports with British political interests | yes | high | all dates and recipients |
| NSI_SHAWCROSS_0043 | 113 | Ch.8 | Herzfeld, Bazaine, Fischer, Gutiérrez de Estrada letters | primary | Herzfeld; Bazaine; Fischer; Maximilian; Gutiérrez de Estrada | PER-MAXIMILIAN; EVT-SECOND-MEXICAN-EMPIRE | internal crisis traffic and court faction signals | scattered letters; provenance must be confirmed | yes | high | source location varies by note |
| NSI_SHAWCROSS_0044 | 109 | Ch.3 n.25-41; Ch.4 n.1-25 | Page 109 cited sources not yet indexed | unclear | French invasion; Mexican Crown; Maximilian; Napoleon III; Carlota | PER-MAXIMILIAN; PER-CARLOTA; PER-NAPOLEON-III | placeholder for missing notes_translation_0109 coverage | cannot infer source names from absent file | yes | high | 要確認: `notes_translation_0109.md` 未発見 |
| NSI_SHAWCROSS_0045 | 114 | Ch.10 | Antoine Forest-related correspondence, AAE CP Mexique 69 | primary | Forest; French diplomacy; trial period | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | trial-period French diplomatic evidence | official correspondence; political self-protection possible | yes | high | exact letter dates and folios |
| NSI_SHAWCROSS_0046 | 114 | Ch.10 | William Harris Chynoweth reference | unclear | Maximilian trial; execution crisis | PER-MAXIMILIAN; PLC-QUERETARO | possible trial/execution source candidate | bibliographic identity not established from current log | yes | medium | identify title, date, genre |
| NSI_SHAWCROSS_0047 | 114 | Ch.10; Epilogue | Le Memorial diplomatique and French legislative material | primary | French legislature; public diplomacy; intervention aftermath | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | French public-political record around collapse and memory | public diplomatic/political record; rhetoric-heavy | yes | medium | title accents and issue/date checks |
| NSI_SHAWCROSS_0048 | 114 | Epilogue | Louis Girard, Napoleon III; Martyn Rady, The Habsburgs | secondary | Napoleon III; Habsburgs; post-imperial memory | PER-NAPOLEON-III; ORG-HABSBURG; PER-FRANZ-JOSEPH | epilogue framing and broader dynastic/Napoleonic context | modern synthesis; use for framing, not primary claims | no | low | no immediate primary-source task |

## 6. High-Priority Source Candidates

- AAE, CP Mexique: Saligny/Thouvenel, Dano/Drouyn de Lhuys, and Forest-related trial-period correspondence.
- HHStA and related edited correspondence: Maximilian/Carlota, Habsburg family, Metternich/Rechberg, and crown-offer negotiations.
- 400AP/61-63: Castelnau and French imperial military/diplomatic papers for abdication and siege phases.
- FO records: Wyke/Russell and Scarlett/Stanley/Fischer as an external diplomatic counterpoint.
- Ratz, Foussemagne, Weckmann: edited letter collections for Maximilian/Carlota/Carlota-European correspondence.
- Basch, Blasio, Felix Salm-Salm, Agnes Salm-Salm: essential but verification-heavy witness accounts for final months, Querétaro, trial, and execution.
- Mexican press and Mexican historiography: La Sociedad, El Siglo, Vigil, Zamacois, Arrangoiz, and Romero de Terreros to counterbalance French/Habsburg framing.
- U.S. official documents: Johnson message, Executive Documents, and related U.S. policy records.

## 7. Memoir / Testimony Sources Requiring Verification

All `memoir_or_testimony` rows are `verification_needed: yes`.

| NSI ID | Source | Main Risk |
|---|---|---|
| NSI_SHAWCROSS_0007 | Calderon de la Barca | foreign elite observer and social filtering |
| NSI_SHAWCROSS_0009 | Lombardo de Miramon | conservative-family retrospective self-defense |
| NSI_SHAWCROSS_0014 | Kendall / Stevenson | reminiscence and witness-position limits |
| NSI_SHAWCROSS_0015 | Maximilian, Recollections | self-fashioning |
| NSI_SHAWCROSS_0022 | French/imperial military memoir cluster | campaign self-justification |
| NSI_SHAWCROSS_0028 | Arrangoiz | conservative participant bias |
| NSI_SHAWCROSS_0035 | Schofield | U.S. memoir and policy self-positioning |
| NSI_SHAWCROSS_0036 | Malortie | retrospective court memory |
| NSI_SHAWCROSS_0037 | Basch | loyal close witness; final-month recollection |
| NSI_SHAWCROSS_0038 | Blasio | proximity valuable but anecdotes need corroboration |
| NSI_SHAWCROSS_0039 | Felix Salm-Salm | participant heroization/self-defense risk |
| NSI_SHAWCROSS_0040 | Agnes Salm-Salm | language barrier and reconstructed dialogue risk |

## 8. Archive / Collection References

| Collection | Related NSI | Next Action |
|---|---|---|
| Archives nationales, Fonds Napoleon, Campagne du Mexique | NSI_SHAWCROSS_0001; NSI_SHAWCROSS_0041 | identify dossier/folio and Castelnau sequence |
| AAE, CP Mexique | NSI_SHAWCROSS_0002; NSI_SHAWCROSS_0008; NSI_SHAWCROSS_0031; NSI_SHAWCROSS_0045 | build sender-recipient-date list |
| FO, National Archives | NSI_SHAWCROSS_0003; NSI_SHAWCROSS_0008; NSI_SHAWCROSS_0042 | verify FO volume and dispatch dates |
| HHStA, Archiv Kaiser Maximilian von Mexiko | NSI_SHAWCROSS_0004; NSI_SHAWCROSS_0020 | map copies/extracts vs originals |

## 9. Cross-reference to Existing IDs

Verified existing entity IDs usable in this index:

- People: `PER-MAXIMILIAN`, `PER-CARLOTA`, `PER-BENITO-JUAREZ`, `PER-NAPOLEON-III`, `PER-FRANZ-JOSEPH`
- Organizations: `ORG-HABSBURG`, `ORG-MEXICAN-CONSERVATIVES`, `ORG-MEXICAN-REPUBLICANS`, `ORG-CATHOLIC-CHURCH`
- Events: `EVT-FRENCH-INTERVENTION-IN-MEXICO`, `EVT-SECOND-MEXICAN-EMPIRE`
- Places: `PLC-MIRAMAR`, `PLC-QUERETARO`
- Themes: `THM-FOREIGN-INTERVENTION`, `THM-LEGITIMACY`, `THM-LIBERAL-REFORM`
- Source note: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`

Verified Shawcross CAP ranges should be treated as non-contiguous because of missing captures:

- `CAP_MEXEMP_0002-0043`
- `CAP_MEXEMP_0045-0051`
- `CAP_MEXEMP_0053-0095`
- `CAP_MEXEMP_0097-0107`

Fact/Timeline links are not assigned at NSI row level. Before linking any Fact/Timeline ID, re-check [[Shawcross_ID_Audit]], because known gaps include `FACT_MEXEMP_2439-2513`, `FACT_MEXEMP_2561-2608`, `TIME_MEXEMP_0387-0413`, and `TIME_MEXEMP_0423-0448`.

## 10. Source Reliability Matrix Handoff

Initial matrix categories:

| Category | NSI IDs | Matrix Note |
|---|---|---|
| primary archive / official documents | 0001-0004, 0008, 0011, 0012, 0020, 0023, 0030, 0031, 0041-0043, 0045, 0047 | strongest source tier after citation and provenance verification |
| quasi-primary edited collections | 0005, 0016-0019, 0029, 0032-0033 | useful but editorial policy, omissions, translation, and original-location checks required |
| memoir_or_testimony | 0007, 0009, 0014-0015, 0022, 0028, 0035-0040 | all require corroboration; do not literalize dialogue or motives without cross-check |
| secondary research | 0010, 0013, 0021, 0024-0027, 0034, 0048 | use for orientation, historiography, and source leads |
| unclear | 0044, 0046 | do not use for claims until bibliographic identity is established |

Perspective axes to track:

- Maximilian / Habsburg / Carlota perspective: HHStA, Ratz, Foussemagne, Weckmann, Corti.
- French imperial perspective: AAE, 400AP, Niox, Gaulot, Castelnau, French press.
- Republican / Juarez-side perspective: Vigil, Mexican Republican documents, U.S. records, Mexican press.
- Conservative Mexican perspective: Gutiérrez de Estrada, Arrangoiz, Zamacois, Lombardo de Miramon.
- U.S. perspective: American Presidency Project, Executive Documents, Schofield, Schoonover.
- Witness/inside-court perspective: Basch, Blasio, Salm-Salm, Pitner, Stevenson, Malortie.

Creative-use caution:

- Memoir details may be excellent for scenes, gestures, atmosphere, fear, rumors, and social dynamics.
- They should be separated from confirmed historical facts until corroborated by diplomatic records, trial records, newspapers, or multiple independent witnesses.
- Querétaro siege, trial, execution, and Carlota's breakdown are high-interest narrative zones with strong political incentives for later self-justification.

## 11. Reading Candidate List

Priority order for next reading:

1. Build a citation map for AAE / FO / HHStA / 400AP references by sender, recipient, date, archive series, and note number.
2. Read Basch, Blasio, Felix Salm-Salm, and Agnes Salm-Salm as a controlled witness cluster, recording bias and corroboration status separately.
3. Check Ratz, Foussemagne, and Weckmann for Maximilian/Carlota letters and editorial principles.
4. Check Mexican-side counterweights: Vigil, La Sociedad, El Siglo, Zamacois, Arrangoiz, Romero de Terreros.
5. Check U.S. official documents and Schofield for foreign-policy pressure and Republican support context.
6. Use modern secondary works only after the primary/quasi-primary map is stable.

## 12. Unresolved / Manual Review Needed

- `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096`: file_absent; do not create speculative files.
- `FACT_MEXEMP_2561-2608`: generation_gap_suspected; not treated as existing IDs.
- `TIME_MEXEMP_0423-0448`: generation_gap_suspected; not treated as existing IDs.
- `FACT_MEXEMP_2439-2513`: generation_gap_suspected/manual review from trial section captures.
- `TIME_MEXEMP_0387-0413`: generation_gap_suspected/manual review from trial section captures.
- `TIME_MEXEMP_0413`: boundary review between `CAP_MEXEMP_0101` and `CAP_MEXEMP_0102`; not linked as existing.
- `SRC_UNSET_001`: remains on `CAP_MEXEMP_0001`, `FACT_MEXEMP_0001-0006`, and `TIME_MEXEMP_0001-0002`; no rewrite here.
- `FACT_MEXEMP_0489 -> FACT_MEXEMP_0431`: existing-card-to-nonexistent-ID reference; not repaired here.
- `FACT_MEXEMP_0638 -> FACT_MEXEMP_0439`: existing-card-to-nonexistent-ID reference; not repaired here.
- `TIME_MEXEMP_0196 -> TIME_MEXEMP_0192`: existing-card-to-nonexistent-ID reference; not repaired here.
- `notes_translation_0109.md` 未発見。109枚目のNOTES範囲は Progress Master 登録済みとして扱うが、索引は `NSI_SHAWCROSS_0044` の暫定行に限定する。
- 109枚目範囲: Chapter 3 n.25-41 and Chapter 4 n.1-25. 要確認: source names cannot be completed without the missing log or screenshot.
- 114枚目 direct log: Chapter 10 n.3 Spanish long title, Chapter 10 n.11 Corti publication-place formatting, and EPILOGUE n.3 `Supplement/Supplement au Journal des debats` spelling remain bibliographic checks.

## 13. Work Log

- 2026-06-13: Created this single aggregated source index because no same-purpose `Shawcross_Notes_Source_Index.md` or `NSI_SHAWCROSS_####` file was found. No individual NSI Markdown files were created.
- 2026-06-13: Converted NOTES pages 107-114 into 48 source-index rows, `NSI_SHAWCROSS_0001-0048`.
- 2026-06-13: Carried forward [[Shawcross_ID_Audit]] gaps and did not modify Capture, Fact, Timeline, or entity cards.
- 2026-06-13: No Shawcross text, NOTES full text, screenshot full transcription, long quotation, Fact Card, or Timeline Entry was created from NOTES.

## 14. Index Stats

| Metric | Count |
|---|---:|
| NSI rows | 48 |
| primary | 13 |
| quasi_primary | 8 |
| memoir_or_testimony | 12 |
| secondary | 9 |
| reference | 0 |
| archive_or_collection | 4 |
| unclear | 2 |
| verification_needed yes | 40 |
