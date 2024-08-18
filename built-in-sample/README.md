# built-in packagesのサンプル
## ローカルでの実行方法
以下のURLからOpenAIのAPIキーを取得する。

<https://platform.openai.com/api-keys>

.dev.varsを作成し、以下のようにAPIキーを記述する。

```
API_KEY=sk-xxxxxxxx
```

以下のコマンドを実行する。

```bash
$ npx wrangler@latest dev
```

curlコマンドでリクエストを送信する。

```bash
$ curl -G -d word=カレー -d season="夏" http://localhost:8787/
{"haiku":"夏の日に\nカレーの香り漂う\n食欲そそる"}
```

## デプロイ方法
2024年8月31日時点では、built-in packageは本番環境へのデプロイができない。
