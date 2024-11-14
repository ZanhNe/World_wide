from abc import ABC, abstractmethod
from typing import List
from app.presentation.models.models import Trip, User, Location

class ITripRepository(ABC):
    @abstractmethod
    def get_all_trips(self) -> List[Trip]:
        pass

    @abstractmethod
    def get_trip(self, trip_id: int) -> Trip:
        pass

    @abstractmethod
    def delete_trip(self, trip: Trip) -> bool:
        pass
    
    @abstractmethod
    def add_trip(self, trip: Trip) -> Trip:
        pass