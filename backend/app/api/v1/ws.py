from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["realtime"])

@router.websocket("/ws/events")
async def events(websocket: WebSocket):
    await websocket.accept()
    try:
        await websocket.send_json({"type": "connection.ready", "payload": {"status": "connected"}})
        while True:
            message = await websocket.receive_text()
            await websocket.send_json({"type": "echo", "payload": {"message": message}})
    except WebSocketDisconnect:
        return
