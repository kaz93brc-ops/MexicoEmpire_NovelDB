---
id: CORE_TIMELINE_1859_1867
type: core_timeline_linkage
status: active
created: 2026-06-14
updated: 2026-06-14
ctl_id_range: CTL_MEXEMP_0001-CTL_MEXEMP_0032
source_handling: existing_db_linkage_only
new_fact_cards_created: no
new_timeline_cards_created: no
new_capture_cards_created: no
long_quotes_or_full_transcription: no
---

# Core Timeline 1859-1867

## 1. Purpose

This document is the Phase 10 core timeline linkage table for the Maximilian of Mexico historical-novel database. It does not create new Timeline, Fact, Capture, Person, Event, Place, Org, Theme, or Source cards. It consolidates already existing cards and management documents into a narrative backbone for 1859-1867, with limited prehistory and aftermath where needed.

The CTL IDs are linkage-row IDs only. They are not Timeline-card IDs.

## 2. Method and Scope

- Vault checked: `MexicoEmpire_NovelDB`.
- Same-purpose file search terms checked: `Core Timeline`, `Master Timeline`, `Timeline Master`, `1859`, `1860`, `1861`, `1862`, `1863`, `1864`, `1865`, `1866`, `1867`, `chronology`, `chronological`, `plot timeline`, `narrative timeline`, `中核タイムライン`, and `年表`.
- Existing same-purpose aggregate file found: none.
- Destination selected: `93_Docs/Core_Timeline_1859_1867.md`.
- Existing `CTL_MEXEMP_####` IDs found before creation: none.
- New CTL range used here: `CTL_MEXEMP_0001-CTL_MEXEMP_0032`.
- No individual CTL notes were created.
- No CAP, FACT, or TIME IDs were renumbered, deleted, filled, or inferred.

## 3. Existing Timeline / Fact / Capture Coverage

Coverage is based on `93_Docs/Shawcross_ID_Audit.md` and cross-checks against existing cards.

| Card type | Audited usable coverage | Known non-links / exclusions |
|---|---:|---|
| Capture | `CAP_MEXEMP_0001-0107`, excluding absent files `0044`, `0052`, `0096` | Only existing CAP IDs are linked. |
| Fact | `FACT_MEXEMP_0001-2560`, with audited internal gaps | `FACT_MEXEMP_2561-2608` are generation-gap or planned IDs and are not used as existing facts. |
| Timeline | `TIME_MEXEMP_0001-0422`, with audited internal gaps | `TIME_MEXEMP_0423-0448` are generation-gap or planned IDs and are not used as existing timeline cards. |
| Source unset cluster | `CAP_MEXEMP_0001`; `FACT_MEXEMP_0001-0006`; `TIME_MEXEMP_0001-0002` | Kept separate from Shawcross-body coverage and marked for verification. |

Management-document coverage used:

- `CDL_MEXEMP_0001-0016`
- `NCD_MEXEMP_0001-0031`
- `NSI_SHAWCROSS_0001-0048`
- `SRM_SHAWCROSS_0001-0048`
- `NRC_SHAWCROSS_0001-0048`
- `RSG_MEXEMP_0001-0022`
- `HJI_MEXEMP_0001-0025`

## 4. Source and Bias Caveats

- Shawcross-derived cards are useful for the imperial, French, and European diplomatic sequence, but the novel cannot rely on them alone for Juarez, republican legality, provincial politics, liberal press, trial legality, or memory politics.
- All CTL rows keep `republican_balance_needed: yes` because the previous chapter and character design indexes already mark the whole structure as requiring republican-side reinforcement.
- Memoirs and witness testimony clusters, especially Basch, Blasio, Felix Salm-Salm, and Agnes Salm-Salm, are treated as `verification_needed`.
- Mexican press, European press, and later memory literature should not be treated as direct proof of private motives without source-trail confirmation.
- Maximilian-centered pathos, Carlota-only tragedy, and Juarez-as-simple-executioner frames are treated as narrative risks.

## 5. Chronological Overview

The backbone runs from liberal-reform legality and the Reform War through foreign debt crisis, tripartite intervention, French escalation, imperial formation, the Liberal Empire contradiction, U.S. pressure, French withdrawal, Queretaro, trial, execution, and post-1867 memory.

The densest existing Timeline / Fact / Capture coverage begins with the French intervention and imperial formation. Earlier republican legality, McLane-Ocampo, debt-payment suspension, and several Mexican-side perspectives remain source-gap areas.

## 6. CTL Index Table

| CTL ID | Date / Range | Precision | Core Event | Narrative Phase | Related Timeline | Related Fact | Related Capture | Related CDL | Related NCD | Evidence Strength | Republican Balance Needed | Maximilian-centered Risk | Verification Needed | Scene Potential | Manual Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `CTL_MEXEMP_0001` | 1857-1858 | approximate | Liberal Reform and Reform War prehistory | Reform / pre-intervention | none existing | none existing | none existing | `CDL_MEXEMP_0016` | `NCD_MEXEMP_0003`; `0014`; `0016` | weak | yes | low | yes | medium | yes |
| `CTL_MEXEMP_0002` | 1859 | year | Reform War violence and Tacubaya memory | Reform / pre-intervention | `TIME_MEXEMP_0071` | none confirmed | none confirmed | `CDL_MEXEMP_0016` | `NCD_MEXEMP_0003`; `0007`; `0008`; `0009` | mixed | yes | medium | yes | medium | yes |
| `CTL_MEXEMP_0003` | 1859 | manual_review_needed | McLane-Ocampo Treaty and U.S.-Mexican liberal diplomacy | Reform / pre-intervention | none existing | none existing | none existing | `CDL_MEXEMP_0016` | `NCD_MEXEMP_0003`; `0014`; `0016` | manual_review_needed | yes | low | yes | medium | yes |
| `CTL_MEXEMP_0004` | 1861 | year | Juarez government returns to Mexico City and faces conservative resistance | Reform / pre-intervention | `TIME_MEXEMP_0110` | none confirmed | none confirmed | `CDL_MEXEMP_0016` | `NCD_MEXEMP_0003`; `0009` | mixed | yes | low | yes | medium | yes |
| `CTL_MEXEMP_0005` | 1861-10-31 to 1861-11 | exact | Debt crisis and Tripartite Convention | French intervention | `TIME_MEXEMP_0050-0052` | `FACT_MEXEMP_0265`; `0291` | `CAP_MEXEMP_0013-0014` | `CDL_MEXEMP_0003`; `0016` | `NCD_MEXEMP_0003`; `0004`; `0014`; `0016` | moderate | yes | medium | yes | high | yes |
| `CTL_MEXEMP_0006` | 1862-01 to 1862-03 | month | Veracruz landing, La Soledad, and Juarez emergency legality | French intervention | `TIME_MEXEMP_0053-0054`; `0064-0067` | `FACT_MEXEMP_0289-0302`; `0351` | `CAP_MEXEMP_0013-0015` | `CDL_MEXEMP_0003`; `0016` | `NCD_MEXEMP_0003`; `0004`; `0005`; `0016` | mixed | yes | medium | yes | high | yes |
| `CTL_MEXEMP_0007` | 1862-04 to 1862-05 | month | French break with allies and Puebla / Cinco de Mayo | French intervention | `TIME_MEXEMP_0072-0078` | `FACT_MEXEMP_0346-0411` | `CAP_MEXEMP_0016-0018` | `CDL_MEXEMP_0003`; `0016` | `NCD_MEXEMP_0003`; `0004`; `0005` | moderate | yes | medium | yes | high | yes |
| `CTL_MEXEMP_0008` | 1862-06 to 1862-12 | month | Forey, French escalation, and imperial intervention planning | French intervention | `TIME_MEXEMP_0066`; `0079`; `0083-0085` | `FACT_MEXEMP_0446-0480` | `CAP_MEXEMP_0019-0020` | `CDL_MEXEMP_0003`; `0004` | `NCD_MEXEMP_0004`; `0005`; `0008` | mixed | yes | high | yes | medium | yes |
| `CTL_MEXEMP_0009` | 1863-03 to 1863-06-10 | exact | Second Puebla siege, Juarez evacuation, French entry into Mexico City | French intervention | `TIME_MEXEMP_0086-0091` | `FACT_MEXEMP_0508-0544` | `CAP_MEXEMP_0020-0022` | `CDL_MEXEMP_0003`; `0016` | `NCD_MEXEMP_0003`; `0004`; `0005`; `0025` | moderate | yes | medium | yes | high | yes |
| `CTL_MEXEMP_0010` | 1863-06 to 1863-07-11 | exact | Junta, regency, and declaration of empire | imperial formation | `TIME_MEXEMP_0092-0094`; `0103` | `FACT_MEXEMP_0563-0567` | `CAP_MEXEMP_0023` | `CDL_MEXEMP_0004`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0004`; `0005`; `0018` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0011` | 1863-10 to 1863-12 | month | Crown offer, Bazaine, regency conflict, and Juarez under pressure | imperial formation | `TIME_MEXEMP_0095`; `0104-0118` | `FACT_MEXEMP_0672-0705` | `CAP_MEXEMP_0024-0032` | `CDL_MEXEMP_0004`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0004`; `0005`; `0007`; `0009`; `0017`; `0018` | mixed | yes | high | yes | medium | yes |
| `CTL_MEXEMP_0012` | 1864-01 to 1864-03 | month | Miramar, Paris, Vienna, and treaty pressure | imperial formation | `TIME_MEXEMP_0119-0129` | `FACT_MEXEMP_0739-0786` | `CAP_MEXEMP_0031-0033` | `CDL_MEXEMP_0002`; `0004` | `NCD_MEXEMP_0001`; `0002`; `0004`; `0031` | moderate | yes | high | yes | high | yes |
| `CTL_MEXEMP_0013` | 1864-04 to 1864-05-28 | exact | Crown acceptance, Treaty of Miramar, departure, Veracruz arrival | imperial formation | `TIME_MEXEMP_0136-0146` | `FACT_MEXEMP_0811-0870` | `CAP_MEXEMP_0034-0037` | `CDL_MEXEMP_0002`; `0004`; `0005` | `NCD_MEXEMP_0001`; `0002`; `0003`; `0004`; `0031` | moderate | yes | high | yes | high | yes |
| `CTL_MEXEMP_0014` | 1864-06 to 1864-10 | month | Mexico City ceremonies, court formation, travel, Juarez displacement | imperial formation | `TIME_MEXEMP_0147-0168` | `FACT_MEXEMP_0883`; `0892`; `0977-0978`; `1015-1019` | `CAP_MEXEMP_0038-0043`; `0045` | `CDL_MEXEMP_0005`; `0007`; `0016` | `NCD_MEXEMP_0001`; `0002`; `0003`; `0005`; `0017`; `0025` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0015` | 1864-12 | month | Meglia, Syllabus, and church-policy decree | liberal empire | `TIME_MEXEMP_0172`; `0174-0178` | `FACT_MEXEMP_1137-1166` | `CAP_MEXEMP_0046-0051` | `CDL_MEXEMP_0006`; `0016` | `NCD_MEXEMP_0001`; `0002`; `0003`; `0017` | moderate | yes | high | yes | high | yes |
| `CTL_MEXEMP_0016` | 1865-01 to 1865-05 | month | Liberal Empire backlash, Dano, Bazaine, Oaxaca, and Juarez pressure | liberal empire | `TIME_MEXEMP_0184-0189`; `0194-0195` | `FACT_MEXEMP_1262-1306`; `1327-1340` | `CAP_MEXEMP_0053-0057` | `CDL_MEXEMP_0006`; `0008`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0004`; `0005`; `0014`; `0015`; `0016`; `0017` | mixed | yes | high | yes | medium | yes |
| `CTL_MEXEMP_0017` | 1865-06 to 1865-10 | month | U.S. pressure, Brownsville / Matamoros, and Black Decree | U.S. pressure | `TIME_MEXEMP_0195-0200` | `FACT_MEXEMP_1128`; `1367-1370`; `1546-1555` | `CAP_MEXEMP_0054-0057`; `0065-0066` | `CDL_MEXEMP_0008`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0005`; `0014`; `0015`; `0016` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0018` | 1865-10 to 1865-12 | month | Carlota in Yucatan and Maximilian's letters to Carlota / Napoleon | liberal empire | `TIME_MEXEMP_0201-0204`; `0217` | `FACT_MEXEMP_1392-1413`; `1428` | `CAP_MEXEMP_0057-0058` | `CDL_MEXEMP_0007`; `0009` | `NCD_MEXEMP_0001`; `0002`; `0004`; `0020`; `0021` | mixed | yes | high | yes | medium | yes |
| `CTL_MEXEMP_0019` | 1866-01 to 1866-02 | month | Napoleon withdrawal decision, Schofield, Leopold death, Cuernavaca crisis | French withdrawal | `TIME_MEXEMP_0215-0221` | `FACT_MEXEMP_1428-1475` | `CAP_MEXEMP_0058-0061` | `CDL_MEXEMP_0009`; `0010`; `0016` | `NCD_MEXEMP_0001`; `0002`; `0004`; `0014`; `0021`; `0022`; `0031` | moderate | yes | high | yes | high | yes |
| `CTL_MEXEMP_0020` | 1866-03 to 1866-04 | month | Langlais reforms, finance crisis, and paper empire problem | liberal empire | `TIME_MEXEMP_0222-0228` | `FACT_MEXEMP_1531-1536` | `CAP_MEXEMP_0062-0065` | `CDL_MEXEMP_0007`; `0010`; `0016` | `NCD_MEXEMP_0001`; `0002`; `0003`; `0005`; `0021` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0021` | 1866-05 to 1866-07 | month | Volunteers, Matamoros collapse, Carlota departure, Monterrey | U.S. pressure | `TIME_MEXEMP_0230-0237`; `0259-0268` | `FACT_MEXEMP_1707-1775` | `CAP_MEXEMP_0067-0074` | `CDL_MEXEMP_0008`; `0009`; `0010`; `0016` | `NCD_MEXEMP_0001`; `0002`; `0003`; `0014`; `0015`; `0025` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0022` | 1866-08 to 1866-09 | month | Carlota in France and Rome; Seward protest; Castelnau orders | French withdrawal | `TIME_MEXEMP_0238-0250`; `0256-0258`; `0275-0281` | `FACT_MEXEMP_1808-1880`; `1833-1834` | `CAP_MEXEMP_0068-0078` | `CDL_MEXEMP_0009`; `0016` | `NCD_MEXEMP_0002`; `0004`; `0006`; `0014`; `0022`; `0031` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0023` | 1866-10 to 1866-11 | month | Orizaba / El Olindo abdication crisis, Miramon return, and court politics | French withdrawal | `TIME_MEXEMP_0282-0291`; `0298-0301` | `FACT_MEXEMP_1909-1936` | `CAP_MEXEMP_0072-0079` | `CDL_MEXEMP_0010`; `0016` | `NCD_MEXEMP_0001`; `0002`; `0004`; `0006`; `0007`; `0019`; `0020`; `0021` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0024` | 1866-12 to 1867-01 | exact | French withdrawal sequence, U.S. border pressure, Castagny, Zacatecas | French withdrawal | `TIME_MEXEMP_0323-0343` | `FACT_MEXEMP_2029-2105` | `CAP_MEXEMP_0084-0088` | `CDL_MEXEMP_0011`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0004`; `0005`; `0022`; `0023`; `0024`; `0025` | moderate | yes | medium | yes | medium | yes |
| `CTL_MEXEMP_0025` | 1867-02 to 1867-03-14 | exact | Maximilian goes to Queretaro and siege begins | Querétaro | `TIME_MEXEMP_0344-0355` | `FACT_MEXEMP_2110-2217` | `CAP_MEXEMP_0088-0090` | `CDL_MEXEMP_0011`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0007`; `0008`; `0009`; `0024` | moderate | yes | high | yes | high | yes |
| `CTL_MEXEMP_0026` | 1867-03 to 1867-04 | month | Siege councils, sorties, Marquez mission, Miramon / Mejia choices | Querétaro | `TIME_MEXEMP_0356-0366` | `FACT_MEXEMP_2218-2315` | `CAP_MEXEMP_0091-0093` | `CDL_MEXEMP_0011`; `0015`; `0016` | `NCD_MEXEMP_0001`; `0007`; `0008`; `0009`; `0024` | moderate | yes | high | yes | high | yes |
| `CTL_MEXEMP_0027` | 1867-05-05 to 1867-05-15 | exact | Final attack, Lopez betrayal, capture, surrender to Escobedo | Querétaro | `TIME_MEXEMP_0367-0375` | `FACT_MEXEMP_2316-2365` | `CAP_MEXEMP_0094-0095` | `CDL_MEXEMP_0011`; `0015`; `0016` | `NCD_MEXEMP_0001`; `0007`; `0008`; `0009`; `0024` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0028` | 1867-05-30 to 1867-06-03 | exact | Trial preparation, escape plans, and Salm-Salm intervention | trial / execution | `TIME_MEXEMP_0379-0386` | `FACT_MEXEMP_2390-2438` | `CAP_MEXEMP_0097-0098` | `CDL_MEXEMP_0012`; `0015`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0010`; `0011`; `0012`; `0013`; `0024` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0029` | 1867-06-13 | exact | Court-martial timing, legal judgment, and Juarez delay | trial / execution | `TIME_MEXEMP_0382` | `FACT_MEXEMP_2416-2429` | `CAP_MEXEMP_0097-0102` | `CDL_MEXEMP_0012`; `0013`; `0015`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0007`; `0009`; `0012`; `0013`; `0024` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0030` | 1867-06-19 | exact | Execution of Maximilian, Miramon, and Mejia | trial / execution | `TIME_MEXEMP_0002`; `0414` | `FACT_MEXEMP_0001-0006`; `2514` | `CAP_MEXEMP_0001`; `0102` | `CDL_MEXEMP_0001`; `0013`; `0015`; `0016` | `NCD_MEXEMP_0001`; `0003`; `0007`; `0009`; `0010`; `0011`; `0012`; `0013`; `0024` | mixed | yes | high | yes | high | yes |
| `CTL_MEXEMP_0031` | 1867-06 to 1867-11-25 | exact | Body return diplomacy and Novara transfer | aftermath / memory | `TIME_MEXEMP_0414-0415` | `FACT_MEXEMP_2515-2519` | `CAP_MEXEMP_0103` | `CDL_MEXEMP_0014`; `0015` | `NCD_MEXEMP_0001`; `0002`; `0003`; `0004`; `0031` | moderate | yes | high | yes | medium | yes |
| `CTL_MEXEMP_0032` | 1868 and after | approximate | Memory politics, Carlota's afterlife, European and Mexican remembrance | aftermath / memory | `TIME_MEXEMP_0416-0422` | `FACT_MEXEMP_2528-2560` | `CAP_MEXEMP_0103-0106` | `CDL_MEXEMP_0014`; `0015`; `0016` | `NCD_MEXEMP_0001`; `0002`; `0003`; `0004`; `0026`; `0027`; `0028`; `0029`; `0030`; `0031` | mixed | yes | high | yes | medium | yes |

## 7. CTL Detail Records

### CTL_MEXEMP_0001

- date_or_range: 1857-1858.
- chronology_precision: approximate.
- core_event: Liberal Reform and Reform War prehistory.
- historical_summary: The constitutional and reform-law background frames why Juarez's government claimed legality and why church-state conflict became central before foreign intervention.
- narrative_phase: Reform / pre-intervention.
- related_CDL: `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0003`; `NCD_MEXEMP_0014`; `NCD_MEXEMP_0016`.
- related_timeline_cards: none existing.
- related_fact_cards: none existing.
- related_capture_cards: none existing.
- related_person_cards: `PER-BENITO-JUAREZ`.
- related_event_cards: none existing.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-CATHOLIC-CHURCH`.
- related_theme_cards: `THM-LIBERAL-REFORM`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: none direct.
- related_SRM: none direct.
- related_NRC: none direct.
- related_RSG: `RSG_MEXEMP_0001`; `RSG_MEXEMP_0002`; `RSG_MEXEMP_0007`; `RSG_MEXEMP_0020`.
- related_HJI: `HJI_MEXEMP_0001`; `HJI_MEXEMP_0002`; `HJI_MEXEMP_0009`; `HJI_MEXEMP_0014`.
- evidence_strength: weak.
- republican_balance_needed: yes.
- maximilian_centered_risk: low.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Use as legal and ideological groundwork for later cabinet, exile-government, and press scenes; avoid exposition dump.
- factual_risk_notes: Do not collapse liberal legality into simple anti-clericalism; distinguish law, war, property, and legitimacy.
- source_gap_notes: Existing card linkage is thin; needs republican constitutional and legal-source reinforcement.
- manual_review_needed: yes.

### CTL_MEXEMP_0002

- date_or_range: 1859.
- chronology_precision: year.
- core_event: Reform War violence and Tacubaya memory.
- historical_summary: Conservative and liberal violence during the Reform War supplies the remembered background for Miramon, Marquez, Mejia, and later republican distrust.
- narrative_phase: Reform / pre-intervention.
- related_CDL: `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0003`; `NCD_MEXEMP_0007`; `NCD_MEXEMP_0008`; `NCD_MEXEMP_0009`.
- related_timeline_cards: `TIME_MEXEMP_0071`.
- related_fact_cards: none confirmed.
- related_capture_cards: none confirmed.
- related_person_cards: `PER-BENITO-JUAREZ`.
- related_event_cards: none existing.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0009`; `NSI_SHAWCROSS_0024`; `NSI_SHAWCROSS_0027`; `NSI_SHAWCROSS_0028`; `NSI_SHAWCROSS_0029`.
- related_SRM: `SRM_SHAWCROSS_0009`; `SRM_SHAWCROSS_0024`; `SRM_SHAWCROSS_0027`; `SRM_SHAWCROSS_0028`; `SRM_SHAWCROSS_0029`.
- related_NRC: `NRC_SHAWCROSS_0009`; `NRC_SHAWCROSS_0024`; `NRC_SHAWCROSS_0027`; `NRC_SHAWCROSS_0028`; `NRC_SHAWCROSS_0029`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0013`; `RSG_MEXEMP_0014`; `RSG_MEXEMP_0015`; `RSG_MEXEMP_0016`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0018`; `HJI_MEXEMP_0019`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: medium.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Use as remembered grievance and reputation rather than a long battle narrative.
- factual_risk_notes: Tacubaya and massacre claims require republican and conservative-source comparison.
- source_gap_notes: Related facts and captures are not yet confidently linked in this pass.
- manual_review_needed: yes.

### CTL_MEXEMP_0003

- date_or_range: 1859.
- chronology_precision: manual_review_needed.
- core_event: McLane-Ocampo Treaty and U.S.-Mexican liberal diplomacy.
- historical_summary: The treaty issue is important for U.S.-Mexico relations and liberal wartime diplomacy, but local cards do not yet provide a verified event chain.
- narrative_phase: Reform / pre-intervention.
- related_CDL: `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0003`; `NCD_MEXEMP_0014`; `NCD_MEXEMP_0016`.
- related_timeline_cards: none existing.
- related_fact_cards: none existing.
- related_capture_cards: none existing.
- related_person_cards: `PER-BENITO-JUAREZ`.
- related_event_cards: none existing.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`.
- related_source_cards: none existing direct.
- related_NSI: `NSI_SHAWCROSS_0011`.
- related_SRM: `SRM_SHAWCROSS_0011`.
- related_NRC: `NRC_SHAWCROSS_0011`.
- related_RSG: `RSG_MEXEMP_0012`.
- related_HJI: `HJI_MEXEMP_0013`.
- evidence_strength: manual_review_needed.
- republican_balance_needed: yes.
- maximilian_centered_risk: low.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Possible diplomatic-paper, rumor, or cabinet scene showing Juarez's constrained choices.
- factual_risk_notes: Do not infer motives from later U.S. policy without source confirmation.
- source_gap_notes: No verified local Timeline / Fact / Capture card found for this pass.
- manual_review_needed: yes.

### CTL_MEXEMP_0004

- date_or_range: 1861.
- chronology_precision: year.
- core_event: Juarez government returns to Mexico City and faces conservative resistance.
- historical_summary: The liberal government appears as the legal republican government after the Reform War, while conservative military resistance continues.
- narrative_phase: Reform / pre-intervention.
- related_CDL: `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0003`; `NCD_MEXEMP_0009`.
- related_timeline_cards: `TIME_MEXEMP_0110`.
- related_fact_cards: none confirmed.
- related_capture_cards: none confirmed.
- related_person_cards: `PER-BENITO-JUAREZ`.
- related_event_cards: none existing.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-LIBERAL-REFORM`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0024`; `NSI_SHAWCROSS_0027`; `NSI_SHAWCROSS_0028`.
- related_SRM: `SRM_SHAWCROSS_0024`; `SRM_SHAWCROSS_0027`; `SRM_SHAWCROSS_0028`.
- related_NRC: `NRC_SHAWCROSS_0024`; `NRC_SHAWCROSS_0027`; `NRC_SHAWCROSS_0028`.
- related_RSG: `RSG_MEXEMP_0002`; `RSG_MEXEMP_0007`; `RSG_MEXEMP_0008`.
- related_HJI: `HJI_MEXEMP_0002`; `HJI_MEXEMP_0009`; `HJI_MEXEMP_0010`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: low.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Use to anchor Juarez before foreign intervention rather than first introducing him through Maximilian's fate.
- factual_risk_notes: Need exact chronology for Mejia and regional conservative resistance.
- source_gap_notes: Existing link is primarily Timeline-level; republican documents should supplement.
- manual_review_needed: yes.

### CTL_MEXEMP_0005

- date_or_range: 1861-10-31 to 1861-11.
- chronology_precision: exact.
- core_event: Debt crisis and Tripartite Convention.
- historical_summary: European powers coordinate intervention after Mexico's debt crisis, turning financial conflict into a military and diplomatic opening for intervention.
- narrative_phase: French intervention.
- related_CDL: `CDL_MEXEMP_0003`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0014`; `NCD_MEXEMP_0016`.
- related_timeline_cards: `TIME_MEXEMP_0050-0052`.
- related_fact_cards: `FACT_MEXEMP_0265`; `FACT_MEXEMP_0291`.
- related_capture_cards: `CAP_MEXEMP_0013-0014`.
- related_person_cards: `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0008`; `NSI_SHAWCROSS_0011`.
- related_SRM: `SRM_SHAWCROSS_0008`; `SRM_SHAWCROSS_0011`.
- related_NRC: `NRC_SHAWCROSS_0008`; `NRC_SHAWCROSS_0011`.
- related_RSG: `RSG_MEXEMP_0012`; `RSG_MEXEMP_0018`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0013`; `HJI_MEXEMP_0025`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: medium.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Can be staged as diplomatic correspondence, creditor politics, or cabinet calculation.
- factual_risk_notes: Debt suspension and convention details need separation; avoid making intervention appear inevitable.
- source_gap_notes: Need Mexican fiscal and diplomatic records beyond imperial-facing narrative.
- manual_review_needed: yes.

### CTL_MEXEMP_0006

- date_or_range: 1862-01 to 1862-03.
- chronology_precision: month.
- core_event: Veracruz landing, La Soledad, and Juarez emergency legality.
- historical_summary: Foreign troops arrive at Veracruz, negotiations temporarily constrain escalation, and Juarez uses emergency legal measures against collaboration.
- narrative_phase: French intervention.
- related_CDL: `CDL_MEXEMP_0003`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0016`.
- related_timeline_cards: `TIME_MEXEMP_0053-0054`; `TIME_MEXEMP_0064-0067`.
- related_fact_cards: `FACT_MEXEMP_0289-0302`; `FACT_MEXEMP_0351`.
- related_capture_cards: `CAP_MEXEMP_0013-0015`.
- related_person_cards: `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0008`; `NSI_SHAWCROSS_0011`; `NSI_SHAWCROSS_0023`.
- related_SRM: `SRM_SHAWCROSS_0008`; `SRM_SHAWCROSS_0011`; `SRM_SHAWCROSS_0023`.
- related_NRC: `NRC_SHAWCROSS_0008`; `NRC_SHAWCROSS_0011`; `NRC_SHAWCROSS_0023`.
- related_RSG: `RSG_MEXEMP_0007`; `RSG_MEXEMP_0008`; `RSG_MEXEMP_0011`; `RSG_MEXEMP_0012`.
- related_HJI: `HJI_MEXEMP_0009`; `HJI_MEXEMP_0010`; `HJI_MEXEMP_0012`; `HJI_MEXEMP_0013`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: medium.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Strong scene potential in port, negotiation, legal decree, and rumor networks.
- factual_risk_notes: Juarez's emergency law should be treated as wartime state policy, not simple cruelty.
- source_gap_notes: Need Mexican official text and press comparison for January 25 law.
- manual_review_needed: yes.

### CTL_MEXEMP_0007

- date_or_range: 1862-04 to 1862-05.
- chronology_precision: month.
- core_event: French break with allies and Puebla / Cinco de Mayo.
- historical_summary: France separates from the tripartite intervention and suffers defeat at Puebla, strengthening republican morale and complicating Napoleon III's expectations.
- narrative_phase: French intervention.
- related_CDL: `CDL_MEXEMP_0003`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0005`.
- related_timeline_cards: `TIME_MEXEMP_0072-0078`.
- related_fact_cards: `FACT_MEXEMP_0346-0411`.
- related_capture_cards: `CAP_MEXEMP_0016-0018`.
- related_person_cards: `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0008`; `NSI_SHAWCROSS_0023`; `NSI_SHAWCROSS_0026`.
- related_SRM: `SRM_SHAWCROSS_0008`; `SRM_SHAWCROSS_0023`; `SRM_SHAWCROSS_0026`.
- related_NRC: `NRC_SHAWCROSS_0008`; `NRC_SHAWCROSS_0023`; `NRC_SHAWCROSS_0026`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0010`; `RSG_MEXEMP_0011`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0012`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: medium.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Can function as a republican morale anchor and as a French miscalculation scene.
- factual_risk_notes: Avoid reducing Puebla to a symbolic holiday; preserve military and diplomatic sequence.
- source_gap_notes: Need Mexican military reports and local press.
- manual_review_needed: yes.

### CTL_MEXEMP_0008

- date_or_range: 1862-06 to 1862-12.
- chronology_precision: month.
- core_event: Forey, French escalation, and imperial intervention planning.
- historical_summary: After Puebla, French policy escalates; Forey and imperial planners turn military intervention toward regime-building.
- narrative_phase: French intervention.
- related_CDL: `CDL_MEXEMP_0003`; `CDL_MEXEMP_0004`.
- related_NCD: `NCD_MEXEMP_0004`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0008`.
- related_timeline_cards: `TIME_MEXEMP_0066`; `TIME_MEXEMP_0079`; `TIME_MEXEMP_0083-0085`.
- related_fact_cards: `FACT_MEXEMP_0446-0480`.
- related_capture_cards: `CAP_MEXEMP_0019-0020`.
- related_person_cards: `PER-NAPOLEON-III`.
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0001`; `NSI_SHAWCROSS_0002`; `NSI_SHAWCROSS_0022`.
- related_SRM: `SRM_SHAWCROSS_0001`; `SRM_SHAWCROSS_0002`; `SRM_SHAWCROSS_0022`.
- related_NRC: `NRC_SHAWCROSS_0001`; `NRC_SHAWCROSS_0002`; `NRC_SHAWCROSS_0022`.
- related_RSG: `RSG_MEXEMP_0018`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0025`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Useful for French command rooms and conservative envoy scenes.
- factual_risk_notes: Do not let French policy documents stand in for Mexican consent.
- source_gap_notes: Conservative Mexican monarchy planning needs Mexican-side checking.
- manual_review_needed: yes.

### CTL_MEXEMP_0009

- date_or_range: 1863-03 to 1863-06-10.
- chronology_precision: exact.
- core_event: Second Puebla siege, Juarez evacuation, French entry into Mexico City.
- historical_summary: French forces take Puebla after a second campaign, Juarez evacuates the capital, and French troops enter Mexico City.
- narrative_phase: French intervention.
- related_CDL: `CDL_MEXEMP_0003`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0025`.
- related_timeline_cards: `TIME_MEXEMP_0086-0091`.
- related_fact_cards: `FACT_MEXEMP_0508-0544`.
- related_capture_cards: `CAP_MEXEMP_0020-0022`.
- related_person_cards: `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0002`; `NSI_SHAWCROSS_0022`; `NSI_SHAWCROSS_0024`; `NSI_SHAWCROSS_0026`.
- related_SRM: `SRM_SHAWCROSS_0002`; `SRM_SHAWCROSS_0022`; `SRM_SHAWCROSS_0024`; `SRM_SHAWCROSS_0026`.
- related_NRC: `NRC_SHAWCROSS_0002`; `NRC_SHAWCROSS_0022`; `NRC_SHAWCROSS_0024`; `NRC_SHAWCROSS_0026`.
- related_RSG: `RSG_MEXEMP_0007`; `RSG_MEXEMP_0008`; `RSG_MEXEMP_0011`; `RSG_MEXEMP_0013`.
- related_HJI: `HJI_MEXEMP_0009`; `HJI_MEXEMP_0010`; `HJI_MEXEMP_0012`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: medium.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Works as a dual scene: French entry and republican evacuation.
- factual_risk_notes: Avoid framing Juarez's departure as flight without legality and continuity context.
- source_gap_notes: Need route and government-continuity documentation from republican sources.
- manual_review_needed: yes.

### CTL_MEXEMP_0010

- date_or_range: 1863-06 to 1863-07-11.
- chronology_precision: exact.
- core_event: Junta, regency, and declaration of empire.
- historical_summary: French-backed institutions move toward monarchy, forming a regency and declaring the empire.
- narrative_phase: imperial formation.
- related_CDL: `CDL_MEXEMP_0004`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0018`.
- related_timeline_cards: `TIME_MEXEMP_0092-0094`; `TIME_MEXEMP_0103`.
- related_fact_cards: `FACT_MEXEMP_0563-0567`.
- related_capture_cards: `CAP_MEXEMP_0023`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0006`; `NSI_SHAWCROSS_0024`; `NSI_SHAWCROSS_0027`; `NSI_SHAWCROSS_0028`; `NSI_SHAWCROSS_0029`.
- related_SRM: `SRM_SHAWCROSS_0006`; `SRM_SHAWCROSS_0024`; `SRM_SHAWCROSS_0027`; `SRM_SHAWCROSS_0028`; `SRM_SHAWCROSS_0029`.
- related_NRC: `NRC_SHAWCROSS_0006`; `NRC_SHAWCROSS_0024`; `NRC_SHAWCROSS_0027`; `NRC_SHAWCROSS_0028`; `NRC_SHAWCROSS_0029`.
- related_RSG: `RSG_MEXEMP_0013`; `RSG_MEXEMP_0014`; `RSG_MEXEMP_0015`; `RSG_MEXEMP_0016`; `RSG_MEXEMP_0018`.
- related_HJI: `HJI_MEXEMP_0018`; `HJI_MEXEMP_0019`; `HJI_MEXEMP_0025`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Can be built as staged legitimacy, signatures, public ceremony, and quiet dissent.
- factual_risk_notes: Do not treat junta procedures as broad national consent.
- source_gap_notes: Need Mexican conservative and republican press comparison.
- manual_review_needed: yes.

### CTL_MEXEMP_0011

- date_or_range: 1863-10 to 1863-12.
- chronology_precision: month.
- core_event: Crown offer, Bazaine, regency conflict, and Juarez under pressure.
- historical_summary: The crown is presented while French and conservative politics continue to shape the future empire, and Juarez's government remains under military pressure.
- narrative_phase: imperial formation.
- related_CDL: `CDL_MEXEMP_0004`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0007`; `NCD_MEXEMP_0009`; `NCD_MEXEMP_0017`; `NCD_MEXEMP_0018`.
- related_timeline_cards: `TIME_MEXEMP_0095`; `TIME_MEXEMP_0104-0118`.
- related_fact_cards: `FACT_MEXEMP_0672-0705`.
- related_capture_cards: `CAP_MEXEMP_0024-0032`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`; `ORG-CATHOLIC-CHURCH`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`; `THM-LIBERAL-REFORM`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0006`; `NSI_SHAWCROSS_0020`; `NSI_SHAWCROSS_0024`; `NSI_SHAWCROSS_0030`.
- related_SRM: `SRM_SHAWCROSS_0006`; `SRM_SHAWCROSS_0020`; `SRM_SHAWCROSS_0024`; `SRM_SHAWCROSS_0030`.
- related_NRC: `NRC_SHAWCROSS_0006`; `NRC_SHAWCROSS_0020`; `NRC_SHAWCROSS_0024`; `NRC_SHAWCROSS_0030`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0013`; `RSG_MEXEMP_0020`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0014`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Useful for showing Maximilian's imagined mandate against Mexican political fractures.
- factual_risk_notes: Conservative invitation and foreign military pressure must not be conflated.
- source_gap_notes: Juarez-side pressure and provincial support require republican-source strengthening.
- manual_review_needed: yes.

### CTL_MEXEMP_0012

- date_or_range: 1864-01 to 1864-03.
- chronology_precision: month.
- core_event: Miramar, Paris, Vienna, and treaty pressure.
- historical_summary: Maximilian, Carlota, Napoleon III, and Franz Joseph negotiate status, guarantees, and dynastic cost before acceptance.
- narrative_phase: imperial formation.
- related_CDL: `CDL_MEXEMP_0002`; `CDL_MEXEMP_0004`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0031`.
- related_timeline_cards: `TIME_MEXEMP_0119-0129`.
- related_fact_cards: `FACT_MEXEMP_0739-0786`.
- related_capture_cards: `CAP_MEXEMP_0031-0033`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`; `PER-FRANZ-JOSEPH`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: `PLC-MIRAMAR`.
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0001`; `NSI_SHAWCROSS_0004`; `NSI_SHAWCROSS_0016`; `NSI_SHAWCROSS_0020`.
- related_SRM: `SRM_SHAWCROSS_0001`; `SRM_SHAWCROSS_0004`; `SRM_SHAWCROSS_0016`; `SRM_SHAWCROSS_0020`.
- related_NRC: `NRC_SHAWCROSS_0001`; `NRC_SHAWCROSS_0004`; `NRC_SHAWCROSS_0016`; `NRC_SHAWCROSS_0020`.
- related_RSG: `RSG_MEXEMP_0018`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0025`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Strong court, negotiation, family pressure, and treaty-room material.
- factual_risk_notes: Do not let dynastic drama erase Mexican legality and coercion.
- source_gap_notes: Treaty and correspondence should be checked against French and Austrian archives.
- manual_review_needed: yes.

### CTL_MEXEMP_0013

- date_or_range: 1864-04 to 1864-05-28.
- chronology_precision: exact.
- core_event: Crown acceptance, Treaty of Miramar, departure, Veracruz arrival.
- historical_summary: Maximilian and Carlota accept the Mexican crown, leave Europe, and arrive near Veracruz.
- narrative_phase: imperial formation.
- related_CDL: `CDL_MEXEMP_0002`; `CDL_MEXEMP_0004`; `CDL_MEXEMP_0005`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0031`.
- related_timeline_cards: `TIME_MEXEMP_0136-0146`.
- related_fact_cards: `FACT_MEXEMP_0811-0870`.
- related_capture_cards: `CAP_MEXEMP_0034-0037`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`; `PER-FRANZ-JOSEPH`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: `PLC-MIRAMAR`.
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0001`; `NSI_SHAWCROSS_0004`; `NSI_SHAWCROSS_0016`; `NSI_SHAWCROSS_0020`.
- related_SRM: `SRM_SHAWCROSS_0001`; `SRM_SHAWCROSS_0004`; `SRM_SHAWCROSS_0016`; `SRM_SHAWCROSS_0020`.
- related_NRC: `NRC_SHAWCROSS_0001`; `NRC_SHAWCROSS_0004`; `NRC_SHAWCROSS_0016`; `NRC_SHAWCROSS_0020`.
- related_RSG: `RSG_MEXEMP_0018`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0025`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Arrival contrast between European expectation and Mexican political reality.
- factual_risk_notes: Arrival does not equal national acceptance.
- source_gap_notes: Need Mexican local reception sources, not only court memory.
- manual_review_needed: yes.

### CTL_MEXEMP_0014

- date_or_range: 1864-06 to 1864-10.
- chronology_precision: month.
- core_event: Mexico City ceremonies, court formation, travel, Juarez displacement.
- historical_summary: The new imperial court forms and stages public legitimacy while Juarez's republican government continues in movement and resistance.
- narrative_phase: imperial formation.
- related_CDL: `CDL_MEXEMP_0005`; `CDL_MEXEMP_0007`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0017`; `NCD_MEXEMP_0025`.
- related_timeline_cards: `TIME_MEXEMP_0147-0168`.
- related_fact_cards: `FACT_MEXEMP_0883`; `FACT_MEXEMP_0892`; `FACT_MEXEMP_0977-0978`; `FACT_MEXEMP_1015-1019`.
- related_capture_cards: `CAP_MEXEMP_0038-0043`; `CAP_MEXEMP_0045`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`; `ORG-CATHOLIC-CHURCH`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`; `THM-LIBERAL-REFORM`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0020`; `NSI_SHAWCROSS_0023`; `NSI_SHAWCROSS_0026`.
- related_SRM: `SRM_SHAWCROSS_0020`; `SRM_SHAWCROSS_0023`; `SRM_SHAWCROSS_0026`.
- related_NRC: `NRC_SHAWCROSS_0020`; `NRC_SHAWCROSS_0023`; `NRC_SHAWCROSS_0026`.
- related_RSG: `RSG_MEXEMP_0007`; `RSG_MEXEMP_0010`; `RSG_MEXEMP_0011`; `RSG_MEXEMP_0020`.
- related_HJI: `HJI_MEXEMP_0009`; `HJI_MEXEMP_0012`; `HJI_MEXEMP_0014`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Use ceremony, travel, language encounter, and displaced republican governance in counterpoint.
- factual_risk_notes: Nahuatl and indigenous-policy episodes must avoid decorative exoticism.
- source_gap_notes: Indigenous and republican reception sources are thin.
- manual_review_needed: yes.

### CTL_MEXEMP_0015

- date_or_range: 1864-12.
- chronology_precision: month.
- core_event: Meglia, Syllabus, and church-policy decree.
- historical_summary: Papal, imperial, conservative, and liberal expectations collide around church property and the empire's liberal policy direction.
- narrative_phase: liberal empire.
- related_CDL: `CDL_MEXEMP_0006`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0017`.
- related_timeline_cards: `TIME_MEXEMP_0172`; `TIME_MEXEMP_0174-0178`.
- related_fact_cards: `FACT_MEXEMP_1137-1166`.
- related_capture_cards: `CAP_MEXEMP_0046-0051`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-CATHOLIC-CHURCH`; `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LIBERAL-REFORM`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0030`; `NSI_SHAWCROSS_0031`; `NSI_SHAWCROSS_0033`.
- related_SRM: `SRM_SHAWCROSS_0030`; `SRM_SHAWCROSS_0031`; `SRM_SHAWCROSS_0033`.
- related_NRC: `NRC_SHAWCROSS_0030`; `NRC_SHAWCROSS_0031`; `NRC_SHAWCROSS_0033`.
- related_RSG: `RSG_MEXEMP_0020`.
- related_HJI: `HJI_MEXEMP_0014`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Strong for nuncio audience, decree drafting, conservative shock, and Carlota's political reading.
- factual_risk_notes: Do not confuse papal condemnation, local clergy interests, and imperial liberalism.
- source_gap_notes: Need legal text and church-state documents.
- manual_review_needed: yes.

### CTL_MEXEMP_0016

- date_or_range: 1865-01 to 1865-05.
- chronology_precision: month.
- core_event: Liberal Empire backlash, Dano, Bazaine, Oaxaca, and Juarez pressure.
- historical_summary: The imperial project continues liberal policies while military and diplomatic pressure grow, exposing the contradiction between monarchy and reform.
- narrative_phase: liberal empire.
- related_CDL: `CDL_MEXEMP_0006`; `CDL_MEXEMP_0008`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0014`; `NCD_MEXEMP_0015`; `NCD_MEXEMP_0016`; `NCD_MEXEMP_0017`.
- related_timeline_cards: `TIME_MEXEMP_0184-0189`; `TIME_MEXEMP_0194-0195`.
- related_fact_cards: `FACT_MEXEMP_1262-1306`; `FACT_MEXEMP_1327-1340`.
- related_capture_cards: `CAP_MEXEMP_0053-0057`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`; `ORG-CATHOLIC-CHURCH`.
- related_theme_cards: `THM-LIBERAL-REFORM`; `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0002`; `NSI_SHAWCROSS_0011`; `NSI_SHAWCROSS_0031`; `NSI_SHAWCROSS_0033`.
- related_SRM: `SRM_SHAWCROSS_0002`; `SRM_SHAWCROSS_0011`; `SRM_SHAWCROSS_0031`; `SRM_SHAWCROSS_0033`.
- related_NRC: `NRC_SHAWCROSS_0002`; `NRC_SHAWCROSS_0011`; `NRC_SHAWCROSS_0031`; `NRC_SHAWCROSS_0033`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0012`; `RSG_MEXEMP_0020`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0013`; `HJI_MEXEMP_0014`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Can show the empire's liberal self-image becoming politically homeless.
- factual_risk_notes: Bazaine and French pressure should be separated from Mexican conservative reaction.
- source_gap_notes: Need Mexican conservative correspondence and republican press.
- manual_review_needed: yes.

### CTL_MEXEMP_0017

- date_or_range: 1865-06 to 1865-10.
- chronology_precision: month.
- core_event: U.S. pressure, Brownsville / Matamoros, and Black Decree.
- historical_summary: The end of the U.S. Civil War changes strategic pressure; border arms, republican movement, and the Black Decree intensify the conflict.
- narrative_phase: U.S. pressure.
- related_CDL: `CDL_MEXEMP_0008`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0014`; `NCD_MEXEMP_0015`; `NCD_MEXEMP_0016`.
- related_timeline_cards: `TIME_MEXEMP_0195-0200`.
- related_fact_cards: `FACT_MEXEMP_1128`; `FACT_MEXEMP_1367-1370`; `FACT_MEXEMP_1546-1555`.
- related_capture_cards: `CAP_MEXEMP_0054-0057`; `CAP_MEXEMP_0065-0066`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0011`; `NSI_SHAWCROSS_0023`; `NSI_SHAWCROSS_0035`.
- related_SRM: `SRM_SHAWCROSS_0011`; `SRM_SHAWCROSS_0023`; `SRM_SHAWCROSS_0035`.
- related_NRC: `NRC_SHAWCROSS_0011`; `NRC_SHAWCROSS_0023`; `NRC_SHAWCROSS_0035`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0010`; `RSG_MEXEMP_0011`; `RSG_MEXEMP_0012`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0012`; `HJI_MEXEMP_0013`; `HJI_MEXEMP_0015`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Border rumors, arms flows, decree drafting, and republican reaction can run in parallel.
- factual_risk_notes: Black Decree must be checked through legal text, military implementation, and republican response.
- source_gap_notes: Need U.S. official documents, Mexican republican military reports, and liberal press.
- manual_review_needed: yes.

### CTL_MEXEMP_0018

- date_or_range: 1865-10 to 1865-12.
- chronology_precision: month.
- core_event: Carlota in Yucatan and Maximilian's letters to Carlota / Napoleon.
- historical_summary: Imperial projection continues through travel and correspondence while military and diplomatic pressures sharpen.
- narrative_phase: liberal empire.
- related_CDL: `CDL_MEXEMP_0007`; `CDL_MEXEMP_0009`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0020`; `NCD_MEXEMP_0021`.
- related_timeline_cards: `TIME_MEXEMP_0201-0204`; `TIME_MEXEMP_0217`.
- related_fact_cards: `FACT_MEXEMP_1392-1413`; `FACT_MEXEMP_1428`.
- related_capture_cards: `CAP_MEXEMP_0057-0058`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0016`; `NSI_SHAWCROSS_0020`; `NSI_SHAWCROSS_0023`.
- related_SRM: `SRM_SHAWCROSS_0016`; `SRM_SHAWCROSS_0020`; `SRM_SHAWCROSS_0023`.
- related_NRC: `NRC_SHAWCROSS_0016`; `NRC_SHAWCROSS_0020`; `NRC_SHAWCROSS_0023`.
- related_RSG: `RSG_MEXEMP_0010`; `RSG_MEXEMP_0011`; `RSG_MEXEMP_0018`.
- related_HJI: `HJI_MEXEMP_0012`; `HJI_MEXEMP_0025`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Carlota should be shown as political actor, not only future victim.
- factual_risk_notes: Personal letters should not substitute for the national situation.
- source_gap_notes: Need local reception and republican response.
- manual_review_needed: yes.

### CTL_MEXEMP_0019

- date_or_range: 1866-01 to 1866-02.
- chronology_precision: month.
- core_event: Napoleon withdrawal decision, Schofield, Leopold death, Cuernavaca crisis.
- historical_summary: French withdrawal becomes concrete, U.S. pressure rises, and dynastic grief intersects with imperial political crisis.
- narrative_phase: French withdrawal.
- related_CDL: `CDL_MEXEMP_0009`; `CDL_MEXEMP_0010`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0014`; `NCD_MEXEMP_0021`; `NCD_MEXEMP_0022`; `NCD_MEXEMP_0031`.
- related_timeline_cards: `TIME_MEXEMP_0215-0221`.
- related_fact_cards: `FACT_MEXEMP_1428-1475`.
- related_capture_cards: `CAP_MEXEMP_0058-0061`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`; `PER-FRANZ-JOSEPH`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0001`; `NSI_SHAWCROSS_0002`; `NSI_SHAWCROSS_0035`; `NSI_SHAWCROSS_0047`.
- related_SRM: `SRM_SHAWCROSS_0001`; `SRM_SHAWCROSS_0002`; `SRM_SHAWCROSS_0035`; `SRM_SHAWCROSS_0047`.
- related_NRC: `NRC_SHAWCROSS_0001`; `NRC_SHAWCROSS_0002`; `NRC_SHAWCROSS_0035`; `NRC_SHAWCROSS_0047`.
- related_RSG: `RSG_MEXEMP_0012`; `RSG_MEXEMP_0018`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0013`; `HJI_MEXEMP_0025`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Use letter, annual message, family death, and Cuernavaca setting as a crisis cluster.
- factual_risk_notes: Personal collapse and imperial policy decision must be separated.
- source_gap_notes: Need French legislative and U.S. diplomatic source confirmation.
- manual_review_needed: yes.

### CTL_MEXEMP_0020

- date_or_range: 1866-03 to 1866-04.
- chronology_precision: month.
- core_event: Langlais reforms, finance crisis, and paper empire problem.
- historical_summary: Administrative and financial reform efforts expose the empire's limited real reach and its dependence on paper institutions.
- narrative_phase: liberal empire.
- related_CDL: `CDL_MEXEMP_0007`; `CDL_MEXEMP_0010`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0021`.
- related_timeline_cards: `TIME_MEXEMP_0222-0228`.
- related_fact_cards: `FACT_MEXEMP_1531-1536`.
- related_capture_cards: `CAP_MEXEMP_0062-0065`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-LIBERAL-REFORM`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0020`; `NSI_SHAWCROSS_0023`; `NSI_SHAWCROSS_0026`.
- related_SRM: `SRM_SHAWCROSS_0020`; `SRM_SHAWCROSS_0023`; `SRM_SHAWCROSS_0026`.
- related_NRC: `NRC_SHAWCROSS_0020`; `NRC_SHAWCROSS_0023`; `NRC_SHAWCROSS_0026`.
- related_RSG: `RSG_MEXEMP_0007`; `RSG_MEXEMP_0010`; `RSG_MEXEMP_0011`.
- related_HJI: `HJI_MEXEMP_0009`; `HJI_MEXEMP_0012`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Useful as bureaucracy, academy, decree, and empty-map material.
- factual_risk_notes: "Paper empire" is an interpretive label; anchor it in concrete administrative failures.
- source_gap_notes: Imperial Academy and similar cultural institutions need explicit existing-card verification.
- manual_review_needed: yes.

### CTL_MEXEMP_0021

- date_or_range: 1866-05 to 1866-07.
- chronology_precision: month.
- core_event: Volunteers, Matamoros collapse, Carlota departure, Monterrey.
- historical_summary: Border and northern losses combine with Carlota's decision to seek European support.
- narrative_phase: U.S. pressure.
- related_CDL: `CDL_MEXEMP_0008`; `CDL_MEXEMP_0009`; `CDL_MEXEMP_0010`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0014`; `NCD_MEXEMP_0015`; `NCD_MEXEMP_0025`.
- related_timeline_cards: `TIME_MEXEMP_0230-0237`; `TIME_MEXEMP_0259-0268`.
- related_fact_cards: `FACT_MEXEMP_1707-1775`.
- related_capture_cards: `CAP_MEXEMP_0067-0074`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0011`; `NSI_SHAWCROSS_0035`; `NSI_SHAWCROSS_0042`.
- related_SRM: `SRM_SHAWCROSS_0011`; `SRM_SHAWCROSS_0035`; `SRM_SHAWCROSS_0042`.
- related_NRC: `NRC_SHAWCROSS_0011`; `NRC_SHAWCROSS_0035`; `NRC_SHAWCROSS_0042`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0012`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0013`; `HJI_MEXEMP_0024`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Strong split-stage sequence: border collapse and Carlota's departure.
- factual_risk_notes: Carlota's departure should not erase republican military agency.
- source_gap_notes: Matamoros and Monterrey require Mexican republican and U.S. border-source checks.
- manual_review_needed: yes.

### CTL_MEXEMP_0022

- date_or_range: 1866-08 to 1866-09.
- chronology_precision: month.
- core_event: Carlota in France and Rome; Seward protest; Castelnau orders.
- historical_summary: Carlota's European mission fails while U.S. diplomatic pressure and French withdrawal planning harden.
- narrative_phase: French withdrawal.
- related_CDL: `CDL_MEXEMP_0009`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0002`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0006`; `NCD_MEXEMP_0014`; `NCD_MEXEMP_0022`; `NCD_MEXEMP_0031`.
- related_timeline_cards: `TIME_MEXEMP_0238-0250`; `TIME_MEXEMP_0256-0258`; `TIME_MEXEMP_0275-0281`.
- related_fact_cards: `FACT_MEXEMP_1808-1880`; `FACT_MEXEMP_1833-1834`.
- related_capture_cards: `CAP_MEXEMP_0068-0078`.
- related_person_cards: `PER-CARLOTA`; `PER-NAPOLEON-III`; `PER-FRANZ-JOSEPH`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`; `EVT-FRENCH-INTERVENTION-IN-MEXICO`.
- related_place_cards: none existing.
- related_org_cards: `ORG-HABSBURG`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0001`; `NSI_SHAWCROSS_0003`; `NSI_SHAWCROSS_0035`; `NSI_SHAWCROSS_0042`; `NSI_SHAWCROSS_0047`.
- related_SRM: `SRM_SHAWCROSS_0001`; `SRM_SHAWCROSS_0003`; `SRM_SHAWCROSS_0035`; `SRM_SHAWCROSS_0042`; `SRM_SHAWCROSS_0047`.
- related_NRC: `NRC_SHAWCROSS_0001`; `NRC_SHAWCROSS_0003`; `NRC_SHAWCROSS_0035`; `NRC_SHAWCROSS_0042`; `NRC_SHAWCROSS_0047`.
- related_RSG: `RSG_MEXEMP_0012`; `RSG_MEXEMP_0018`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0013`; `HJI_MEXEMP_0025`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Use Carlota as a diplomatic actor whose mission collapses across capitals.
- factual_risk_notes: Her mental crisis must not become the only explanation for imperial collapse.
- source_gap_notes: Papal and French records need checking against memoir traditions.
- manual_review_needed: yes.

### CTL_MEXEMP_0023

- date_or_range: 1866-10 to 1866-11.
- chronology_precision: month.
- core_event: Orizaba / El Olindo abdication crisis, Miramon return, and court politics.
- historical_summary: Maximilian considers departure or abdication, but conservative and court pressures redirect him toward a final Mexican stand.
- narrative_phase: French withdrawal.
- related_CDL: `CDL_MEXEMP_0010`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0006`; `NCD_MEXEMP_0007`; `NCD_MEXEMP_0019`; `NCD_MEXEMP_0020`; `NCD_MEXEMP_0021`.
- related_timeline_cards: `TIME_MEXEMP_0282-0291`; `TIME_MEXEMP_0298-0301`.
- related_fact_cards: `FACT_MEXEMP_1909-1936`.
- related_capture_cards: `CAP_MEXEMP_0072-0079`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-HABSBURG`.
- related_theme_cards: `THM-LEGITIMACY`; `THM-FOREIGN-INTERVENTION`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0001`; `NSI_SHAWCROSS_0020`; `NSI_SHAWCROSS_0043`; `NSI_SHAWCROSS_0047`.
- related_SRM: `SRM_SHAWCROSS_0001`; `SRM_SHAWCROSS_0020`; `SRM_SHAWCROSS_0043`; `SRM_SHAWCROSS_0047`.
- related_NRC: `NRC_SHAWCROSS_0001`; `NRC_SHAWCROSS_0020`; `NRC_SHAWCROSS_0043`; `NRC_SHAWCROSS_0047`.
- related_RSG: `RSG_MEXEMP_0018`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0025`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Strong enclosed-palace and ship-departure tension.
- factual_risk_notes: Do not overstate single-person influence from Eloin, Faverney, or Fischer without source checks.
- source_gap_notes: Faverney and El Olindo details require manual review; some related people have no Person cards.
- manual_review_needed: yes.

### CTL_MEXEMP_0024

- date_or_range: 1866-12 to 1867-01.
- chronology_precision: exact.
- core_event: French withdrawal sequence, U.S. border pressure, Castagny, Zacatecas.
- historical_summary: French withdrawal proceeds while republican forces gain room, and the imperial military situation narrows.
- narrative_phase: French withdrawal.
- related_CDL: `CDL_MEXEMP_0011`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0005`; `NCD_MEXEMP_0022`; `NCD_MEXEMP_0023`; `NCD_MEXEMP_0024`; `NCD_MEXEMP_0025`.
- related_timeline_cards: `TIME_MEXEMP_0323-0343`.
- related_fact_cards: `FACT_MEXEMP_2029-2105`.
- related_capture_cards: `CAP_MEXEMP_0084-0088`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`.
- related_event_cards: `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-FOREIGN-INTERVENTION`; `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0001`; `NSI_SHAWCROSS_0022`; `NSI_SHAWCROSS_0035`; `NSI_SHAWCROSS_0041`; `NSI_SHAWCROSS_0042`.
- related_SRM: `SRM_SHAWCROSS_0001`; `SRM_SHAWCROSS_0022`; `SRM_SHAWCROSS_0035`; `SRM_SHAWCROSS_0041`; `SRM_SHAWCROSS_0042`.
- related_NRC: `NRC_SHAWCROSS_0001`; `NRC_SHAWCROSS_0022`; `NRC_SHAWCROSS_0035`; `NRC_SHAWCROSS_0041`; `NRC_SHAWCROSS_0042`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0012`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0013`; `HJI_MEXEMP_0024`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: medium.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Use military maps, orders, and shifting border news.
- factual_risk_notes: Republican advance should not be written as empty backdrop to French departure.
- source_gap_notes: Need Escobedo, Diaz, and republican command documentation.
- manual_review_needed: yes.

### CTL_MEXEMP_0025

- date_or_range: 1867-02 to 1867-03-14.
- chronology_precision: exact.
- core_event: Maximilian goes to Queretaro and siege begins.
- historical_summary: Maximilian concentrates forces at Queretaro, where republican siege operations begin.
- narrative_phase: Querétaro.
- related_CDL: `CDL_MEXEMP_0011`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0007`; `NCD_MEXEMP_0008`; `NCD_MEXEMP_0009`; `NCD_MEXEMP_0024`.
- related_timeline_cards: `TIME_MEXEMP_0344-0355`.
- related_fact_cards: `FACT_MEXEMP_2110-2217`.
- related_capture_cards: `CAP_MEXEMP_0088-0090`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: `PLC-QUERETARO`.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0022`; `NSI_SHAWCROSS_0037`; `NSI_SHAWCROSS_0038`; `NSI_SHAWCROSS_0039`; `NSI_SHAWCROSS_0040`.
- related_SRM: `SRM_SHAWCROSS_0022`; `SRM_SHAWCROSS_0037`; `SRM_SHAWCROSS_0038`; `SRM_SHAWCROSS_0039`; `SRM_SHAWCROSS_0040`.
- related_NRC: `NRC_SHAWCROSS_0022`; `NRC_SHAWCROSS_0037`; `NRC_SHAWCROSS_0038`; `NRC_SHAWCROSS_0039`; `NRC_SHAWCROSS_0040`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0009`; `RSG_MEXEMP_0021`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0011`; `HJI_MEXEMP_0016`; `HJI_MEXEMP_0023`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Arrival, command debate, and siege geometry can carry the final-act turn.
- factual_risk_notes: Need republican operational perspective from Escobedo's side.
- source_gap_notes: Existing Person card exists only for Maximilian/Juarez, not Miramon, Mejia, Marquez, or Escobedo.
- manual_review_needed: yes.

### CTL_MEXEMP_0026

- date_or_range: 1867-03 to 1867-04.
- chronology_precision: month.
- core_event: Siege councils, sorties, Marquez mission, Miramon / Mejia choices.
- historical_summary: Queretaro becomes a closed decision-space where imperial commanders argue, sortie, and seek relief while republicans tighten control.
- narrative_phase: Querétaro.
- related_CDL: `CDL_MEXEMP_0011`; `CDL_MEXEMP_0015`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0007`; `NCD_MEXEMP_0008`; `NCD_MEXEMP_0009`; `NCD_MEXEMP_0024`.
- related_timeline_cards: `TIME_MEXEMP_0356-0366`.
- related_fact_cards: `FACT_MEXEMP_2218-2315`.
- related_capture_cards: `CAP_MEXEMP_0091-0093`.
- related_person_cards: `PER-MAXIMILIAN`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: `PLC-QUERETARO`.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0022`; `NSI_SHAWCROSS_0037`; `NSI_SHAWCROSS_0038`; `NSI_SHAWCROSS_0039`; `NSI_SHAWCROSS_0040`.
- related_SRM: `SRM_SHAWCROSS_0022`; `SRM_SHAWCROSS_0037`; `SRM_SHAWCROSS_0038`; `SRM_SHAWCROSS_0039`; `SRM_SHAWCROSS_0040`.
- related_NRC: `NRC_SHAWCROSS_0022`; `NRC_SHAWCROSS_0037`; `NRC_SHAWCROSS_0038`; `NRC_SHAWCROSS_0039`; `NRC_SHAWCROSS_0040`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0009`; `RSG_MEXEMP_0021`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0011`; `HJI_MEXEMP_0016`; `HJI_MEXEMP_0023`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Strong for council-room conflict, military risk, and silence between commanders.
- factual_risk_notes: Memoir testimony must be checked against military records.
- source_gap_notes: Republican siege logs and maps are needed.
- manual_review_needed: yes.

### CTL_MEXEMP_0027

- date_or_range: 1867-05-05 to 1867-05-15.
- chronology_precision: exact.
- core_event: Final attack, Lopez betrayal, capture, surrender to Escobedo.
- historical_summary: The Queretaro defense collapses after final republican pressure and disputed betrayal / surrender narratives.
- narrative_phase: Querétaro.
- related_CDL: `CDL_MEXEMP_0011`; `CDL_MEXEMP_0015`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0007`; `NCD_MEXEMP_0008`; `NCD_MEXEMP_0009`; `NCD_MEXEMP_0024`.
- related_timeline_cards: `TIME_MEXEMP_0367-0375`.
- related_fact_cards: `FACT_MEXEMP_2316-2365`.
- related_capture_cards: `CAP_MEXEMP_0094-0095`.
- related_person_cards: `PER-MAXIMILIAN`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: `PLC-QUERETARO`.
- related_org_cards: `ORG-MEXICAN-CONSERVATIVES`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0022`; `NSI_SHAWCROSS_0037`; `NSI_SHAWCROSS_0038`; `NSI_SHAWCROSS_0039`; `NSI_SHAWCROSS_0040`.
- related_SRM: `SRM_SHAWCROSS_0022`; `SRM_SHAWCROSS_0037`; `SRM_SHAWCROSS_0038`; `SRM_SHAWCROSS_0039`; `SRM_SHAWCROSS_0040`.
- related_NRC: `NRC_SHAWCROSS_0022`; `NRC_SHAWCROSS_0037`; `NRC_SHAWCROSS_0038`; `NRC_SHAWCROSS_0039`; `NRC_SHAWCROSS_0040`.
- related_RSG: `RSG_MEXEMP_0008`; `RSG_MEXEMP_0009`; `RSG_MEXEMP_0021`.
- related_HJI: `HJI_MEXEMP_0010`; `HJI_MEXEMP_0011`; `HJI_MEXEMP_0016`; `HJI_MEXEMP_0023`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Use contested betrayal as uncertainty, not as settled melodrama.
- factual_risk_notes: Lopez narrative is memoir-sensitive and politically charged.
- source_gap_notes: `CAP_MEXEMP_0096`, `FACT_MEXEMP_2366-2389`, and `TIME_MEXEMP_0376-0378` are absent/gap areas, not filled here.
- manual_review_needed: yes.

### CTL_MEXEMP_0028

- date_or_range: 1867-05-30 to 1867-06-03.
- chronology_precision: exact.
- core_event: Trial preparation, escape plans, and Salm-Salm intervention.
- historical_summary: After capture, trial preparation and attempted intervention by the Salm-Salm witness cluster begin to shape memory of the final days.
- narrative_phase: trial / execution.
- related_CDL: `CDL_MEXEMP_0012`; `CDL_MEXEMP_0015`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0010`; `NCD_MEXEMP_0011`; `NCD_MEXEMP_0012`; `NCD_MEXEMP_0013`; `NCD_MEXEMP_0024`.
- related_timeline_cards: `TIME_MEXEMP_0379-0386`.
- related_fact_cards: `FACT_MEXEMP_2390-2438`.
- related_capture_cards: `CAP_MEXEMP_0097-0098`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: `PLC-QUERETARO`.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0037`; `NSI_SHAWCROSS_0038`; `NSI_SHAWCROSS_0039`; `NSI_SHAWCROSS_0040`.
- related_SRM: `SRM_SHAWCROSS_0037`; `SRM_SHAWCROSS_0038`; `SRM_SHAWCROSS_0039`; `SRM_SHAWCROSS_0040`.
- related_NRC: `NRC_SHAWCROSS_0037`; `NRC_SHAWCROSS_0038`; `NRC_SHAWCROSS_0039`; `NRC_SHAWCROSS_0040`.
- related_RSG: `RSG_MEXEMP_0009`; `RSG_MEXEMP_0021`.
- related_HJI: `HJI_MEXEMP_0011`; `HJI_MEXEMP_0017`; `HJI_MEXEMP_0023`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Courtroom, prison, petition, attempted escape, and witness-position scenes are available.
- factual_risk_notes: Salm-Salm claims require verification and should be signaled as testimony.
- source_gap_notes: Need court-martial records and republican legal framing.
- manual_review_needed: yes.

### CTL_MEXEMP_0029

- date_or_range: 1867-06-13.
- chronology_precision: exact.
- core_event: Court-martial timing, legal judgment, and Juarez delay.
- historical_summary: Trial timing and judgment become the legal hinge before the execution decision, with Juarez's role needing careful treatment.
- narrative_phase: trial / execution.
- related_CDL: `CDL_MEXEMP_0012`; `CDL_MEXEMP_0013`; `CDL_MEXEMP_0015`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0007`; `NCD_MEXEMP_0009`; `NCD_MEXEMP_0012`; `NCD_MEXEMP_0013`; `NCD_MEXEMP_0024`.
- related_timeline_cards: `TIME_MEXEMP_0382`.
- related_fact_cards: `FACT_MEXEMP_2416-2429`.
- related_capture_cards: `CAP_MEXEMP_0097-0102`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: `PLC-QUERETARO`.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0037`; `NSI_SHAWCROSS_0038`; `NSI_SHAWCROSS_0039`; `NSI_SHAWCROSS_0040`; `NSI_SHAWCROSS_0045`.
- related_SRM: `SRM_SHAWCROSS_0037`; `SRM_SHAWCROSS_0038`; `SRM_SHAWCROSS_0039`; `SRM_SHAWCROSS_0040`; `SRM_SHAWCROSS_0045`.
- related_NRC: `NRC_SHAWCROSS_0037`; `NRC_SHAWCROSS_0038`; `NRC_SHAWCROSS_0039`; `NRC_SHAWCROSS_0040`; `NRC_SHAWCROSS_0045`.
- related_RSG: `RSG_MEXEMP_0009`; `RSG_MEXEMP_0021`.
- related_HJI: `HJI_MEXEMP_0011`; `HJI_MEXEMP_0017`; `HJI_MEXEMP_0023`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Legal scene should include republican state reasoning, not only mercy appeals.
- factual_risk_notes: Juarez must not be reduced to a personal executioner; distinguish court, law, cabinet, and political necessity.
- source_gap_notes: `TIME_MEXEMP_0387-0413` and `FACT_MEXEMP_2439-2513` are absent/gap areas and are not linked as existing cards.
- manual_review_needed: yes.

### CTL_MEXEMP_0030

- date_or_range: 1867-06-19.
- chronology_precision: exact.
- core_event: Execution of Maximilian, Miramon, and Mejia.
- historical_summary: Maximilian, Miramon, and Mejia are executed at Queretaro; the moment becomes the central memory knot of empire, republic, and Europe.
- narrative_phase: trial / execution.
- related_CDL: `CDL_MEXEMP_0001`; `CDL_MEXEMP_0013`; `CDL_MEXEMP_0015`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0007`; `NCD_MEXEMP_0009`; `NCD_MEXEMP_0010`; `NCD_MEXEMP_0011`; `NCD_MEXEMP_0012`; `NCD_MEXEMP_0013`; `NCD_MEXEMP_0024`.
- related_timeline_cards: `TIME_MEXEMP_0002`; `TIME_MEXEMP_0414`.
- related_fact_cards: `FACT_MEXEMP_0001-0006`; `FACT_MEXEMP_2514`.
- related_capture_cards: `CAP_MEXEMP_0001`; `CAP_MEXEMP_0102`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-BENITO-JUAREZ`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: `PLC-QUERETARO`.
- related_org_cards: `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_UNSET_001`; `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0037`; `NSI_SHAWCROSS_0038`; `NSI_SHAWCROSS_0039`; `NSI_SHAWCROSS_0040`; `NSI_SHAWCROSS_0045`.
- related_SRM: `SRM_SHAWCROSS_0037`; `SRM_SHAWCROSS_0038`; `SRM_SHAWCROSS_0039`; `SRM_SHAWCROSS_0040`; `SRM_SHAWCROSS_0045`.
- related_NRC: `NRC_SHAWCROSS_0037`; `NRC_SHAWCROSS_0038`; `NRC_SHAWCROSS_0039`; `NRC_SHAWCROSS_0040`; `NRC_SHAWCROSS_0045`.
- related_RSG: `RSG_MEXEMP_0009`; `RSG_MEXEMP_0017`; `RSG_MEXEMP_0021`.
- related_HJI: `HJI_MEXEMP_0011`; `HJI_MEXEMP_0017`; `HJI_MEXEMP_0023`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: high.
- novel_use_notes: Use as controlled final scene, preserving Miramon, Mejia, republican officers, witnesses, and later memory.
- factual_risk_notes: `SRC_UNSET_001` cluster needs source replacement; execution details must avoid unverifiable set-piece invention.
- source_gap_notes: Execution-specific missing/gap IDs remain unfilled; no generated placeholders were created.
- manual_review_needed: yes.

### CTL_MEXEMP_0031

- date_or_range: 1867-06 to 1867-11-25.
- chronology_precision: exact.
- core_event: Body return diplomacy and Novara transfer.
- historical_summary: The handling and return of Maximilian's body becomes a diplomatic, dynastic, and memory-politics sequence.
- narrative_phase: aftermath / memory.
- related_CDL: `CDL_MEXEMP_0014`; `CDL_MEXEMP_0015`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0031`.
- related_timeline_cards: `TIME_MEXEMP_0414-0415`.
- related_fact_cards: `FACT_MEXEMP_2515-2519`.
- related_capture_cards: `CAP_MEXEMP_0103`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`; `PER-FRANZ-JOSEPH`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-REPUBLICANS`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0043`; `NSI_SHAWCROSS_0048`.
- related_SRM: `SRM_SHAWCROSS_0043`; `SRM_SHAWCROSS_0048`.
- related_NRC: `NRC_SHAWCROSS_0043`; `NRC_SHAWCROSS_0048`.
- related_RSG: `RSG_MEXEMP_0017`; `RSG_MEXEMP_0018`; `RSG_MEXEMP_0019`.
- related_HJI: `HJI_MEXEMP_0017`; `HJI_MEXEMP_0018`; `HJI_MEXEMP_0019`.
- evidence_strength: moderate.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Useful for restrained diplomatic aftermath and body-as-symbol scenes.
- factual_risk_notes: Avoid confusing posthumous ritual with the politics of the trial decision.
- source_gap_notes: Need diplomatic records for body transfer and Mexican-state positioning.
- manual_review_needed: yes.

### CTL_MEXEMP_0032

- date_or_range: 1868 and after.
- chronology_precision: approximate.
- core_event: Memory politics, Carlota's afterlife, European and Mexican remembrance.
- historical_summary: After the empire's fall, different political communities reinterpret Maximilian, Carlota, Juarez, and the republic.
- narrative_phase: aftermath / memory.
- related_CDL: `CDL_MEXEMP_0014`; `CDL_MEXEMP_0015`; `CDL_MEXEMP_0016`.
- related_NCD: `NCD_MEXEMP_0001`; `NCD_MEXEMP_0002`; `NCD_MEXEMP_0003`; `NCD_MEXEMP_0004`; `NCD_MEXEMP_0026`; `NCD_MEXEMP_0027`; `NCD_MEXEMP_0028`; `NCD_MEXEMP_0029`; `NCD_MEXEMP_0030`; `NCD_MEXEMP_0031`.
- related_timeline_cards: `TIME_MEXEMP_0416-0422`.
- related_fact_cards: `FACT_MEXEMP_2528-2560`.
- related_capture_cards: `CAP_MEXEMP_0103-0106`.
- related_person_cards: `PER-MAXIMILIAN`; `PER-CARLOTA`; `PER-BENITO-JUAREZ`; `PER-NAPOLEON-III`; `PER-FRANZ-JOSEPH`.
- related_event_cards: `EVT-SECOND-MEXICAN-EMPIRE`.
- related_place_cards: none existing.
- related_org_cards: `ORG-HABSBURG`; `ORG-MEXICAN-REPUBLICANS`; `ORG-MEXICAN-CONSERVATIVES`.
- related_theme_cards: `THM-LEGITIMACY`.
- related_source_cards: `SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO`.
- related_NSI: `NSI_SHAWCROSS_0024`; `NSI_SHAWCROSS_0027`; `NSI_SHAWCROSS_0028`; `NSI_SHAWCROSS_0029`; `NSI_SHAWCROSS_0048`.
- related_SRM: `SRM_SHAWCROSS_0024`; `SRM_SHAWCROSS_0027`; `SRM_SHAWCROSS_0028`; `SRM_SHAWCROSS_0029`; `SRM_SHAWCROSS_0048`.
- related_NRC: `NRC_SHAWCROSS_0024`; `NRC_SHAWCROSS_0027`; `NRC_SHAWCROSS_0028`; `NRC_SHAWCROSS_0029`; `NRC_SHAWCROSS_0048`.
- related_RSG: `RSG_MEXEMP_0013`; `RSG_MEXEMP_0014`; `RSG_MEXEMP_0015`; `RSG_MEXEMP_0016`; `RSG_MEXEMP_0017`.
- related_HJI: `HJI_MEXEMP_0018`; `HJI_MEXEMP_0019`; `HJI_MEXEMP_0023`; `HJI_MEXEMP_0025`.
- evidence_strength: mixed.
- republican_balance_needed: yes.
- maximilian_centered_risk: high.
- verification_needed: yes.
- scene_potential: medium.
- novel_use_notes: Use epilogue or interlaced memory rather than direct contemporaneous psychology.
- factual_risk_notes: Do not project later memory politics backward into 1867 decision-making.
- source_gap_notes: Separate liberal, conservative, European, memoir, and historiographical memory routes.
- manual_review_needed: yes.

## 8. Year-by-Year Timeline Notes

| Year / Range | CTL count | CTL IDs | Main function |
|---|---:|---|---|
| 1857-1858 prehistory | 1 | `CTL_MEXEMP_0001` | Legal and ideological groundwork. |
| 1859 | 2 | `CTL_MEXEMP_0002-0003` | Reform War memory and U.S.-Mexican liberal diplomacy gaps. |
| 1861 | 2 | `CTL_MEXEMP_0004-0005` | Juarez legality, debt crisis, and intervention opening. |
| 1862 | 3 | `CTL_MEXEMP_0006-0008` | Veracruz, La Soledad, Puebla, and French escalation. |
| 1863 | 3 | `CTL_MEXEMP_0009-0011` | Puebla fall, Mexico City, regency, and imperial declaration. |
| 1864 | 4 | `CTL_MEXEMP_0012-0015` | Miramar, arrival, court formation, church-policy rupture. |
| 1865 | 3 | `CTL_MEXEMP_0016-0018` | Liberal Empire contradiction and U.S. pressure. |
| 1866 | 5 | `CTL_MEXEMP_0019-0023` | French withdrawal decision, Carlota mission, border pressure, abdication crisis. |
| 1867 | 8 | `CTL_MEXEMP_0024-0031` | Final withdrawal, Queretaro, trial, execution, body return. |
| 1868 and after | 1 | `CTL_MEXEMP_0032` | Memory and aftermath. |

## 9. Phase-by-Phase Narrative Notes

| Narrative phase | CTL count | CTL IDs | Use note |
|---|---:|---|---|
| Reform / pre-intervention | 4 | `CTL_MEXEMP_0001-0004` | Needs the most republican-source reinforcement. |
| French intervention | 5 | `CTL_MEXEMP_0005-0009` | Strong event spine, but Mexican republican agency must stay visible. |
| imperial formation | 5 | `CTL_MEXEMP_0010-0014` | High Maximilian-centered risk; link ceremony to coercion and contested legitimacy. |
| liberal empire | 4 | `CTL_MEXEMP_0015-0016`; `0018`; `0020` | Shows the empire's liberal contradiction and conservative alienation. |
| U.S. pressure | 2 | `CTL_MEXEMP_0017`; `0021` | Needs U.S. official and border-source checking. |
| French withdrawal | 4 | `CTL_MEXEMP_0019`; `0022-0024` | Do not make withdrawal alone explain republican victory. |
| Querétaro | 3 | `CTL_MEXEMP_0025-0027` | Military, witness, and betrayal narratives need cross-checking. |
| trial / execution | 3 | `CTL_MEXEMP_0028-0030` | Keep legal process, mercy appeals, and memory separate. |
| aftermath / memory | 2 | `CTL_MEXEMP_0031-0032` | Avoid backward projection of later memory. |

## 10. Chapter Linkage Notes

- `CDL_MEXEMP_0001`: linked through `CTL_MEXEMP_0030` for the Queretaro prologue / execution setup.
- `CDL_MEXEMP_0002`: linked through `CTL_MEXEMP_0012-0013` as European planning and Miramar-adjacent background.
- `CDL_MEXEMP_0003`: linked through `CTL_MEXEMP_0005-0009`.
- `CDL_MEXEMP_0004`: linked through `CTL_MEXEMP_0008`; `0010-0013`.
- `CDL_MEXEMP_0005`: linked through `CTL_MEXEMP_0013-0014`.
- `CDL_MEXEMP_0006`: linked through `CTL_MEXEMP_0015-0016`.
- `CDL_MEXEMP_0007`: linked through `CTL_MEXEMP_0014`; `0018`; `0020`.
- `CDL_MEXEMP_0008`: linked through `CTL_MEXEMP_0016-0017`; `0021`.
- `CDL_MEXEMP_0009`: linked through `CTL_MEXEMP_0018-0019`; `0021-0022`.
- `CDL_MEXEMP_0010`: linked through `CTL_MEXEMP_0019-0021`; `0023`.
- `CDL_MEXEMP_0011`: linked through `CTL_MEXEMP_0024-0027`.
- `CDL_MEXEMP_0012`: linked through `CTL_MEXEMP_0028-0029`.
- `CDL_MEXEMP_0013`: linked through `CTL_MEXEMP_0029-0030`.
- `CDL_MEXEMP_0014`: linked through `CTL_MEXEMP_0031-0032`.
- `CDL_MEXEMP_0015`: linked through `CTL_MEXEMP_0026-0032`.
- `CDL_MEXEMP_0016`: linked across the whole timeline, especially `CTL_MEXEMP_0001-0007`; `0009-0011`; `0014-0017`; `0019-0030`; `0032`.

## 11. Character Linkage Notes

All `NCD_MEXEMP_0001-0031` are connected at least once by CTL row, either directly through core events or through memory/source-trail roles.

Primary existing Person-card connections:

- `PER-MAXIMILIAN`: `CTL_MEXEMP_0010-0032`, plus `CTL_MEXEMP_0030` via `SRC_UNSET_001` cluster.
- `PER-CARLOTA`: `CTL_MEXEMP_0012-0015`; `0018-0023`; `0031-0032`.
- `PER-BENITO-JUAREZ`: `CTL_MEXEMP_0001-0007`; `0009-0017`; `0020-0032`.
- `PER-NAPOLEON-III`: `CTL_MEXEMP_0005-0013`; `0016`; `0018-0019`; `0022-0024`; `0031-0032`.
- `PER-FRANZ-JOSEPH`: `CTL_MEXEMP_0012-0013`; `0019`; `0022`; `0031-0032`.

Missing-person-card candidate roles remain linked through NCD only, not as Person cards. This includes Bazaine, Castelnau, Miramon, Marquez, Mejia, Basch, Blasio, Felix Salm-Salm, Agnes Salm-Salm, Seward, Johnson, Lincoln, Meglia, the Iturbide group, Alice Green, Eloin, Faverney, Schofield, Castagny, Escobedo, Porfirio Diaz, Pedro Santacilia, Vigil, Zamacois, Arrangoiz, and Romero de Terreros.

## 12. Source Trail Linkage: NSI / SRM / NRC / RSG / HJI

- `NSI/SRM/NRC_SHAWCROSS_0001-0004`: French, diplomatic, Austrian, and Habsburg archive routes used mainly for `CTL_MEXEMP_0008`; `0012-0013`; `0019`; `0022-0024`.
- `NSI/SRM/NRC_SHAWCROSS_0006`: Gutiérrez de Estrada route, used for imperial formation `CTL_MEXEMP_0010-0011`.
- `NSI/SRM/NRC_SHAWCROSS_0008`; `0011`: debt, intervention, and U.S. official route, used for `CTL_MEXEMP_0005-0007`; `0016-0017`; `0021-0022`.
- `NSI/SRM/NRC_SHAWCROSS_0020-0023`: Maximilian, French / imperial military, and press routes used across imperial formation, Liberal Empire, and collapse.
- `NSI/SRM/NRC_SHAWCROSS_0024`; `0027-0029`: Mexican historiographical and memory routes used for Reform War, legitimacy, and postwar memory.
- `NSI/SRM/NRC_SHAWCROSS_0030-0033`: church-policy and legal-reform routes, used mainly for `CTL_MEXEMP_0015-0016`.
- `NSI/SRM/NRC_SHAWCROSS_0035`: Schofield / U.S. pressure route, used for `CTL_MEXEMP_0017`; `0019`; `0021-0024`.
- `NSI/SRM/NRC_SHAWCROSS_0037-0040`: Basch / Blasio / Salm-Salm witness cluster, used only with verification flags for `CTL_MEXEMP_0025-0030`.
- `NSI/SRM/NRC_SHAWCROSS_0041-0048`: late withdrawal, trial, legislative / public diplomacy, and memory routes, used for `CTL_MEXEMP_0023-0032`.
- `RSG_MEXEMP_0001-0022` and `HJI_MEXEMP_0001-0025` are attached where republican balance, trial legality, military reports, liberal press, U.S. sources, church-state law, and memory comparison are needed.

## 13. Scene Potential Notes

High scene-potential CTLs:

- `CTL_MEXEMP_0005`: debt crisis and intervention diplomacy.
- `CTL_MEXEMP_0006`: Veracruz / La Soledad / emergency legality.
- `CTL_MEXEMP_0007`: Puebla and French miscalculation.
- `CTL_MEXEMP_0009`: second Puebla siege and Juarez evacuation.
- `CTL_MEXEMP_0010`: junta and empire declaration.
- `CTL_MEXEMP_0012-0015`: Miramar, arrival, court formation, and church-policy rupture.
- `CTL_MEXEMP_0017`: Black Decree and border pressure.
- `CTL_MEXEMP_0019-0023`: withdrawal, paper empire, Carlota's mission, Orizaba / El Olindo.
- `CTL_MEXEMP_0025-0030`: Queretaro, trial, mercy appeals, and execution.

Medium or low rows should be used as connective tissue, not long standalone scenes unless future sources support them.

## 14. Factual Risk and Verification Notes

- `SRC_UNSET_001` remains on `CAP_MEXEMP_0001`, `FACT_MEXEMP_0001-0006`, and `TIME_MEXEMP_0001-0002`; these are used only with verification flags.
- `FACT_MEXEMP_2561-2608` are not linked as existing fact cards.
- `TIME_MEXEMP_0423-0448` are not linked as existing timeline cards.
- Missing or gap areas are recorded, not filled: `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096`; `FACT_MEXEMP_2366-2389`; `FACT_MEXEMP_2439-2513`; `TIME_MEXEMP_0376-0378`; `TIME_MEXEMP_0387-0413`.
- McLane-Ocampo, debt suspension specifics, Imperial Academy, Mexican republican military reports, liberal press, and trial/court-martial records need targeted source work.
- Basch, Blasio, Felix Salm-Salm, Agnes Salm-Salm, and other witness accounts must be treated as testimony, not neutral chronology.

## 15. Source Gaps and Missing Links

Priority gaps:

1. Republican legality and Reform War: `CTL_MEXEMP_0001-0004`.
2. Debt suspension and McLane-Ocampo: `CTL_MEXEMP_0003-0005`.
3. Mexican press and local reception: `CTL_MEXEMP_0006-0014`.
4. Church-state legal records: `CTL_MEXEMP_0015-0016`.
5. U.S. border and arms policy: `CTL_MEXEMP_0017`; `0021-0022`.
6. Republican military reporting for 1866-1867: `CTL_MEXEMP_0024-0027`.
7. Trial / court-martial primary records: `CTL_MEXEMP_0028-0030`.
8. Memory separation between liberal, conservative, European, and memoir traditions: `CTL_MEXEMP_0031-0032`.

## 16. Manual Review / Dependency List

Every CTL row remains `manual_review_needed: yes` because this document is a linkage and planning layer rather than a new source-certification layer.

Specific dependencies:

- Confirm McLane-Ocampo coverage in source cards or add it to a future source-gap workflow, not here.
- Confirm exact source routes for debt-payment suspension and the Tripartite Convention.
- Verify Black Decree legal text and implementation records.
- Verify Imperial Academy and cultural-policy mentions before scene use.
- Cross-check Queretaro betrayal narratives with republican military and court records.
- Replace or qualify `SRC_UNSET_001` for the prologue / execution cluster before drafting final scenes.

## 17. Work Log and Stats

| Metric | Count / value |
|---|---:|
| CTL ID range | `CTL_MEXEMP_0001-CTL_MEXEMP_0032` |
| CTL count | 32 |
| chronology_precision exact | 11 |
| chronology_precision month | 16 |
| chronology_precision year | 2 |
| chronology_precision approximate | 2 |
| chronology_precision disputed | 0 |
| chronology_precision manual_review_needed | 1 |
| evidence_strength strong | 0 |
| evidence_strength moderate | 11 |
| evidence_strength mixed | 19 |
| evidence_strength weak | 1 |
| evidence_strength manual_review_needed | 1 |
| republican_balance_needed yes | 32 |
| maximilian_centered_risk high | 23 |
| verification_needed yes | 32 |
| scene_potential high | 21 |
| manual_review_needed yes | 32 |

High Maximilian-centered-risk CTLs:

`CTL_MEXEMP_0008`; `0010-0023`; `0025-0032`.

High scene-potential CTLs:

`CTL_MEXEMP_0005-0007`; `0009-0010`; `0012-0015`; `0017`; `0019-0023`; `0025-0030`.

## 18. Next Recommended Step

Recommended Phase 11: build a republican-side verification matrix for the CTL rows, prioritizing `CTL_MEXEMP_0001-0007`, `0015-0017`, and `0024-0030`. The next work should not create missing CAP / FACT / TIME cards automatically; it should first map source candidates and identify which existing rows can be strengthened from republican government documents, military reports, liberal press, U.S. official records, and trial/court-martial records.
