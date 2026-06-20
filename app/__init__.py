from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.customers import customers_bp
    from app.routes.employees import employees_bp
    from app.routes.rooms import rooms_bp
    from app.routes.room_types import room_types_bp
    from app.routes.reservations import reservations_bp
    from app.routes.services import services_bp
    from app.routes.reservation_services import reservation_services_bp

    app.register_blueprint(auth_bp,               url_prefix="/api/auth")
    app.register_blueprint(customers_bp,          url_prefix="/api/customers")
    app.register_blueprint(employees_bp,          url_prefix="/api/employees")
    app.register_blueprint(rooms_bp,              url_prefix="/api/rooms")
    app.register_blueprint(room_types_bp,         url_prefix="/api/room-types")
    app.register_blueprint(reservations_bp,       url_prefix="/api/reservations")
    app.register_blueprint(services_bp,           url_prefix="/api/services")
    app.register_blueprint(reservation_services_bp, url_prefix="/api/reservation-services")

    return app