from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from typing import Dict
import os

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
ma = Marshmallow()
bcrypt = Bcrypt()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()


@jwt.user_identity_loader
def user_identity_lookup(user):
    if (type(user) == dict):
        new_user = user
    else: 
        new_user = {"user_id": user.user_id, "user_name": user.user_name}
    return new_user

