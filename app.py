import uvicorn

from core import exceptions
from core.settings import settings
from core.routers import api_router
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError


app = FastAPI(
    title=settings.TITLE,
    debug=settings.APP_DEBUG,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.DOCUMENTATION_URL,
)

app.add_exception_handler(HTTPException, exceptions.http_error_handler)
app.add_exception_handler(RequestValidationError, exceptions.params_valid_check_exception_handler)
app.add_exception_handler(exceptions.UnicornException, exceptions.unicorn_exception_handler)

app.include_router(api_router, tags=['Chat'])


if __name__ == '__main__':
    uvicorn.run(
        app="app:app",
        host="0.0.0.0",
        port=8080,
        reload=settings.APP_DEBUG,
    )

