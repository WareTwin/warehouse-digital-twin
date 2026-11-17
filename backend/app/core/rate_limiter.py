"""Rate limiting should be implemented with a shared store (e.g. Redis) before deployment."""
class RateLimitPolicy:
    def __init__(self, requests: int = 60, window_seconds: int = 60):
        self.requests = requests
        self.window_seconds = window_seconds
