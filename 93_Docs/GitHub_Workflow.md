# GitHub Workflow

## 基本方針

- GitHubリポジトリ名: `MexicoEmpire_NovelDB`
- Visibility: Public
- default branch: `main`
- 通常作業では`main`を直接変更しない。
- 1作業単位で1ブランチを作成する。
- 1～5画像程度を1PRとする。特殊ページは1画像1PRでもよい。
- 各画像を別commitに分けてもよい。
- 通常の史料取込はDraftではないPull Requestを作成し、`safety`成功後のsquash auto-mergeを設定する。
- 特殊作業や安全条件を満たさない作業はDraft Pull Requestで停止し、人間の確認を待つ。
- Repository Auto-mergeとmerge後のhead branch自動削除を有効にする。
- Codexはbranch protectionを回避せず、即時mergeや自己承認を行わない。

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

## 通常取込の標準フロー

通常のHamnett本文、注、Chronology等で、判読不確実性や大量変更がない場合は次を標準とする。

1. `main`を最新化する。
2. 専用branchを作成する。
3. 指定作業だけを実施する。
4. テスト、監査、差分を確認する。
5. 意図したファイルだけstageする。
6. commitする。
7. 作業branchをpushする。
8. Draftではない通常Pull Requestを作成する。
9. squash方式のauto-mergeを設定する。
10. 必須check `safety`成功後にGitHubがmergeする。
11. 作業branchを自動削除する。
12. local `main`をff-onlyで最新化する。
13. working tree cleanと`origin/main`との一致を確認する。

## 通常取込の作業終了コマンド

```powershell
git status
git diff
git add <意図したファイルだけ>
git diff --cached
git commit -m "<commit message>"
git push -u origin <作業ブランチ>
gh pr create `
  --base main `
  --head <作業ブランチ> `
  --title "<PR title>" `
  --body-file "<PR body file>"
gh pr merge <PR番号またはURL> `
  --auto `
  --squash `
  --delete-branch
```

PR本文用の一時ファイルはリポジトリ外に作成するか、stage前にリポジトリ内から除外されていることを確認する。commitへ含めない。

## Auto-mergeを設定してよい条件

次をすべて満たす場合だけauto-mergeを設定する。

- 通常の史料取込である。
- 指定範囲外の変更がない。
- ID重複がない。
- YAMLエラーがない。
- wiki linkの重大エラーがない。
- 長文引用や全文転記がない。
- `safety`対象テストが実行可能である。
- ローカル検証が成功している。
- 秘密情報候補がない。
- `main`との競合がない。
- 変更ファイル数が50件以下である。
- 既存ファイルの削除・改名がない。
- `AGENTS.md`、`.github/`、`.gitignore`、テンプレート、スクリプト等の保護対象を変更していない。

## Draft Pull Requestで停止する条件

次のいずれかに該当する場合は`gh pr create --draft ...`でDraft Pull Requestを作り、auto-mergeを設定せず人間の確認を待つ。

- 地図またはIndexを扱う。
- 判読不確実箇所がある。
- 出典特定に「要確認」がある。
- 既存IDの不整合またはID重複の疑いがある。
- 既存カードの移動、改名、削除を伴う。
- テンプレートまたはスクリプトを変更する。
- `.github/`、`AGENTS.md`、`.gitignore`を変更する。
- 変更ファイル数が50件を超える、または通常範囲を明らかに超える大量差分である。
- テストまたは監査が失敗した。
- `main`との競合がある。
- Codexが安全な判断に確信を持てない。
- ユーザーがレビューを明示的に要求した。

## Auto-merge後の確認

auto-merge設定後は次で状態を確認する。

```powershell
gh pr view <PR番号> `
  --json number,url,state,isDraft,mergeStateStatus,autoMergeRequest,statusCheckRollup
```

合理的な範囲で`statusCheckRollup`を確認する。`safety`が成功してPull Requestがmergeされたら次を実行する。

```powershell
git switch main
git pull --ff-only
git status
git log --oneline -3
```

最終的にPull Requestが`MERGED`、remoteの作業branchが削除済み、local `main`と`origin/main`が一致、working treeがcleanであることを確認する。

## Auto-merge失敗時

`safety`失敗、競合、strict check未充足、branch protection拒否、API／CLIエラー、必須check名変更、Draft状態、秘密情報候補、想定外の大量差分がある場合は、force pushや保護回避を行わない。Pull RequestをopenまたはDraftのまま残し、PR URL、停止理由、失敗check、人間確認事項、mainへ未mergeであることを報告する。

## 禁止事項

- `git add .`を無確認で実行しない。
- `git push --force`を実行しない。
- `git reset --hard`を実行しない。
- `git clean -fd`を実行しない。
- 通常作業で`main`へ直接commitしない。
- branch protectionを回避してPull Requestをmergeしない。
- Draftまたは安全条件未充足のPull Requestへauto-mergeを設定しない。
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
10. 安全条件を判定し、通常Pull RequestまたはDraft Pull Requestを作成する。
11. 通常取込だけauto-mergeを設定する。Draftには設定しない。
12. 通常取込は`safety`成功とsquash mergeを確認し、特殊作業は人間レビュー待ちで終了する。
13. merge後はlocal `main`を最新化し、remote branch削除とworking tree cleanを確認する。
