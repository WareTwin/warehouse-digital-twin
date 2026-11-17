# ADR-001: Start with a modular monolith

- Status: Accepted
- Decision: Keep one deployable backend with strict internal module boundaries.
- Context: Early development benefits from simple local setup and transactional consistency.
- Consequences: Lower operational overhead now; extract services only when scale, team ownership or reliability requirements justify it.
