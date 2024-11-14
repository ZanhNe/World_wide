from abc import ABC, abstractmethod
from typing import List
from app.presentation.models.models import Country

class ICountryRepository(ABC):
    @abstractmethod
    def get_all_countries(self) -> List[Country]:
        pass

    @abstractmethod
    def get_country(self, country_id: int) -> Country:
        pass

    @abstractmethod
    def get_country_by_name(self, name: str) -> Country:
        pass

    @abstractmethod
    def add_country(self, country: Country) -> Country:
        pass

    @abstractmethod
    def update_country(self, country: Country) -> Country:
        pass

    @abstractmethod
    def delete_country(self, country: Country) -> Country:
        pass