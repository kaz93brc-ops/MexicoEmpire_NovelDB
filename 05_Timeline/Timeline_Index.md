---
id: TL-INDEX
type: timeline_index
status: active
created: 2026-05-31
updated: 2026-06-10
tags:
  - index
  - timeline
source_id: ""
chapter: ""
page: ""
kindle_location: ""
screenshot_file: ""
---

# Timeline Index

年表はMarkdownノートとCSVの両方で扱います。

CSV入力は `91_CSV_Templates/timeline_template.csv` を使い、Markdown化は `92_Scripts/csv_to_md.py` で行います。

## Dataviewを使う場合

```dataview
TABLE date_start, date_end, date_precision, summary, source_id, evidence_category, confidence
FROM "05_Timeline"
WHERE type = "timeline_entry"
SORT date_start ASC
```

## 手動管理用テーブル

| date_start | date_end | event | place | source | evidence_category | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1861-12 |  | MaximilianはGutiérrez de EstradaをMiramarでのChristmasに招き、Mexico皇帝案について直接会談した。 | Miramar | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1862-01 |  | MaximilianはFranz Josephと新年を過ごし、Mexicoの将来構想を語り、Franz JosephはNovara号をMexico渡航に貸すことに同意した。 | near Venice; Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1862-01-02 |  | MaximilianはNapoleon IIIへ直接書簡を書き、Mexico皇帝位受諾をMexican nationの明確な意思表示に条件づけた。 | Miramar; France; Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | primary_testimony | probable |
| 1863 |  | 1863年末の作戦中、Achille Bazaineは15年間連れ添った妻の死を知ったとされる。 | Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1864-04-04 |  | 米国議会関係者は、メキシコ情勢に無関心ではなく、欧州列強の後援による米州の君主政樹立を容認しない趣旨の決議を採択したとされる。 | United States; Republic of Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | primary_testimony | probable |
| 1864-12 |  | papal nuncioがメキシコに到着し、Maximilianは宗教問題と教会土地問題をめぐる教皇庁との調整に直面したとされる。 | Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1864-12 |  | Papal nuncio Francesco MegliaがVeracruzからMexico Cityへ向かい、Maximilianは首都到着時に手厚い歓迎儀礼を用意したとされる。 | Veracruz;Mexico City | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1864-12 |  | MegliaがMexico Cityへ到着した翌日、Pope Pius IXはSyllabus of Errorsとして知られる文書で自由主義的価値を非難したとShawcrossは述べる。 | Rome;Mexico City | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1864-12-23 |  | MaximilianはCarlotaをMegliaへ送り、交渉しなければJuárezの法律を確認する布告を出すという最後通牒を伝えさせたとされる。 | Mexico City | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1864-12-27 |  | Maximilianは信教の自由、教会財産売却の確認、Juárez改革の多くの受容を布告したとされる。 | Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1865-01 |  | CarlotaはEugenieへの書簡で、12月27日の布告後に情勢が激しく揺れたことを伝えたとされる。 | Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | primary_testimony | uncertain |
| 1865-01 |  | 1865年1月時点でMaximilian側にはBelgian volunteers、Austrian Legion、Egyptian contingentが含まれていたとされる。 | Mexico; Habsburg lands; Egypt | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1865-04 |  | By April 1865, Juárez had only a few thousand poorly equipped fighters facing the French, and his ability to resupply had been constrained by the wartime embargo on weapons exports from the North. | Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1865-05 |  | Andrew Johnson revoked the wartime ban on weapons exports from the North, after which military equipment began moving across the border to Juárez's forces. | United States;US-Mexico border;Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1865-08 |  | Brincourt's capture of Chihuahua in August 1865 marked Maximilian's empire at its greatest territorial extent, while Juárez remained precariously on the northern border and liberal forces were beginning to secure the means to recover. | Chihuahua;northern Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | author_interpretation | probable |
| 1865-summer |  | In the summer of 1865, Brownsville became a gathering place for liberal exiles, adventurers, and Union officers, while Juaristas used the Rio Grande border zone to rebuild their forces against Maximilian’s empire. | Brownsville;Matamoros;Rio Grande;Texas | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1865 |  | After learning of the US military buildup in Texas, Napoleon III ordered Bazaine to withdraw French soldiers southward and prepare for a possible US invasion, disrupting Brincourt’s movement against Juárez near El Paso del Norte. | Texas;El Paso del Norte;Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1865-10 |  | In October 1865, a liberal army attacked Matamoros after issuing Mejía an ultimatum; Juaristas, including numerous Americans, seized a fort but were repelled by imperial gunboats and Mejía’s cavalry, after which they withdrew into the countryside. | Matamoros;Rio Grande | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1866-01 |  | Carlotaは1866年1月、父Leopold Iの死を知り、強い悲嘆と服喪に入ったとされる。 | Mexico;Belgium | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | primary_testimony | probable |
| 1866-01-15 |  | Maximilianは義父Leopold Iのための公式追悼式を行い、Leopold Iと自らの政治的使命を重ねるような演説をした。 | Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | primary_testimony | probable |
| 1866-01-15 |  | Napoleon IIIは、フランス軍のMexico撤退を告げる書簡を書いたとされる。 | France;Mexico | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1866-02-14 |  | MaximilianはCuernavacaで、Napoleon IIIからの緊急書簡を携えたフランス特使がMexico Cityに到着したとの知らせを受けた。 | Cuernavaca;Mexico City | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1867-03-04 |  | Querétaroの帝政側に、共和派軍が接近しているという知らせが届いた。 | Querétaro | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1867-03-05 |  | 3月4日の翌日、共和派軍がQuerétaro西方の平原に集結し、共和派軍を各個撃破する帝政側の可能性は消え、包囲が始まった。 | Querétaro | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1867-03-13 |  | MaximilianはCerro de las Campanasから、より安全で快適なLa Cruzへ本営を移し、元修道女の房を執務室と寝室として使い始めた。 | Cerro de las Campanas;La Cruz;Convent of Santa Cruz;Querétaro | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1867-03-14 |  | 1867年3月14日朝、MaximilianがLa Cruzの修道院中庭で兵を閲兵し演説している最中、共和派砲兵の砲撃が始まり、Querétaroへの攻撃が開始された。 | La Cruz; Querétaro | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1867-03-14 |  | 1867年3月14日、Querétaroは南・東・北の三方面から共和派の攻撃を受けた。 | Querétaro; La Cruz | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1867-03-14 |  | 1867年3月14日、南方ではTomás Mejíaが騎兵反撃を率い、Juarista騎兵を押し返した。 | Querétaro | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
| 1867-03-14 |  | 1867年3月14日、北方の橋方面でSalm-Salmが部隊を率いて共和派砲兵・家屋陣地を攻撃し、共和派兵の殺害を伴う激しい市街戦が起きた。 | Querétaro; river bridge | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | primary_testimony | probable |
| 1867-03-14 |  | 1867年3月14日、Escobedo軍はLa Cruz東側の礼拝堂と周辺家屋を占拠し、Márquezは部隊が動揺する中で反撃を指揮した。反撃の結果は次ページ確認が必要。 | La Cruz; Querétaro | SRC_SHAWCROSS_2022_LAST_EMPEROR_MEXICO | historical_fact | probable |
