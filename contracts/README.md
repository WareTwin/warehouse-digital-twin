# Shared contracts

`events.ts` defines the event envelope and initial realtime event types. `openapi.json` is a bootstrap snapshot, not a substitute for the generated live schema.

Export the current backend schema from the repository root:

```bash
python scripts/export_openapi.py
```

Coordinate breaking API/event changes with backend and frontend owners. Prefer additive changes and document versioning decisions.
