# API Documentation

FastAPI generates interactive API documentation at `/docs` while the backend is running.

Initial endpoints:
- `GET /health`
- `POST /api/v1/auth/demo-token` (development-only)
- `GET /api/v1/warehouses`
- `POST /api/v1/warehouses`
- `GET /api/v1/fleet/agvs`
- `GET /api/v1/tasks`
- `POST /api/v1/tasks`
- `GET /api/v1/twin/snapshot`
- `POST /api/v1/routing/bfs`
- `WS /api/v1/ws/events`

Most list endpoints are placeholders. Do not treat their empty responses as production data.
