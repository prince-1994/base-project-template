import abc
from .entities import User


class UserRepository(abc.ABC):
    """Interface for  Repo"""
    @abc.abstractmethod
    def create(self, user: User) -> str | None:
        """Create a new title"""
        pass

    @abc.abstractmethod
    def find_one(self, id: int) -> User:
        """Get a title object"""
        pass

    @abc.abstractmethod
    def find_all(self) -> User:
        """Get a title object"""
        pass

    @abc.abstractmethod
    def delete(self, id: int):
        """Delete an existing title"""
        pass
