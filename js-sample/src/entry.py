from js import Headers, Response, fetch, console, URL


API_URL = "https://httpbin.org"


async def on_fetch(request, env):
    url = URL.new(request.url)
    if url.pathname == "/old":
        return Response.redirect(url.origin, 307)

    # JSON形式でレスポンスを返すためのヘッダーを設定
    headers = Headers.new({"content-type": "application/json; charset=utf-8"}.items())

    # fetch()関数を使ってAPIサーバーにリクエストを送信
    res = await fetch(f"{API_URL}/ip")

    # レスポンスの内容をコンソールに出力
    console.log(res)

    return Response.new(res.body, headers=headers)
