from js import Response

async def on_fetch(request, env):
    return Response.new(f"My name is {env.MY_NAME}.\nSECRET_KEY: {env.SECRET_KEY}")
