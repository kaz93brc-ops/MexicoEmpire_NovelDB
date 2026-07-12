---
id: PRE_HAMNETT_INGESTION_READINESS_AUDIT
type: readiness_audit
status: active
created: 2026-06-14
updated: 2026-06-14
phr_id_range: PHR_MEXEMP_0001-PHR_MEXEMP_0020
scope: pre_hamnett_ingestion_readiness
source_handling: management_audit_only
new_capture_cards_created: no
new_fact_cards_created: no
new_timeline_cards_created: no
new_entity_cards_created: no
long_quotes_or_full_transcription: no
---

# Pre-Hamnett Ingestion Readiness Audit

## 1. Overview

This file is the final management check before ingesting Brian R. Hamnett, *Juarez* into `MexicoEmpire_NovelDB`.

This pass does not create new Capture, Fact, Timeline, Person, Event, Place, Org, Theme, Source, Scene, or Question cards. It also does not read or ingest Hamnett body text or notes.

The purpose is to confirm that existing management documents, ID references, source-handling rules, copyright restrictions, and Hamnett-ingestion preparation are safe enough to receive the next reading workflow.

If no blocking issue is found, the next workflow can begin controlled reading of Hamnett body text and notes, using HJI/RSG as source-candidate and manual-review guides rather than as proof that Hamnett has already been read.

## 2. Summary

| metric | count |
|---|---:|
| PHR件数 | 20 |
| critical_issue件数 | 0 |
| minor_issue件数 | 4 |
| manual_review_needed件数 | 3 |
| Hamnett投入前に修正必須の件数 | 0 |
| Hamnett投入後に再確認すべき件数 | 2 |

| check_area | count |
|---|---:|
| file_existence | 2 |
| ID_integrity | 5 |
| source_handling | 2 |
| copyright_safety | 2 |
| Hamnett_not_yet_ingested | 2 |
| republican_balance | 1 |
| narrative_bias | 1 |
| entity_card_readiness | 1 |
| scene_design_readiness | 1 |
| next_step_readiness | 2 |
| other | 1 |

| status | count |
|---|---:|
| ok | 13 |
| caution | 4 |
| needs_fix | 0 |
| manual_review_needed | 3 |

Definitions used in this summary: `critical_issue` means a `needs_fix` or high-risk blocker before Hamnett ingestion. `minor_issue` means a `caution` row that does not block Hamnett ingestion if the row's notes are followed.

## 3. PHR Table

| PHR_ID | check_area | checked_file_or_scope | check_item | status | finding_summary | affected_IDs_or_files | risk_level | required_action_before_Hamnett | action_timing | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| PHR_MEXEMP_0001 | file_existence | Required management Docs and Source Note | Required-file existence | ok | All required management files and the Shawcross Source Note exist. | `01_Sources/Source_Notes/SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO.md`; `93_Docs/Shawcross_Progress_Master.md`; `93_Docs/Shawcross_ID_Audit.md`; `93_Docs/Shawcross_Notes_Source_Index.md`; `93_Docs/Shawcross_Source_Reliability_Matrix.md`; `93_Docs/Shawcross_Next_Reading_Candidates.md`; `93_Docs/Juarez_Republican_Source_Gap_Analysis.md`; `93_Docs/Hamnett_Juarez_Source_Trail_Index.md`; `93_Docs/Novel_Chapter_Design_Linkage.md`; `93_Docs/Novel_Character_Design_Index.md`; `93_Docs/Core_Timeline_1859_1867.md`; `93_Docs/Entity_Card_Consolidation_Audit.md` | none | none | no_action_needed | No target file was missing. |
| PHR_MEXEMP_0002 | file_existence | Same-purpose Pre-Hamnett audit search | Existing same-purpose file and PHR IDs | ok | No prior same-purpose Pre-Hamnett audit file or `PHR_MEXEMP_####` IDs were found; this file starts at `PHR_MEXEMP_0001`. | `93_Docs/Pre_Hamnett_Ingestion_Readiness_Audit.md` | none | none | no_action_needed | New PHR IDs are management-row IDs only. |
| PHR_MEXEMP_0003 | next_step_readiness | RSG / HJI / CTL / ECA | Workflow connection | ok | RSG defines republican gaps, HJI maps Hamnett/source trails, CTL supplies chronology linkage, and ECA inventories entity-card follow-up work. The roles are distinct and compatible. | `RSG_MEXEMP_0001`; `RSG_MEXEMP_0022`; `HJI_MEXEMP_0001`; `HJI_MEXEMP_0025`; `CTL_MEXEMP_0001`; `CTL_MEXEMP_0032`; `ECA_MEXEMP_0001`; `ECA_MEXEMP_0081` | none | none | no_action_needed | Use RSG/HJI during Hamnett reading, then reflect confirmed results into CTL/ECA later. |
| PHR_MEXEMP_0004 | ID_integrity | Capture / Fact / Timeline cards | Existing ID coverage and known gaps | caution | Existing-card coverage matches Shawcross ID Audit: CAP through `0107` with known absent files, Fact through `2560`, Timeline through `0422`. Internal gaps are recorded, not repaired. | `CAP_MEXEMP_0001`; `CAP_MEXEMP_0107`; `FACT_MEXEMP_0001`; `FACT_MEXEMP_2560`; `TIME_MEXEMP_0001`; `TIME_MEXEMP_0422`; `93_Docs/Shawcross_ID_Audit.md` | medium | none | during_Hamnett_ingestion | Do not fill gaps, renumber, or infer IDs when starting Hamnett work. |
| PHR_MEXEMP_0005 | ID_integrity | Post-max Fact / Timeline ranges | Forbidden post-max ranges | caution | The specified post-max Fact/Timeline ranges have no card files and are already excluded by CTL/HJI/ECA as existing IDs. Existing Capture logs still mention them, so the warning must stay visible. | `CAP_MEXEMP_0105`; `CAP_MEXEMP_0106`; `93_Docs/Shawcross_ID_Audit.md`; `93_Docs/Core_Timeline_1859_1867.md`; `93_Docs/Hamnett_Juarez_Source_Trail_Index.md`; `93_Docs/Entity_Card_Consolidation_Audit.md` | medium | none | during_Hamnett_ingestion | `FACT_MEXEMP_2561-2608` and `TIME_MEXEMP_0423-0448` are non-existing ranges, not usable existing cards. |
| PHR_MEXEMP_0006 | ID_integrity | NSI / SRM / NRC / RSG / HJI / CDL / NCD / CTL / ECA | Management-row ID existence | ok | Management-row IDs exist in their defining files: NSI/SRM/NRC 48 each, RSG 22, HJI 25, CDL 16, NCD 31, CTL 32, ECA 81. | `NSI_SHAWCROSS_0001`; `NSI_SHAWCROSS_0048`; `SRM_SHAWCROSS_0001`; `SRM_SHAWCROSS_0048`; `NRC_SHAWCROSS_0001`; `NRC_SHAWCROSS_0048`; `RSG_MEXEMP_0001`; `RSG_MEXEMP_0022`; `HJI_MEXEMP_0001`; `HJI_MEXEMP_0025`; `CDL_MEXEMP_0001`; `CDL_MEXEMP_0016`; `NCD_MEXEMP_0001`; `NCD_MEXEMP_0031`; `CTL_MEXEMP_0001`; `CTL_MEXEMP_0032`; `ECA_MEXEMP_0001`; `ECA_MEXEMP_0081` | none | none | no_action_needed | Row IDs are management IDs, not card IDs. |
| PHR_MEXEMP_0007 | ID_integrity | Shawcross ID Audit and known broken references | Existing unresolved ID warnings | manual_review_needed | Existing audit already records unresolved broken references and generation-gap suspects. They are not repaired here and do not block Hamnett reading, but must not be used as confirmed IDs. | `FACT_MEXEMP_0489`; `FACT_MEXEMP_0638`; `TIME_MEXEMP_0196`; `CAP_MEXEMP_0105`; `CAP_MEXEMP_0106`; `93_Docs/Shawcross_ID_Audit.md` | medium | none | after_Hamnett_ingestion | Resolve in a later ID-cleanup pass, not by gap-filling during Hamnett ingestion. |
| PHR_MEXEMP_0008 | source_handling | Shawcross NOTES workflow | NOTES not treated as body Fact | ok | Progress, NSI, SRM, NRC, RSG, HJI, and Source Note all keep NOTES as source-discovery material, not as body Fact/Timeline evidence. | `93_Docs/Shawcross_Progress_Master.md`; `93_Docs/Shawcross_Notes_Source_Index.md`; `93_Docs/Shawcross_Source_Reliability_Matrix.md`; `93_Docs/Shawcross_Next_Reading_Candidates.md`; `01_Sources/Source_Notes/SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO.md` | none | none | no_action_needed | NOTES 107-114 remain index material only. |
| PHR_MEXEMP_0009 | copyright_safety | Management Docs | Full text, full transcription, and long quotation controls | ok | Required management Docs contain explicit rules against storing Shawcross text, NOTES text, Hamnett text/notes, screenshot full transcription, or long quotations. No long quotation block was added in this audit. | `93_Docs/Shawcross_Progress_Master.md`; `93_Docs/Shawcross_ID_Audit.md`; `93_Docs/Hamnett_Juarez_Source_Trail_Index.md`; `93_Docs/Novel_Chapter_Design_Linkage.md`; `93_Docs/Novel_Character_Design_Index.md` | none | none | no_action_needed | Continue summary-only and citation-checklist handling. |
| PHR_MEXEMP_0010 | Hamnett_not_yet_ingested | Fact / Timeline / Capture card scan | Hamnett-derived card absence | ok | No Fact, Timeline, or Capture card was found using Hamnett as source_id/source_title or treating Hamnett as an ingested source. | `02_Fact_Cards/`; `05_Timeline/`; `01_Sources/Captures/` | none | none | no_action_needed | Existing Hamnett mentions are management/source-candidate references. |
| PHR_MEXEMP_0011 | Hamnett_not_yet_ingested | HJI abbreviation and map preparation | Hamnett abbreviations and maps | manual_review_needed | HJI records Hamnett abbreviations and map routes as candidates. They are correctly marked as requiring Hamnett edition, page, note, document, and source confirmation. | `HJI_MEXEMP_0001`; `HJI_MEXEMP_0025`; `93_Docs/Hamnett_Juarez_Source_Trail_Index.md` | medium | none | during_Hamnett_ingestion | Treat AGEO, AGN, APBJPS, BJDOCS, FJ, HAHR, UNAM, and maps as source_candidate until directly checked. |
| PHR_MEXEMP_0012 | republican_balance | Juarez / republican reinforcement docs | Republican-side source balance | manual_review_needed | RSG/HJI clearly identify Juarez government, republican army, legalism, Liberal Reform, Oaxaca, BJDOCS, APBJPS, AGN, and FJ gaps without asserting that the evidence has been read. | `RSG_MEXEMP_0001`; `RSG_MEXEMP_0022`; `HJI_MEXEMP_0001`; `HJI_MEXEMP_0025`; `PER-BENITO-JUAREZ`; `ORG-MEXICAN-REPUBLICANS`; `THM-LIBERAL-REFORM` | medium | none | during_Hamnett_ingestion | Manual review remains necessary before any new Fact/Timeline claims about republican decision-making. |
| PHR_MEXEMP_0013 | narrative_bias | CDL / NCD / CTL / ECA | Maximilian, Juarez, and Carlota framing | ok | Design Docs preserve warnings against Maximilian-only martyr framing, Juarez as simple executioner or flawless hero, and Carlota as tragic heroine only. | `CDL_MEXEMP_0001`; `CDL_MEXEMP_0016`; `NCD_MEXEMP_0001`; `NCD_MEXEMP_0003`; `CTL_MEXEMP_0001`; `CTL_MEXEMP_0032`; `ECA_MEXEMP_0001`; `ECA_MEXEMP_0081` | none | none | no_action_needed | Narrative caveats are consistent across the design layer. |
| PHR_MEXEMP_0014 | source_handling | Witness, memoir, press, and rumor handling | Verification separation | ok | Basch, Blasio, Felix Salm-Salm, Agnes Salm-Salm, newspapers, rumor, and public opinion are treated as testimony or public-discourse material requiring verification. | `NSI_SHAWCROSS_0037`; `NSI_SHAWCROSS_0040`; `SRM_SHAWCROSS_0037`; `SRM_SHAWCROSS_0040`; `NRC_SHAWCROSS_0037`; `NRC_SHAWCROSS_0040`; `RSG_MEXEMP_0010`; `RSG_MEXEMP_0021`; `HJI_MEXEMP_0023` | none | none | no_action_needed | Do not literalize dialogue, gestures, or motives from testimony alone. |
| PHR_MEXEMP_0015 | scene_design_readiness | Novel Chapter / Character / Core Timeline / ECA | Historical claim vs creative-use separation | ok | CDL/NCD/CTL/ECA separate historical verification from novel-use notes and keep close interiority, dialogue, and scene texture under verification or creative inference controls. | `CDL_MEXEMP_0001`; `CDL_MEXEMP_0016`; `NCD_MEXEMP_0001`; `NCD_MEXEMP_0031`; `CTL_MEXEMP_0001`; `CTL_MEXEMP_0032`; `ECA_MEXEMP_0001`; `ECA_MEXEMP_0081` | none | none | no_action_needed | No novel prose, dialogue, or psychological scene text was created here. |
| PHR_MEXEMP_0016 | entity_card_readiness | Event / Place / Org / Theme cards and ECA | Entity-card follow-up capacity | caution | ECA provides a controlled queue for missing, merge, and reinforcement candidates. Existing Event/Place/Org/Theme cards remain sparse but safe because no candidate was assigned a new card ID. | `EVT-FRENCH-INTERVENTION-IN-MEXICO`; `EVT-SECOND-MEXICAN-EMPIRE`; `PLC-MIRAMAR`; `PLC-QUERETARO`; `ORG-MEXICAN-REPUBLICANS`; `THM-LIBERAL-REFORM`; `ECA_MEXEMP_0001`; `ECA_MEXEMP_0081` | medium | none | after_Hamnett_ingestion | Update or create entity cards only after Hamnett and primary-source checks support the scope. |
| PHR_MEXEMP_0017 | next_step_readiness | HJI next recommended workflow | Hamnett ingestion entry point | ok | The next controlled entry point is to open Hamnett directly and build a page/note-level checklist before creating any new source-derived cards. | `HJI_MEXEMP_0001`; `HJI_MEXEMP_0025`; `RSG_MEXEMP_0001`; `RSG_MEXEMP_0022` | none | none | during_Hamnett_ingestion | Start with citation mapping, not claim extraction. |
| PHR_MEXEMP_0018 | ID_integrity | Future Hamnett Capture / Fact / Timeline creation | Next-ID safety | caution | Hamnett ingestion may later require new Capture/Fact/Timeline IDs, but this audit creates none. Fresh next-ID checks are required immediately before any future card creation. | `CAP_MEXEMP_0107`; `FACT_MEXEMP_2560`; `TIME_MEXEMP_0422`; `93_Docs/Shawcross_ID_Audit.md` | medium | none | during_Hamnett_ingestion | Do not assume the next ID from old Capture logs. |
| PHR_MEXEMP_0019 | copyright_safety | Card and management scope scan | Hamnett/Shawcross full-text risk | ok | No Hamnett-source Fact/Timeline/Capture cards were found. Management Docs continue to prohibit full text, long quotation, full note transcription, and screenshot full transcription. | `02_Fact_Cards/`; `05_Timeline/`; `01_Sources/Captures/`; `93_Docs/Hamnett_Juarez_Source_Trail_Index.md` | none | none | no_action_needed | Keep future Hamnett work to short citation metadata and summaries. |
| PHR_MEXEMP_0020 | other | This workflow | No card mutation or ID repair | ok | This workflow creates only this management audit and a short Source Note log. It does not create, delete, renumber, gap-fill, or merge cards. | `93_Docs/Pre_Hamnett_Ingestion_Readiness_Audit.md`; `01_Sources/Source_Notes/SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO.md` | none | none | no_action_needed | Existing unresolved items remain in their existing audit queues. |

## 4. Readiness Conclusion

`minor_cautions_but_ready`

Reason: the management Doc chain is present, HJI/RSG/CTL/ECA roles are clear, Hamnett body text and notes are still treated as not ingested, and there is no before-Hamnett blocking fix. The remaining cautions are ID hygiene and source-verification controls that must be respected during and after Hamnett ingestion, especially the non-existing `FACT_MEXEMP_2561-2608` / `TIME_MEXEMP_0423-0448` ranges and republican-side manual review requirements.
