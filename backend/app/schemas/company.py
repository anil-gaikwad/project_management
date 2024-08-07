from pydantic import BaseModel


class CreateCompany(BaseModel):
    name: str
    admin_email: str


class CompanyUpdate(BaseModel):
    name: str
    admin_email: str
    password: str
