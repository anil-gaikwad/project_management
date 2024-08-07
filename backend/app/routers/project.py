from fastapi import APIRouter, Request

from backend.app.common.custom_router import ProjectAuthDependencies
from backend.app.common.routes import ProjectRoutes
from backend.app.schemas.comment import CommentCreate
from backend.app.schemas.project import CreateProject, UpdateProject
from backend.app.schemas.response import Response
from backend.app.usecases.project import ProjectCommentUseCase, CreateProjectUseCase, UpdateProjectUseCase, \
    RemoveProjectUseCase, GetProjectUseCase
from backend.app.common.utils import merge_request

project_router = APIRouter(
    prefix="/api/v1",
    tags=ProjectRoutes.TAGS,
    dependencies=ProjectAuthDependencies().injected_dependencies
)


@project_router.post(path=ProjectRoutes.BASE_PROJECT, response_model=Response)
async def create_project(request: Request, body: CreateProject):
    payload = merge_request(request=request, body=body)
    return CreateProjectUseCase(payload).execute()


@project_router.put(path=ProjectRoutes.UPDATE_PROJECT, response_model=Response)
async def edit_project(request: Request, project_id: str, body: UpdateProject):
    payload = merge_request(request=request, project_id=project_id, body=body)
    return UpdateProjectUseCase(payload).execute()


@project_router.delete(path=ProjectRoutes.DELETE_PROJECT, response_model=Response)
async def delete_project(request: Request, project_id: str):
    payload = merge_request(request=request, project_id=project_id, body=None)
    return RemoveProjectUseCase(payload).execute()


@project_router.get(path=ProjectRoutes.GET_PROJECT, response_model=Response)
async def get_project(request: Request, project_id: str):
    payload = merge_request(request=request, project_id=project_id, body=None)
    return GetProjectUseCase(payload).execute()


@project_router.post(path=ProjectRoutes.ADD_COMMENT, response_model=Response)
async def post_comment(request: Request, project_id: str, body: CommentCreate):
    payload = merge_request(request=request, project_id=project_id, body=body)
    return ProjectCommentUseCase(payload).execute()
