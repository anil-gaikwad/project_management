from backend.app.common.utils import serialize_object_id
from backend.app.core.db import Mongodb
from backend.app.models.comment import Comment
from backend.app.models.project import Project


class ProjectService:
    def __init__(self):
        self.collection = Mongodb()._mongo_client
        self.project_model = Project
        self.comment_model = Comment

    def get_project(self, project_id: str):
        project = self.collection.projects.find_one({"project_id": project_id})
        if project:
            return serialize_object_id(project)
        return None

    def create_project(self, payload: dict):
        project_data = self.project_model(**payload).dict(by_alias=True, exclude={'id'})
        result = self.collection.projects.insert_one(project_data)
        project_data["_id"] = str(result.inserted_id)
        return project_data

    def update_project(self, project_id: str, payload: dict):
        result = self.collection.projects.find_one_and_update(
            {"project_id": project_id}, {"$set": payload}, return_document=True
        )
        if result:
            return serialize_object_id(result)
        return None

    def delete_project(self, project_id: str):
        result = self.collection.projects.find_one_and_delete({"project_id": project_id})
        if result:
            return serialize_object_id(result)
        return None

    def add_comment(self, payload: dict):
        comment_data = self.comment_model(**payload).dict(by_alias=True, exclude={'id'})
        result = self.collection.comments.insert_one(comment_data)
        comment_data["_id"] = str(result.inserted_id)
        return comment_data


