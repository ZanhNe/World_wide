from app.BLL.IServices.ICountryLocationService import ICountryLocationService
from app.presentation.models.models import Country, Location
from app.DAL.IRepositories.ICountryLocationRepository import ICountryLocationRepository
from app.DAL.IRepositories.ICountryRepository import ICountryRepository
from app.DAL.IRepositories.ILocationRepository import ILocationRepository


class CountryLocationService(ICountryLocationService):
    def __init__(self, country_location_repository: ICountryLocationRepository, country_repository: ICountryRepository, location_repository: ILocationRepository) -> None:
        self.country_location_repository = country_location_repository
        self.country_repository = country_repository
        self.location_repository = location_repository
    
    def add_country_location(self, country_raw: Country, location_raw: Location) -> Location:
        location = country = None
        check_location = self.location_repository.get_location_by_coord(lat=location_raw.latitude, lng=location_raw.longitude)
        check_country = self.country_repository.get_country_by_name(name=country_raw.country_name)
        if (not check_location):
            location = location_raw
            if (not check_country):
                country = country_raw
                return self.country_location_repository.add_new_location_to_new_country(country=country, location=location)
            else:
                return self.country_location_repository.add_country_location(country=check_country, location=location)
        else:
            location = check_location
        return location