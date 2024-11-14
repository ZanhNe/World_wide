from app.DAL.IRepositories.ICountryLocationRepository import ICountryLocationRepository
from app.presentation.models.models import Country, Location
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class CountryLocationRepository(ICountryLocationRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    

    def add_country_location(self, country: Country, location: Location) -> Location:
        try:
            country.locations.append(location)
            self.session.commit()
            return location
        except SQLAlchemyError as e:
            print(e)
            self.session.rollback()
            return None
        
    def add_new_location_to_new_country(self, country: Country, location: Location) -> Location:
            self.session.add(country)
            self.session.add(location)
            return self.add_country_location(country=country, location=location)
