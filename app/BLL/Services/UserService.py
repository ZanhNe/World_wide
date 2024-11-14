from app.BLL.IServices.IUserService import IUserService
from app.DAL.IRepositories.IUserRepository import IUserRepository
from typing import List
from app.presentation.models.models import User
from app.extentions.extentions import bcrypt

class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all_users()
    
    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user(user_id=user_id)
    
    def get_user_by_account_name(self, account_name: str) -> User:
        return self.user_repository.get_user_by_account_name(account_name=account_name)
    
    def add_user(self, user: User) -> User:
        check_user = self.get_user_by_account_name(account_name=user.account_name)
        if (not check_user):
            
            user = self.user_repository.add_user(user=user)
            if (not user):
                return None
            return user
        return None
    