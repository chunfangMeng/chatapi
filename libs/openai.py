import os
import openai

from core.settings import settings


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class OpenAiHandler(metaclass=Singleton):
    def __init__(self):
        self.openai = openai
        self.openai.organization = settings.OPENAI_ORGANIZATION
        self.openai.api_key = settings.OPENAI_APIKEY
