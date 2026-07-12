---
id: SHAWCROSS_ID_AUDIT
type: id_audit
status: active
created: 2026-06-13
updated: 2026-06-13
tags:
  - id-audit
  - shawcross
  - mexemp
  - manual-review
source_id: SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO
---

# Shawcross ID Audit

Source: SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO  
Audit date: 2026-06-13  
Related progress master: [[Shawcross_Progress_Master]]

## 1. Audit Scope and Rules

- 対象は `CAP_MEXEMP_*`, `FACT_MEXEMP_*`, `TIME_MEXEMP_*` の実在ファイル、frontmatter、本文中のID参照、`Shawcross_Progress_Master.md` の予定範囲である。
- 本監査では、欠番を削除・再採番・補完せず、まず状態を分類する。
- `file_absent`: ファイル名として実在しない。
- `planned_only`: Captureまたは工程表に予定・次ID候補として出るが、作成済みとは確認できない。
- `generation_gap_suspected`: Capture本文が `Created ...` と記録しているが、対応ファイルが実在しない。
- `manual_review_needed`: 内容照合または生成判断が必要。自動修正しない。
- Shawcross本文・NOTES本文・スクリーンショット本文の全文保存、長文引用、全文文字起こしは行っていない。

## 2. High-Level Result

| kind | actual file range | actual count | file_absent ranges in actual sequence | duplicate IDs | frontmatter id/type mismatch |
|---|---:|---:|---|---:|---:|
| CAP | CAP_MEXEMP_0001-CAP_MEXEMP_0107 | 104 | CAP_MEXEMP_0044, CAP_MEXEMP_0052, CAP_MEXEMP_0096 | 0 | 0 |
| FACT | FACT_MEXEMP_0001-FACT_MEXEMP_2560 | 2040 | FACT_MEXEMP_0303-0330, 0422-0445, 0787-0810, 1088-1118, 1167-1261, 1307-1326, 1414-1427, 1674-1706, 1776-1807, 1881-1908, 1937-2028, 2366-2389, 2439-2513 | 0 | 0 |
| TIME | TIME_MEXEMP_0001-TIME_MEXEMP_0422 | 323 | TIME_MEXEMP_0055-0063, 0130-0135, 0169-0171, 0179-0183, 0190-0193, 0209-0214, 0251-0255, 0269-0272, 0292-0297, 0302-0322, 0376-0378, 0387-0413 | 0 | 0 |

Shawcross source_id限定では、`CAP_MEXEMP_0002-CAP_MEXEMP_0107` が103件、`FACT_MEXEMP_0007-FACT_MEXEMP_2560` が2034件、`TIME_MEXEMP_0003-TIME_MEXEMP_0422` が321件である。`CAP_MEXEMP_0001`, `FACT_MEXEMP_0001-0006`, `TIME_MEXEMP_0001-0002` は `SRC_UNSET_001` で、Shawcross本体範囲とは別扱いにする。

## 3. CAP Audit

| item | result | status |
|---|---|---|
| 実在範囲 | `CAP_MEXEMP_0001-CAP_MEXEMP_0107` | checked |
| Shawcross source_id範囲 | `CAP_MEXEMP_0002-CAP_MEXEMP_0107` | checked |
| 欠番疑い | `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096` | file_absent; manual_review_needed |
| 重複 | なし | checked |
| frontmatter id/type不一致 | なし | checked |

### CAP Special Checks

| CAP ID | actual file | other-folder file | frontmatter check | references found | action |
|---|---|---|---|---|---|
| CAP_MEXEMP_0044 | not found | not found | file_absentのため未確認 | `Shawcross_Progress_Master.md` | manual_review_needed |
| CAP_MEXEMP_0052 | not found | not found | file_absentのため未確認 | `Shawcross_Progress_Master.md`, `CAP_MEXEMP_0051.md` | manual_review_needed |
| CAP_MEXEMP_0096 | not found | not found | file_absentのため未確認 | `Shawcross_Progress_Master.md`, `CAP_MEXEMP_0095.md` | manual_review_needed |

## 4. FACT Audit

| item | result | status |
|---|---|---|
| 実在範囲 | `FACT_MEXEMP_0001-FACT_MEXEMP_2560` | checked |
| Shawcross source_id範囲 | `FACT_MEXEMP_0007-FACT_MEXEMP_2560` | checked |
| 欠番疑い | `FACT_MEXEMP_0303-0330`, `0422-0445`, `0787-0810`, `1088-1118`, `1167-1261`, `1307-1326`, `1414-1427`, `1674-1706`, `1776-1807`, `1881-1908`, `1937-2028`, `2366-2389`, `2439-2513`, plus post-max `2561-2608` from Capture/Progress only | file_absent; manual_review_needed |
| 重複 | なし | checked |
| frontmatter id/type不一致 | なし | checked |

`FACT_MEXEMP_2561-FACT_MEXEMP_2608` は通常の実在範囲外で、ファイルは0件。`CAP_MEXEMP_0105` と `CAP_MEXEMP_0106` が `Created` と記録しているため、単なる予定IDではなく `generation_gap_suspected` として扱う。

## 5. TIME Audit

| item | result | status |
|---|---|---|
| 実在範囲 | `TIME_MEXEMP_0001-TIME_MEXEMP_0422` | checked |
| Shawcross source_id範囲 | `TIME_MEXEMP_0003-TIME_MEXEMP_0422` | checked |
| 欠番疑い | `TIME_MEXEMP_0055-0063`, `0130-0135`, `0169-0171`, `0179-0183`, `0190-0193`, `0209-0214`, `0251-0255`, `0269-0272`, `0292-0297`, `0302-0322`, `0376-0378`, `0387-0413`, plus post-max `0423-0448` from Capture/Progress only | file_absent; manual_review_needed |
| 重複 | なし | checked |
| frontmatter id/type不一致 | なし | checked |

`TIME_MEXEMP_0423-TIME_MEXEMP_0448` は通常の実在範囲外で、ファイルは0件。`CAP_MEXEMP_0105` と `CAP_MEXEMP_0106` が `Created` と記録しているため、単なる予定IDではなく `generation_gap_suspected` として扱う。

## 6. Progress Master Planned Ranges vs Actual Files

以下は `Shawcross_Progress_Master.md` 上の欠番疑いである。工程表記載は欠番確定ではなく、実在ファイル未発見として手動確認に回す。

| screenshot_no | missing from progress range | status |
|---:|---|---|
| 14 | `FACT_MEXEMP_0303-0330`; `TIME_MEXEMP_0055-0063` | 推定範囲; manual_review_needed |
| 18 | `FACT_MEXEMP_0422-0445` | 推定範囲; manual_review_needed |
| 32 | `FACT_MEXEMP_0787-0810`; `TIME_MEXEMP_0130-0135` | 推定範囲; manual_review_needed |
| 43 | `CAP_MEXEMP_0044`; `FACT_MEXEMP_1088-1118`; `TIME_MEXEMP_0169-0171` | 推定範囲; manual_review_needed |
| 46 | `FACT_MEXEMP_1167-1203`; `TIME_MEXEMP_0179-0181` | 推定範囲; manual_review_needed |
| 47 | `FACT_MEXEMP_1204-1238`; `TIME_MEXEMP_0182-0183` | 推定範囲; manual_review_needed |
| 48 | `FACT_MEXEMP_1239-1261` | 推定範囲; Capture記載境界ズレあり |
| 51 | `CAP_MEXEMP_0052`; `FACT_MEXEMP_1307-1326`; `TIME_MEXEMP_0190-0193` | 推定範囲; manual_review_needed |
| 58 | `FACT_MEXEMP_1414-1427`; `TIME_MEXEMP_0209-0214` | 推定範囲; manual_review_needed |
| 69 | `FACT_MEXEMP_1674-1706`; `TIME_MEXEMP_0251-0255` | 推定範囲; manual_review_needed |
| 73 | `FACT_MEXEMP_1776-1807`; `TIME_MEXEMP_0269-0272` | 推定範囲; manual_review_needed |
| 77 | `FACT_MEXEMP_1881-1908`; `TIME_MEXEMP_0292-0297` | 推定範囲; manual_review_needed |
| 79 | `FACT_MEXEMP_1937-1958`; `TIME_MEXEMP_0302-0305` | 推定範囲; manual_review_needed |
| 80 | `FACT_MEXEMP_1959-1984`; `TIME_MEXEMP_0306-0309` | 推定範囲; manual_review_needed |
| 81 | `FACT_MEXEMP_1985-2008`; `TIME_MEXEMP_0310-0318` | 推定範囲; manual_review_needed |
| 82 | `FACT_MEXEMP_2009-2028`; `TIME_MEXEMP_0319-0322` | 推定範囲; manual_review_needed |
| 95 | `CAP_MEXEMP_0096`; `FACT_MEXEMP_2366-2389`; `TIME_MEXEMP_0376-0378` | 推定範囲; manual_review_needed |
| 98 | `FACT_MEXEMP_2439-2460`; `TIME_MEXEMP_0387-0393` | 推定範囲; manual_review_needed |
| 99 | `FACT_MEXEMP_2461-2484`; `TIME_MEXEMP_0394-0403` | 推定範囲; manual_review_needed |
| 100 | `FACT_MEXEMP_2485-2513`; `TIME_MEXEMP_0404-0413` | 推定範囲; manual_review_needed |
| 101 | `TIME_MEXEMP_0413` | 境界ズレ疑い; manual_review_needed |
| 104 | `FACT_MEXEMP_2561-2585`; `TIME_MEXEMP_0423-0434` | generation_gap_suspected |
| 105 | `FACT_MEXEMP_2586-2608`; `TIME_MEXEMP_0435-0448` | generation_gap_suspected |

## 7. Capture Planned / Created IDs vs Actual Files

### Capture `Created` Logs with Missing Files

| capture | missing files despite `Created` log | classification |
|---|---|---|
| CAP_MEXEMP_0099 | `FACT_MEXEMP_2439-2460`; `TIME_MEXEMP_0387-0393` | generation_gap_suspected |
| CAP_MEXEMP_0100 | `FACT_MEXEMP_2461-2484`; `TIME_MEXEMP_0394-0403` | generation_gap_suspected |
| CAP_MEXEMP_0101 | `FACT_MEXEMP_2485-2513`; `TIME_MEXEMP_0404-0413` | generation_gap_suspected |
| CAP_MEXEMP_0105 | `FACT_MEXEMP_2561-2585`; `TIME_MEXEMP_0423-0434` | generation_gap_suspected |
| CAP_MEXEMP_0106 | `FACT_MEXEMP_2586-2608`; `TIME_MEXEMP_0435-0448` | generation_gap_suspected |

### Capture Planned-Only or Next-Candidate IDs

| capture | missing planned/candidate IDs | classification |
|---|---|---|
| CAP_MEXEMP_0019 | `FACT_MEXEMP_0422-0445` | planned_only |
| CAP_MEXEMP_0033 | `FACT_MEXEMP_0787-0810`; `TIME_MEXEMP_0130-0135` | planned_only |
| CAP_MEXEMP_0048 | `FACT_MEXEMP_1238` | next_candidate |
| CAP_MEXEMP_0051 | `CAP_MEXEMP_0052`; `FACT_MEXEMP_1307`; `TIME_MEXEMP_0190` | next_candidate |
| CAP_MEXEMP_0070 | `FACT_MEXEMP_1674-1706`; `TIME_MEXEMP_0251-0255` | planned_only |
| CAP_MEXEMP_0074 | `FACT_MEXEMP_1776-1807`; `TIME_MEXEMP_0269-0272` | planned_only |
| CAP_MEXEMP_0078 | `FACT_MEXEMP_1881`, `FACT_MEXEMP_1908`; `TIME_MEXEMP_0292`, `TIME_MEXEMP_0297` | planned_only endpoints; range in progress master |
| CAP_MEXEMP_0080 | `FACT_MEXEMP_1937`, `FACT_MEXEMP_1958`; `TIME_MEXEMP_0302`, `TIME_MEXEMP_0305` | planned_only endpoints; range in progress master |
| CAP_MEXEMP_0081 | `FACT_MEXEMP_1959`, `FACT_MEXEMP_1984`; `TIME_MEXEMP_0306`, `TIME_MEXEMP_0309` | planned_only endpoints; range in progress master |
| CAP_MEXEMP_0082 | `FACT_MEXEMP_1985`, `FACT_MEXEMP_2008`; `TIME_MEXEMP_0310`, `TIME_MEXEMP_0318` | planned_only endpoints; range in progress master |
| CAP_MEXEMP_0083 | `FACT_MEXEMP_2009-2028`; `TIME_MEXEMP_0319-0322` | planned_only |
| CAP_MEXEMP_0095 | `CAP_MEXEMP_0096`; `FACT_MEXEMP_2366`; `TIME_MEXEMP_0376` | next_candidate |
| CAP_MEXEMP_0098 | `FACT_MEXEMP_2439`; `TIME_MEXEMP_0387` | next_candidate |
| CAP_MEXEMP_0102 | `TIME_MEXEMP_0413` | planned_only; boundary overlap |
| CAP_MEXEMP_0104 | `FACT_MEXEMP_2561`; `TIME_MEXEMP_0423` | next_candidate only; not generated by CAP_MEXEMP_0104 |

`CAP_MEXEMP_0107` explicitly says ACKNOWLEDGMENTSであり、`FACT_MEXEMP_2609` and `TIME_MEXEMP_0449` remain unused. This is not a generation gap.

## 8. Source ID Audit

| result | cards |
|---|---|
| source_id key missing | none |
| source_id placeholder `SRC_UNSET_001` | `CAP_MEXEMP_0001`; `FACT_MEXEMP_0001-0006`; `TIME_MEXEMP_0001-0002` |
| source_id other than Shawcross and not placeholder | none |

`SRC_UNSET_001` cards are not automatically rewritten. They are outside the confirmed Shawcross source range used in the progress master and require manual source attribution review.

## 9. Broken or Unresolved ID References

The following are references from existing CAP / FACT / TIME files to IDs that have no corresponding actual file. Capture references may represent planned IDs rather than hard links, but they still need manual review before generation or cleanup.

| source file ID | unresolved referenced IDs | classification |
|---|---|---|
| FACT_MEXEMP_0489 | `FACT_MEXEMP_0431` | manual_review_needed |
| FACT_MEXEMP_0638 | `FACT_MEXEMP_0439` | manual_review_needed |
| TIME_MEXEMP_0196 | `TIME_MEXEMP_0192` | manual_review_needed |
| CAP_MEXEMP_0019 | `FACT_MEXEMP_0422`, `FACT_MEXEMP_0445` | planned/reference unresolved |
| CAP_MEXEMP_0033 | `FACT_MEXEMP_0787`, `FACT_MEXEMP_0810`; `TIME_MEXEMP_0130-0135` | planned/reference unresolved |
| CAP_MEXEMP_0047 | `FACT_MEXEMP_1167-1203`; `TIME_MEXEMP_0179-0181` | planned/reference unresolved |
| CAP_MEXEMP_0048 | `FACT_MEXEMP_1204-1238`; `TIME_MEXEMP_0182-0183` | planned/reference unresolved |
| CAP_MEXEMP_0049 | `FACT_MEXEMP_1238-1261` | planned/reference unresolved |
| CAP_MEXEMP_0051 | `CAP_MEXEMP_0052`; `FACT_MEXEMP_1307`; `TIME_MEXEMP_0190` | next candidate unresolved |
| CAP_MEXEMP_0058 | `FACT_MEXEMP_1414`; `TIME_MEXEMP_0209` | planned/reference unresolved |
| CAP_MEXEMP_0059 | `FACT_MEXEMP_1414-1427`; `TIME_MEXEMP_0209-0214` | planned/reference unresolved |
| CAP_MEXEMP_0069 | `FACT_MEXEMP_1674`; `TIME_MEXEMP_0251` | planned/reference unresolved |
| CAP_MEXEMP_0070 | `FACT_MEXEMP_1674-1706`; `TIME_MEXEMP_0251-0255` | planned/reference unresolved |
| CAP_MEXEMP_0073 | `FACT_MEXEMP_1776`; `TIME_MEXEMP_0269` | planned/reference unresolved |
| CAP_MEXEMP_0074 | `FACT_MEXEMP_1776-1807`; `TIME_MEXEMP_0269-0272` | planned/reference unresolved |
| CAP_MEXEMP_0077 | `FACT_MEXEMP_1881`; `TIME_MEXEMP_0292` | planned/reference unresolved |
| CAP_MEXEMP_0078 | `FACT_MEXEMP_1881`, `FACT_MEXEMP_1908`; `TIME_MEXEMP_0292`, `TIME_MEXEMP_0297` | planned/reference unresolved |
| CAP_MEXEMP_0079 | `FACT_MEXEMP_1937`; `TIME_MEXEMP_0302` | planned/reference unresolved |
| CAP_MEXEMP_0080 | `FACT_MEXEMP_1937`, `FACT_MEXEMP_1958`; `TIME_MEXEMP_0302`, `TIME_MEXEMP_0305` | planned/reference unresolved |
| CAP_MEXEMP_0081 | `FACT_MEXEMP_1959`, `FACT_MEXEMP_1984`; `TIME_MEXEMP_0306`, `TIME_MEXEMP_0309` | planned/reference unresolved |
| CAP_MEXEMP_0082 | `FACT_MEXEMP_1985`, `FACT_MEXEMP_2008`; `TIME_MEXEMP_0310`, `TIME_MEXEMP_0318` | planned/reference unresolved |
| CAP_MEXEMP_0083 | `FACT_MEXEMP_2009`, `FACT_MEXEMP_2028`; `TIME_MEXEMP_0319`, `TIME_MEXEMP_0322` | planned/reference unresolved |
| CAP_MEXEMP_0095 | `CAP_MEXEMP_0096`; `FACT_MEXEMP_2366`; `TIME_MEXEMP_0376` | next candidate unresolved |
| CAP_MEXEMP_0098 | `FACT_MEXEMP_2439`; `TIME_MEXEMP_0387` | next candidate unresolved |
| CAP_MEXEMP_0099 | `FACT_MEXEMP_2439`, `FACT_MEXEMP_2460-2461`; `TIME_MEXEMP_0387`, `TIME_MEXEMP_0393-0394` | generation gap and next candidate unresolved |
| CAP_MEXEMP_0100 | `FACT_MEXEMP_2461`, `FACT_MEXEMP_2484-2485`; `TIME_MEXEMP_0394`, `TIME_MEXEMP_0403-0404` | generation gap and next candidate unresolved |
| CAP_MEXEMP_0101 | `FACT_MEXEMP_2485`, `FACT_MEXEMP_2513`; `TIME_MEXEMP_0404`, `TIME_MEXEMP_0413` | generation gap unresolved |
| CAP_MEXEMP_0102 | `TIME_MEXEMP_0413` | boundary unresolved |
| CAP_MEXEMP_0104 | `FACT_MEXEMP_2561`; `TIME_MEXEMP_0423` | next candidate unresolved |
| CAP_MEXEMP_0105 | `FACT_MEXEMP_2561`, `FACT_MEXEMP_2585-2586`; `TIME_MEXEMP_0423`, `TIME_MEXEMP_0434-0435` | generation gap and next candidate unresolved |
| CAP_MEXEMP_0106 | `FACT_MEXEMP_2586`, `FACT_MEXEMP_2608`; `TIME_MEXEMP_0435`, `TIME_MEXEMP_0448` | generation gap unresolved |
| CAP_MEXEMP_0107 | `FACT_MEXEMP_2609`; `TIME_MEXEMP_0449` | explicitly unused; no generation needed |

## 10. NOTES / ACKNOWLEDGMENTS Checks

| check | result | action |
|---|---|---|
| NOTES由来情報が本文Fact化されている疑い | strict search found none in Fact/Timeline frontmatter or IDs | no_action |
| ACKNOWLEDGMENTS由来情報が本文扱いされている疑い | none found | no_action |
| `notes_translation_0109.md` | not found | reference only; 109枚目のNOTES範囲はProgress Master登録済みとして扱う |
| `CAP_MEXEMP_0107` | ACKNOWLEDGMENTS boundary capture | Fact/Timelineは作成しない |

## 11. Minor Fixes Applied

None. This pass created only this audit file and did not modify Capture, Fact, Timeline, Source Note, or Progress Master records.

## 12. Manual Review Queue

- `CAP_MEXEMP_0044`, `CAP_MEXEMP_0052`, `CAP_MEXEMP_0096`: ファイル未発見。削除・再採番せず、画像番号・スクリーンショット・隣接Captureとの対応を確認する。
- `FACT_MEXEMP_2561-2608` and `TIME_MEXEMP_0423-0448`: `CAP_MEXEMP_0105` and `CAP_MEXEMP_0106` に `Created` 記録があるため、生成漏れ疑いとして確認する。Capture側の予定IDだけとは扱わない。
- `CAP_MEXEMP_0099-0101`: `Created` 記録があるが `FACT_MEXEMP_2439-2513` and `TIME_MEXEMP_0387-0413` が未実在。生成漏れか、Captureログ誤記か確認する。
- `TIME_MEXEMP_0413`: `CAP_MEXEMP_0101` と `CAP_MEXEMP_0102` の境界で重複的に出るが、ファイル未実在。境界整理が必要。
- `FACT_MEXEMP_0489`, `FACT_MEXEMP_0638`, `TIME_MEXEMP_0196`: 実在カードから未実在IDへの参照がある。内容リンクとして必要か、隣接IDの誤記か確認する。
- `SRC_UNSET_001` cards: `CAP_MEXEMP_0001`, `FACT_MEXEMP_0001-0006`, `TIME_MEXEMP_0001-0002` の出典確定が必要。
- `FACT_MEXEMP_1238`: `CAP_MEXEMP_0048` と `CAP_MEXEMP_0049` の境界で重複的に現れる。生成前に境界確認する。

## 13. Handoff to Next Workflow

Next workflow: NOTESページを出典探索インデックスへ変換。

- NOTES 107-114は本文Fact/Timeline生成対象にしない。
- 109枚目は `notes_translation_0109.md` 未発見だが、Progress Master上のNOTES範囲は登録済みとして扱う。
- NOTES処理では、本文Fact化ではなく、引用元・一次史料候補・二次史料候補・書誌確認候補へのインデックス化に限定する。
- Chapter 10 注および EPILOGUE 注の書誌確認候補は Source Note側の既存メモを参照し、長文引用・全文転記は行わない。
