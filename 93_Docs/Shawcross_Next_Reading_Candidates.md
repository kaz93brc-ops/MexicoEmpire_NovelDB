---
id: SHAWCROSS_NEXT_READING_CANDIDATES
type: next_reading_candidates
status: active
created: 2026-06-13
updated: 2026-06-13
tags:
  - shawcross
  - next-reading
  - source-planning
  - mexemp
source_id: SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO
nsi_range: NSI_SHAWCROSS_0001-0048
srm_range: SRM_SHAWCROSS_0001-0048
nrc_range: NRC_SHAWCROSS_0001-0048
---

# Shawcross Next Reading Candidates

## 1. Purpose

This file converts [[Shawcross_Source_Reliability_Matrix]] into a next-reading plan for the Mexico Empire novel database.

- It ranks what to read next after Edward Shawcross, *The Last Emperor of Mexico*.
- It separates historical verification value from novel-scene value.
- It treats Basch / Blasio / Felix Salm-Salm / Agnes Salm-Salm as a controlled witness cluster.
- It keeps the Maximilian / Habsburg / French / loyal-witness pull visible.
- It preserves the need for a later Juárez / republican-side source reinforcement workflow.

This file does not create Fact Cards, Timeline Entries, entity cards, source-specific Markdown files, or quotation archives.

## 2. Scope

| Item | Value |
|---|---|
| Input NSI range | `NSI_SHAWCROSS_0001-0048` |
| Input SRM range | `SRM_SHAWCROSS_0001-0048` |
| Output NRC range | `NRC_SHAWCROSS_0001-0048` |
| Coverage | 48/48 SRM rows converted into NRC rows |
| Treatment | reading plan only |
| Same-purpose existing file | not found before creation |

## 3. Inputs

Confirmed before this file was created:

- [[Shawcross_Progress_Master]]
- [[Shawcross_ID_Audit]]
- [[Shawcross_Notes_Source_Index]]
- [[Shawcross_Source_Reliability_Matrix]]
- [[SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO]]
- Shawcross-related Capture / Fact / Timeline counts from local files: 103 Shawcross Capture files, 2034 Shawcross Fact files, 321 Shawcross Timeline files.
- Existing entity/event/place/theme IDs verified from local files: `PER-MAXIMILIAN`, `PER-CARLOTA`, `PER-BENITO-JUAREZ`, `PER-NAPOLEON-III`, `PER-FRANZ-JOSEPH`, `ORG-HABSBURG`, `ORG-MEXICAN-CONSERVATIVES`, `ORG-MEXICAN-REPUBLICANS`, `ORG-CATHOLIC-CHURCH`, `EVT-FRENCH-INTERVENTION-IN-MEXICO`, `EVT-SECOND-MEXICAN-EMPIRE`, `PLC-MIRAMAR`, `PLC-QUERETARO`, `THM-FOREIGN-INTERVENTION`, `THM-LEGITIMACY`, `THM-LIBERAL-REFORM`.
- Representative late-trial / epilogue cards checked for context: `CAP_MEXEMP_0097`, `CAP_MEXEMP_0098`, `CAP_MEXEMP_0102`, `CAP_MEXEMP_0104`, `FACT_MEXEMP_2390`, `FACT_MEXEMP_2419`, `FACT_MEXEMP_2514`, `FACT_MEXEMP_2560`, `TIME_MEXEMP_0379`, `TIME_MEXEMP_0383`, `TIME_MEXEMP_0414`, `TIME_MEXEMP_0422`.

## 4. Method

- One NRC row is assigned to each SRM row.
- `reading_priority` is not identical to SRM `priority`. It describes reading order for the next research cycle.
- Memoir/testimony sources receive separate use notes for scene writing and historical verification.
- Official and diplomatic sources are treated as chronology and institutional-position checks, not direct evidence of private motive or popular feeling.
- Press sources are treated as public opinion / propaganda / rumor material.
- Existing IDs are included only where local files or prior NSI/SRM verification confirm them.
- Known missing or suspected IDs are carried forward as manual review dependencies, not used as existing IDs.

## 5. Reading Priority Scale

| Priority | Meaning |
|---|---|
| first | Read first for core reconstruction of French withdrawal, Querétaro, trial/execution, Maximilian/Carlota correspondence, and witness-cluster comparison. |
| second | Read after the first set to strengthen cross-checks, Mexican-side counterweights, edited correspondence, and political context. |
| third | Read for scene texture, historiographical orientation, public rhetoric, or secondary support after core checks. |
| later | Hold until bibliographic identity, access need, or relevance is clearer. |

## 6. Next Reading Candidate Table

| NRC ID | SRM ID | NSI ID | Source / Author | Source Type | Reading Priority | Reading Purpose | Key Questions | Related Focus | Cross-check With | Novel Use | Reliability Caution / Bias | Existing IDs | Verification Needed | Manual Review | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NRC_SHAWCROSS_0001 | SRM_SHAWCROSS_0001 | NSI_SHAWCROSS_0001 | 400AP/61-63, Archives nationales, Fonds Napoleon / French imperial archive | archive_or_collection | first | Diplomatic and military chronology; abdication and siege evidence | What did Castelnau and French command report about withdrawal, orders, blame, and late imperial policy? | People: Napoleon III, Castelnau, Bazaine, Maximilian; Events: French intervention, Querétaro; Places: Querétaro; Themes: foreign intervention | AAE; FO; HHStA; Basch; Blasio; Salm-Salm; Mexican press | French command-room pressure and collapse atmosphere | French imperial archive may preserve self-protective or selective files | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO; THM-FOREIGN-INTERVENTION | yes | folio and dossier references needed | Build dossier/folio list and link to Castelnau sequence |
| NRC_SHAWCROSS_0002 | SRM_SHAWCROSS_0002 | NSI_SHAWCROSS_0002 | AAE, CP Mexique / French Foreign Ministry | archive_or_collection | first | French diplomatic chronology; withdrawal and trial-period diplomacy | How did Paris frame support, withdrawal, responsibility, and the trial crisis? | People: Saligny, Dano, Drouyn de Lhuys, Forest, Napoleon III; Events: French intervention, trial crisis; Themes: foreign intervention | FO; HHStA; 400AP; U.S. official documents; Mexican press | Diplomatic pressure scenes and bureaucratic tone | Official dispatches may defend French policy and protect officials | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | volume, folio, sender, recipient, date list needed | Create AAE sender-recipient-date table |
| NRC_SHAWCROSS_0003 | SRM_SHAWCROSS_0003 | NSI_SHAWCROSS_0003 | FO, National Archives, London / British Foreign Office | archive_or_collection | first | External diplomatic counterpoint to French and Mexican accounts | What did British observers report about French motives, abdication pressure, and late crisis? | People: Wyke, Russell, Scarlett, Stanley, Fischer; Events: French intervention, abdication crisis; Themes: foreign intervention | AAE; U.S. documents; Mexican press; HHStA | Outside-observer diplomatic texture | British interests and limited access may shape reports | EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | FO series and dispatch dates needed | Verify FO volumes and dispatch chronology |
| NRC_SHAWCROSS_0004 | SRM_SHAWCROSS_0004 | NSI_SHAWCROSS_0004 | HHStA, Archiv Kaiser Maximilian von Mexiko / Habsburg archive | archive_or_collection | first | Habsburg correspondence, crown-offer negotiations, family pressure | What do dynastic papers show about Maximilian's commitment, Carlota, Franz Joseph, and Miramar? | People: Maximilian, Carlota, Franz Joseph; Event: Second Mexican Empire; Place: Miramar; Themes: legitimacy, foreign intervention | Ratz; Foussemagne; Weckmann; AAE; FO | Court and family scenes; dynastic stakes | Strong Habsburg viewpoint may normalize imperial assumptions | PER-MAXIMILIAN; PER-CARLOTA; PER-FRANZ-JOSEPH; ORG-HABSBURG; PLC-MIRAMAR | yes | series and item-level confirmation needed | Map originals, copies, extracts, and edited reprints |
| NRC_SHAWCROSS_0005 | SRM_SHAWCROSS_0005 | NSI_SHAWCROSS_0005 | Daniel Harvey Hill diary edition / Daniel Harvey Hill and editor | quasi_primary | later | U.S.-Mexico War memory background | Does the diary illuminate U.S. military memory relevant to later Mexico policy? | People: U.S. military actors; Themes: foreign intervention | U.S. official documents; later U.S. diplomacy; Mexican accounts | Background atmosphere only | Edited diary; distant from core empire events | THM-FOREIGN-INTERVENTION | yes | original diary context and editor policy | Defer unless U.S. war-memory scene is needed |
| NRC_SHAWCROSS_0006 | SRM_SHAWCROSS_0006 | NSI_SHAWCROSS_0006 | Gutiérrez de Estrada pamphlet and letters / José María Gutiérrez de Estrada | primary | second | Conservative monarchy project and legitimacy claims | How did conservative monarchists justify a foreign prince and define Mexican consent? | People: Gutiérrez de Estrada, Maximilian; Event: Second Mexican Empire; Themes: legitimacy | Vigil; Zamacois; Arrangoiz; HHStA; French diplomacy | Conservative ideological voice and court-persuasion scenes | Programmatic monarchist advocacy; not neutral Mexican opinion | ORG-MEXICAN-CONSERVATIVES; THM-LEGITIMACY; EVT-SECOND-MEXICAN-EMPIRE | yes | title, date, and letter locations | Read with Vigil/Arrangoiz comparison |
| NRC_SHAWCROSS_0007 | SRM_SHAWCROSS_0007 | NSI_SHAWCROSS_0007 | *Life in Mexico* / Frances Calderón de la Barca | memoir_or_testimony | third | Pre-intervention social texture | Which elite-observer details help render Mexican society without overgeneralizing? | People: Mexican elite society; Themes: legitimacy | Mexican press; Mexican memoirs; modern social history | Social atmosphere and outsider perception | Foreign elite, classed, and gendered filter; not empire-period evidence alone | THM-LEGITIMACY | yes | edition and passage context | Use only for background texture |
| NRC_SHAWCROSS_0008 | SRM_SHAWCROSS_0008 | NSI_SHAWCROSS_0008 | Wyke/Russell and Saligny/Thouvenel dispatch clusters / British and French diplomats | primary | first | Debt-crisis and intervention-motive comparison | Where do British and French motives diverge before intervention? | People: Wyke, Russell, Saligny, Thouvenel; Event: French intervention; Themes: foreign intervention | FO originals; AAE originals; U.S. documents; Mexican government records | Diplomatic disagreement and policy misunderstanding | Strategic diplomatic language; national-interest framing | EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | separate FO and AAE citations | Split into FO and AAE sublists by date |
| NRC_SHAWCROSS_0009 | SRM_SHAWCROSS_0009 | NSI_SHAWCROSS_0009 | *Memorias* / Concepción Lombardo de Miramón | memoir_or_testimony | third | Conservative household and faction memory | How does Miramón's circle remember empire, defeat, and honor? | People: Miramón, Carlota, Maximilian; Org: Mexican Conservatives | Arrangoiz; Zamacois; Vigil; official records | Conservative family voice and emotional stakes | Family honor and retrospective self-defense likely | ORG-MEXICAN-CONSERVATIVES | yes | edition and chapter reference | Read after core conservative sources |
| NRC_SHAWCROSS_0010 | SRM_SHAWCROSS_0010 | NSI_SHAWCROSS_0010 | Second Empire political context works / multiple secondary authors | secondary | third | Bonapartist and French Second Empire context | Which interpretive frame explains Napoleon III's Mexico imagination? | People: Napoleon III; Theme: foreign intervention | Primary pamphlets; AAE; French public records | Ideological framing for French scenes | Secondary interpretation may privilege French imperial frame | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | no | split works later if used heavily | Use as orientation only |
| NRC_SHAWCROSS_0011 | SRM_SHAWCROSS_0011 | NSI_SHAWCROSS_0011 | U.S. presidential and congressional documents / U.S. executive and Congress | primary | first | U.S. pressure, Monroe Doctrine, republican legitimacy | What official U.S. pressure affected French withdrawal and Juárez recognition? | People: Buchanan, Andrew Johnson, U.S. Congress, Juárez; Org: Mexican Republicans; Theme: foreign intervention | FO; AAE; Mexican republican records; Schofield | U.S. diplomatic pressure and post-Civil War atmosphere | Domestic U.S. politics and printed-document selection matter | THM-FOREIGN-INTERVENTION; ORG-MEXICAN-REPUBLICANS | yes | exact document titles and pages | Build U.S. document checklist |
| NRC_SHAWCROSS_0012 | SRM_SHAWCROSS_0012 | NSI_SHAWCROSS_0012 | Michel Chevalier and Charles du Pin texts / Chevalier; du Pin | primary | second | French policy ideology and imperial rhetoric | How was Mexico imagined as economic, racial, or geopolitical project? | People: Napoleon III; Theme: foreign intervention | AAE; French press; Mexican liberal replies | Ideological rhetoric and propaganda texture | Interventionist and imperial economic bias | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | yes | title and publication context | Read after AAE chronology is stable |
| NRC_SHAWCROSS_0013 | SRM_SHAWCROSS_0013 | NSI_SHAWCROSS_0013 | *Maximilian and Charlotte of Mexico* / Egon Caesar Corti | secondary | second | Gateway to letters and court narrative | Which quoted letters or anecdotes must be checked against originals? | People: Maximilian, Carlota; Org: Habsburg; Events: trial and epilogue | HHStA; Ratz; Foussemagne; Weckmann; primary letters | Court narrative scaffolding | Strong narrative influence; one step away from letters | PER-MAXIMILIAN; PER-CARLOTA; ORG-HABSBURG | yes | verify originals behind quotations | Use as finding aid, not final authority |
| NRC_SHAWCROSS_0014 | SRM_SHAWCROSS_0014 | NSI_SHAWCROSS_0014 | Kendall and Sara Yorke Stevenson reminiscences / Kendall; Stevenson | memoir_or_testimony | third | Foreign witness texture and anecdotal court material | Which anecdotes are corroborated and which are social memory? | People: Maximilian; Event: French intervention | Court records; press; Basch/Blasio where relevant | Social and court atmosphere | Retrospective reminiscence; witness-position limits | PER-MAXIMILIAN; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | distinguish Kendall and Stevenson | Defer to scene-texture stage |
| NRC_SHAWCROSS_0015 | SRM_SHAWCROSS_0015 | NSI_SHAWCROSS_0015 | *Recollections of My Life* / Maximilian | memoir_or_testimony | second | Maximilian's self-image, ideals, and voice before Mexico | How does Maximilian fashion himself as liberal, dynastic, adventurous, or providential? | People: Maximilian; Org: Habsburg; Themes: legitimacy | HHStA letters; Ratz; Carlota letters; hostile accounts | Character voice and internal monologue reference | Self-fashioning; not neutral factual evidence | PER-MAXIMILIAN; ORG-HABSBURG | yes | original edition and translation | Read for voice after official chronology |
| NRC_SHAWCROSS_0016 | SRM_SHAWCROSS_0016 | NSI_SHAWCROSS_0016 | *Correspondencia inédita entre Maximiliano y Carlota* / Konrad Ratz, editor | quasi_primary | first | Maximilian-Carlota private correspondence and crisis | What do letters show about commitment, separation, political confidence, and anxiety? | People: Maximilian, Carlota; Place: Miramar; Themes: legitimacy | HHStA originals; Weckmann; Foussemagne; Corti | Intimate correspondence and emotional arc | Edited/translated collection; omissions and editorial policy need checking | PER-MAXIMILIAN; PER-CARLOTA; PLC-MIRAMAR | yes | editorial method and original-location check | Read early with HHStA map |
| NRC_SHAWCROSS_0017 | SRM_SHAWCROSS_0017 | NSI_SHAWCROSS_0017 | *Charlotte de Belgique* / Foussemagne | quasi_primary | second | Carlota and Belgian court correspondence | How does Belgian/dynastic framing shape Carlota's political role and later memory? | People: Carlota, Marie-Amélie; Org: Habsburg; Place: Miramar | Ratz; Weckmann; HHStA; Belgian records | Carlota scenes and European family pressure | Possible pro-Carlota or dynastic framing | PER-CARLOTA; PLC-MIRAMAR; ORG-HABSBURG | yes | letter dates and editorial policy | Compare with Ratz and Weckmann |
| NRC_SHAWCROSS_0018 | SRM_SHAWCROSS_0018 | NSI_SHAWCROSS_0018 | *Letters of Queen Victoria* / Queen Victoria and editors | quasi_primary | third | Royal/dynastic perception of marriage and politics | How did British/Belgian court observers frame Carlota and Maximilian? | People: Queen Victoria, Leopold, Carlota; Org: Habsburg | Foussemagne; Weckmann; HHStA; British FO | Court-world texture | Edited royal correspondence; decorum and pruning | PER-CARLOTA; ORG-HABSBURG | yes | volume and page check | Defer unless dynastic reception scenes need detail |
| NRC_SHAWCROSS_0019 | SRM_SHAWCROSS_0019 | NSI_SHAWCROSS_0019 | Carlota de Bélgica correspondence / Luis Weckmann, editor | quasi_primary | second | Carlota's Mexico-related writings and European archive trail | Which Carlota letters confirm agency, optimism, crisis, or retrospective memory? | People: Carlota, Leopold II; Org: Habsburg | Ratz; Foussemagne; HHStA; Belgian archive material | Carlota's voice and diplomatic/personal arc | Edited collection; scope and archive selection must be known | PER-CARLOTA; ORG-HABSBURG | yes | collection scope and archive basis | Read after Ratz, before Carlota-heavy scene drafting |
| NRC_SHAWCROSS_0020 | SRM_SHAWCROSS_0020 | NSI_SHAWCROSS_0020 | HHStA reports and Maximilian correspondence cluster / Maximilian, Metternich, Rechberg, Flahaut, Hidalgo, etc. | primary | first | Crown negotiations and French-Austrian traffic | How did Habsburg and French actors record the crown offer, guarantees, and doubts? | People: Maximilian, Franz Joseph, Metternich; Org: Habsburg; Theme: legitimacy | HHStA item originals; AAE; FO; Ratz | Miramar negotiations and family-state tension | Copy/extract status and court/state interests matter | PER-MAXIMILIAN; PER-FRANZ-JOSEPH; ORG-HABSBURG | yes | copy/extract versus original status | Build provenance checklist |
| NRC_SHAWCROSS_0021 | SRM_SHAWCROSS_0021 | NSI_SHAWCROSS_0021 | *Prelude to Tragedy* / Carl Bock | secondary | third | Tripartite Convention and early intervention orientation | Which primary records does Bock use for negotiation breakdown? | Event: French intervention | FO; AAE; U.S. documents; Mexican sources | Early-diplomacy scaffolding | Secondary framing depends on primary base | EVT-FRENCH-INTERVENTION-IN-MEXICO | no | identify primary basis | Use only as guide to primary checks |
| NRC_SHAWCROSS_0022 | SRM_SHAWCROSS_0022 | NSI_SHAWCROSS_0022 | French/imperial military memoir cluster / du Barail, Laurent, Kératry, Blanchot, Hans, Pitner, etc. | memoir_or_testimony | second | Military texture, troop movement, campaign atmosphere | Which military memories corroborate or contradict official French records and witness accounts? | People: French and imperial officers; Event: French intervention, Querétaro; Place: Querétaro | AAE; 400AP; Niox; Gaulot; FO; Mexican military accounts | Camp life, fatigue, fear, rumor, siege texture | Participant self-justification and blame allocation | EVT-FRENCH-INTERVENTION-IN-MEXICO; PLC-QUERETARO | yes | split by author in later reading | Split cluster into author checklist later, not individual files now |
| NRC_SHAWCROSS_0023 | SRM_SHAWCROSS_0023 | NSI_SHAWCROSS_0023 | Newspapers and periodicals / La Sociedad, El Siglo, Times, Journal des débats, Revue des deux mondes, Journal de Bruxelles, Mexican Times, Harper's Weekly | primary | second | Press, public opinion, propaganda, rumor | What issue/date/political line frames each report, and what was rumor vs reported fact? | Events: French intervention, Second Mexican Empire; Themes: legitimacy, foreign intervention | Official records; rival newspapers; memoirs | Crowd mood, city air, propaganda, ceremony, rumor flow | Press reports are positional and may reflect censorship or party line | EVT-FRENCH-INTERVENTION-IN-MEXICO; THM-LEGITIMACY | yes | issue dates, article titles, political alignment | Build issue/date/political-alignment table |
| NRC_SHAWCROSS_0024 | SRM_SHAWCROSS_0024 | NSI_SHAWCROSS_0024 | *México a través de los siglos* / José María Vigil | secondary | second | Liberal/republican historiographical counterweight | How does liberal national memory frame Juárez, empire, trial, and legitimacy? | People: Benito Juárez; Org: Mexican Republicans; Theme: liberal reform | Zamacois; Arrangoiz; Mexican official records; press | Republican-side narrative correction | Liberal national-history framing and memory politics | PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS; THM-LIBERAL-REFORM | no | volume and title confirmation | Read as counterweight, then identify republican primary sources |
| NRC_SHAWCROSS_0025 | SRM_SHAWCROSS_0025 | NSI_SHAWCROSS_0025 | *Expédition du Mexique* / Gustave Niox | secondary | third | French military chronology and document trail | Which operational details can be traced to primary reports? | People: French army, Randon, Lorencez; Event: French intervention | 400AP; AAE; military memoirs; Mexican accounts | Military sequence orientation | French institutional viewpoint | EVT-FRENCH-INTERVENTION-IN-MEXICO | no | quoted report source check | Use after 400AP/AAE outline |
| NRC_SHAWCROSS_0026 | SRM_SHAWCROSS_0026 | NSI_SHAWCROSS_0026 | Cunningham, Hamnett, Taladoire, Schoonover / modern secondary cluster | secondary | second | Modern research scaffolding; Juárez, U.S.-Mexico, counter-guerrillas | Which works lead to Juárez-side and U.S.-pressure primary records? | People: Napoleon III, Benito Juárez; Org: Mexican Republicans | Primary archives by topic; U.S. documents; Mexican records | Context map for later republican-side workflow | Secondary synthesis may hide source disputes | PER-NAPOLEON-III; PER-BENITO-JUAREZ; ORG-MEXICAN-REPUBLICANS | no | assign by topic if cited later | Use Hamnett as bridge into Juárez-side reinforcement |
| NRC_SHAWCROSS_0027 | SRM_SHAWCROSS_0027 | NSI_SHAWCROSS_0027 | *Historia de Méjico* / Niceto de Zamacois | secondary | second | Conservative-leaning Mexican narrative and memory | Where does Zamacois support, resist, or reshape the Maximilian-centered story? | Event: Second Mexican Empire; Org: Mexican Conservatives | Vigil; Arrangoiz; Mexican press; official records | Conservative memory and Mexican narrative breadth | Conservative-leaning or anti-liberal framing likely | EVT-SECOND-MEXICAN-EMPIRE; ORG-MEXICAN-CONSERVATIVES | no | title/spelling and volume verification | Read against Vigil and Arrangoiz |
| NRC_SHAWCROSS_0028 | SRM_SHAWCROSS_0028 | NSI_SHAWCROSS_0028 | *Méjico desde 1808 hasta 1867* / Arrangoiz y Berzábal | memoir_or_testimony | second | Conservative participant interpretation | How does a conservative participant defend monarchy and explain collapse? | Org: Mexican Conservatives; Theme: legitimacy | Vigil; Zamacois; Gutiérrez de Estrada; Mexican official records | Conservative motive, resentment, and faction interior | Partisan retrospective self-defense | ORG-MEXICAN-CONSERVATIVES; THM-LEGITIMACY | yes | publication details and bias profile | Pair with Vigil and Gutiérrez de Estrada |
| NRC_SHAWCROSS_0029 | SRM_SHAWCROSS_0029 | NSI_SHAWCROSS_0029 | *Correspondencias contemporáneas* / Romero de Terreros, editor/source | quasi_primary | second | Contemporary correspondence and Mexico City reactions | Which letters are contemporary, who wrote them, and what political world do they reveal? | Event: Second Mexican Empire; Place: Mexico City | Press; official records; Vigil; Zamacois | Elite correspondence and urban political atmosphere | Edited selection; editorial framing unknown | EVT-SECOND-MEXICAN-EMPIRE | yes | exact letter and publication data | Identify correspondents, dates, and editorial basis |
| NRC_SHAWCROSS_0030 | SRM_SHAWCROSS_0030 | NSI_SHAWCROSS_0030 | *Syllabus of Errors* / Pius IX and Catholic Church | primary | later | Church-state ideological background | Does this help explain church conflict, or can it wait for Mexico-specific church records? | Org: Catholic Church; Theme: liberal reform | Mexican church documents; Maximilian decrees; liberal sources | Background to religious conflict | Not Mexico-specific by itself | ORG-CATHOLIC-CHURCH; THM-LIBERAL-REFORM | yes | official text preferred | Defer until church-state chapter planning |
| NRC_SHAWCROSS_0031 | SRM_SHAWCROSS_0031 | NSI_SHAWCROSS_0031 | Dano / Drouyn de Lhuys diplomatic letters / French Foreign Ministry actors | primary | first | French policy shift and pressure on Maximilian | How did French officials pressure Maximilian and justify withdrawal? | People: Dano, Drouyn de Lhuys, Maximilian, Napoleon III; Event: French intervention | AAE originals; 400AP; HHStA; FO | Withdrawal-pressure dialogue and official tone | Strategic official language | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | AAE volume 66-67 checks | Prioritize with NRC 0002 |
| NRC_SHAWCROSS_0032 | SRM_SHAWCROSS_0032 | NSI_SHAWCROSS_0032 | *Lettres* / Brincourt | quasi_primary | third | Supplemental French-side evidence | Who wrote to whom, and does the edited letter add distinct operational evidence? | Event: French intervention | AAE; 400AP; military memoirs; Niox | Supplemental French-side voice | Authorship, addressee, and editorial omissions unclear | EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | incomplete note details | Defer until French-side gaps are known |
| NRC_SHAWCROSS_0033 | SRM_SHAWCROSS_0033 | NSI_SHAWCROSS_0033 | *Documentos inéditos o muy raros* / García and Pereyra, editors | quasi_primary | second | Mexican documentary source leads | Which Mexican documents can counterbalance French/Habsburg testimony? | Event: Second Mexican Empire; Themes: legitimacy, liberal reform | Original documents; Mexican archives; Vigil; press | Source leads for Mexican-side scenes | Editorial criteria and authenticity need review | EVT-SECOND-MEXICAN-EMPIRE | yes | exact volume/document | Use in republican-side reinforcement workflow |
| NRC_SHAWCROSS_0034 | SRM_SHAWCROSS_0034 | NSI_SHAWCROSS_0034 | *L'Expédition du Mexique* / Paul Gaulot | secondary | third | French narrative bridge for military/diplomatic episodes | Which primary references underlie Gaulot's siege and Castelnau narrative? | Event: French intervention; Place: Querétaro | AAE; 400AP; Niox; military memoirs | Narrative orientation for French scenes | Later French retrospective framing | EVT-FRENCH-INTERVENTION-IN-MEXICO; PLC-QUERETARO | no | primary references behind narrative | Read after official French records |
| NRC_SHAWCROSS_0035 | SRM_SHAWCROSS_0035 | NSI_SHAWCROSS_0035 | *Forty-Six Years in the Army* / John M. Schofield | memoir_or_testimony | second | U.S. military perspective on French withdrawal pressure | How does Schofield's memoir compare with official U.S. documents? | People: U.S. army; Theme: foreign intervention | U.S. official documents; Johnson papers; Mexican republican accounts | U.S. pressure scenes and postwar confidence | Retrospective self-positioning likely | THM-FOREIGN-INTERVENTION | yes | compare with official documents | Read after NRC 0011 |
| NRC_SHAWCROSS_0036 | SRM_SHAWCROSS_0036 | NSI_SHAWCROSS_0036 | *Twixt Old Times and New* / Carl von Malortie | memoir_or_testimony | later | European court/military atmosphere | Is the witness identity and context useful enough for court atmosphere? | People: Maximilian; Org: Habsburg | HHStA; court letters; other memoirs | Late-imperial background color | Identity/context unclear; retrospective court nostalgia | PER-MAXIMILIAN; ORG-HABSBURG | yes | identity and context check | Defer until court-atmosphere gaps remain |
| NRC_SHAWCROSS_0037 | SRM_SHAWCROSS_0037 | NSI_SHAWCROSS_0037 | *Memories of Mexico* / Samuel Basch | memoir_or_testimony | first | Close witness to final months, Querétaro, trial, execution atmosphere | What can Basch confirm about Maximilian's body, mood, decisions, captivity, and final conduct? | People: Basch, Maximilian; Event: trial/execution crisis; Place: Querétaro | Blasio; Felix Salm-Salm; Agnes Salm-Salm; trial records; AAE/FO; press | Medical/intimate detail, prison texture, final-month gestures | Loyal close witness; retrospective framing; possible honor defense | PER-MAXIMILIAN; PLC-QUERETARO | yes | prioritize witness-cluster comparison | Read first within witness cluster |
| NRC_SHAWCROSS_0038 | SRM_SHAWCROSS_0038 | NSI_SHAWCROSS_0038 | José Luis Blasio memoirs / private secretary account | memoir_or_testimony | first | Court life, Carlota observations, private secretary viewpoint, trial context | Which court anecdotes are corroborated, and how close was Blasio to each episode? | People: Blasio, Maximilian, Carlota; Event: Second Mexican Empire, trial | Basch; Salm-Salm; Ratz; Foussemagne; official court documents | Court interiors, interpersonal scenes, private atmosphere | Role politics and anecdotal reconstruction need profiling | PER-MAXIMILIAN; PER-CARLOTA; EVT-SECOND-MEXICAN-EMPIRE | yes | build bias profile before using anecdotes | Read second within witness cluster |
| NRC_SHAWCROSS_0039 | SRM_SHAWCROSS_0039 | NSI_SHAWCROSS_0039 | *My Diary in Mexico in 1867* / Felix Salm-Salm | memoir_or_testimony | first | Querétaro action, escape plans, execution aftermath | What does Felix claim about agency, rescue plans, military conduct, and responsibility? | People: Felix Salm-Salm, Maximilian; Place: Querétaro; Events: siege, trial, execution | Basch; Blasio; Agnes Salm-Salm; court-martial sources; press | Siege action and failed-escape drama | Self-defense, heroization, rescue-plot dramatization | PER-MAXIMILIAN; PLC-QUERETARO | yes | compare with witness cluster and trial records | Read third within witness cluster |
| NRC_SHAWCROSS_0040 | SRM_SHAWCROSS_0040 | NSI_SHAWCROSS_0040 | Agnes Salm-Salm testimony/memoir references / Agnes Salm-Salm | memoir_or_testimony | first | Mercy diplomacy, prison/trial scenes, Juárez contact | What actually happened in mercy appeals, and how much is reconstructed for readers? | People: Agnes Salm-Salm, Juárez, Maximilian; Place: Querétaro; Theme: legitimacy | Basch; Felix Salm-Salm; Blasio; Juárez-side records; press | High drama, mercy mission, emotional scenes | Language barrier, reconstructed dialogue, dramatic self-presentation | PER-BENITO-JUAREZ; PER-MAXIMILIAN; PLC-QUERETARO | yes | do not literalize dialogue without corroboration | Read fourth within witness cluster |
| NRC_SHAWCROSS_0041 | SRM_SHAWCROSS_0041 | NSI_SHAWCROSS_0041 | Castelnau correspondence in 400AP/61, Dossier 3 / Castelnau and French imperial mission | primary | first | French mission, abdication pressure, late orders | What were Castelnau's instructions and how did he explain his conduct? | People: Castelnau, Napoleon III, Bazaine, Maximilian; Event: French intervention | 400AP broader file; AAE; FO; Basch/Blasio | French mission and official blame tension | Report to emperor may justify mission conduct | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | exact dossier/pages | Read with NRC 0001 |
| NRC_SHAWCROSS_0042 | SRM_SHAWCROSS_0042 | NSI_SHAWCROSS_0042 | Scarlett / Stanley / Fischer correspondence, FO 50/397 / British diplomats and correspondents | primary | first | British external view of abdication crisis and late empire | What did external observers know, misunderstand, or relay as rumor? | People: Scarlett, Stanley, Fischer, Maximilian; Event: French intervention | AAE; HHStA; 400AP; Mexican press | Outsider perspective and rumor filtering | British interests and incomplete access | EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | dates, recipients, and FO references | Read with NRC 0003 |
| NRC_SHAWCROSS_0043 | SRM_SHAWCROSS_0043 | NSI_SHAWCROSS_0043 | Herzfeld, Bazaine, Fischer, Gutiérrez de Estrada letters / multiple writers | primary | first | Internal crisis traffic and court/faction signals | Which letters expose factional pressure, responsibility, and court fracture? | People: Herzfeld, Bazaine, Fischer, Maximilian, Gutiérrez de Estrada; Event: Second Mexican Empire | HHStA; AAE; FO; Ratz; Mexican conservative sources | Crisis communications and faction conflict | Scattered provenance, factional interests, copy status | PER-MAXIMILIAN; EVT-SECOND-MEXICAN-EMPIRE | yes | source location varies by note | Build provenance list before claim use |
| NRC_SHAWCROSS_0044 | SRM_SHAWCROSS_0044 | NSI_SHAWCROSS_0044 | Page 109 cited sources not yet indexed / unknown | unclear | later | Preserve source-index gap | Which source names are hidden by the missing `notes_translation_0109.md` log? | People: Maximilian, Carlota, Napoleon III; Events: French invasion, crown offer | Progress Master; source note; original notes image if available | None until identified | Source names and genres cannot be inferred | PER-MAXIMILIAN; PER-CARLOTA; PER-NAPOLEON-III | yes | `notes_translation_0109.md` not found | Locate missing log or image; do not infer sources |
| NRC_SHAWCROSS_0045 | SRM_SHAWCROSS_0045 | NSI_SHAWCROSS_0045 | Antoine Forest-related correspondence, AAE CP Mexique 69 / Forest and French diplomacy | primary | first | Trial-period French diplomatic evidence | How did French officials record or distance themselves from the trial/execution crisis? | People: Forest, Napoleon III; Event: trial/execution crisis; Theme: foreign intervention | AAE broader file; FO; U.S. documents; Mexican press; Basch/Salm-Salm | Trial diplomacy and official anxiety | Official self-protection around trial/execution | PER-NAPOLEON-III; EVT-FRENCH-INTERVENTION-IN-MEXICO | yes | exact dates and folios | Read with AAE trial-period set |
| NRC_SHAWCROSS_0046 | SRM_SHAWCROSS_0046 | NSI_SHAWCROSS_0046 | William Harris Chynoweth reference / identity and title unclear | unclear | later | Possible trial/execution source lead | What is this source's title, genre, date, and relation to trial records? | People: Maximilian; Place: Querétaro | Shawcross note image; library catalogue; trial sources | No scene use yet | Bibliographic identity not established | PER-MAXIMILIAN; PLC-QUERETARO | yes | identify title, date, genre | Bibliographic identification only |
| NRC_SHAWCROSS_0047 | SRM_SHAWCROSS_0047 | NSI_SHAWCROSS_0047 | Le Mémorial diplomatique and French legislative material / French public-political sources | primary | third | French public diplomacy and aftermath rhetoric | How was collapse publicly explained to French political audiences? | People: Napoleon III; Theme: foreign intervention | AAE; French press; parliamentary records; Girard | Aftermath rhetoric and public-political staging | Rhetoric-heavy public positioning | PER-NAPOLEON-III; THM-FOREIGN-INTERVENTION | yes | titles, issue dates, accents | Read after official French chronology |
| NRC_SHAWCROSS_0048 | SRM_SHAWCROSS_0048 | NSI_SHAWCROSS_0048 | *Napoleon III*; *The Habsburgs* / Louis Girard; Martyn Rady | secondary | later | Broad dynastic and Napoleonic epilogue framing | Which broad frames help epilogue without replacing primary evidence? | People: Napoleon III, Franz Joseph; Org: Habsburg | Primary French/Habsburg records; Corti; HHStA | Epilogue context only | Synthesis-level; not Mexico-specific claim evidence | PER-NAPOLEON-III; ORG-HABSBURG; PER-FRANZ-JOSEPH | no | no immediate primary-source task | Defer until epilogue framing pass |

## 7. First-Priority Reading Set

Recommended first-pass order:

1. `NRC_SHAWCROSS_0037` Basch.
2. `NRC_SHAWCROSS_0038` Blasio.
3. `NRC_SHAWCROSS_0039` Felix Salm-Salm.
4. `NRC_SHAWCROSS_0040` Agnes Salm-Salm.
5. `NRC_SHAWCROSS_0002`, `NRC_SHAWCROSS_0031`, `NRC_SHAWCROSS_0045` AAE / French diplomatic trial and withdrawal set.
6. `NRC_SHAWCROSS_0001`, `NRC_SHAWCROSS_0041` 400AP / Castelnau set.
7. `NRC_SHAWCROSS_0003`, `NRC_SHAWCROSS_0042` FO external diplomatic set.
8. `NRC_SHAWCROSS_0004`, `NRC_SHAWCROSS_0020`, `NRC_SHAWCROSS_0016` HHStA / Habsburg / Ratz correspondence set.
9. `NRC_SHAWCROSS_0011` U.S. official documents.
10. `NRC_SHAWCROSS_0008`, `NRC_SHAWCROSS_0043` mixed dispatch and internal crisis letters.

Rationale: begin with the final-month witness cluster, but do not certify its claims until the diplomatic/official sets are checked against it.

## 8. Witness Cluster: Basch / Blasio / Salm-Salm

### 8.1 Witness Reading Order

| Order | NRC ID | Source | Reason |
|---:|---|---|---|
| 1 | NRC_SHAWCROSS_0037 | Samuel Basch, *Memories of Mexico* | Closest medical/personal witness for final months; useful baseline for prison and execution atmosphere. |
| 2 | NRC_SHAWCROSS_0038 | José Luis Blasio memoirs / private secretary account | Court and Carlota-adjacent material; helps test whether Basch's final-month view fits the longer court history. |
| 3 | NRC_SHAWCROSS_0039 | Felix Salm-Salm, *My Diary in Mexico in 1867* | Military and rescue-plot perspective; read after Basch/Blasio to detect self-heroization and tactical divergences. |
| 4 | NRC_SHAWCROSS_0040 | Agnes Salm-Salm testimony/memoir references | Mercy mission and Juárez-contact material; high scene value but dialogue and gestures require strict corroboration. |

### 8.2 Witness Comparison Table

| Source | Maximilian Distance | Carlota Distance | Republican Distance | French / Conservative Distance | Time Gap / Text Problem | Self-Justification Risk | Loyalty / Honor Recovery Risk | Reader-Performance Risk | Language / Editing Risk | Novel Value | Historical Risk | Cross-check Points |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Basch | Very close in final months; medical and personal witness | Indirect or episode-dependent | Mainly through captivity/trial context | Loyalist imperial circle; observes French and conservative failures from inside collapse | Retrospective memoir/testimony; exact composition history to verify | May defend own proximity, judgment, and loyalty | High loyalty to Maximilian; possible martyr-making | Moderate; final scenes invite solemn dramatization | Edition/title and translation history need check | Intimate detail, physical condition, prison mood, final gestures | Single-witness emotion and dialogue cannot stand alone | Querétaro sequence; capture; prison access; trial anxieties; execution conduct; Maximilian's agency |
| Blasio | Close court/private-secretary or court-adjacent viewpoint | Stronger Carlota/court access than Basch for some episodes | Not a republican-side witness | Court and imperial-loyal perspective; may know conservative factions | Later account; exact role by episode must be profiled | May justify court actors and his own access | Possible defense of court loyalty and memory | Anecdotal court storytelling risk | Textual form and edition need check | Court rooms, private staff, Carlota scenes, interpersonal dynamics | Anecdotes can harden into false certainty | Court atmosphere; Carlota after crisis; private communications; trial-era recollections; comparison with letters |
| Felix Salm-Salm | Close in 1867 campaign and final crisis | Mostly indirect | Through military defeat, captivity, and rescue context | Military participant; loyal to Maximilian; may judge French/conservatives harshly | Diary/memoir boundary and publication shaping must be checked | High; rescue plot and battlefield role invite self-defense | High; can frame himself as loyal actor who tried to save the emperor | High; adventure narrative and heroization likely | Edition and translation/publication audience matter | Action scenes, siege tension, escape planning, failure | Motives, blame, and dialogue need external proof | Escape plans; military responsibility; Miramón/Mejía relation; surrender; execution aftermath |
| Agnes Salm-Salm | Close through mercy diplomacy, not as continuous military/court witness | Indirect | Directly important for Juárez and republican officials | Loyalist petitioner confronting republican power | Later testimony/memoir; exact source form must be identified | May heighten own role in mercy mission | High; reputation as courageous petitioner | Very high; dramatic appeal scenes | Language barrier noted; dialogue may be gesture/reconstruction | Mercy mission, prison visits, emotional confrontation scenes | Do not literalize dialogue; verify access, dates, and officials present | Juárez contact; pardon efforts; prison/trial access; public reaction; reported speeches/gestures |

### 8.3 Cluster Cross-check Questions

- Querétaro包囲戦: siege chronology, surrender conditions, military morale, and who knew what when.
- Maximilianの退位・抗戦意思: whether refusal, hesitation, or compulsion is reported consistently across witnesses and documents.
- Maximilianの処刑前後: exact sequence, access to prisoners, final conduct, reported words, body handling.
- Miramón / Mejíaとの関係: shared loyalty, rivalry, courtroom/prison behavior, execution grouping.
- 軍内部・宮廷内部の雰囲気: fear, exhaustion, blame, rumor, and loyalty performance.
- Carlota不在後の宮廷・帝政側心理: use Blasio and correspondence, not Basch/Salm-Salm alone.
- 敗北後の自己正当化: compare every witness against AAE, FO, 400AP, trial records, press, and Mexican-side accounts.
- 共和派側との接触・交渉: Agnes claims need Juárez-side records and press checks before use as fact.

## 9. Diplomatic and Official Documents Reading Set

| Reading Order | NRC IDs | Source Set | Strong Use | Main Caution | Witness Cross-check |
|---:|---|---|---|---|---|
| 1 | NRC_SHAWCROSS_0002; NRC_SHAWCROSS_0031; NRC_SHAWCROSS_0045 | AAE / French Foreign Ministry | French withdrawal, Dano/Drouyn de Lhuys pressure, Forest trial-period correspondence | Official self-protection; Paris-facing rhetoric | Test Basch/Salm-Salm claims about French abandonment, responsibility, and trial diplomacy |
| 2 | NRC_SHAWCROSS_0001; NRC_SHAWCROSS_0041 | 400AP / Fonds Napoleon / Castelnau | Castelnau mission, late orders, abdication pressure, command blame | Mission files may defend Castelnau/Napoleon III | Compare with Felix Salm-Salm, Basch, Blasio on last military options |
| 3 | NRC_SHAWCROSS_0003; NRC_SHAWCROSS_0042 | FO / British diplomatic records | External diplomatic view of French and Mexican narratives | British interests and rumor filtering | Check whether British reporting confirms or undermines loyalist testimony |
| 4 | NRC_SHAWCROSS_0004; NRC_SHAWCROSS_0020; NRC_SHAWCROSS_0016 | HHStA / Habsburg / Ratz | Crown offer, Miramar, Maximilian-Carlota letters, family pressure | Dynastic framing and edited correspondence | Check Maximilian's self-presentation against final-month testimony |
| 5 | NRC_SHAWCROSS_0011 | U.S. official documents | U.S. pressure, Juárez recognition/support, Monroe Doctrine rhetoric | Domestic U.S. politics and printed selection | Compare with Schofield, AAE, FO, and republican-side materials |
| 6 | NRC_SHAWCROSS_0008; NRC_SHAWCROSS_0043 | Mixed dispatches and crisis letters | Early intervention motives and scattered internal crisis communications | Mixed provenance; factional motives | Use for specific claim checks after sender/date/provenance is identified |

Key diplomatic/official questions:

- フランス撤兵: timing, pressure, responsibility shifting, and what Maximilian was told.
- Napoleon III と Maximilian: promises, ambiguity, abandonment, and blame.
- Miramar条約: guarantees, expectations, and later reinterpretation.
- 米国外交圧力: official pressure, post-Civil War military posture, and republican legitimacy.
- Juárez政権承認・支援: U.S. and external recognition versus imperial legitimacy claims.
- フランス軍・メキシコ帝政側の責任関係: Bazaine, Castelnau, conservative factions, and court actors.
- 帝政崩壊過程: chronology must rest on documents first, then memoir texture.

## 10. Mexican-Side Counterweight Reading Set

| Reading Order | NRC ID | Source | Position | Use | Limit |
|---:|---|---|---|---|---|
| 1 | NRC_SHAWCROSS_0024 | José María Vigil / *México a través de los siglos* | Liberal/republican national historiography | Counter Maximilian/Habsburg/French framing; connect to Juárez and liberal memory | Later secondary narrative; partisan memory politics |
| 2 | NRC_SHAWCROSS_0028 | Arrangoiz y Berzábal / *Méjico desde 1808 hasta 1867* | Conservative participant, retrospective | Conservative internal explanation and self-defense | Strong partisan bias and anti-liberal framing |
| 3 | NRC_SHAWCROSS_0029 | Romero de Terreros / *Correspondencias contemporáneas* | Edited contemporary correspondence | Mexico City elite reactions and political atmosphere | Editorial selection and correspondent identity must be checked |
| 4 | NRC_SHAWCROSS_0027 | Niceto de Zamacois / *Historia de Méjico* | Broad Mexican narrative, likely conservative-leaning | Compare conservative memory against Vigil and Arrangoiz | Later narrative conventions and party framing |
| 5 | NRC_SHAWCROSS_0026 | Hamnett within modern secondary cluster | Modern Juárez/republican bridge | Use Hamnett to identify stronger Juárez-side primary sources | Secondary work; not a substitute for republican records |

Treatment:

- These sources help correct Maximilian-centered narration but do not automatically supply a neutral Mexican viewpoint.
- Vigil helps with liberal/republican memory, but it is still later historiography.
- Zamacois and Arrangoiz help with Mexican conservative motives, not republican experience.
- Romero de Terreros may be closer to contemporary reactions, but only after correspondent/date/editorial checks.
- A dedicated Juárez/republican-side source reinforcement workflow remains necessary.

## 11. Press and Public Opinion Sources

Primary press candidate:

- `NRC_SHAWCROSS_0023`: La Sociedad, El Siglo, Times, Journal des débats, Revue des deux mondes, Journal de Bruxelles, Mexican Times, Harper's Weekly.
- Related public-political source: `NRC_SHAWCROSS_0047` Le Mémorial diplomatique and French legislative material.

Use press as:

- public opinion
- propaganda
- rumor circulation
- urban atmosphere
- ceremonial language
- political legitimacy performance
- international reception

Do not use press as direct fact certification until issue/date, article title, political alignment, censorship context, and independent corroboration are established.

## 12. Secondary Scholarship and Editorial Gateways

| NRC IDs | Group | Use |
|---|---|---|
| NRC_SHAWCROSS_0013 | Corti | Gateway to letters and court narrative; verify every important quotation or anecdote against letters/archives. |
| NRC_SHAWCROSS_0016; NRC_SHAWCROSS_0017; NRC_SHAWCROSS_0019 | Ratz / Foussemagne / Weckmann | Edited correspondence route for Maximilian/Carlota/Carlota-European materials; check editorial method and original locations. |
| NRC_SHAWCROSS_0021; NRC_SHAWCROSS_0025; NRC_SHAWCROSS_0034 | Bock / Niox / Gaulot | Orientation for diplomatic and military chronology; use to locate primary references. |
| NRC_SHAWCROSS_0026 | Cunningham / Hamnett / Taladoire / Schoonover | Bridge to Juárez, U.S.-Mexico, counter-guerrilla, and historiographical questions. |
| NRC_SHAWCROSS_0048 | Girard / Rady | Broad epilogue context only. |

## 13. Cross-reference to Existing IDs

Verified existing IDs available for NRC use:

- People: `PER-MAXIMILIAN`, `PER-CARLOTA`, `PER-BENITO-JUAREZ`, `PER-NAPOLEON-III`, `PER-FRANZ-JOSEPH`
- Organizations: `ORG-HABSBURG`, `ORG-MEXICAN-CONSERVATIVES`, `ORG-MEXICAN-REPUBLICANS`, `ORG-CATHOLIC-CHURCH`
- Events: `EVT-FRENCH-INTERVENTION-IN-MEXICO`, `EVT-SECOND-MEXICAN-EMPIRE`
- Places: `PLC-MIRAMAR`, `PLC-QUERETARO`
- Themes: `THM-FOREIGN-INTERVENTION`, `THM-LEGITIMACY`, `THM-LIBERAL-REFORM`
- Source note: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`
- Source-management docs: `SHAWCROSS_PROGRESS_MASTER`, `SHAWCROSS_ID_AUDIT`, `SHAWCROSS_NOTES_SOURCE_INDEX`, `SHAWCROSS_SOURCE_RELIABILITY_MATRIX`

Verified Shawcross card context:

- Capture: 103 Shawcross `source_id` files found.
- Fact: 2034 Shawcross `source_id` files found.
- Timeline: 321 Shawcross `source_id` files found.

NRC rows intentionally do not assign specific Fact/Timeline IDs because the relevant late-trial and epilogue ranges include known generation gaps.

## 14. Novel Use Notes

- Historical verification first: `NRC_SHAWCROSS_0001`, `0002`, `0003`, `0004`, `0008`, `0011`, `0020`, `0031`, `0041`, `0042`, `0045`.
- Final-month scene construction: `NRC_SHAWCROSS_0037`, `0038`, `0039`, `0040`, then cross-check against official records.
- Character psychology: private correspondence and edited letter collections are stronger than later memoirs, but Ratz/Foussemagne/Weckmann still need editorial checks.
- Court and military atmosphere: Blasio, Basch, Felix Salm-Salm, French military memoirs, and press are strong for texture but weak as standalone fact proof.
- Republican-side perspective: Vigil, U.S. official documents, Mexican press, García/Pereyra, Romero de Terreros, and Hamnett are useful entry points but insufficient.
- Maximilian-side pull: HHStA, Ratz, Foussemagne, Weckmann, Corti, Basch, Blasio, and Salm-Salm can over-center Maximilian, Carlota, loyal witnesses, and dynastic tragedy.
- French-side pull: AAE, 400AP, Niox, Gaulot, Castelnau, and French public records can over-center French responsibility management.
- Mexican conservative pull: Gutiérrez de Estrada, Arrangoiz, Zamacois, Lombardo de Miramón, and conservative press can overstate monarchist legitimacy.
- U.S.-side pull: U.S. official documents and Schofield may frame events through Monroe Doctrine, post-Civil War strength, and U.S. self-justification.

## 15. Juárez / Republican-Side Gap Notes

Current SRM/NRC sources do not yet provide a sufficiently strong direct Juárez/republican-side evidentiary base.

Useful but insufficient current bridges:

- `NRC_SHAWCROSS_0011` U.S. official documents: good for external recognition/support, not internal republican policy alone.
- `NRC_SHAWCROSS_0024` Vigil: liberal/republican memory, but later and historiographical.
- `NRC_SHAWCROSS_0023` Mexican press: good for public rhetoric and rumor, but not neutral fact proof.
- `NRC_SHAWCROSS_0026` Hamnett cluster: best bridge into a later Juárez-focused workflow.
- `NRC_SHAWCROSS_0033` García/Pereyra: possible Mexican documentary trail, pending exact document identification.
- `NRC_SHAWCROSS_0040` Agnes Salm-Salm: direct Juárez-contact claims require republican-side corroboration.

Recommended next workflow:

- Create a separate "Juárez / Republican-Side Source Reinforcement Candidates" pass after this NRC plan.
- Identify Juárez correspondence, republican government decrees, trial/court-martial records, republican military reports, liberal press issue lists, and Mexican archival/documentary collections.
- Use Hamnett's *Juárez* as a guide to republican-side primary evidence, not as a substitute for that evidence.

## 16. Unresolved / Manual Review Needed

Carried forward without repair, renumbering, deletion, or speculative file creation:

- `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096`: file-absent; manual review.
- `FACT_MEXEMP_2561-2608`: generation-gap suspected; not treated as existing IDs.
- `TIME_MEXEMP_0423-0448`: generation-gap suspected; not treated as existing IDs.
- `FACT_MEXEMP_2439-2513`: generation-gap/manual-review range from trial section captures.
- `TIME_MEXEMP_0387-0413`: generation-gap/manual-review range from trial section captures.
- `TIME_MEXEMP_0413`: boundary review between `CAP_MEXEMP_0101` and `CAP_MEXEMP_0102`; not linked as existing.
- `SRC_UNSET_001`: remains on `CAP_MEXEMP_0001`, `FACT_MEXEMP_0001-0006`, and `TIME_MEXEMP_0001-0002`.
- `FACT_MEXEMP_0489 -> FACT_MEXEMP_0431`: unresolved existing-card-to-nonexistent-ID reference.
- `FACT_MEXEMP_0638 -> FACT_MEXEMP_0439`: unresolved existing-card-to-nonexistent-ID reference.
- `TIME_MEXEMP_0196 -> TIME_MEXEMP_0192`: unresolved existing-card-to-nonexistent-ID reference.
- `notes_translation_0109.md` not found. Page 109 NOTES range is registered in [[Shawcross_Progress_Master]], but source names remain unresolved in `NSI_SHAWCROSS_0044` / `SRM_SHAWCROSS_0044` / `NRC_SHAWCROSS_0044`.
- 114-page bibliographic checks remain: Chapter 10 n.3 Spanish long title; Chapter 10 n.11 Corti publication-place formatting; EPILOGUE n.3 `Supplement/Supplément au Journal des débats`.

## 17. Work Log

- 2026-06-13: Confirmed no existing same-purpose `Shawcross_Next_Reading_Candidates.md`, `Shawcross_Next_Reading_*`, or `NRC_SHAWCROSS_####` file was present.
- 2026-06-13: Created this single aggregated NRC file. No individual candidate/source/person Markdown files were created.
- 2026-06-13: Converted `SRM_SHAWCROSS_0001-0048` and `NSI_SHAWCROSS_0001-0048` into `NRC_SHAWCROSS_0001-0048`.
- 2026-06-13: Added witness, diplomatic/official, Mexican-side, press, secondary-gateway, novel-use, and Juárez/republican-gap planning sections.
- 2026-06-13: Checked representative existing late-trial and epilogue Capture / Fact / Timeline cards for context, without changing them.
- 2026-06-13: Did not create Fact Cards, Timeline Entries, Capture files, or entity cards. Did not renumber, delete, or fill gaps.
- 2026-06-13: Did not store Shawcross body text, NOTES full text, screenshot full transcription, or long quotation.

## 18. Candidate Stats

| Metric | Count |
|---|---:|
| NRC rows | 48 |
| SRM rows covered | 48 |
| NSI rows covered | 48 |
| reading_priority first | 17 |
| reading_priority second | 15 |
| reading_priority third | 10 |
| reading_priority later | 6 |
| primary | 13 |
| quasi_primary | 8 |
| memoir_or_testimony | 12 |
| secondary | 9 |
| archive_or_collection | 4 |
| unclear | 2 |
| verification_needed yes | 40 |
| verification_needed no | 8 |
