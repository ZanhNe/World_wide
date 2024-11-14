from app.DAL.IRepositories.ILocationRepository import ILocationRepository
from typing import List
from app.presentation.models.models import Location
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class LocationRepository(ILocationRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all_locations(self) -> List[Location]:
        return self.session.query(Location).all()
    
    def get_location_by_address(self, address: str) -> Location:
        results = self.session.query(Location).filter(Location.address.like(f'%{address}%')).all()
        if (not results): 
            return None
        return results[0]
    
    def get_location_by_name(self, name: str) -> Location:
        return self.session.query(Location).filter(Location.location_name == name).all()
    
    def get_location_by_coord(self, lat: float, lng: float) -> Location:
        return self.session.query(Location).filter(Location.latitude == lat and Location.longitude == lng).first()
    
    
    def add_location(self, location: Location) -> Location:
        try: 
            self.session.add(location)
            self.session.commit()
            return location
        except SQLAlchemyError as e:
            self.session.rollback()
            print(e)
            return None
        
    def update_location(self, location: Location) -> Location:
        pass

    def delete_location(self, location: Location) -> bool:
        try:
            self.session.delete(location)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(e)
            return False