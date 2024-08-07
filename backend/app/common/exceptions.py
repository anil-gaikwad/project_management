import logging
from http import HTTPStatus

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)


SERVER_ERROR_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
SERVER_ERROR_MESSAGE = "Internal Server Error -  Please try again later."


class CustomException(Exception):
    def __init__(
        self, status_code: int = None, message: str = None, payload: dict = None
    ) -> None:
        if payload is None:
            payload = {}
        self.status_code = status_code or HTTPStatus.BAD_REQUEST.value
        self.message = message
        self.payload = payload


class FastAPIExceptionHandlers:
    """
    Add FastAPI Custom Exception Handlers
    """

    def __init__(self, app: FastAPI) -> None:
        self.fast_api_app = app
        self.__add_global_exception_handler(exe_cls=Exception)
        self.__add_custom_exception_handler(exe_cls=CustomException)

    def __add_custom_exception_handler(self, exe_cls: dict, headers: dict = None):
        if headers is None:
            headers = {}

        @self.fast_api_app.exception_handler(exe_cls)
        def send_error_response(request: Request, cls: exe_cls):
            request_meta = request.state._state.get("request_meta", {})
            message = "CustomException- Processed" if not cls.message else cls.message
            logger.info(
                message,
                extra={
                    "props": {
                        "response_status": cls.status_code,
                        "method": request.method,
                        "path": request.url.path,
                        "tenant_id": request_meta.get("tenant_id"),
                    }
                },
                exc_info=cls.status_code >= status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
            if request_meta:
                headers["X-Request-ID"] = request_meta.get("correlation_id")
            return JSONResponse(
                status_code=cls.status_code,
                content={"message": cls.message, "data": cls.payload, "error": True},
                headers=headers,
            )

    def __add_global_exception_handler(self, exe_cls: Exception, headers: dict = None):
        if headers is None:
            headers = {}

        @self.fast_api_app.exception_handler(exe_cls)
        async def global_exception_handler(request: Request, cls: exe_cls):
            request_meta = request.state._state.get("request_meta", {})
            if request_meta:
                headers["X-Request-ID"] = request_meta.get("correlation_id")
            logger.exception(
                f"GlobalException - {str(cls)}",
                extra={
                    "props": {
                        "type": "request",
                        "method": request.method,
                        "path": request.url.path,
                        "response_status": SERVER_ERROR_CODE,
                        "tenant_id": request_meta.get("tenant_id"),
                    }
                },
                exc_info=cls,
                stack_info=True,
            )
            return JSONResponse(
                status_code=SERVER_ERROR_CODE,
                content={
                    "message": SERVER_ERROR_MESSAGE,
                    "error": True,
                    "Success": False,
                },
                headers=headers,
            )

