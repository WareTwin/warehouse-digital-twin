from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

@dataclass(frozen=True)
class RouteResult:
    path: list[Point]
    cost: float
    algorithm: str
