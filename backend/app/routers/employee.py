from fastapi import APIRouter, Request

from backend.app.common.custom_router import ProjectAuthDependencies
from backend.app.common.routes import EmployeeRoutes
from backend.app.schemas.employee import UpdateEmployee, CreateEmployee
from backend.app.schemas.response import Response
from backend.app.usecases.employee import CreateEmployeeUsecase, RemoveEmployeeUseCase, UpdateEmployeeUsecase
from backend.app.common.utils import merge_request

employee_router = APIRouter(
    prefix="/api/v1",
    tags=EmployeeRoutes.TAGS,
)


@employee_router.post(path=EmployeeRoutes.BASE_EMPLOYEE, response_model=Response,
                      dependencies=ProjectAuthDependencies().injected_dependencies)
async def create_employee(request: Request, body: CreateEmployee):
    payload = merge_request(request=request, body=body)
    return CreateEmployeeUsecase(payload).execute()


@employee_router.delete(path=EmployeeRoutes.DELETE_EMPLOYEE, response_model=Response,
                        dependencies=ProjectAuthDependencies().injected_dependencies)
async def delete_employee(request: Request, employee_id: str):
    payload = merge_request(request=request, employee_id=employee_id, body=None)
    return RemoveEmployeeUseCase(payload).execute()


@employee_router.put(path=EmployeeRoutes.UPDATE_EMPLOYEE, response_model=Response,
                     dependencies=ProjectAuthDependencies().injected_dependencies)
async def update_employee(request: Request, employee_id: str, body: UpdateEmployee):
    payload = merge_request(request=request, employee_id=employee_id, body=body)
    return UpdateEmployeeUsecase(payload).execute()
