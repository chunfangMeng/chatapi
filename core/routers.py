from api.v1.chat_views import chat_router
from fastapi import APIRouter


api_router = APIRouter(prefix='/api/v1')

api_router.include_router(chat_router)
