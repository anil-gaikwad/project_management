from backend.app.common.functions import get_current_utc_time, get_short_uuid
from backend.app.common.utils import HTTPResponse
from backend.app.services.company_service import CompanyService
from backend.app.services.employee_service import EmployeeService
from backend.app.services.project_service import ProjectService


class CreateProjectUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.company_id = payload.get("company_id")
        self.project_service = ProjectService()
        self.company_service = CompanyService()

    def execute(self):

        company = self.company_service.get_company(company_id=self.company_id)
        if not company:
            return HTTPResponse(
                status_code=400,
                message="Company not found",
            ).return_response()

        # create project payload
        payload = {
            "company_id": self.company_id,
            "name": self.payload.get("name"),
            "description": self.payload.get("description"),
            "project_id": get_short_uuid()
        }
        response = self.project_service.create_project(payload=payload)

        return HTTPResponse(
            status_code=200,
            data=response,
            message="success",
        ).return_response()


class UpdateProjectUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.project_id = self.payload.get("project_id")
        self.company_id = payload.get("company_id")
        self.project_service = ProjectService()
        self.company_service = CompanyService()

    def execute(self):

        company = self.company_service.get_company(company_id=self.company_id)
        if not company:
            return HTTPResponse(
                status_code=400,
                message="Company not found",
            ).return_response()

        project = self.project_service.get_project(project_id=self.project_id)

        if not project:
            return HTTPResponse(
                status_code=400,
                message="Project not found",
            ).return_response()

        # update the last_modified_date in payload
        self.payload["last_modified_date"] = get_current_utc_time()
        response = self.project_service.update_project(project_id=self.project_id, payload=self.payload)

        return HTTPResponse(
            status_code=200,
            data=response,
            message="success",
        ).return_response()


class RemoveProjectUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.project_service = ProjectService()
        self.project_id = self.payload.get("project_id")

    def execute(self):
        project = self.project_service.get_project(project_id=self.project_id)

        if not project:
            return HTTPResponse(
                status_code=400,
                message="Project not found",
            ).return_response()

        self.project_service.delete_project(project_id=self.project_id)
        return HTTPResponse(
            status_code=200,
            message="Project deleted Successfully",
        ).return_response()


class GetProjectUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.project_service = ProjectService()
        self.project_id = self.payload.get("project_id")

    def execute(self):
        project = self.project_service.get_project(project_id=self.project_id)
        if not project:
            return HTTPResponse(
                status_code=400,
                message="Project not found",
            ).return_response()

        return HTTPResponse(
            status_code=200,
            data=project,
            message="success",
        ).return_response()


class ProjectCommentUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.project_id = self.payload.get("project_id")
        self.project_service = ProjectService()

    def execute(self):

        project = self.project_service.get_project(project_id=self.project_id)
        if not project:
            return HTTPResponse(
                status_code=400,
                message="Project not found",
            ).return_response()

        payload = {
            "project_id": self.project_id,
            "author_id": self.payload.get("employee_id"),
            "comment": self.payload.get("comment"),
            "comment_id": get_short_uuid()
        }
        response = self.project_service.add_comment(payload=payload)
        return HTTPResponse(
            status_code=200,
            data=response,
            message="success",
        ).return_response()
