---
id: DOC-SCREENSHOT-NAMING
type: documentation
status: active
created: 2026-05-31
updated: 2026-05-31
tags:
  - docs
  - screenshots
source_id: ""
chapter: ""
page: ""
kindle_location: ""
screenshot_file: ""
---

# Screenshot Naming

スクリーンショットは本文保存の代替ではありません。Fact CardやCapture Noteの検証用参照として扱います。

## 保存場所

```text
09_Attachments/Screenshots/
  SRC-YYYY-NNN/
    screenshot files
```

## 基本形式

```text
sourceid_chXX_pYYYY_YYYYMMDD_seqNN_subject.png
sourceid_chXX_locNNNNNN_YYYYMMDD_seqNN_subject.png
sourceid_boxXX_folderXX_docXX_YYYYMMDD_seqNN_subject.png
```

## 例

```text
SRC-BOOK-001_ch07_p0213_20260531_01_queretaro-context.png
SRC-KINDLE-002_ch05_loc004512_20260531_01_carlota-letter-summary.png
SRC-ARCH-003_box02_folder05_doc03_20260531_01-diplomatic-note.png
```

## 命名ルール

- ファイル名はできるだけASCIIにする。
- スペースは使わず、単語区切りはハイフンかアンダースコアにする。
- 先頭に必ず `source_id` を入れる。
- ページがある場合は `p0213` のように桁をそろえる。
- Kindle位置だけの場合は `loc004512` のように書く。
- 同じ日に同じ位置を複数撮る場合は `seqNN` を増やす。
- 画像の内容説明は短いsubjectにする。

## ノートへの記録

各ノートのfrontmatterに次のように記録します。

```yaml
source_id: "SRC-BOOK-001"
chapter: "7"
page: "213"
kindle_location: ""
screenshot_file: "SRC-BOOK-001_ch07_p0213_20260531_01_queretaro-context.png"
```

本文側には、必要に応じて短く参照を書きます。

```markdown
- Screenshot file: SRC-BOOK-001_ch07_p0213_20260531_01_queretaro-context.png
```

## 注意

- スクリーンショット画像そのものに情報整理を依存しない。
- 長文引用や全文翻訳を画像の代替テキストとして保存しない。
- 要約、Fact Card、創作メモをMarkdown側に作り、画像は検証用参照として残す。

