# GitHub Workflow

`MexicoEmpire_NovelDB`のDB更新をGitHubへ安全に反映するための詳細ルールです。`AGENTS.md`は強制ルールだけを持ち、判定と手順はこの文書を正とします。

## 完了の定義

- ローカルDBの編集・検証だけでは作業完了としない。
- 専用branch、対象ファイルだけのstage、commit、push、Pull Request作成までをGitHub反映の必須工程とする。
- branch名、commit SHA、PR URLの3点を確認できた場合だけ「GitHub反映完了」と報告する。
- 3点のいずれかがない場合は「ローカルDB更新完了・GitHub反映未完了」と明記し、不足工程と理由を報告する。
- Draft Pull RequestはGitHub上への反映が完了した状態だが、`main`への反映は未完了として区別する。

## 作業開始時の確認

作業前に次を確認する。

```powershell
git status --short --branch
git branch --show-current
git remote -v
gh auth status
git fetch origin
git rev-list --left-right --count main...origin/main
```

- GitHubリポジトリ、`origin`、default branch `main`、GitHub CLIの認証先が意図どおりであることを確認する。
- `main`がcleanなら`git switch main`と`git pull --ff-only`で最新化してから専用branchを作る。
- 未コミット変更がある場合は巻き戻さない。依頼対象と所有者を確認し、対象外変更を保持したまま明示的なpathだけをstageできる場合に限って続行する。
- `main`と`origin/main`が分岐している場合、または安全に最新化できない場合は競合扱いとし、通常PR・auto-mergeへ進めない。
- 1作業単位で1branchとする。例: `hamnett/capture-0147-description`、`chore/update-audit`、`fix/entity-link-resolution`。
- `main`上で編集を始めていた場合も、commit前に専用branchへ移す。

## 共通の安全条件

commit前に次をすべて満たす。

- 指定範囲外の内容を変更していない。
- `git add .`や`git add -A`を使わず、依頼対象のpathだけをstageしている。
- `git diff --cached --name-status`と`git diff --cached`でstage内容を確認した。
- ID重複、YAML、wiki link、locator、必須metadata、長文引用、秘密情報候補を確認した。
- 作業種別に必要なローカル検証・監査が成功している。
- `main`との競合がない。
- PR本文に変更内容、対象資料・ページまたは文書、ID、検証結果、要確認事項、対象外変更を含めていないことを記載する。

## 通常取込とauto-merge

次をすべて満たす通常の史料取込だけ、Draftではない通常Pull Requestを作成する。

- 地図・Index・運用文書の変更ではない。
- 判読、出典、ID、metadata、内容の不確実性が残っていない。
- ローカル検証がすべて成功し、必須check `safety`を実行可能である。
- 変更ファイル数が50件以下である。
- 既存ファイルの削除・移動・改名がない。
- 保護対象を変更していない。
- 秘密情報候補、想定外の差分、`main`との競合がない。

通常Pull Request作成後は、次の条件でsquash auto-mergeを設定する。

```powershell
gh pr merge <PR番号またはURL> --auto --squash --delete-branch
```

- mergeは必須check `safety`成功後にGitHubへ実行させる。
- branch protectionを回避せず、即時mergeや自己承認を行わない。
- auto-merge設定後は`gh pr view`で`autoMergeRequest`と`statusCheckRollup`を確認する。

## Draft Pull Requestで停止する条件

次のいずれかに該当する場合はDraft Pull Requestを作成し、auto-mergeを設定せず人間の確認を待つ。

- 地図またはIndexを扱う。
- 判読、出典、ID、metadata、内容に不確実性または要確認がある。
- テスト、監査、リンク検証、秘密情報検査のいずれかが失敗または実行不能である。
- `main`との競合または分岐がある。
- 変更ファイル数が50件を超える。
- 既存ファイルの削除・移動・改名を伴う。
- 保護対象を変更する。
- 想定外の大量差分、無関係な差分、または安全判断に確信を持てない点がある。
- ユーザーがDraftまたは人間レビューを指定した。

保護対象は、`.github/`、`.gitignore`、`AGENTS.md`、`README.md`、`90_Templates/`、`92_Scripts/`、GitHub運用文書、プロンプト運用文書とする。

Draft PRの状態確認例:

```powershell
gh pr view <PR番号またはURL> --json number,url,state,isDraft,mergeStateStatus,autoMergeRequest,statusCheckRollup
```

Draft PRでは`isDraft: true`、`autoMergeRequest: null`を確認する。

## stage・commit・push・PR作成

```powershell
git status --short --branch
git diff -- <対象ファイル>
git add -- <対象ファイル>
git diff --cached --name-status
git diff --cached
git commit -m "<commit message>"
git push -u origin <作業branch>
gh pr create --base main --head <作業branch> --title "<PR title>" --body-file "<PR body file>"
```

- Draft条件に該当する場合は`gh pr create`へ`--draft`を付ける。
- PR本文用一時ファイルはリポジトリ外に作るか、stage対象外であることを確認する。
- commit後に`git rev-parse HEAD`、push後にbranch名、PR作成後にPR URLを記録する。

## 禁止事項

- 通常作業で`main`へ直接commitまたはpushしない。
- 対象外のユーザー変更をstage、修正、削除、巻き戻ししない。
- `git add .`、無確認の`git add -A`、`git push --force`、履歴改変を行わない。
- `git reset --hard`、`git clean -fd`、既存IDの再利用を行わない。
- branch protection、必須check、レビュー要件を回避しない。
- Draft PRまたは安全条件未充足のPRへauto-mergeを設定しない。
- 大量改名、既存ID変更、無関係な自動整形を作業範囲へ混入させない。
- PR URL、commit SHA、branch名を推測または未確認のまま報告しない。

## merge後の確認

通常PRのauto-merge後は次を確認する。

```powershell
gh pr view <PR番号またはURL> --json number,url,state,isDraft,mergeStateStatus,autoMergeRequest,statusCheckRollup,mergedAt
git switch main
git pull --ff-only
git status --short --branch
git rev-list --left-right --count main...origin/main
```

- PRが`MERGED`で、`safety`が成功している。
- remoteの作業branchが削除されている。
- local `main`と`origin/main`が一致している。
- working treeがcleanである。作業開始前からの対象外変更がある場合は、cleanではない理由と残存pathを報告する。
- auto-merge失敗、競合、check失敗、branch protection拒否が起きた場合はforceや回避をせず、PRをopenまたはDraftのまま残す。

## 最終報告

最終報告には次を含める。

- 変更箇所と主要な変更内容。
- branch名。
- commit SHA。
- PR URL、PR番号、通常PRまたはDraftの別。
- auto-merge設定の有無。設定した場合はsquash方式と`safety`の状態。
- 実行した検証と結果。
- merge済みか、Draft／openで`main`未反映か。
- 対象外の未コミット変更、失敗、競合、要確認事項など残存事項。

branch名、commit SHA、PR URLのいずれかが欠ける場合、結論は必ず「ローカルDB更新完了・GitHub反映未完了」とする。
