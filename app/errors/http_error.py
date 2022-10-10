from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:

    if type(exc.detail) is list:
        return JSONResponse({"errors": exc.detail}, status_code=exc.status_code)
    else:
        return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)
