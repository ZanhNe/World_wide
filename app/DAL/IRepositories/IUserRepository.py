from abc import ABC, abstractmethod
from typing import List
from app.presentation.models.models import User

class IUserRepository(ABC):
    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def get_user_by_account_name(self, account_name: str) -> User:
        pass
    
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def add_user(self, user: User) -> User:
        pass

