class ConnectionManager:
    """In-memory connection registry for local demos; use pub/sub for multi-worker deployments."""
    def __init__(self):
        self.connections = []

    async def connect(self, websocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket):
        if websocket in self.connections:
            self.connections.remove(websocket)
