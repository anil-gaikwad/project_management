from backend.app.common.functions import get_short_uuid, get_current_utc_time
from backend.app.services.company_service import CompanyService
from backend.app.services.employee_service import EmployeeService
from backend.app.common.utils import HTTPResponse


class CreateEmployeeUsecase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.company_id = payload.get("company_id",)
        self.employee_service = EmployeeService()
        self.company_service = CompanyService()

    def execute(self):

        # check if the company is available or not
        company = self.company_service.get_company(company_id=self.company_id)

        if not company:
            return HTTPResponse(
                status_code=400,
                message="Company not found",
            ).return_response()

        payload = {
            "name": self.payload.get("name"),
            "email": self.payload.get("email"),
            "company_id": self.company_id,
            "role":  self.payload.get("role"),
            "employee_id": get_short_uuid(),
        }
        response = self.employee_service.create_employee(payload)

        return HTTPResponse(
            status_code=200,
            data=response,
            message="success",
        ).return_response()


class RemoveEmployeeUseCase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.employee_id = self.payload.get("employee_id")
        self.employee_service = EmployeeService()

    def execute(self):

        employee = self.employee_service.get_employees(employee_id=self.employee_id)

        if not employee:
            return HTTPResponse(
                status_code=400,
                message="Employee not found",
            ).return_response()

        self.employee_service.delete_employee(employee_id=self.employee_id)

        return HTTPResponse(
            status_code=200,
            message="Employee has been deleted",
        ).return_response()


class UpdateEmployeeUsecase:
    def __init__(self, payload):
        self.payload = payload.get("payload")
        self.company_id = payload.get("company_id")
        self.employee_id = self.payload.get("employee_id")
        self.company_service = CompanyService()
        self.employee_service = EmployeeService()

    def execute(self):
        # check if the company is available or not
        company = self.company_service.get_company(company_id=self.company_id)

        if not company:
            return HTTPResponse(
                status_code=400,
                message="Company not found",
            ).return_response()

        employee = self.employee_service.get_employees(employee_id=self.employee_id)

        if not employee:
            return HTTPResponse(
                status_code=400,
                message="Employee not found",
            ).return_response()

        # update the last_modified_date in payload
        self.payload["last_modified_date"] = get_current_utc_time()
        response = self.employee_service.update_employee(employee_id=self.employee_id, payload=self.payload)

        return HTTPResponse(
            status_code=200,
            data=response,
            message="success",
        ).return_response()
