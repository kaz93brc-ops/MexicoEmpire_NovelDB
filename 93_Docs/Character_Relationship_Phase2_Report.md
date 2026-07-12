---
id: CHARACTER_RELATIONSHIP_PHASE2_REPORT
type: operation_report
status: complete
created: 2026-06-14
updated: 2026-06-14
tags:
  - report
  - character-evidence
  - relationship
  - phase2
  - mexemp
rights_note: "No long quotations, translations, screenshots, or full text reproduction; use only existing DB summaries and IDs."
---

# Character Relationship Phase 2 Report

## 作業目的

前工程で作成した主要人物Relationshipを拡張し、次点人物のPersonカード作成可否を判定する。人物像を確定せず、既存DB内のFact / Timeline / Capture / Source / Theme / Index情報から、人物像・関係性・陣営構造を考えるための入口を作る。

## 事前確認結果

- REL_MEXEMP_0001-0006の実在確認: 6件すべて存在確認済み。
- 配置フォルダ確認: 6件すべて `03_Entities/Relationships/` 配下に存在。
- Personカードからのリンク確認: [[Maximilian]], [[Carlota]], [[Benito_Juarez]], [[Napoleon_III]] から `REL_MEXEMP_0001-0006` へのリンクを確認。
- Indexからのリンク確認: [[Novel_Character_Design_Index]] に `REL_MEXEMP_0001-0006` へのリンクあり。
- ID重複確認: Relationshipカードfrontmatter上の `REL_MEXEMP_0001-0006` は各1件。`REL_MEXEMP_0007` は前回レポート中の将来予定として1件だけ言及されていたが、カード実体・frontmatter IDではなかった。
- 既存最大REL ID: 実体カードでは `REL_MEXEMP_0006` が最大。今回の新規Relationshipは `REL_MEXEMP_0007` から採番。
- Git未追跡状態への対応: `git diff` には依存せず、ファイル実在、PowerShell検索、frontmatter ID検索、リンク検索で確認した。`rg` は実行権限エラーで使用不可だった。

## 作成・更新ファイル一覧

- Created: [[REL_MEXEMP_0007_Maximilian_Mexican_Conservative_Elites]]
- Created: [[REL_MEXEMP_0008_Maximilian_Mexican_Liberals]]
- Created: [[REL_MEXEMP_0009_Carlota_Imperial_Court_Project]]
- Created: [[REL_MEXEMP_0010_Bazaine_French_Command_Napoleon_III]]
- Created: [[REL_MEXEMP_0011_Juarez_Republican_Generals]]
- Created: [[REL_MEXEMP_0012_Juarez_Porfirio_Diaz]]
- Created: [[REL_MEXEMP_0013_Juarez_Escobedo]]
- Created: [[REL_MEXEMP_0014_Mexican_Conservative_Elites_French_Intervention]]
- Created: [[Bazaine]]
- Created: [[William H. Seward]]
- Created: [[Miguel_Miramon]]
- Created: [[Leonardo_Marquez]]
- Created: [[Tomas_Mejia]]
- Created: [[Mariano_Escobedo]]
- Created: [[Porfirio_Diaz]]
- Created: [[Juan_Nepomuceno_Almonte]]
- Created: [[Character_Relationship_Phase2_Report]]
- Updated: [[REL_MEXEMP_0004_Maximilian_Bazaine]]
- Updated: [[REL_MEXEMP_0006_Juarez_United_States_Seward]]
- Updated: [[Maximilian]]
- Updated: [[Carlota]]
- Updated: [[Benito_Juarez]]
- Updated: [[Napoleon_III]]
- Updated: [[Novel_Character_Design_Index]]
- Updated: [[Character_Relationship_Evidence_Expansion_Report]]

## 新規Relationship ID範囲

- `REL_MEXEMP_0007-REL_MEXEMP_0014`

## 新規作成・更新したRelationshipカード

- [[REL_MEXEMP_0007_Maximilian_Mexican_Conservative_Elites]]: 保守派支持基盤、自由主義政策、教会問題、保守派失望の入口。
- [[REL_MEXEMP_0008_Maximilian_Mexican_Liberals]]: 自由主義的自己像、Juaristas取り込み、共和国合法性との衝突。
- [[REL_MEXEMP_0009_Carlota_Imperial_Court_Project]]: Carlotaの宮廷運営・外交・実務支柱としての材料。
- [[REL_MEXEMP_0010_Bazaine_French_Command_Napoleon_III]]: Bazaine、Napoleon III、French commandの命令・現地実行・責任問題。
- [[REL_MEXEMP_0011_Juarez_Republican_Generals]]: Juárezの政治的正統性と共和派軍事指揮官の接続。
- [[REL_MEXEMP_0012_Juarez_Porfirio_Diaz]]: DíazのOaxaca / Army of the East方面の軍事寄与。
- [[REL_MEXEMP_0013_Juarez_Escobedo]]: EscobedoのArmy of the North、Querétaro包囲、Juárez方針との関係。
- [[REL_MEXEMP_0014_Mexican_Conservative_Elites_French_Intervention]]: 保守派協力者とFrench interventionの相互依存、代表性リスク。
- Updated [[REL_MEXEMP_0004_Maximilian_Bazaine]]: imperial governmentの自立性とBazaine-French command関係への入口を追記。
- Updated [[REL_MEXEMP_0006_Juarez_United_States_Seward]]: Seward Personカード作成に合わせてstatus_noteを更新。

## Personカード作成可否判定表

| Person | 判定 A/B/C | 理由 | 既存根拠 | 今回対応 |
|---|---|---|---|---|
| Achille Bazaine | A | French command、Black Decree、退位勧告、帝政自立性に重要 | [[FACT_MEXEMP_0655]], [[FACT_MEXEMP_0666]], [[FACT_MEXEMP_1367]], [[FACT_MEXEMP_2036]] | [[Bazaine]] 作成 |
| William H. Seward | A | U.S.非承認、義勇兵阻止、対仏圧力に重要 | [[FACT_MEXEMP_1327]], [[FACT_MEXEMP_1334]], [[FACT_MEXEMP_1546]], [[FACT_MEXEMP_1551]] | [[William H. Seward]] 作成 |
| Miguel Miramón | A | 保守派正統性、Maximilian擁立懐疑、最終局面に重要 | [[FACT_MEXEMP_0002]], [[FACT_MEXEMP_0279]], [[FACT_MEXEMP_0722]], [[FACT_MEXEMP_2108]] | [[Miguel_Miramon]] 作成 |
| Leonardo Márquez | A | Tacubaya評判、保守派軍事力、最終局面の強硬助言に重要 | [[FACT_MEXEMP_0360]], [[FACT_MEXEMP_0361]], [[FACT_MEXEMP_0368]], [[FACT_MEXEMP_2117]] | [[Leonardo_Marquez]] 作成 |
| Tomás Mejía | A | Sierra Gorda/Otomí系保守派、地域軍事基盤、Matamorosに重要 | [[FACT_MEXEMP_0003]], [[FACT_MEXEMP_0702]], [[FACT_MEXEMP_0708]], [[FACT_MEXEMP_1769]] | [[Tomas_Mejia]] 作成 |
| Mariano Escobedo | A | Juárezの軍事実行、Army of the North、Querétaro包囲に重要 | [[FACT_MEXEMP_1744]], [[FACT_MEXEMP_1745]], [[FACT_MEXEMP_2160]], [[FACT_MEXEMP_2197]] | [[Mariano_Escobedo]] 作成 |
| Porfirio Díaz | A | Oaxaca、Army of the East、帝政包囲に重要 | [[FACT_MEXEMP_1280]], [[FACT_MEXEMP_1284]], [[FACT_MEXEMP_2071]], [[FACT_MEXEMP_2088]] | [[Porfirio_Diaz]] 作成 |
| Juan Nepomuceno Almonte | A | 保守派政治工作、Regency、French interventionの現地窓口 | [[FACT_MEXEMP_0355]], [[FACT_MEXEMP_0356]], [[FACT_MEXEMP_0554]], [[FACT_MEXEMP_0666]] | [[Juan_Nepomuceno_Almonte]] 作成 |
| Andrew Johnson | B | U.S.政策転換・武器輸出解除で重要だが、Person像材料は薄め | [[FACT_MEXEMP_1328]], [[FACT_MEXEMP_1332]], [[FACT_MEXEMP_1342]] | 今回はカード化せず候補記録 |
| Empress Eugénie | B | Napoleon III周辺・Almonte観測・宮廷政治で重要だが、今回対象関係の中核ではない | [[FACT_MEXEMP_0416]]ほか | 今回はカード化せず候補記録 |
| Leopold I | B | Carlota形成・ベルギー王室文脈で重要だが、帝政崩壊関係の今回主軸から外れる | NCD/既存Fact出現あり | 今回はカード化せず候補記録 |
| Alice Green / Agustín de Iturbide y Green | B | Iturbide legitimacy/adoption clusterとして重要だが、個別人物像は別工程向き | [[FACT_MEXEMP_1379]]ほか | 今回はカード化せず候補記録 |

## 新規作成・更新したPersonカード

- [[Bazaine]]
- [[William H. Seward]]
- [[Miguel_Miramon]]
- [[Leonardo_Marquez]]
- [[Tomas_Mejia]]
- [[Mariano_Escobedo]]
- [[Porfirio_Diaz]]
- [[Juan_Nepomuceno_Almonte]]
- Updated: [[Maximilian]], [[Carlota]], [[Benito_Juarez]], [[Napoleon_III]]

## 主要な整理結果

### Maximilian - Mexican conservative elites

保守派は帝政成立の支持基盤だったが、Maximilianの自由主義的綱領、Juaristas取り込み、教会問題によって緊張を抱えた。失望時期は一律ではなく、Almonte、Gutiérrez de Estrada、Miramón、Márquez、Mejía、教会勢力を分ける必要がある。

### Maximilian - Mexican liberals

Maximilianは自由主義者を自称し、自由主義的綱領でJuaristasを取り込もうとしたが、Juárez側自由主義は国家主権・共和国合法性と結びついていた。政策一致だけでは妥協可能性を判断できない。

### Carlota - imperial court / imperial project

Carlotaは配偶者だけでなく、礼状代筆、Dano接待、Yucatán巡幸、Cuernavaca宮廷、渡欧交渉で帝国計画の実務的支柱として読める材料がある。孤立か支柱かは時期と場面で分ける。

### Bazaine

Bazaineは帝国の軍事的支柱であり、French commandの現地実行者でもある。Regency、Almonteへの行政助言、Black Decree、French officersの政府関与、退位勧告を通じ、帝政自立性を制限する存在としても読める。

### Seward

SewardはJuárezの単純な盟友ではなく、U.S.国益・非承認・欧州義勇兵阻止・対仏圧力を通じてJuárez側を利した制度的外交アクターとして整理した。

### Miramón / Márquez / Mejía

三者は同じ「保守派軍人」ではない。Miramónは保守派正統性とMaximilian擁立への初期懐疑、MárquezはTacubaya評判と強硬軍事、MejíaはSierra Gorda/Otomí系の地域保守派軍事基盤として分けた。

### Escobedo / Porfirio Díaz

EscobedoはJuárez政府の合法性を北部・Querétaro軍事指揮へ接続する人物、DíazはOaxaca / Army of the East方面から帝政包囲を進める人物として整理した。両者とも後年像から逆算しない。

## 解釈上の注意

- 史実・推論・解釈・噂・創作用材料をカード内で明示した。
- Shawcross由来情報は帝政側・French command・loyal witness側が厚いため、共和派側・保守派側一次資料で補強する。
- Hamnett・共和派側史料で補強すべき点: BJDOCS = Benito Juárez. Documentos, discursos y correspondencia, ed. Jorge L. Tamayo, 15 vols, Mexico, 1964-71; APBJPS = Archivo Privado de D. Benito Juárez y D. Pedro Santacilia, ed. J. Puig Casauranc, Mexico, 1928; AGN = Archivo General de la Nación (Mexico City); AGEO = Archivo del Estado de Oaxaca; FJ = Fondo Juárez, Archivo General del Estado, Oaxaca.
- その他略語: BBSHCP = Boletín Bibliográfico de la Secretaría de Hacienda y Crédito Público; BEO CMMG = Biblioteca del Estado de Oaxaca, Colección Manuel Martínez Gracida; HAHR = Hispanic American Historical Review; UNAM = Universidad Nacional Autónoma de México.
- 参照用地図: Map 1 = Mexico, 1821-53, p.282; Map 2 = The State of Oaxaca, 1857, p.283; Map 3 = The Mexican Republic in 1867, p.284.
- 一次資料で確認すべき点: Bazaine命令・書簡、Juárez-Escobedo/Díaz命令、Tacubaya関連記録、Almonte/Regency記録、U.S. official documents。

## 未処理・要確認

- Andrew Johnson、Empress Eugénie、Leopold I、Alice Green / Agustín de Iturbide y Green はB判定として保留。
- United States Orgカードは未作成。
- Mexican imperial government / imperial courtはまだ独立Orgカード未作成。
- Bazaine-Almonte書簡、Regency Council文書、French commandの原命令は未確認。
- Mexican conservative elites側のMaximilian評価変化は、保守派側資料・教会資料で補強が必要。
- Mexican liberals側のMaximilian政策評価は、liberal press、BJDOCS、APBJPSで補強が必要。

## 次工程案

- B判定人物のうち、Andrew Johnson / Empress Eugénie / Leopold I / Alice Green-Iturbide clusterのPersonカード作成可否を、Fact ID単位で再判定する。
- United States、Mexican imperial government、imperial courtをOrgカード化するか判定する。
- Bazaine-Almonte-Regencyの関係を、書簡・行政・French commandの3軸で追加Relationship化する。
- Witness clusterとして、Basch / Blasio / Felix Salm-Salm / Agnes Salm-Salmの証言比較表を作る。
- Juárez側source trailを、BJDOCS / APBJPS / AGN / AGEO / FJ単位でチェックリスト化する。
