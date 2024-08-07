from backend.app.common.utils import serialize_object_id
from backend.app.core.db import Mongodb
from backend.app.models.company import Company


class CompanyService:
    def __init__(self):
        self.collection = Mongodb()._mongo_client
        self.company_model = Company

    def create_company(self, payload: dict):
        company_data = self.company_model(**payload).dict(by_alias=True, exclude={'id'})
        result = self.collection.companies.insert_one(company_data)
        company_data["_id"] = str(result.inserted_id)
        return company_data

    def delete_company(self, company_id: str):
        result = self.collection.companies.find_one_and_delete({"company_id": company_id})
        if result:
            return serialize_object_id(result)
        return None

    def get_company(self, company_id: str):
        company = self.collection.companies.find_one({"company_id": company_id})
        if company:
            return serialize_object_id(company)
        return None
