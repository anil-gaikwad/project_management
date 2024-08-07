from typing import Optional, Union, Any

from pydantic import BaseModel


class Response(BaseModel):
    error: bool = False
    data: Optional[Union[list[Any], dict[str, Any]]] = None
    success: bool = True
    message: Optional[str] = ""
    status_code: int = 200
