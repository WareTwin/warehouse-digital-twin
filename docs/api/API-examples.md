# API Examples

Health check:

```bash
curl http://localhost:8000/health
```

Create a warehouse (starter in-memory response):

```bash
curl -X POST http://localhost:8000/api/v1/warehouses \
  -H "Content-Type: application/json" \
  -d '{"name":"Demo DC","width":20,"height":12}'
```

Route around an obstacle:

```bash
curl -X POST http://localhost:8000/api/v1/routing/bfs \
  -H "Content-Type: application/json" \
  -d '{"start":{"x":0,"y":0},"goal":{"x":3,"y":0},"blocked":[{"x":1,"y":0}]}'
```
