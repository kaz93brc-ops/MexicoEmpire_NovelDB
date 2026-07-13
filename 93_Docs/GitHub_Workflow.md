# GitHub Workflow

## 基本方針

- GitHubリポジトリ名: `MexicoEmpire_NovelDB`
- Visibility: Public
- default branch: `main`
- 通常作業では`main`を直接変更しない。
- 1作業単位で1ブランチを作成する。
- 通常の史料取込は、最新の`main`から作業branchを作り、`base: main`、`head: 作業branch`のPull Requestとして逐次マージする。未マージの取込branchをbaseに次の通常取込を積み上げない。
- 1～5画像程度を1PRとする。特殊ページは1画像1PRでもよい。
- 各画像を別commitに分けてもよい。
- 通常の史料取込はDraftではないPull Requestを作成し、`safety`成功後のsquash auto-mergeを設定する。
- 特殊作業や安全条件を満たさない作業はDraft Pull Requestで停止し、人間の確認を待つ。
- Repository Auto-mergeとmerge後のhead branch自動削除を有効にする。
- Codexはbranch protectionを回避せず、即時mergeや自己承認を行わない。

## 標準作業開始手順

新しい通常取込を始める前に、直前の取込Pull Requestが`main`へマージ済みであることを確認する。確認後、最新の`main`から専用branchを作成する。

```powershell
git status
gh pr list --state open
git switch main
git pull --ff-only
git status
git switch -c <作業ブランチ>
git merge-base HEAD origin/main
```

作業開始前に現在ブランチと`origin`も確認する。

## 通常取込ではstacked PRを作らない

Hamnett *Juarez* などの通常のCapture単位・ページ単位の史料取込では、未マージの取込branchから次の取込branchを作成してはならない。通常取込は1件ずつ`main`へ反映し、次の作業は更新後の`main`から開始する。

禁止例:

```text
main
└─ cap0122
   └─ cap0123
      └─ cap0124
```

標準形:

```text
main ── merge cap0122 ── merge cap0123 ── merge cap0124
```

直前の取込Pull Requestが未マージの場合は、次の順で扱う。

1. 安全条件を検証し、マージ可能なら既存規則に従ってauto-mergeを設定し、`main`へのマージを確認する。
2. 人間レビューが必要でマージできない場合は、新しい通常取込を開始せず、未マージ理由を報告する。
3. エージェントにマージ権限がない、または運用規則上マージできない場合も停止する。未マージbranchをbaseにして作業を続けない。
4. ユーザーがstacked PRを明示指定し、後述の例外条件を満たす場合だけ積み上げを認める。

Draftまたは人間レビュー待ちのPull Requestをbaseに次の通常取込を積み上げてはならない。

## Pull Requestのbase / head確認

通常取込のPull Requestは`base: main`、`head: 作業用取込branch`とする。PR作成前に、現在のhead、`origin/main`、merge-baseを確認し、PR作成時にbaseとheadを明示する。

```powershell
git branch --show-current
git rev-parse origin/main
git merge-base HEAD origin/main
gh pr create --base main --head <作業ブランチ> --title "<PR title>" --body-file "<PR body file>"
gh pr view --json number,url,baseRefName,headRefName,isDraft
```

`baseRefName`が`main`でなく別の取込branchになっていた場合は、通常取込として後続作業を始めず、原因を確認する。

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

1. 直前の取込Pull Requestが`main`へマージ済みであることを確認する。
2. `main`を最新化する。
3. 最新の`main`から専用branchを作成する。
4. 指定作業だけを実施する。
5. テスト、監査、差分を確認する。
6. 意図したファイルだけstageする。
7. commitする。
8. 作業branchをpushする。
9. `base: main`、`head: 作業branch`を確認し、Draftではない通常Pull Requestを作成する。
10. squash方式のauto-mergeを設定する。
11. 必須check `safety`成功後にGitHubがmergeする。
12. 作業branchを自動削除する。
13. local `main`をff-onlyで最新化する。
14. working tree cleanと`origin/main`との一致を確認する。
15. 次の通常取込は、ここまで完了してから開始する。

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
- 必須メタデータの欠落がない。
- 新規未解決wiki linkがない。
- 長文引用、全文転記、全文翻訳、全文OCRがない。
- `safety`対象テストが実行可能である。
- ローカル検証が成功している。
- 秘密情報候補がない。
- `main`との競合がない。
- 変更ファイル数が50件以下である。
- 既存ファイルの削除・改名がない。
- `AGENTS.md`、`93_Docs/GitHub_Workflow.md`、`.github/`、`.gitignore`、テンプレート、スクリプト等の保護対象を変更していない。

auto-mergeは上記条件を満たす通常取込に設定できるが、実際のmergeはGitHub Actionsの必須check `safety`成功後に限る。

## Draft Pull Requestで停止する条件

次のいずれかに該当する場合は`gh pr create --draft ...`でDraft Pull Requestを作り、auto-mergeを設定せず人間の確認を待つ。

- 地図またはIndexを扱う。
- 判読不確実箇所がある。
- 出典特定に「要確認」がある。
- 既存IDの不整合またはID重複の疑いがある。
- 既存カードの移動、改名、削除を伴う。
- テンプレートまたはスクリプトを変更する。
- `.github/`、`AGENTS.md`、`.gitignore`を変更する。
- `93_Docs/GitHub_Workflow.md`などの保護対象の運用規則を変更する。
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

`safety`失敗、競合、strict check未充足、branch protection拒否、API／CLIエラー、必須check名変更、Draft状態、秘密情報候補、想定外の大量差分がある場合は、force pushや保護回避を行わない。Pull RequestをopenまたはDraftのまま残し、PR URL、停止理由、失敗check、人間確認事項、mainへ未mergeであることを報告する。そのPull Requestをbaseに次の通常取込を積み上げない。

## stacked PRの例外

stacked PRは、次のいずれかに該当し、通常取込を逐次マージするより合理的な場合だけ使用できる。

- ユーザーが明示的にstacked PRを指示した。
- 独立した複数変更をレビュー単位に分割する技術的必要がある。
- 通常の史料取込とは異なる長期開発機能である。
- 前段Pull Requestが意図的な依存関係を持つ。

単に「前のPull Requestが未マージだから」という理由だけではstacked PRを作成しない。例外を使う場合は、作業開始前または最終報告で次を明記する。

- stacked PRを使う理由
- 各Pull Requestの依存順序
- `main`へ反映されている範囲
- 最新branchだけに存在する範囲
- 推奨マージ順序
- 後続Pull Requestのbase更新またはrebaseが必要か

既存のstacked PRを解消する場合は、各branchの内容を失わないよう、別途統合または順次マージの計画を立てる。解消作業は通常の新規取込と分け、依存関係と差分を確認してから行う。

## `main`と進捗表示の一致

完了状態は、次の4段階を区別して報告する。

1. ローカルファイルだけに存在する。
2. GitHub上の作業branchへpush済みである。
3. Pull Requestを作成済みだが`main`へ未マージである。
4. `main`へマージ済みである。

branchへのpushやPull Request作成だけを、`main`へ「GitHub反映済み」または「取込完了」と表現してはならない。最新Capture、最新Fact / Timeline範囲、Progress Master、Ingestion Readiness、次対象ページ、README等の進捗表示は、原則として`main`上の実状態と一致させる。未マージbranch上だけの進捗を示す場合は、`branch only`または`PR未マージ`と明記する。

## 取込の最終報告

GitHubを伴う取込の最終報告には、最低限次を記載する。「GitHub反映完了」だけで済ませない。

- repository root
- 対象Captureとprinted page
- 作業開始時のbase branch
- 作業branch
- commit SHA
- Pull Request番号とURL
- Pull Requestのbase / head
- Draftか通常Pull Requestか
- CI結果
- auto-merge設定の有無
- `main`へのmerge済み／未実施
- `main`上の最新Capture
- 未マージ依存Pull Requestの有無
- 次対象ページ

## 禁止事項

- `git add .`を無確認で実行しない。
- `git push --force`を実行しない。
- `git reset --hard`を実行しない。
- `git clean -fd`を実行しない。
- 通常作業で`main`へ直接commitしない。
- branch protectionを回避してPull Requestをmergeしない。
- Draftまたは安全条件未充足のPull Requestへauto-mergeを設定しない。
- 通常取込のPull Requestのbaseに別の取込branchを指定しない。
- 未マージの取込Pull Requestを理由にstacked PRへ切り替えない。
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
2. 直前の取込Pull Requestが`main`へマージ済みであることを確認する。
3. `git switch main`を実行する。
4. `git pull --ff-only`で最新化する。
5. 最新の`main`から作業専用ブランチを作る。
6. 指定作業だけを実施する。
7. テスト・監査・差分を確認する。
8. 意図したファイルだけをstageする。
9. commitする。
10. 作業ブランチをpushする。
11. base / head / merge-baseを確認し、安全条件を判定して通常Pull RequestまたはDraft Pull Requestを`main`向けに作成する。
12. 通常取込だけauto-mergeを設定する。Draftには設定しない。
13. 通常取込は`safety`成功とsquash mergeを確認し、特殊作業は人間レビュー待ちで終了する。
14. merge後はlocal `main`を最新化し、remote branch削除とworking tree cleanを確認する。
15. 次の通常取込は、直前Pull Requestの`main`へのマージ確認後に開始する。
