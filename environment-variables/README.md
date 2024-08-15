# 環境変数を使ったアプリケーションのサンプル
## ローカルでの実行方法
.dev.varsファイルを作成し、以下の内容を記述する（`local_value`の部分は何の値でもよい）。

```
SECRET_KEY="local_value"
```

以下のコマンドを実行する。

```bash
$ npx wrangler@latest dev
```

## デプロイ方法
以下のコマンドを実行する。
`Enter a secret value:`と表示されるので、任意の値を入力する。

```bash
$ npx wrangler secret put
```

以下のコマンドを実行する。

```bash
$ npx wrangler@latest deploy
```
