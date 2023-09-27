from fastapi import APIRouter
from fastapi.responses import JSONResponse

from libs.openai import OpenAiHandler

chat_router = APIRouter()


@chat_router.post('/chat/message/')
async def send_message(message: str):
    openai_handler = OpenAiHandler()
    response = openai_handler.openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.5,
        max_tokens=2048,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return JSONResponse({
        "code": 200,
        "msg": "success",
        "data": response['choices'][0].text
    })

