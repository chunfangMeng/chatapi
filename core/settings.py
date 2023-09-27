import os

from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings

load_dotenv(find_dotenv(), override=True)


class Config(BaseSettings):
    TITLE: str = 'ChatApi'
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    DOCS_URL: str = '/docs' if APP_DEBUG else None
    DOCUMENTATION_URL: str = '/documentation' if APP_DEBUG else None
    OPENAI_APIKEY: str = os.environ.get('OPENAI_APIKEY')
    OPENAI_ORGANIZATION: str = os.environ.get('OPENAI_ORGANIZATION')


settings = Config()
