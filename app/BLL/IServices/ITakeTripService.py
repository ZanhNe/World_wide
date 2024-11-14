from abc import ABC, abstractmethod
from typing import List
from app.presentation.models.models import  Trip


class ITakeTripService(ABC):
    @abstractmethod
    def add_new_trip(self) -> Trip:
        pass