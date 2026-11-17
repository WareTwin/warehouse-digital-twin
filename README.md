# WareTwin — Warehouse Digital Twin

A collaborative foundation for simulating and managing warehouse operations, including warehouse layout, AGV fleets, task allocation, routing, orders, analytics, and real-time state updates.

## Technology

- **Backend:** Python 3.12, FastAPI, SQLAlchemy 2, Alembic, PostgreSQL
- **Frontend:** Next.js App Router, React, TypeScript
- **Realtime:** WebSockets
- **Infrastructure:** Docker Compose
- **Quality:** pytest, Ruff, TypeScript, ESLint, GitHub Actions

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Then open:
- Frontend: http://localhost:3000
- Backend health: http://localhost:8000/health
- API documentation: http://localhost:8000/docs

Stop services with `docker compose down`. Add `-v` only when you intentionally want to delete the local PostgreSQL volume.

## Repository map

```text
backend/       FastAPI app, domain services, engines, migrations, tests
frontend/      Next.js dashboard and reusable UI components
contracts/     OpenAPI and shared event definitions
docs/          Architecture, database, API, ADRs, team workflow
scripts/       OpenAPI export, seed and demo reset helpers
.github/       CI, issue templates, PR template, CODEOWNERS
```

## Development status

This is a runnable engineering foundation, not a certified warehouse-control product. The health endpoint, API skeleton, domain contracts, routing baseline, event types, UI shell, Docker environment, and CI checks are provided. Implement and validate operational algorithms against realistic scenarios before using them in a live facility.

## Engineering and safety

- Keep business rules in `services/` and `engines/`, not route handlers.
- Treat `contracts/` as the shared interface source of truth.
- Use pull requests for all changes to `main`.
- Never commit `.env`, credentials, tokens, customer data, or production telemetry.
- Do not connect this demo to physical warehouse equipment without authorization, safety engineering, fail-safe design, and operational acceptance testing.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md), [Git workflow](docs/team/GIT-WORKFLOW.md), and [Security policy](SECURITY.md).
