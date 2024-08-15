# Cloudflare D1を使ったシンプルなAPIのサンプル
## データベースの作成方法
以下のコマンドを実行する。
`Created your new D1 database.`の下に表示される`[[d1_databases]]`以下の内容をコピーして、wrangler.tomlの下に貼り付ける。

```bash
$ npx wrangler d1 create bookshelf
```

## ローカルでの実行方法
以下のコマンドを実行する。

```bash
$ npx wrangler d1 execute bookshelf --local --file=./schema.sql
$ npx wrangler@latest dev
```

## デプロイ方法
以下のコマンドを実行する。

```bash
$ npx wrangler d1 execute bookshelf --remote --file=./schema.sql
$ npx wrangler@latest deploy
```
