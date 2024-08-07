from backend.app.common.utils import serialize_object_id
from backend.app.core.db import Mongodb
from backend.app.models.employee import Employee


class EmployeeService:
    def __init__(self):
        self.collection = Mongodb()._mongo_client
        self.employee_model = Employee

    def create_employee(self, payload: dict):
        employee_data = self.employee_model(**payload).dict(by_alias=True, exclude={'id'})
        result = self.collection.employees.insert_one(employee_data)
        employee_data["_id"] = str(result.inserted_id)
        return employee_data

    def update_employee(self, employee_id: str, payload: dict):
        result = self.collection.employees.find_one_and_update(
            {"employee_id": employee_id}, {"$set": payload}, return_document=True
        )
        if result:
            return serialize_object_id(result)
        return None

    def delete_employee(self, employee_id: str):
        result = self.collection.employees.find_one_and_delete({"employee_id": employee_id})
        if result:
            return serialize_object_id(result)
        return None

    def get_employees(self, employee_id: str):
        employee = self.collection.employees.find_one({"employee_id": employee_id})
        if employee:
            return serialize_object_id(employee)
        return None




