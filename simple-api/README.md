# Cloudflare D1を使ったシンプルなAPIのサンプル
## APIの仕様
* パス: `/`
* POSTメソッドの場合：書籍のtitleとdescriptionを受け取るとDBに登録する
* titleとdescriptionのいずれかがない場合は400エラーを返す
* GETメソッドの場合：DBに保存されている書籍情報（titleとdescription）を取得する
* POST、GET以外のメソッドの場合：405エラーを返す

## データベースの作成方法
以下のコマンドを実行する。
`Created your new D1 database.`の下に表示される`[[d1_databases]]`以下の内容をコピーして、wrangler.tomlの下に貼り付ける。

```bash
% npx wrangler d1 create bookshelf
```

## ローカルでの実行方法
以下のコマンドを実行する。

```bash
% npx wrangler d1 execute bookshelf --local --file=./schema.sql
% npx wrangler@latest dev
% curl -X POST "http://localhost:8787/" -d '{"title": "Python実践レシピ", "description": "Pythonでプログラムを作成するときに役立つ機能とライブラリを網羅した、実践的なレシピ集です。"}'
{'message': 'ok'}
% curl -X POST "http://localhost:8787/" -d '{"title": "最短距離でゼロからしっかり学ぶ Python入門 必修編", "description": "プログラミング環境の用意，基本的なプログラムの書き方に始まり，リスト，辞書，クラス，関数といった基礎的な知識からエラー処理，テストコードの書き方までを演習問題を交えながら，わかりやすく解説します。"}'
{'message': 'ok'}
% curl -X POST "http://localhost:8787/" -d '{"title": "最短距離でゼロからしっかり学ぶ Python入門 実践編", "description": "「エイリアン侵略ゲーム」「データの可視化」「Webアプリケーション」という3つのプロジェクトにチャレンジします。"}'
{'message': 'ok'}
% curl "http://localhost:8787/"
[{"id":1,"title":"Python実践レシピ","description":"Pythonでプログラムを作成するときに役立つ機能とライブラリを網羅した、実践的なレシピ集です。"},{"id":2,"title":"最短距離でゼロからしっかり学ぶ Python入門 必修編","description":"プログラミング環境の用意，基本的なプログラムの書き方に始まり，リスト，辞書，クラス，関数といった基礎的な知識からエラー処理，テストコードの書き方までを演習問題を交えながら，わかりやすく解説します。"},{"id":3,"title":"最短距離でゼロからしっかり学ぶ Python入門 実践編","description":"「エイリアン侵略ゲーム」「データの可視化」「Webアプリケーション」という3つのプロジェクトにチャレンジします。"}]
```

## デプロイ方法
以下のコマンドを実行する。

```bash
% npx wrangler d1 execute bookshelf --remote --file=./schema.sql
% npx wrangler@latest deploy
% export API_URL="https://****"  # デプロイしたアプリケーションのURL
% curl -X POST $API_URL -d '{"title": "Python実践レシピ", "description": "Pythonでプログラムを作成するときに役立つ機能とライブラリを網羅した、実践的なレシピ集です。"}'
{'message': 'ok'}
% curl -X POST $API_URL -d '{"title": "最短距離でゼロからしっかり学ぶ Python入門 必修編", "description": "プログラミング環境の用意，基本的なプログラムの書き方に始まり，リスト，辞書，クラス，関数といった基礎的な知識からエラー処理，テストコードの書き方までを演習問題を交えながら，わかりやすく解説します。"}'
{'message': 'ok'}
% curl -X POST $API_URL -d '{"title": "最短距離でゼロからしっかり学ぶ Python入門 実践編", "description": "「エイリアン侵略ゲーム」「データの可視化」「Webアプリケーション」という3つのプロジェクトにチャレンジします。"}'
{'message': 'ok'}
% curl $API_URL
[{"id":1,"title":"Python実践レシピ","description":"Pythonでプログラムを作成するときに役立つ機能とライブラリを網羅した、実践的なレシピ集です。"},{"id":2,"title":"最短距離でゼロからしっかり学ぶ Python入門 必修編","description":"プログラミング環境の用意，基本的なプログラムの書き方に始まり，リスト，辞書，クラス，関数といった基礎的な知識からエラー処理，テストコードの書き方までを演習問題を交えながら，わかりやすく解説します。"},{"id":3,"title":"最短距離でゼロからしっかり学ぶ Python入門 実践編","description":"「エイリアン侵略ゲーム」「データの可視化」「Webアプリケーション」という3つのプロジェクトにチャレンジします。"}]
```
