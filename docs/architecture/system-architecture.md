# System Architecture

## Context

WareTwin models a warehouse as a digital state and exposes workflows for warehouse layout, AGV fleet, tasks, orders, routing and simulation.

## Initial architecture: modular monolith

- FastAPI provides the HTTP and WebSocket boundary.
- Domain services own use cases and transaction boundaries.
- Engines contain routing, allocation, simulation and optimization algorithms.
- PostgreSQL stores durable state.
- Next.js provides the operator dashboard.
- Shared contracts define API and event interfaces.

## Runtime flow

1. Frontend requests current state through the versioned API.
2. API validates input and delegates to a service.
3. Services use repositories/database sessions and domain engines.
4. State changes are persisted and emitted as typed events.
5. WebSocket clients receive updates and refresh relevant views.

## Deployment evolution

Start with Docker Compose for development. For a production deployment, add managed PostgreSQL, TLS termination, secrets management, centralized logs/metrics, background workers, Redis or a message broker for multi-instance event fan-out, backups, and a tested recovery plan.

## Safety boundary

The digital twin is advisory until separately validated. Never use this starter as a direct control plane for physical AGVs or safety systems.
