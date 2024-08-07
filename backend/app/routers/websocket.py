from fastapi import APIRouter, WebSocket

from backend.app.common.routes import CommentRoutes
from backend.app.usecases.websocket import WebsocketUseCase

router = APIRouter()


ws_router = APIRouter()


@ws_router.websocket(path=CommentRoutes.WEBSOCKET)
async def get_comments(websocket: WebSocket, project_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")
        comments = WebsocketUseCase(project_id=project_id).execute()
        await websocket.send_json(comments)
