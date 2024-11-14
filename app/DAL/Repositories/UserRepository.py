from app.DAL.IRepositories.IUserRepository import IUserRepository
from typing import List
from app.presentation.models.models import User, Trip
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class UserRepository(IUserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all_users(self) -> List[User]:
        return self.session.query(User).all()
    
    def get_user(self, user_id: int) -> User:
        return self.session.query(User).get(ident=user_id)
    
    def get_user_by_account_name(self, account_name: str) -> User:
        return self.session.query(User).filter(User.account_name == account_name).first()


    def add_user(self, user: User) -> User:
        try:
            self.session.add(user)
            self.session.commit()
            return user
        except SQLAlchemyError as e:
            self.session.rollback()
            print(e)
            return None
    
    