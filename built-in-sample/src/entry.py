from enum import Enum

import micropip
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


PYCAMP_URL = "https://www.pycon.jp/support/bootcamp.html"


async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)


app = FastAPI()


class Season(Enum):
    sprint = "春"
    summer = "夏"
    autumn = "秋"
    winter = "冬"


@app.get("/")
async def root(req: Request, word: str, season: Season):
    """AIに俳句を詠ませる"""

    # 環境変数を取得する際はpydantic.BaseSettingsを使わず、この書き方にする。
    env = req.scope["env"]
    llm = OpenAI(api_key=env.API_KEY)
    prompt = PromptTemplate.from_template(
        '"{word}"という単語を使って{season}の俳句を詠んでください。'
    )
    chain = prompt | llm
    res = await chain.ainvoke({"word": word, "season": str(season)})
    haiku = res.split(".")[0].strip()
    return JSONResponse(content={"haiku": haiku})


@app.get("/pycamp-events")
async def pycamp_events(req: Request):
    """Python Boot Campのイベント情報を取得する"""

    await micropip.install("beautifulsoup4==4.12.3")

    # beautifulsoup4はbuilt-in packagesにはないがmicropipでインストールできる
    from bs4 import BeautifulSoup

    async with httpx.AsyncClient() as client:
        r = await client.get(PYCAMP_URL)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        section = soup.select_one("section#id7")
        table = section.select_one("table") if section else None
        tbody = table.tbody if table else None

        events = (tr.find_all("td")[0].text for tr in tbody.find_all("tr"))
        events = [
            event
            for event in events
            if event.startswith("Python Boot Camp in") and "中止" not in event
        ]
        return JSONResponse(content={"events": events})


@app.get("/micropip-install-error")
async def micropip_install_error(req: Request):
    """micropip.install()が失敗する例"""

    # pandas==2.2.2はpure Pyhon wheelがないため、micropipでインストールできずエラーになる
    # 参考: https://pyodide.org/en/stable/usage/faq.html#why-can-t-micropip-find-a-pure-python-wheel-for-a-package
    await micropip.install("pandas==2.2.2")

    import pandas as pd

    data = [1, 2, 3, 4]
    df = pd.DataFrame(data, columns=["number"])
    return JSONResponse(content={"participants": df.to_dict(orient="records")})
