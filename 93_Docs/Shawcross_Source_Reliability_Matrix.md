---
id: SHAWCROSS_SOURCE_RELIABILITY_MATRIX
type: source_reliability_matrix
status: active
created: 2026-06-13
updated: 2026-06-13
tags:
  - shawcross
  - source-reliability
  - notes
  - mexemp
source_id: SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO
nsi_range: NSI_SHAWCROSS_0001-0048
srm_range: SRM_SHAWCROSS_0001-0048
---

# Shawcross Source Reliability Matrix

## 1. Purpose

This matrix converts [[Shawcross_Notes_Source_Index]] into a working reliability guide for the Mexico Empire novel database. It does not certify Shawcross's notes as historical proof.

- Use it to classify cited sources as primary, quasi-primary, memoir/testimony, secondary, archive/collection, or unclear.
- Keep source standpoint, bias, limits, and cross-check needs visible before using any claim in Fact, Timeline, Person, Event, Place, Org, or Theme cards.
- Treat SRM IDs as reliability-management IDs only. They are not Fact IDs.
- Do not create new Fact / Timeline / Person / Event / Place / Org / Theme cards from this file automatically.
- Do not store Shawcross body text, NOTES text, screenshots, or long quotations here.

## 2. Scope

| Item | Value |
|---|---|
| Input source index | [[Shawcross_Notes_Source_Index]] |
| Covered NSI range | `NSI_SHAWCROSS_0001-0048` |
| SRM range | `SRM_SHAWCROSS_0001-0048` |
| Source note | [[SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO]] |
| Progress / audit context | [[Shawcross_Progress_Master]], [[Shawcross_ID_Audit]] |
| Treatment | source evaluation only; no body Fact/Timeline conversion |

## 3. Inputs

- [[Shawcross_Progress_Master]]
- [[Shawcross_ID_Audit]]
- [[Shawcross_Notes_Source_Index]]
- [[SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO]]
- Existing Shawcross-related Capture / Fact / Timeline file ranges were checked for context only.
- Existing entity IDs carried forward only where already verified in [[Shawcross_Notes_Source_Index]] and local entity/event/theme files.

## 4. Method

- Each NSI row receives one SRM row.
- Source type follows the NSI classification unless the row itself is an archive/collection or unclear placeholder.
- `verification_needed` remains `yes` for primary, quasi-primary, memoir/testimony, archive/collection, unclear rows, and the Corti secondary row because it acts as a route into letters and court narrative.
- `reliability_score` is provisional. It measures usefulness for historical claim-building, not vividness for fiction.
- `priority` measures next-reading / cross-check urgency for Maximilian's fall, Querétaro, trial/execution, Carlota, Juárez/republicans, French withdrawal, U.S. pressure, and memory politics.

## 5. Reliability Scale

| Score | Meaning |
|---:|---|
| 5 | Strong base for historical reconstruction, usually official/archival primary material; still requires item-level verification. |
| 4 | Quasi-primary or edited source collection, or public official/press source with strong evidentiary value; editorial and context checks required. |
| 3 | Useful secondary work or comparatively useful testimony; suitable as guide or scene support only after corroboration. |
| 2 | Strong retrospective, partisan, self-justifying, or performative risk; high descriptive value but weak for fact certification alone. |
| 1 | Bibliographic identity, source text, or evidentiary status unclear; do not use for claims yet. |

## 6. Source Reliability Matrix

| SRM ID | NSI ID | Source / Archive | Author / Body | Source Type | Contemporaneity / Party | Bias Risk / Limit | Strength | Best Use | Cross-check With | Related Entities | Existing IDs | verification_needed | reliability_score | priority | manual_review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---|---|
| SRM_SHAWCROSS_0001 | NSI_SHAWCROSS_0001 | 400AP/61-63, Archives nationales, Fonds Napoleon | French imperial archive / Campagne du Mexique | archive_or_collection | Contemporary official archive; French imperial command and court perspective | Survival, selection, and dossier context; French imperial self-protection | High-value access point for Castelnau, military, and late-imperial correspondence | Diplomatic/military chronology; abdication and siege evidence | AAE; FO; HHStA; Basch; Blasio; Salm-Salm; Mexican press | Napoleon III; Castelnau; Bazaine; Maximilian; Querétaro; foreign intervention | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO; THM-FOREIGN-INTERVENTION | yes | 5 | high | folio and dossier references needed |
| SRM_SHAWCROSS_0002 | NSI_SHAWCROSS_0002 | AAE, CP Mexique | French Foreign Ministry | archive_or_collection | Contemporary official French diplomatic perspective | Dispatches written for Paris; bureaucratic self-defense and policy framing | Core source for French intervention, withdrawal, and trial-period diplomacy | Diplomatic chronology; French policy motives; official pressure | FO; HHStA; 400AP; U.S. official documents; Mexican press | Saligny; Dano; Drouyn de Lhuys; Forest; Napoleon III; Mexico | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 5 | high | volume, folio, sender, recipient, date list needed |
| SRM_SHAWCROSS_0003 | NSI_SHAWCROSS_0003 | FO, National Archives, London | British Foreign Office | archive_or_collection | Contemporary British diplomatic reporting | British anti-French or interest-driven framing; legation rumor risk | External diplomatic counterpoint to French and Mexican accounts | Cross-check of intervention, abdication, and trial diplomacy | AAE; U.S. documents; Mexican press; HHStA | Wyke; Russell; Scarlett; Stanley; Fischer; British legation | EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 5 | high | FO series and dispatch dates needed |
| SRM_SHAWCROSS_0004 | NSI_SHAWCROSS_0004 | HHStA, Archiv Kaiser Maximilian von Mexiko | Habsburg state/house archive | archive_or_collection | Contemporary dynastic, court, and Maximilian correspondence | Habsburg family/state viewpoint; dynastic self-fashioning | Core evidence for crown negotiation, Miramar, Maximilian/Carlota letters | Court politics; family pressure; private/public imperial language | Ratz; Foussemagne; Weckmann; AAE; FO | Maximilian; Carlota; Franz Joseph; Habsburg; Metternich; Miramar | PER-MAXIMILIAN; PER-CARLOTA; PER-FRANZ-JOSEPH; ORG-HABSBURG; PLC-MIRAMAR | yes | 5 | high | series and item-level confirmation needed |
| SRM_SHAWCROSS_0005 | NSI_SHAWCROSS_0005 | Daniel Harvey Hill diary edition | Daniel Harvey Hill / editor | quasi_primary | Contemporary diary material in later edition; U.S. military memory | Edited text; U.S. soldier worldview; distant from Mexican Empire core | Background texture for U.S.-Mexico War memory | Scene/background only; U.S. memory atmosphere | U.S. official documents; later U.S. diplomacy; Mexican accounts | U.S.-Mexico War memory; U.S. expansion; foreign intervention | THM-FOREIGN-INTERVENTION | yes | 4 | medium | original diary context and editor policy |
| SRM_SHAWCROSS_0006 | NSI_SHAWCROSS_0006 | Gutiérrez de Estrada pamphlet and letters | José María Gutiérrez de Estrada | primary | Contemporary monarchist advocacy / Mexican conservative position | Not neutral; programmatic monarchist argument | Direct evidence for conservative monarchy project and legitimacy claims | Conservative ideology; crown diplomacy; faction voice | Vigil; Zamacois; Arrangoiz; HHStA; French diplomacy | Mexican Conservatives; monarchy project; Metternich; Maximilian | ORG-MEXICAN-CONSERVATIVES; THM-LEGITIMACY; EVT-SECOND-MEXICAN-EMPIRE | yes | 3 | high | title, date, and letter locations |
| SRM_SHAWCROSS_0007 | NSI_SHAWCROSS_0007 | Life in Mexico | Frances Calderon de la Barca | memoir_or_testimony | Near-contemporary foreign elite observation, pre-intervention context | Foreign, elite, classed and gendered filter; not empire-period evidence by itself | Social texture and outsider description of Mexican elite life | Atmosphere and social setting; not claim foundation alone | Mexican press; Mexican memoirs; modern social history | Mexico; elite society; legitimacy background | THM-LEGITIMACY | yes | 3 | medium | edition and passage context |
| SRM_SHAWCROSS_0008 | NSI_SHAWCROSS_0008 | Wyke/Russell and Saligny/Thouvenel dispatch clusters | British and French diplomats | primary | Contemporary official diplomatic documents | Strategic diplomatic language; national-interest framing | Direct comparative evidence for debt crisis and intervention motives | Diplomatic sequence; British/French divergence | AAE; FO originals; U.S. documents; Mexican government records | Wyke; Russell; Saligny; Thouvenel; Mexico debt crisis | EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 5 | high | separate FO and AAE citations |
| SRM_SHAWCROSS_0009 | NSI_SHAWCROSS_0009 | Memorias | Concepción Lombardo de Miramón | memoir_or_testimony | Retrospective conservative-family testimony | Family honor, conservative self-defense, retrospective reconstruction | Useful for conservative household and faction memory | Character/worldview reference; bias-aware conservative voice | Arrangoiz; Zamacois; Vigil; official records | Miramón; Mexican Conservatives; Carlota/Maximilian context | ORG-MEXICAN-CONSERVATIVES | yes | 2 | medium | edition and chapter reference |
| SRM_SHAWCROSS_0010 | NSI_SHAWCROSS_0010 | Second Empire political context works | Multiple secondary authors | secondary | Later interpretive scholarship / political history | Interpretive distance from Mexico; may privilege French imperial frame | Useful framework for Napoleon III, Bonapartism, and ideology | Historiographical scaffolding; not direct evidence | Primary pamphlets; AAE; French public records | Napoleon III; French Second Empire; Bonapartism | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | no | 3 | medium | split works later if used heavily |
| SRM_SHAWCROSS_0011 | NSI_SHAWCROSS_0011 | U.S. presidential and congressional documents | U.S. executive / Congress | primary | Contemporary official U.S. political documents | Domestic political agenda; Monroe Doctrine rhetoric; printed selection | Core U.S. perspective on intervention pressure and republican legitimacy | U.S. policy chronology; diplomatic pressure; official stance | FO; AAE; Mexican republican records; Schofield | Buchanan; Andrew Johnson; U.S. Congress; Mexico policy | THM-FOREIGN-INTERVENTION; ORG-MEXICAN-REPUBLICANS | yes | 5 | high | exact document titles and page references |
| SRM_SHAWCROSS_0012 | NSI_SHAWCROSS_0012 | Michel Chevalier and Charles du Pin texts | Chevalier; du Pin | primary | Contemporary French policy/economic texts | Imperial economic ideology and interventionist argument | Reveals French public-policy imagination of Mexico | Ideology; propaganda; policy rhetoric | AAE; French press; Mexican liberal replies | Napoleon III; French imperial policy; Mexico | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | yes | 3 | high | title and publication context |
| SRM_SHAWCROSS_0013 | NSI_SHAWCROSS_0013 | Maximilian and Charlotte of Mexico | Egon Caesar Corti | secondary | Later biography using letters and court material | Habsburg/court narrative pull; source mediation | Strong source map for Maximilian/Carlota correspondence and court narrative | Orientation; source leads; memory/history framing | HHStA; Ratz; Foussemagne; Weckmann; primary letters | Maximilian; Carlota; Habsburg; trial and epilogue | PER-MAXIMILIAN; PER-CARLOTA; ORG-HABSBURG | yes | 3 | high | verify originals behind quotations |
| SRM_SHAWCROSS_0014 | NSI_SHAWCROSS_0014 | Kendall and Sara Yorke Stevenson reminiscences | Kendall; Stevenson | memoir_or_testimony | Retrospective foreign witness reminiscence | Anecdotal memory; witness-position limits | Foreign observer texture and court/social anecdote | Scene detail only after corroboration | Court records; press; Basch/Blasio where relevant | Maximilian; French Intervention; court observers | PER-MAXIMILIAN; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 3 | medium | distinguish Kendall and Stevenson |
| SRM_SHAWCROSS_0015 | NSI_SHAWCROSS_0015 | Recollections of My Life | Maximilian | memoir_or_testimony | Self-authored/self-presenting Maximilian voice | Self-fashioning; idealized self-image; not neutral evidence | Direct access to Maximilian's language, ideals, and persona | Character voice and ideology; not factual certification alone | HHStA letters; Ratz; Carlota letters; hostile accounts | Maximilian; Habsburg self-fashioning | PER-MAXIMILIAN; ORG-HABSBURG | yes | 2 | high | original edition and translation |
| SRM_SHAWCROSS_0016 | NSI_SHAWCROSS_0016 | Correspondencia inédita entre Maximiliano y Carlota | Konrad Ratz, editor | quasi_primary | Edited private correspondence based on contemporary letters | Editorial selection, transcription, translation, omissions | Core material for Maximilian/Carlota relationship, politics, and crisis | Private correspondence; emotion/politics; separation scenes | HHStA originals; Weckmann; Foussemagne; Corti | Maximilian; Carlota; Miramar; crisis | PER-MAXIMILIAN; PER-CARLOTA; PLC-MIRAMAR | yes | 4 | high | editorial method and original-location check |
| SRM_SHAWCROSS_0017 | NSI_SHAWCROSS_0017 | Charlotte de Belgique | Foussemagne, editor/author | quasi_primary | Edited Carlota-related correspondence / Belgian court angle | Pro-Carlota or dynastic framing; selection risk | Important for Carlota, Belgium, and European court network | Carlota psychology/politics with caution; Belgian court context | Ratz; Weckmann; HHStA; Belgian records | Carlota; Madame d'Hulst; Marie-Amélie; Belgium | PER-CARLOTA; PLC-MIRAMAR; ORG-HABSBURG | yes | 4 | high | letter dates and editorial policy |
| SRM_SHAWCROSS_0018 | NSI_SHAWCROSS_0018 | Letters of Queen Victoria | Queen Victoria / editors | quasi_primary | Edited royal correspondence | Court self-presentation; diplomatic decorum; editorial pruning | Dynastic perception of marriage and politics | Court viewpoint; European perception | Foussemagne; Weckmann; HHStA; British FO | Queen Victoria; Leopold; Carlota; Belgian/British court | PER-CARLOTA; ORG-HABSBURG | yes | 4 | medium | volume and page check |
| SRM_SHAWCROSS_0019 | NSI_SHAWCROSS_0019 | Carlota de Bélgica correspondence | Luis Weckmann, editor | quasi_primary | Edited Carlota / European correspondence | Editorial scope and archive selection must be known | Key for Carlota's Mexico-related writings and European archive basis | Carlota voice; politics; mental-state caution | Ratz; Foussemagne; HHStA; Belgian archive material | Carlota; Leopold II; European archives | PER-CARLOTA; ORG-HABSBURG | yes | 4 | high | collection scope and archive basis |
| SRM_SHAWCROSS_0020 | NSI_SHAWCROSS_0020 | HHStA reports and Maximilian correspondence cluster | Maximilian, Metternich, Rechberg, Flahaut, Hidalgo, etc. | primary | Contemporary diplomatic/private documents | Copy/extract status; court and state interests | Core evidence for crown negotiations and French-Austrian traffic | Negotiation chronology; Habsburg/French relations | HHStA item originals; AAE; FO; Ratz | Maximilian; Metternich; Rechberg; Flahaut; Hidalgo | PER-MAXIMILIAN; PER-FRANZ-JOSEPH; ORG-HABSBURG | yes | 5 | high | copy/extract versus original status |
| SRM_SHAWCROSS_0021 | NSI_SHAWCROSS_0021 | Prelude to Tragedy | Carl Bock | secondary | Later diplomatic history | Depends on cited primary base; interpretive framing | Useful for Tripartite Convention and early intervention sequence | Orientation before primary verification | FO; AAE; U.S. documents; Mexican sources | Tripartite Convention; French invasion | EVT-FRENCH-INTERVENTION-IN-MEXICO | no | 3 | medium | identify primary basis |
| SRM_SHAWCROSS_0022 | NSI_SHAWCROSS_0022 | French/imperial military memoir cluster | du Barail; Laurent; Kératry; Blanchot; Hans; Pitner, etc. | memoir_or_testimony | Participant memoirs, mostly retrospective | Campaign self-justification; blame allocation; rank/service interest | Useful for troop life, operational texture, siege atmosphere | Scene texture and military perspective after corroboration | AAE; 400AP; Niox; Gaulot; FO; Mexican military accounts | French army; imperial forces; Querétaro; campaign | EVT-FRENCH-INTERVENTION-IN-MEXICO; PLC-QUERETARO | yes | 2 | high | split by author in later reading |
| SRM_SHAWCROSS_0023 | NSI_SHAWCROSS_0023 | Newspapers and periodicals | La Sociedad; El Siglo; Times; Journal des débats; Revue des deux mondes; Journal de Bruxelles; Mexican Times; Harper's Weekly | primary | Contemporary press and public opinion | Propaganda, rumor, party line, censorship, foreign audience shaping | Excellent for public atmosphere, timing, and competing narratives | Press/public opinion; rumor; scene atmosphere | Official records; rival newspapers; memoirs | Mexico City public sphere; French/British/Mexican press | EVT-FRENCH-INTERVENTION-IN-MEXICO; THM-LEGITIMACY | yes | 3 | high | issue dates, article titles, political alignment |
| SRM_SHAWCROSS_0024 | NSI_SHAWCROSS_0024 | México a través de los siglos / Vigil material | José María Vigil | secondary | Later liberal/national historiography | Liberal republican memory; anti-imperial framing | Important counterweight to Maximilian/Habsburg/French material | Republican narrative and memory politics | Zamacois; Arrangoiz; Mexican official records; press | Liberal Reform; Juárez side; republican memory | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS; THM-LIBERAL-REFORM | no | 3 | medium | volume and title confirmation |
| SRM_SHAWCROSS_0025 | NSI_SHAWCROSS_0025 | Expédition du Mexique | Gustave Niox | secondary | Later French military history near official frame | French military institutional viewpoint | Useful chronology and document trail for French operations | Military chronology, not final evidence alone | 400AP; AAE; military memoirs; Mexican accounts | French army; Randon; Lorencez; intervention | EVT-FRENCH-INTERVENTION-IN-MEXICO | no | 3 | medium | quoted report source check |
| SRM_SHAWCROSS_0026 | NSI_SHAWCROSS_0026 | Cunningham, Hamnett, Taladoire, Schoonover | Modern secondary scholarship cluster | secondary | Later scholarship / mixed topics | Varies by author; synthesis may hide source disputes | Good scaffolding for Napoleon III, Juárez, U.S.-Mexico, counter-guerrillas | Research guide and historiographic check | Primary archives by topic; U.S. documents; Mexican records | Napoleon III; Juárez; U.S.-Mexico relations | PER-NAPOLEON-III; PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS | no | 3 | medium | assign by topic if cited later |
| SRM_SHAWCROSS_0027 | NSI_SHAWCROSS_0027 | Historia de Méjico | Niceto de Zamacois | secondary | Later nineteenth-century Mexican narrative | Conservative-leaning or anti-liberal framing likely; old narrative conventions | Broad Mexican narrative and memory source | Compare conservative memory with liberal Vigil | Vigil; Arrangoiz; Mexican press; official records | Mexican Empire; conservatives; trial/war narrative | EVT-SECOND-MEXICAN-EMPIRE; ORG-MEXICAN-CONSERVATIVES | no | 2 | medium | title/spelling and volume verification |
| SRM_SHAWCROSS_0028 | NSI_SHAWCROSS_0028 | Méjico desde 1808 hasta 1867 | Arrangoiz y Berzábal | memoir_or_testimony | Conservative participant / retrospective account | Partisan conservative self-defense and anti-liberal framing | Valuable inside view of conservative imperial politics | Conservative motive and ideology; not neutral fact base | Vigil; Zamacois; Gutiérrez de Estrada; Mexican official records | Mexican Conservatives; imperial politics | ORG-MEXICAN-CONSERVATIVES; THM-LEGITIMACY | yes | 2 | high | publication details and bias profile |
| SRM_SHAWCROSS_0029 | NSI_SHAWCROSS_0029 | Correspondencias contemporáneas | Romero de Terreros, editor/source | quasi_primary | Edited contemporary correspondence | Selection and editorial framing unknown | Useful Mexico City correspondence and reactions | Political atmosphere and elite communication | Press; official records; Vigil; Zamacois | Antonio Riba y Echeverría; Mexico City | EVT-SECOND-MEXICAN-EMPIRE | yes | 4 | medium | exact letter and publication data |
| SRM_SHAWCROSS_0030 | NSI_SHAWCROSS_0030 | Syllabus of Errors | Pius IX / Catholic Church | primary | Contemporary doctrinal document | Not Mexico-specific; theological/political agenda | Context for Catholic-liberal conflict and Maximilian's church problem | Ideological background; church-state conflict | Mexican church documents; Maximilian decrees; liberal sources | Catholic Church; liberal empire; Rome | ORG-CATHOLIC-CHURCH; THM-LIBERAL-REFORM | yes | 4 | medium | official text preferred |
| SRM_SHAWCROSS_0031 | NSI_SHAWCROSS_0031 | Dano / Drouyn de Lhuys diplomatic letters | French Foreign Ministry actors | primary | Contemporary official French diplomatic correspondence | Strategic pressure and bureaucratic language | Direct evidence for French policy shift and pressure on Maximilian | Withdrawal chronology; French-Maximilian conflict | AAE originals; 400AP; HHStA; FO | Dano; Drouyn de Lhuys; Maximilian; Napoleon III | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 5 | high | AAE volume 66-67 checks |
| SRM_SHAWCROSS_0032 | NSI_SHAWCROSS_0032 | Lettres | Brincourt | quasi_primary | Edited letters, French military/diplomatic context | Authorship, addressee, and editorial omissions need checking | French operational or political evidence if authenticated | Supplemental French-side evidence | AAE; 400AP; military memoirs; Niox | French military/diplomatic actors | EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 4 | medium | incomplete note details |
| SRM_SHAWCROSS_0033 | NSI_SHAWCROSS_0033 | Documentos inéditos o muy raros | García and Pereyra, editors | quasi_primary | Edited Mexican documentary collection | Editorial criteria and authenticity need review | Possible route to rare Mexican documents | Source leads; Mexican-side primary trail | Original documents; Mexican archives; Vigil; press | Mexican documentary evidence; imperial period | EVT-SECOND-MEXICAN-EMPIRE | yes | 4 | medium | exact volume/document |
| SRM_SHAWCROSS_0034 | NSI_SHAWCROSS_0034 | L'Expédition du Mexique | Paul Gaulot | secondary | Later French expedition narrative | French retrospective framing; possible policy defense/critique | Narrative bridge for military/diplomatic episodes | Orientation, then check cited sources | AAE; 400AP; Niox; military memoirs | French expedition; Castelnau; siege context | EVT-FRENCH-INTERVENTION-IN-MEXICO; PLC-QUERETARO | no | 3 | medium | primary references behind narrative |
| SRM_SHAWCROSS_0035 | NSI_SHAWCROSS_0035 | Forty-Six Years in the Army | John M. Schofield | memoir_or_testimony | Retrospective U.S. military memoir | Self-positioning in U.S. pressure narrative | Useful U.S. military perspective on post-Civil War pressure | U.S. pressure scenes only after official-document check | U.S. official documents; Johnson papers; Mexican republican accounts | U.S. army; French withdrawal pressure | THM-FOREIGN-INTERVENTION | yes | 3 | medium | compare with official documents |
| SRM_SHAWCROSS_0036 | NSI_SHAWCROSS_0036 | Twixt Old Times and New | Carl von Malortie | memoir_or_testimony | Retrospective European court/military memory | Identity/context unclear; court nostalgia | Possible court atmosphere and late-imperial recollection | Background color with caution | HHStA; court letters; other memoirs | European court/military perspective; Maximilian | PER-MAXIMILIAN; ORG-HABSBURG | yes | 2 | medium | identity and context check |
| SRM_SHAWCROSS_0037 | NSI_SHAWCROSS_0037 | Memories of Mexico | Samuel Basch | memoir_or_testimony | Close witness, final months, retrospective | Loyal to Maximilian; medical/intimate proximity; hindsight shaping | High-value witness for final months, Querétaro, trial, execution atmosphere | Scene detail and personal behavior; fact use only after corroboration | Blasio; Felix Salm-Salm; Agnes Salm-Salm; trial records; AAE/FO; press | Basch; Maximilian; Querétaro; trial | PER-MAXIMILIAN; PLC-QUERETARO | yes | 3 | high | prioritize witness-cluster comparison |
| SRM_SHAWCROSS_0038 | NSI_SHAWCROSS_0038 | José Luis Blasio memoirs / private secretary account | José Luis Blasio | memoir_or_testimony | Near-court testimony, later account | Role, politics, and anecdotal reconstruction must be profiled | Valuable court anecdotes, Carlota observations, private-secretary proximity | Court scenes, relationships, private atmosphere after corroboration | Basch; Salm-Salm; Ratz; Foussemagne; official court documents | Blasio; Maximilian; Carlota; court life; trial | PER-MAXIMILIAN; PER-CARLOTA; EVT-SECOND-MEXICAN-EMPIRE | yes | 3 | high | build bias profile before using anecdotes |
| SRM_SHAWCROSS_0039 | NSI_SHAWCROSS_0039 | My Diary in Mexico in 1867 | Felix Salm-Salm | memoir_or_testimony | Participant diary/memoir around 1867 events | Self-defense, heroization, rescue-plot drama | Important for Querétaro, escape plans, execution aftermath | Action and siege scenes; motives/dialogue need checks | Basch; Blasio; Agnes Salm-Salm; court-martial sources; press | Felix Salm-Salm; Maximilian; Querétaro | PER-MAXIMILIAN; PLC-QUERETARO | yes | 2 | high | compare with witness cluster and trial records |
| SRM_SHAWCROSS_0040 | NSI_SHAWCROSS_0040 | Agnes Salm-Salm testimony/memoir references | Agnes Salm-Salm | memoir_or_testimony | Participant/witness account, later presentation | Language barrier, reconstructed dialogue, dramatic self-presentation | Strong scene value for mercy mission and prison/trial episodes | Dramatic scenes only with strict corroboration | Basch; Felix Salm-Salm; Blasio; Juárez-side records; press | Agnes Salm-Salm; Juárez; Maximilian; mercy diplomacy | PER-BENITO-JUAREZ; PER-MAXIMILIAN; PLC-QUERETARO | yes | 2 | high | do not literalize dialogue without corroboration |
| SRM_SHAWCROSS_0041 | NSI_SHAWCROSS_0041 | Castelnau correspondence in 400AP/61, Dossier 3 | Castelnau / French imperial mission | primary | Contemporary official French correspondence | Report to emperor; mission self-justification | Core evidence for French mission, abdication pressure, late orders | French command/policy chronology | 400AP broader file; AAE; FO; Basch/Blasio | Castelnau; Napoleon III; Bazaine; Maximilian | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 5 | high | exact dossier/pages |
| SRM_SHAWCROSS_0042 | NSI_SHAWCROSS_0042 | Scarlett / Stanley / Fischer correspondence, FO 50/397 | British diplomats and correspondents | primary | Contemporary British diplomatic reporting | British interests; incomplete access to internal imperial politics | External view of abdication crisis and late empire | Diplomatic cross-check; outside observer view | AAE; HHStA; 400AP; Mexican press | Scarlett; Stanley; Fischer; Maximilian | EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 5 | high | dates, recipients, and FO references |
| SRM_SHAWCROSS_0043 | NSI_SHAWCROSS_0043 | Herzfeld, Bazaine, Fischer, Gutiérrez de Estrada letters | Multiple letter writers | primary | Contemporary scattered letters | Scattered provenance; factional interests; copy status | Internal crisis traffic and court/faction signals | Crisis reconstruction after provenance check | HHStA; AAE; FO; Ratz; Mexican conservative sources | Herzfeld; Bazaine; Fischer; Maximilian; Gutiérrez de Estrada | PER-MAXIMILIAN; EVT-SECOND-MEXICAN-EMPIRE | yes | 4 | high | source location varies by note |
| SRM_SHAWCROSS_0044 | NSI_SHAWCROSS_0044 | Page 109 cited sources not yet indexed | unknown | unclear | Unknown; missing notes_translation_0109 coverage | Source names and genres cannot be inferred | Placeholder preserves gap visibility | Do not use for claims; locate missing log/screenshot | Progress Master; source note; original notes image if available | French invasion; Mexican Crown; Maximilian; Napoleon III; Carlota | PER-MAXIMILIAN; PER-CARLOTA; PER-NAPOLEON-III | yes | 1 | high | `notes_translation_0109.md` not found |
| SRM_SHAWCROSS_0045 | NSI_SHAWCROSS_0045 | Antoine Forest-related correspondence, AAE CP Mexique 69 | Forest / French diplomacy | primary | Contemporary French trial-period diplomatic correspondence | Official self-protection around trial/execution | Core evidence for French stance during trial crisis | Trial diplomacy; French reaction to execution crisis | AAE broader file; FO; U.S. documents; Mexican press; Basch/Salm-Salm | Forest; French diplomacy; trial period | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | 5 | high | exact dates and folios |
| SRM_SHAWCROSS_0046 | NSI_SHAWCROSS_0046 | William Harris Chynoweth reference | William Harris Chynoweth, identity/title unclear | unclear | Unknown | Bibliographic identity not established; genre uncertain | Possible trial/execution source lead only | No claim use until identified | Shawcross note image; library catalogue; trial sources | Maximilian trial; Querétaro | PER-MAXIMILIAN; PLC-QUERETARO | yes | 1 | medium | identify title, date, genre |
| SRM_SHAWCROSS_0047 | NSI_SHAWCROSS_0047 | Le Mémorial diplomatique and French legislative material | French public-political sources | primary | Contemporary public diplomatic / legislative record | Rhetoric-heavy; public positioning; political theater | Useful for French public record and collapse-memory framing | Public diplomacy; aftermath; memory politics | AAE; French press; parliamentary records; Girard | French legislature; public diplomacy; intervention aftermath | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | yes | 4 | medium | titles, issue dates, accents |
| SRM_SHAWCROSS_0048 | NSI_SHAWCROSS_0048 | Napoleon III; The Habsburgs | Louis Girard; Martyn Rady | secondary | Modern synthesis / broader dynastic context | Synthesis-level; not Mexico-specific evidence for claims | Good epilogue and broad Napoleonic/Habsburg framing | Context and historiography only | Primary French/Habsburg records; Corti; HHStA | Napoleon III; Habsburgs; Franz Joseph; memory | PER-NAPOLEON-III; ORG-HABSBURG; PER-FRANZ-JOSEPH | no | 3 | low | no immediate primary-source task |

## 7. High-Priority Sources

High-priority rows are the sources to read or verify first because they bear directly on intervention policy, Carlota/Maximilian private politics, French withdrawal, Querétaro, the trial, execution, and post-imperial memory.

| Cluster | SRM IDs | Why It Matters |
|---|---|---|
| French official / diplomatic | SRM_SHAWCROSS_0001; 0002; 0008; 0031; 0041; 0045 | Establish French decisions, withdrawal pressure, Castelnau's mission, and trial-period diplomacy. |
| Habsburg / Maximilian-Carlota | SRM_SHAWCROSS_0004; 0013; 0016; 0017; 0019; 0020 | Core for dynastic negotiations, private letters, Carlota, Miramar, and imperial self-understanding. |
| British and U.S. official counterpoints | SRM_SHAWCROSS_0003; 0011; 0042 | Checks French/Habsburg narrative against external diplomacy and U.S. pressure. |
| Mexican political voices | SRM_SHAWCROSS_0006; 0023; 0024; 0027; 0028; 0029; 0033 | Needed to avoid a Maximilian/French-centered version of the conflict. |
| Final-month witness cluster | SRM_SHAWCROSS_0037; 0038; 0039; 0040 | Rich for scenes but risky for fact certification; must be read comparatively. |
| Unknown but blocking | SRM_SHAWCROSS_0044; 0046 | Bibliographic gaps affect Chapter 3-4 notes and trial/execution source mapping. |

## 8. Memoir / Testimony Cluster

### Cluster Members

| Source | SRM ID | Witness Position | Maximilian Distance | Carlota Distance | Main Risk |
|---|---|---|---|---|---|
| Basch | SRM_SHAWCROSS_0037 | close medical/personal witness in final months | very close | indirect to limited depending episode | loyalist proximity, retrospective framing |
| Blasio | SRM_SHAWCROSS_0038 | private secretary / court-adjacent account | close | close enough for court observations | role politics, anecdotal reconstruction |
| Felix Salm-Salm | SRM_SHAWCROSS_0039 | military participant, 1867 focus | close during final campaign | indirect | self-defense, heroization, rescue-plot drama |
| Agnes Salm-Salm | SRM_SHAWCROSS_0040 | participant in mercy diplomacy | close through intervention efforts | indirect | language barrier, dramatic reconstruction |

### Common Strengths

- Strong scene value for Querétaro, imprisonment, trial anxiety, failed rescue/mercy efforts, execution aftermath, interpersonal gestures, and rumor flow.
- Provide close-to-the-ground details absent from official dispatches.
- Useful for building contrasting witness voices around the same events.

### Cross-check Priorities

- Exact sequence of Querétaro siege and surrender.
- Maximilian's decisions, mood, and communications after capture.
- Escape plans and who supported or opposed them.
- Trial procedure, defense efforts, and access to prisoners.
- Mercy appeals to Juárez and republican authorities.
- Reported dialogue, gestures, and emotionally dramatic scenes.

### Expected Divergences

- Degree of Maximilian's agency versus coercion.
- Responsibility for failed escape or failed mercy diplomacy.
- Presentation of Juárez and republican officials.
- Role and competence of French officers, Mexican conservatives, and imperial loyalists.
- Later self-fashioning by witnesses for European or American readers.

### Fiction Use

- Good for atmosphere, fear, fatigue, loyalty, performance of courage, and intimate court/prison dynamics.
- Do not use single-witness dialogue or motive as settled fact.
- Mark scenes based on these accounts as witness-colored unless corroborated by official records, press, or independent testimony.

## 9. Diplomatic / Official Documents Cluster

| Subcluster | SRM IDs | Use | Caution |
|---|---|---|---|
| AAE / French Foreign Ministry | SRM_SHAWCROSS_0002; 0008; 0031; 0045 | French policy, withdrawal pressure, trial diplomacy | Official dispatches justify policy and protect officials. |
| 400AP / Fonds Napoleon | SRM_SHAWCROSS_0001; 0041 | Castelnau, French imperial command, late-stage orders | Court/mission files may shape blame and responsibility. |
| FO / British records | SRM_SHAWCROSS_0003; 0008; 0042 | External diplomatic view; useful check on French documents | British interests and incomplete access affect reporting. |
| HHStA / Habsburg records | SRM_SHAWCROSS_0004; 0020 | Crown offer, family/dynastic politics, Maximilian/Carlota papers | Dynastic perspective can normalize imperial assumptions. |
| U.S. official documents | SRM_SHAWCROSS_0011 | U.S. pressure, Monroe Doctrine, republican legitimacy | Domestic U.S. politics and printed-document selection matter. |

Official documents can support chronology and institutional positions, but they do not automatically establish intent, popular opinion, private motive, or moral meaning.

## 10. Press and Public Opinion Sources

Primary press sources are grouped in SRM_SHAWCROSS_0023, with French public-political material in SRM_SHAWCROSS_0047.

- Use for rumor timing, propaganda, public mood, rhetoric, legitimacy claims, and how events were framed for different audiences.
- Separate Mexican conservative press, Mexican liberal/republican press, French imperial press, British press, Belgian/Catholic press, and U.S. illustrated/popular press.
- Do not treat press reports as neutral event certification without date, issue, article title, political alignment, and independent corroboration.
- Press is especially useful for novel scenes involving public anxiety, ceremonies, expectation, war news, and memory formation after collapse.

## 11. Secondary Scholarship Cluster

| SRM IDs | Source Group | Use | Caution |
|---|---|---|---|
| SRM_SHAWCROSS_0010; 0021; 0025; 0026; 0034; 0048 | Modern or later scholarly/contextual works | Orientation, historiography, source leads, chronology scaffolding | Do not convert their summaries into Fact Cards without checking cited primary evidence where possible. |
| SRM_SHAWCROSS_0013 | Corti | Especially useful source map for letters and court narrative | High narrative influence; verify original letters and archive basis. |
| SRM_SHAWCROSS_0024; 0027 | Vigil and Zamacois | Mexican liberal/republican and conservative narrative counterweights | Both carry memory-politics and partisan framing. |

## 12. Archive / Collection Access Notes

| Archive / Collection | SRM IDs | Next Check |
|---|---|---|
| Archives nationales, Fonds Napoleon, 400AP/61-63 | SRM_SHAWCROSS_0001; 0041 | identify dossier, folio/page, sender, recipient, date, and whether Shawcross cites originals or edited references. |
| AAE, CP Mexique | SRM_SHAWCROSS_0002; 0008; 0031; 0045 | build a sender-recipient-date table for Saligny, Thouvenel, Dano, Drouyn de Lhuys, Forest, and trial-period items. |
| FO, National Archives | SRM_SHAWCROSS_0003; 0008; 0042 | verify FO series/volume and dispatch dates; compare with French and Mexican accounts. |
| HHStA, Archiv Kaiser Maximilian von Mexiko | SRM_SHAWCROSS_0004; 0020 | distinguish originals, copies, extracts, and edited retransmissions in Ratz/Corti. |

## 13. Cross-reference to Existing IDs

Verified existing IDs carried forward from the source index and local entity/event/theme checks:

- People: `PER-MAXIMILIAN`, `PER-CARLOTA`, `PER-BENITO-JUAREZ`, `PER-NAPOLEON-III`, `PER-FRANZ-JOSEPH`
- Organizations: `ORG-HABSBURG`, `ORG-MEXICAN-CONSERVATIVES`, `ORG-MEXICAN-REPUBLICANS`, `ORG-CATHOLIC-CHURCH`
- Events: `EVT-FRENCH-INTERVENTION-IN-MEXICO`, `EVT-SECOND-MEXICAN-EMPIRE`
- Places: `PLC-MIRAMAR`, `PLC-QUERETARO`
- Themes: `THM-FOREIGN-INTERVENTION`, `THM-LEGITIMACY`, `THM-LIBERAL-REFORM`
- Source note: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`

Fact/Timeline IDs are intentionally not assigned at SRM row level. Known gap ranges in [[Shawcross_ID_Audit]] must be checked before any future Fact/Timeline linking.

## 14. Novel Use Notes

- Historical claim base: start with AAE, FO, HHStA, 400AP, U.S. official documents, and item-level letters. Use press and memoirs only after corroboration.
- Scene description: Basch, Blasio, Felix Salm-Salm, Agnes Salm-Salm, military memoirs, and press are high-value for atmosphere, gestures, fear, rumor, and dramatic pacing.
- Character psychology: private correspondence collections are stronger than memoirs, but edited letters still require editorial checks.
- Court and family scenes: Ratz, Foussemagne, Weckmann, HHStA, and Corti can support Maximilian/Carlota/Habsburg angles, but this cluster naturally pulls the narrative toward dynastic self-understanding.
- Republican/Juárez side: Vigil, U.S. official documents, Mexican press, and Mexican documentary collections are necessary counterweights but remain underdeveloped in the current NSI set.
- Conservative Mexican side: Gutiérrez de Estrada, Arrangoiz, Zamacois, Lombardo de Miramón, and Mexican conservative press can explain monarchist motives, but they are partisan sources.
- Maximilian-centered caution: Shawcross's notes strongly surface Maximilian/Carlota/Habsburg/French and loyal-witness materials. The matrix should therefore trigger deliberate checks against republican, liberal, Mexican popular, regional, and military-opposition sources before treating motives or legitimacy claims as settled.

## 15. Unresolved / Manual Review Needed

Carried forward from [[Shawcross_ID_Audit]] and [[Shawcross_Notes_Source_Index]]. These are not repaired or normalized in this workflow.

- `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096`: file-absent; no speculative Capture files created.
- `FACT_MEXEMP_2561-2608`: generation-gap suspected; not treated as existing IDs.
- `TIME_MEXEMP_0423-0448`: generation-gap suspected; not treated as existing IDs.
- `FACT_MEXEMP_2439-2513`: generation-gap/manual-review range from trial section captures.
- `TIME_MEXEMP_0387-0413`: generation-gap/manual-review range from trial section captures.
- `TIME_MEXEMP_0413`: boundary review between `CAP_MEXEMP_0101` and `CAP_MEXEMP_0102`; not linked as existing.
- `SRC_UNSET_001`: remains on `CAP_MEXEMP_0001`, `FACT_MEXEMP_0001-0006`, and `TIME_MEXEMP_0001-0002`; no rewrite here.
- `FACT_MEXEMP_0489 -> FACT_MEXEMP_0431`: unresolved existing-card-to-nonexistent-ID reference; not repaired here.
- `FACT_MEXEMP_0638 -> FACT_MEXEMP_0439`: unresolved existing-card-to-nonexistent-ID reference; not repaired here.
- `TIME_MEXEMP_0196 -> TIME_MEXEMP_0192`: unresolved existing-card-to-nonexistent-ID reference; not repaired here.
- `notes_translation_0109.md` not found. Page 109 NOTES range is registered in [[Shawcross_Progress_Master]], but source names remain unresolved in SRM_SHAWCROSS_0044.
- 114-page bibliographic checks remain: Chapter 10 n.3 Spanish long title; Chapter 10 n.11 Corti publication-place formatting; EPILOGUE n.3 `Supplement/Supplément au Journal des débats`.

## 16. Work Log

- 2026-06-13: Confirmed no separate existing `Shawcross_Source_Reliability_Matrix.md` or same-purpose SRM file was present. Created this single aggregated matrix.
- 2026-06-13: Converted `NSI_SHAWCROSS_0001-0048` into `SRM_SHAWCROSS_0001-0048`.
- 2026-06-13: Added cluster notes for memoir/testimony, diplomatic/official documents, press/public opinion, secondary scholarship, and archive access.
- 2026-06-13: Carried forward ID audit unresolved items without fixing, renumbering, deleting, or filling gaps.
- 2026-06-13: No Shawcross body text, NOTES full text, screenshot full transcription, long quotation, Fact Card, Timeline Entry, or individual SRM/NSI/source Markdown file was created.

## 17. Matrix Stats

| Metric | Count |
|---|---:|
| SRM rows | 48 |
| NSI rows covered | 48 |
| primary | 13 |
| quasi_primary | 8 |
| memoir_or_testimony | 12 |
| secondary | 9 |
| reference | 0 |
| archive_or_collection | 4 |
| unclear | 2 |
| verification_needed yes | 40 |
| verification_needed no | 8 |
| reliability_score 5 | 11 |
| reliability_score 4 | 11 |
| reliability_score 3 | 16 |
| reliability_score 2 | 8 |
| reliability_score 1 | 2 |
| priority high | 27 |
| priority medium | 20 |
| priority low | 1 |
