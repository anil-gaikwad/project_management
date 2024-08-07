from fastapi import APIRouter, Request

from backend.app.common.routes import CompanyRoutes
from backend.app.schemas.company import CreateCompany
from backend.app.schemas.response import Response
from backend.app.usecases.company import CreateCompanyUseCase, RemoveCompanyUseCase, GetCompanyUseCase
from backend.app.common.utils import merge_request

router = APIRouter()


company_router = APIRouter(
    prefix="/api/v1",
    tags=CompanyRoutes.TAGS,
)


@company_router.post(path=CompanyRoutes.BASE_COMPANY, response_model=Response)
async def add_company(request: Request, body: CreateCompany):
    payload = merge_request(request=request, body=body)
    return CreateCompanyUseCase(payload).execute()


@company_router.delete(path=CompanyRoutes.DELETE_COMPANY, response_model=Response)
async def remove_company(request: Request, company_id: str):
    payload = merge_request(request=request, company_id=company_id, body=None)
    return RemoveCompanyUseCase(payload).execute()


@company_router.get(path=CompanyRoutes.GET_COMPANY,  response_model=Response)
async def get_company(request: Request, company_id: str):
    payload = merge_request(request=request, company_id=company_id, body=None)
    return GetCompanyUseCase(payload).execute()
