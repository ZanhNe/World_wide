from abc import ABC, abstractmethod
from typing import List
from app.presentation.models.models import Location, Country

class ICountryLocationRepository(ABC):
    
    @abstractmethod
    def add_country_location(self, country: Country, location: Location) -> Location:
        pass

    @abstractmethod
    def add_new_location_to_new_country(self, country: Country, location: Location) -> Location:
        pass