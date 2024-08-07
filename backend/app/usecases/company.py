from backend.app.common.constant import Roles
from backend.app.common.functions import get_short_uuid
from backend.app.services.company_service import CompanyService
from backend.app.common.utils import HTTPResponse


class CreateCompanyUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.role = payload.get("role")
        self.company_service = CompanyService()

    def execute(self):
        if self.role not in Roles.ADMIN_ROLES:
            return HTTPResponse(
                status_code=403,
                message="You are not authorized to perform this action",
            ).return_response()

        payload = {
            "name": self.payload.get("name"),
            "admin_email": self.payload.get("admin_email"),
            "company_id": get_short_uuid(),
        }
        # To create a company
        response = self.company_service.create_company(payload)
        return HTTPResponse(
            status_code=200,
            data=response,
            message="success",
        ).return_response()


class RemoveCompanyUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.company_id = self.payload.get("company_id")
        self.role = self.payload.get("role")
        self.company_service = CompanyService()

    def execute(self):

        if self.role not in Roles.ADMIN_ROLES:
            return HTTPResponse(
                status_code=403,
                message="You are not authorized to perform this action",
            ).return_response()

        response = self.company_service.delete_company(company_id=self.company_id)
        return HTTPResponse(
            status_code=200,
            data=response,
            message="Company Deleted Successfully",
        ).return_response()


class GetCompanyUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.company_id = self.payload.get("company_id")
        self.company_service = CompanyService()

    def execute(self):
        response = self.company_service.get_company(company_id=self.company_id)
        return HTTPResponse(
            status_code=200,
            data=response,
            message="success",
        ).return_response()
