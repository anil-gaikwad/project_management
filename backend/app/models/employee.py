from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from backend.app.common.functions import get_current_utc_time


class Employee(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    email: str
    name: str
    company_id: str
    employee_id: Optional[str] = None
    role: str  # "employee"
    projects: list[str] = []
    create_date: datetime = Field(default_factory=lambda: get_current_utc_time())
    last_modified_date: datetime = Field(default_factory=lambda: get_current_utc_time())

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
