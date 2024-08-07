from backend.app.services.project_service import ProjectService
from backend.app.services.websocket_service import WebSocketService


class WebsocketUseCase:
    def __init__(self, project_id):
        self.project_id = project_id
        self.websocket_service = WebSocketService()
        self.project_service = ProjectService()

    def execute(self):
        project = self.project_service.get_project(self.project_id)
        if not project:
            return {"status": 404, "message": "Project not found"}

        comments = self.websocket_service.get_comments(self.project_id)
        return {"status": 200, "data": comments, "message": "success"}