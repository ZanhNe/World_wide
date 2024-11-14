from app.BLL.IServices.ILocationService import ILocationService
from app.DAL.IRepositories.ILocationRepository import ILocationRepository
from typing import List
from app.presentation.models.models import Location

class LocationService(ILocationService):
    def __init__(self, location_repository: ILocationRepository) -> None:
        self.location_repository = location_repository

    def get_all_locations(self) -> List[Location]:
        return self.location_repository.get_all_locations()
    
    def get_location_by_address(self, address: str) -> Location:
        location = self.location_repository.get_location_by_address(address=address)
        if (not location):
            return None
        return location
    
    def get_location_by_name(self, name: str) -> Location:
        return self.location_repository.get_location_by_name(name=name)
    
    def get_location_by_coord(self, lat: float, lng: float) -> Location:
        return self.location_repository.get_location_by_coord(lat=lat, lng=lng)

    def add_location(self, location: Location) -> Location:
        location = self.location_repository.add_location(location=location)
        if (not location):
            return None
        return location

    def update_location(self, location: Location) -> Location:
        pass

    def delete_location(self, location: Location) -> Location:
        return self.location_repository.delete_location(location=location)