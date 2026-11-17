from collections import deque
from app.engines.contracts import Point, RouteResult

def find_path(blocked: set[Point], start: Point, goal: Point) -> RouteResult:
    if start in blocked or goal in blocked:
        raise ValueError("Start and goal must be traversable")
    queue = deque([start])
    previous: dict[Point, Point | None] = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            node: Point | None = current
            while node is not None:
                path.append(node)
                node = previous[node]
            path.reverse()
            return RouteResult(path=path, cost=float(len(path) - 1), algorithm="bfs")
        for nxt in (Point(current.x+1,current.y), Point(current.x-1,current.y),
                    Point(current.x,current.y+1), Point(current.x,current.y-1)):
            if nxt not in blocked and nxt not in previous and nxt.x >= 0 and nxt.y >= 0:
                previous[nxt] = current
                queue.append(nxt)
    raise ValueError("No route found")
