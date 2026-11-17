class DomainError(Exception):
    """Base exception for expected domain failures."""

class ResourceNotFound(DomainError):
    pass

class InvalidStateTransition(DomainError):
    pass
