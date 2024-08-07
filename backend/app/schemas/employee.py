from pydantic import BaseModel


class CreateEmployee(BaseModel):
    name: str
    email: str
    role: str


class UpdateEmployee(BaseModel):
    name: str
    email: str
    role: str
    projects: list[str] = []


