from flask import Blueprint, request, jsonify
from app.library_API import geocoder

geocoding_bp = Blueprint('geocoding',__name__)

@geocoding_bp.route('/api/v1/geocoding', methods=['POST'])
def get_geocode():
    json_data = request.get_json()
    print(json_data)
    lat = json_data.get('lat')
    lng = json_data.get('lng')

    results = geocoder.reverse_geocode(lat=lat, lng=lng)
    return results
