from flask import Flask
from .extentions.extentions import db, ma, bcrypt, migrate, jwt, cors
from app.presentation.controllers.geocoding_routes import geocoding_bp
from app.presentation.controllers.user_routes import user_bp
from app.presentation.controllers.auth_routes import auth_bp
from app.presentation.controllers.trip_routes import trip_bp
from app.config import Config


def create_db(app: Flask):
    with app.app_context():
        db.create_all()
        print('successful')


def create_app():
    app = Flask(__name__)
    app.config.from_object(obj=Config)
    db.init_app(app=app)
    ma.init_app(app=app)
    jwt.init_app(app=app)
    bcrypt.init_app(app=app)
    migrate.init_app(app=app, db=db)
    cors.init_app(app=app, resources={r'/api/*': {'origins': '*'}})
    app.register_blueprint(blueprint=geocoding_bp)
    app.register_blueprint(blueprint=user_bp)
    app.register_blueprint(blueprint=trip_bp)
    app.register_blueprint(blueprint=auth_bp)
    return app