from fastapi import Request, status
from fastapi.exceptions import HTTPException, RequestValidationError, ValidationError
from fastapi.responses import JSONResponse
from typing import Union


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    if exc.status_code == 401:
        return JSONResponse({
            "code": 401,
            "msg": exc.detail,
            "data": []
        }, status_code=exc.status_code)

    return JSONResponse({
        "code": exc.status_code,
        "msg": exc.detail,
        "data": exc.detail
    }, status_code=exc.status_code, headers=exc.headers)


async def params_valid_check_exception_handler(
        _: Request,
        exc: Union[RequestValidationError, ValidationError],) -> JSONResponse:
    return JSONResponse(
        {
            "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "msg": f"数据校验错误 {exc.errors()}",
            "data": exc.errors(),
        },
        status_code=422,
    )


class UnicornException(Exception):

    def __init__(self, errno, msg, data=None):
        if data is None:
            data = {}
        self.errno = errno
        self.msg = msg
        self.data = data


async def unicorn_exception_handler(_: Request, exc: UnicornException):
    return JSONResponse({
        "code": exc.errno,
        "msg": exc.msg,
        "data": exc.data,
    })

