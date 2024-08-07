from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from backend.app.common.functions import get_current_utc_time


class Comment(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    project_id: str
    author_id: str
    comment: str
    comment_id: Optional[str] = None
    create_date: datetime = Field(default_factory=lambda: get_current_utc_time())
    last_modified_date: datetime = Field(default_factory=lambda: get_current_utc_time())

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
