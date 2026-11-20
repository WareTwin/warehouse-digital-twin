"""A* routing implementation will share the routing engine contract."""
from app.engines.contracts import Point, RouteResult
from app.engines.routing.bfs import find_path as _bfs


def find_path(blocked: set[Point], start: Point, goal: Point) -> RouteResult:
    # BFS is retained as a correctness baseline until the A* implementation is benchmarked.
    result = _bfs(blocked, start, goal)
    return RouteResult(path=result.path, cost=result.cost, algorithm="astar-baseline-bfs")
