from abc import ABC, abstractmethod
from typing import List
from app.presentation.models.models import Location

class ILocationService(ABC):
    @abstractmethod
    def get_all_locations(self) -> List[Location]:
        pass

    @abstractmethod
    def get_location_by_address(self, address: str) -> Location:
        pass

    @abstractmethod
    def get_location_by_name(self, name: str) -> List[Location]:
        pass

    @abstractmethod
    def get_location_by_coord(self, lat: float, lng: float) -> Location:
        pass


    @abstractmethod
    def add_location(self, location: Location) -> Location:
        pass

    @abstractmethod
    def update_location(self, location: Location) -> Location:
        pass

    @abstractmethod
    def delete_location(self, location: Location) -> Location:
        pass