from .DIContainer import ServiceDIContainer, RepositoryDIContainer
from app.extentions.extentions import db
from app.library_ma.marshmallow_ma import UserSchema, TripSchema, LocationSchema, CountrySchema

from app.DAL.IRepositories.ILocationRepository import ILocationRepository
from app.DAL.IRepositories.ICountryRepository import ICountryRepository
from app.DAL.IRepositories.ITripRepository import ITripRepository
from app.DAL.IRepositories.IUserRepository import IUserRepository
from app.DAL.IRepositories.ICountryLocationRepository import ICountryLocationRepository

from app.DAL.Repositories.LocationRepository import LocationRepository
from app.DAL.Repositories.CountryRepository import CountryRepository
from app.DAL.Repositories.TripRepository import TripRepository
from app.DAL.Repositories.UserRepository import UserRepository
from app.DAL.Repositories.CountryLocationRepository import CountryLocationRepository

from app.BLL.IServices.ILocationService import ILocationService
from app.BLL.IServices.ICountryService import ICountryService
from app.BLL.IServices.ITripService import ITripService
from app.BLL.IServices.IUserService import IUserService
from app.BLL.IServices.ICountryLocationService import ICountryLocationService

from app.BLL.Services.LocationService import LocationService
from app.BLL.Services.CountryService import CountryService
from app.BLL.Services.TripService import TripService
from app.BLL.Services.UserService import UserService
from app.BLL.Services.CountryLocationService import CountryLocationService


#init DI
repo_container = RepositoryDIContainer()
service_container = ServiceDIContainer()

#register DI
repo_container.register_container(interface=ILocationRepository, implementation=LocationRepository)
repo_container.register_container(interface=ICountryRepository, implementation=CountryRepository)
repo_container.register_container(interface=ITripRepository, implementation=TripRepository)
repo_container.register_container(interface=IUserRepository, implementation=UserRepository)
repo_container.register_container(interface=ICountryLocationRepository, implementation=CountryLocationRepository)

service_container.register_container(interface=ILocationService, implementation=LocationService)
service_container.register_container(interface=ICountryService, implementation=CountryService)
service_container.register_container(interface=ITripService, implementation=TripService)
service_container.register_container(interface=IUserService, implementation=UserService)
service_container.register_container(interface=ICountryLocationService, implementation=CountryLocationService)

location_repository = repo_container.resolve(interface=ILocationRepository)(session=db.session)
country_repository = repo_container.resolve(interface=ICountryRepository)(session=db.session)
trip_repository = repo_container.resolve(interface=ITripRepository)(session=db.session)
user_repository = repo_container.resolve(interface=IUserRepository)(session=db.session)
country_location_repository = repo_container.resolve(interface=ICountryLocationRepository)(session=db.session)


location_service = service_container.resolve(interface=ILocationService)(location_repository=location_repository)
country_service = service_container.resolve(interface=ICountryService)(country_repository=country_repository)
trip_service = service_container.resolve(interface=ITripService)(trip_repository=trip_repository)
user_service = service_container.resolve(interface=IUserService)(user_repository=user_repository)
country_location_service = service_container.resolve(interface=ICountryLocationService)(country_location_repository=country_location_repository, country_repository=country_repository, location_repository=location_repository)

location_schema = LocationSchema()
country_schema = CountrySchema()
trip_schema = TripSchema()
user_schema = UserSchema()