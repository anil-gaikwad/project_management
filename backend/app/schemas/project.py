from pydantic import BaseModel


class CreateProject(BaseModel):
    name: str
    description: str


class UpdateProject(BaseModel):
    title: str
    description: str


