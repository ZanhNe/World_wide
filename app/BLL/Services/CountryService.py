from app.BLL.IServices.ICountryService import ICountryService
from app.DAL.IRepositories.ICountryRepository import ICountryRepository
from typing import List
from app.presentation.models.models import Country

class CountryService(ICountryService):
    def __init__(self, country_repository: ICountryRepository) -> None:
        self.country_repository = country_repository

    def get_all_countries(self) -> List[Country]:
        return self.country_repository.get_all_countries()
    
    def get_country_by_name(self, name: str) -> Country:
        return self.country_repository.get_country_by_name(name=name)
    
    def get_country(self, country_id: int) -> Country:
        return self.country_repository.get_country(country_id=country_id)
    
    def add_country(self, country: Country) -> Country:
        pass

    def update_country(self, country: Country) -> Country:
        pass

    def delete_country(self, country: Country) -> Country:
        pass