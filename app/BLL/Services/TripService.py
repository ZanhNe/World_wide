from app.BLL.IServices.ITripService import ITripService
from app.DAL.IRepositories.ITripRepository import ITripRepository
from typing import List
from app.presentation.models.models import Trip, Location, User
from datetime import datetime

class TripService(ITripService):
    def __init__(self, trip_repository: ITripRepository) -> None:
        self.trip_repository = trip_repository

    def get_all_trips(self) -> List[Trip]:
        return self.trip_repository.get_all_trips()
    
    def get_trip(self, trip_id: int) -> Trip:
        return self.trip_repository.get_trip(trip_id=trip_id)
    
    def delete_trip(self, trip: Trip) -> bool:
        flag = self.trip_repository.delete_trip(trip=trip)
        return flag

    def add_trip(self, user: User, location: Location, trip: Trip) -> Trip:
        trip.location = location
        trip.user = user
        return self.trip_repository.add_trip(trip=trip)