from collections.abc import Callable
from app.engines.contracts import Point, RouteResult

RouteEngine = Callable[[set[Point], Point, Point], RouteResult]
_REGISTRY: dict[str, RouteEngine] = {}

def register(name: str, engine: RouteEngine) -> None:
    if name in _REGISTRY:
        raise ValueError(f"Engine already registered: {name}")
    _REGISTRY[name] = engine

def get_engine(name: str) -> RouteEngine:
    try:
        return _REGISTRY[name]
    except KeyError as exc:
        raise ValueError(f"Unknown routing engine: {name}") from exc
