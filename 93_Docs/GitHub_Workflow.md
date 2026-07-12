# GitHub Workflow

## 基本方針

- GitHubリポジトリ名: `MexicoEmpire_NovelDB`
- Visibility: Private
- default branch: `main`
- 通常作業では`main`を直接変更しない。
- 1作業単位で1ブランチを作成する。
- 1～5画像程度を1PRとする。特殊ページは1画像1PRでもよい。
- 各画像を別commitに分けてもよい。
- Pull RequestはDraftで作成し、人間の確認後にmergeする。
- Codex自身はPull Requestをmergeしない。

## 標準作業開始手順

```powershell
git status
git switch main
git pull --ff-only
git status
git switch -c <作業ブランチ>
```

作業開始前に現在ブランチと`origin`も確認する。

## ブランチ命名例

- `hamnett/capture-0147`
- `hamnett/captures-0147-0150`
- `hamnett/map-02-oaxaca-1857`
- `hamnett/index-j`
- `chore/update-audit`
- `fix/entity-link-resolution`

Hamnett取込では、必要に応じて説明を加えた`hamnett/capture-NNNN-description`形式を基本とする。

## 作業終了手順

```powershell
git status
git diff
git add <意図したファイルだけ>
git diff --cached
git commit
git push -u origin <作業ブランチ>
gh pr create --draft --base main
```

Pull Request作成後はmergeせず終了する。一時的なPR本文ファイルを使った場合は、リポジトリ内に残さない。

## 禁止事項

- `git add .`を無確認で実行しない。
- `git push --force`を実行しない。
- `git reset --hard`を実行しない。
- `git clean -fd`を実行しない。
- 通常作業で`main`へ直接commitしない。
- ユーザー指示なしにPull Requestをmergeしない。
- 大量改名、既存ID変更、無関係な自動整形を行わない。

## Pull Request本文の必須項目

- 対象資料・ページ
- 変更ファイル
- 新規・更新ID
- 主な登録内容
- 実施した検証
- 要確認事項
- 指示外変更がないこと
- 今回変更しなかった範囲

## Codex標準フロー

1. `git status`を確認する。
2. `git switch main`を実行する。
3. `git pull --ff-only`で最新化する。
4. 作業専用ブランチを作る。
5. 指定作業だけを実施する。
6. テスト・監査・差分を確認する。
7. 意図したファイルだけをstageする。
8. commitする。
9. 作業ブランチをpushする。
10. Draft Pull Requestを作成する。
11. mergeせず終了する。

Draft Pull Requestは、必要に応じて次の形式で作成する。

```powershell
gh pr create --draft --base main --title "<作業名>" --body-file "<PR本文ファイル>"
```
