# Architecture Diagram

```mermaid
flowchart LR
  UI[Next.js Dashboard] --> API[FastAPI API]
  UI <-->|WebSocket events| WS[Realtime Gateway]
  API --> SVC[Domain Services]
  SVC --> ENG[Routing / Allocation / Simulation Engines]
  SVC --> DB[(PostgreSQL)]
  ENG --> SVC
```
