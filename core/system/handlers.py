# handlers.py
import traceback
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from core.system.exceptions import BusinessRuleException

def register_exception_handlers(app):

    @app.exception_handler(BusinessRuleException)
    async def business_rule_exception_handler(request: Request, exc: BusinessRuleException):
        return JSONResponse(
            status_code=422,
            content={"error": "Regra de negócio", "detail": exc.message}
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": "HTTP Error", "detail": exc.detail}
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=400,
            content={"error": "Erro de validação", "detail": exc.errors()}
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "error": "Erro Interno do Servidor",
                "type": type(exc).__name__,
                "message": str(exc),
                "trace": traceback.format_exc()
            }
        )
