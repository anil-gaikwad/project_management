import logging

from typing import Optional, Union, Any

from bson import ObjectId
from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from backend.app.schemas.response import Response

logger = logging.getLogger(__name__)


def merge_request(
    request: Request,
    body: Optional[Union[BaseModel, list, dict]],
    external_param: str = None,
    **query_path_params,
) -> dict:
    """
    Merge request body, request path params, query params and payload
    Args:
        request: FastAPI request
        body: Body to be merged if any
        **query_path_params: Query params and path params to be merged if any
        external_param: Param which will be added in payload
    """
    if body and isinstance(body, BaseModel):
        payload = body.model_dump(exclude_unset=True)
    elif body and isinstance(body, list):
        payload = {external_param: [item.dict(exclude_unset=True) for item in body]}
    else:
        payload = body if body else {}

    for key, value in query_path_params.items():
        payload[key] = value

    # Get context from request state
    context = request.state.context if hasattr(request.state, "context") else {}
    if "company_id" in context:
        payload["company_id"] = context["company_id"]
    request = {**context, **request.state._state, "payload": payload}
    logger.info(f"request: {payload}")
    return request


class HTTPResponse:
    def __init__(
        self,
        status_code: int = None,
        data: Optional[Union[list[Any], dict[str, Any]]] = None,
        message: Optional[str] = "",
    ):
        self.status_code = status_code
        if data is None:
            self.data = {}
        elif isinstance(data, list) and not data:
            self.data = []
        else:
            self.data = data
        self.message = message or ""
        self.error = status_code > 300 if status_code is not None else False

    def return_response(self):
        if self.status_code > 300:
            return JSONResponse(
                status_code=self.status_code,
                content={
                    "message": self.message,
                    "error": True,
                    "success": False,
                    "data": self.data,
                },
            )
        return Response(
            error=self.error,
            data=self.data,
            message=self.message,
            success=not self.error,
            status_code=self.status_code,
        )


def serialize_object_id(data: dict[str, Any]) -> dict[str, Any]:
    if '_id' in data and isinstance(data['_id'], ObjectId):
        data['_id'] = str(data['_id'])
    return data


def get_validation_error_message(error_dict: dict, loc: tuple) -> str:
    error_type = error_dict.get("type")
    if not loc or error_type == "json_invalid":
        return "Invalid Payload"

    if error_type == "type_error.dict":
        return "Value is not a valid dict"
    elif error_type == "value_error.missing":
        return f"{loc[-1]} is required property"
    elif error_type == "value_error":
        return error_dict.get("msg")