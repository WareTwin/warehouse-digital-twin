from app.engines.contracts import Point
from app.engines.routing.bfs import find_path

def test_bfs_finds_shortest_manhattan_route():
    result = find_path(set(), Point(0, 0), Point(2, 1))
    assert result.cost == 3
    assert result.path[0] == Point(0, 0)
    assert result.path[-1] == Point(2, 1)

def test_bfs_avoids_blocked_cell():
    result = find_path({Point(1, 0)}, Point(0, 0), Point(2, 0))
    assert Point(1, 0) not in result.path
