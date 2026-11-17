# ADR-002: Use PostgreSQL

- Status: Accepted
- Decision: Use PostgreSQL as the primary relational store.
- Context: Warehouse entities and task/order relationships require transactions, constraints and reliable querying.
- Consequences: Use Alembic migrations, indexes and explicit transaction boundaries. Consider time-series/event storage separately only when justified by measured load.
