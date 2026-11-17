# Low-Level Design

## Backend package boundaries
- `api/v1`: transport and request/response validation only.
- `schemas`: Pydantic transport contracts.
- `services`: application use cases.
- `engines`: pure or isolated algorithms.
- `db`: SQLAlchemy metadata, session and persistence models.
- `core`: settings, security primitives, dependencies and shared errors.

## Algorithm contract
Routing engines accept traversability constraints, a start point and a goal point and return a path, cost and algorithm identifier. Keep algorithms deterministic and cover edge cases with unit tests.

## Frontend boundaries
- `app`: routes and layouts.
- `components`: reusable visual elements.
- `features`: capability-specific UI and data logic.
- `hooks`: reusable stateful integration.
- `lib`: API and WebSocket clients.
- `types`: shared frontend types.
