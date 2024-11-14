from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os

load_dotenv()

geocoder = OpenCageGeocode(key=os.getenv('OPENCAGE_KEY'))
