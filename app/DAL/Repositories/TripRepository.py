from app.DAL.IRepositories.ITripRepository import ITripRepository
from typing import List
from app.presentation.models.models import Trip, User, Location
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


class TripRepository(ITripRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all_trips(self) -> List[Trip]:
        return self.session.query(Trip).all()
    
    def get_trip(self, trip_id: int) -> Trip:
        return self.session.query(Trip).get(ident=trip_id)
    
    def delete_trip(self, trip: Trip) -> bool:
        try:
            self.session.delete(instance=trip)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(e)
            return False
    
    def add_trip(self, trip: Trip) -> Trip:
        try:
            self.session.add(trip)
            self.session.commit()
            return trip
        except SQLAlchemyError as e:
            print(e)
            self.session.rollback()
            return None
