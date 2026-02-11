from flask import Flask
from config import Config
from extensions import db, login_manager
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.key import key_bp
from routes.laptop import laptop_bp
from flask_migrate import Migrate
from routes.fingerprint import fingerprint_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)


    # register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(key_bp)
    app.register_blueprint(laptop_bp)
    app.register_blueprint(fingerprint_bp)


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=True)

