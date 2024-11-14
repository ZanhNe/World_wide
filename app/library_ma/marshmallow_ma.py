from app.extentions.extentions import ma
from app.presentation.models.models import Location, Country, Trip, User
import simplejson

class LocationSchema(ma.SQLAlchemyAutoSchema):
    country = ma.Nested('CountrySchema', exclude=('locations',))
    users = ma.Nested('TripSchema', many=True, exclude=('location',))
    class Meta:
        render_module = simplejson
        model = Location
        load_instance = True
    
    

class CountrySchema(ma.SQLAlchemyAutoSchema):
    locations = ma.Nested('LocationSchema', many=True, exclude=('country',))
    class Meta:
        render_module = simplejson
        model = Country
        load_instance = True

class TripSchema(ma.SQLAlchemyAutoSchema):
    location = ma.Nested('LocationSchema', exclude=('users',))
    user = ma.Nested('UserSchema', exclude=('locations',))
    class Meta:
        render_module = simplejson
        model = Trip
        load_instance = True

class UserSchema(ma.SQLAlchemyAutoSchema):
    locations = ma.Nested('TripSchema', many=True, exclude=('user',))
    class Meta:
        render_module = simplejson
        model = User
        load_instance = True

