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
% npx wrangler@latest dev
```

curlコマンドでリクエストを送信する。

```bash
% curl -G -d word=カレー -d season="夏" http://localhost:8787/
{"haiku":"夏の日に\nカレーの香り漂う\n食欲そそる"}
% curl -X GET http://localhost:8787/pycamp-events
{"events":["Python Boot Camp in 京都","Python Boot Camp in 愛媛","Python Boot Camp in 熊本","Python Boot Camp in 札幌","Python Boot Camp in 栃木小山","Python Boot Camp in 広島","Python Boot Camp in 大阪","Python Boot Camp in 神戸","Python Boot Camp in 長野","Python Boot Camp in 香川","Python Boot Camp in 愛知","Python Boot Camp in 福岡","Python Boot Camp in 長野八ヶ岳","Python Boot Camp in 鹿児島","Python Boot Camp in 静岡","Python Boot Camp in 新潟南魚沼","Python Boot Camp in 埼玉","Python Boot Camp in 神奈川","Python Boot Camp in 金沢","Python Boot Camp in 福島","Python Boot Camp in 柏の葉","Python Boot Camp in 岩手","Python Boot Camp in 茨城","Python Boot Camp in 徳島","Python Boot Camp in 京都","Python Boot Camp in 山形","Python Boot Camp in 山梨","Python Boot Camp in 岡山","Python Boot Camp in 仙台","Python Boot Camp in 静岡県藤枝市","Python Boot Camp in 和歌山","Python Boot Camp in 福井","Python Boot Camp in 山形市","Python Boot Camp in 岐阜","Python Boot Camp in 沖縄","Python Boot Camp in 高知","Python Boot Camp in 群馬","Python Boot Camp in 福岡2nd","Python Boot Camp in 熊本2nd","Python Boot Camp in 長崎","Python Boot Camp in 山口","Python Boot Camp in 佐賀","Python Boot Camp in 広島2nd","Python Boot Camp in 静岡県沼津市","Python Boot Camp in 新潟2nd","Python Boot Camp in 香川2nd","Python Boot Camp in 鹿児島2nd","Python Boot Camp in 愛知 Re:2nd","Python Boot Camp in 富山県富山市","Python Boot Camp in 徳島2nd","Python Boot Camp in 札幌2nd","Python Boot Camp in 愛知3rd","Python Boot Camp in 山形3rd (@産業技術短大庄内校)","Python Boot Camp in 宮崎"]}
% curl -X GET http://localhost:8787/micropip-install-error
（省略)
ValueError: Can't find a pure Python 3 wheel for 'pandas==2.2.2'.
See: https://pyodide.org/en/stable/usage/faq.html#why-can-t-micropip-find-a-pure-python-wheel-for-a-package
You can use `await micropip.install(..., keep_going=True)` to get a list of all packages with missing wheels.
（省略)
```

## デプロイ方法
2024年8月31日時点では、built-in packageは本番環境へのデプロイができない。
