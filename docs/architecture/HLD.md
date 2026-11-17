# High-Level Design

## Components
- Web dashboard: operator views and scenario controls.
- API application: authentication boundary, validation and orchestration.
- Domain services: warehouse, fleet, tasks, orders, audit and twin snapshot.
- Engines: routing, coordination, allocation, simulation and ML experiments.
- PostgreSQL: durable warehouse and operational records.
- Realtime gateway: WebSocket event delivery.

## Quality attributes
- Modularity: isolate business capabilities behind service interfaces.
- Testability: algorithms accept deterministic inputs and return deterministic outputs.
- Observability: structured logs, metrics and trace correlation.
- Security: authenticated access, least privilege, secret rotation and audit trails.
- Resilience: database health checks, bounded retries and graceful degradation.
