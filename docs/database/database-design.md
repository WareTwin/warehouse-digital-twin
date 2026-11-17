# Database Design

Initial SQLAlchemy models are provided for:
- `warehouses`: name and grid dimensions.
- `agvs`: unique code, status and grid coordinates.
- `tasks`: title, status and JSON payload.

Before production, define foreign keys and relationships for warehouse zones, AGV assignments, orders, task dependencies, inventory, simulation runs, audit records, timestamps, optimistic concurrency, retention and tenant boundaries. Add Alembic migrations for every schema change; do not rely on `create_all` in production.
