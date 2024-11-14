from abc import ABC, abstractmethod
from app.presentation.models.models import Country, Location

class ICountryLocationService(ABC):
    @abstractmethod
    def add_country_location(self, country: Country, location: Location) -> Location:
        pass

    