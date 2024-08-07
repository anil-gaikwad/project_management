from backend.app.common.utils import serialize_object_id
from backend.app.core.db import Mongodb
from backend.app.models.comment import Comment


class WebSocketService:
    def __init__(self):
        self.collection = Mongodb()._mongo_client
        self.comment_model = Comment

    def get_comments(self, project_id: str):
        comments = list(self.collection.comments.find({"project_id": project_id}))
        if comments:
            return [serialize_object_id(comment) for comment in comments]
        return None
