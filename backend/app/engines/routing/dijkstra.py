"""Dijkstra routing baseline; currently delegates to unit-cost BFS."""
from app.engines.contracts import Point, RouteResult
from app.engines.routing.bfs import find_path as _bfs


def find_path(blocked: set[Point], start: Point, goal: Point) -> RouteResult:
    result = _bfs(blocked, start, goal)
    return RouteResult(path=result.path, cost=result.cost, algorithm="dijkstra-baseline-bfs")
