from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    from app import models

    # Register blueprints
    from app.routes.questions import bp as questions_bp
    from app.routes.recommendations import bp as recommendations_bp
    from app.routes.suggestions import bp as suggestions_bp

    app.register_blueprint(questions_bp)
    app.register_blueprint(recommendations_bp)
    app.register_blueprint(suggestions_bp)

    return app