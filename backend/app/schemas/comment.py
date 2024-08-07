from pydantic import BaseModel


class CommentCreate(BaseModel):
    comment: str
    employee_id: str