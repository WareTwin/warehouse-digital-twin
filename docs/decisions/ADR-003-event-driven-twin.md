# ADR-003: Use typed events for twin updates

- Status: Accepted
- Decision: Represent realtime state changes as typed event envelopes.
- Context: The dashboard needs timely updates without coupling UI components to internal service implementation.
- Consequences: Version event schemas, include event IDs/timestamps, and add broker-backed fan-out before multi-instance deployment.
