from flask import Blueprint, jsonify, request
from app.presentation.models.models import User, Location, Country, Trip
from app.container.InstanceContainer import user_service, trip_service, trip_schema, country_location_service
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

trip_bp = Blueprint('trip', __name__)


@trip_bp.route('/api/v1/user/trips', methods=['GET'])
@jwt_required()
def get_all_trips():
    user_jwt = get_jwt_identity()
    current_user = user_service.get_user(user_id=user_jwt['user_id'])

    trips_json = trip_schema.dump(current_user.locations, many=True)

    return jsonify({'status': 200, 'trips': trips_json})

@trip_bp.route('/api/v1/user/trip/<int:trip_id>', methods=['GET'])
def get_user_trip(trip_id):
    trip = trip_service.get_trip(trip_id=trip_id)
    if (not trip):
        return jsonify({'error': 'Không tồn tại chuyến đi', 'status': 404})
    trip_json = trip_schema.dump(obj=trip, many=True)
    return jsonify(trip=trip_json, status=200, success='Thành công')

@trip_bp.route('/api/v1/user/trip/<int:trip_id>', methods=['DELETE'])
def delete_user_trip(trip_id):
    trip = trip_service.get_trip(trip_id=trip_id)
    if (not trip):
        return jsonify(status=404, error='Trip is not found')
    flag = trip_service.delete_trip(trip=trip)
    if (not flag):
        return jsonify(status=400, error='Failed to delete')
    return jsonify(status=200, success='Delete successful')




@trip_bp.route('/api/v1/user/trips', methods=['POST'])
@jwt_required()
def add_new_trip():
    location = None
    json_data = request.get_json()
    cityName = json_data.get('cityName')
    country_name = json_data.get('country')
    emoji = json_data.get('emoji')
    coordinate = json_data.get('coordinate')
    notes = json_data.get('notes')
    date = json_data.get('date')
    if (not cityName or not country_name or not emoji or not coordinate or not date):
        return jsonify({'error': 'Vui lòng nhập đủ thông tin', 'status': 400})
    if (not coordinate['lat'] or not coordinate['lng']):
        return jsonify({'error': 'Vui lòng nhập đủ tọa độ latitude, longitude', 'status': 400})
    location_raw = Location(location_name=cityName, latitude=coordinate['lat'], longitude=coordinate['lng'])
    country_raw = Country(country_name=country_name, emoji=emoji)

    location = country_location_service.add_country_location(country_raw=country_raw, location_raw=location_raw)
    if (not location):
        return jsonify({'error': 'Lỗi khi thêm vị trí mới', 'status': 400})
    user_jwt = get_jwt_identity()
    current_user = user_service.get_user(user_id=user_jwt['user_id'])
    
    tripped_date = datetime.fromisoformat(date.replace('Z', '+00:00'))
    new_trip_for_current_user = Trip(note=notes, tripped_date=tripped_date)

    trip_after_add = trip_service.add_trip(trip=new_trip_for_current_user, user=current_user, location=location)
    if (not trip_after_add):
        return jsonify({'error': 'Lỗi khi thêm chuyến đi cho user hiện tại', 'status': 400})
    trip_json = trip_schema.dump(trip_after_add)
    print(trip_json)
    return jsonify({'success': 'Thêm chuyến thành công', 'status': 200, 'trip': trip_json})

    
    

    
    
