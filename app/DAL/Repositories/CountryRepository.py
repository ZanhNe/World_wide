from app.DAL.IRepositories.ICountryRepository import ICountryRepository
from typing import List
from app.presentation.models.models import Country
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class CountryRepository(ICountryRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all_countries(self) -> List[Country]:
        return self.session.query(Country).all()
    
    def get_country(self, country_id: int) -> Country:
        return self.session.query(Country).get(ident=country_id)
    
    def get_country_by_name(self, name: str) -> Country:
        return self.session.query(Country).filter(Country.country_name == name).first()
    
    def add_country(self, country: Country) -> Country:
        pass

    def update_country(self, country: Country) -> Country:
        pass

    def delete_country(self, country: Country) -> Country:
        pass