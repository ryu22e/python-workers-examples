from js import Headers, Response
from pyodide.ffi import JsException

async def on_fetch(request, env):
    # JSON形式でレスポンスを返すためのヘッダーを設定
    headers = Headers.new({"content-type": "application/json; charset=utf-8"}.items())

    if "POST" in request.method:
        # POSTリクエストの場合
        try:
            data = await request.json()
        except JsException:
            # json()メソッドはリクエストボディがJSONでない場合に例外を発生させる仕様なので、ここで例外処理を行う
            return Response.new({"error": "Invalid JSON"}, status=400, headers=headers)
        # JSONリクエストボディからtitleとdescriptionを取得
        title = getattr(data, "title")
        description = getattr(data, "description")
        if not title or not description:
            # titleとdescriptionがない場合はエラーレスポンスを返す
            return Response.new(
                {"error": "Title and description are required"},
                status=400,
                headers=headers,
            )
        # データベースに書籍情報を登録
        await env.DB.prepare(
            "INSERT INTO books (title, description) VALUES (?, ?)"
        ).bind(title, description).run()
        return Response.new({"message": "ok"}, headers=headers)
    elif "GET" in request.method:
        # GETリクエストの場合
        # データベースから書籍情報を取得
        r = await env.DB.prepare("SELECT * from books").all()
        return Response.json(r.results, headers=headers)
    else:
        # POST, GET以外のリクエストの場合
        # POST, GET以外には非対応なので、405エラーを返す
        return Response.new({"error": "Method not allowed"}, status=405, headers=headers)
