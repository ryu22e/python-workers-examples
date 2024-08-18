from enum import Enum

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


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
    env = req.scope["env"]  # 環境変数を取得
    llm = OpenAI(api_key=env.API_KEY)
    prompt = PromptTemplate.from_template(
        '"{word}"という単語を使って{season}の俳句を詠んでください。'
    )
    chain = prompt | llm
    res = await chain.ainvoke({"word": word, "season": str(season)})
    haiku = res.split(".")[0].strip()
    return JSONResponse(content={"haiku": haiku})
