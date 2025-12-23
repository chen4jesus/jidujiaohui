import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from .config import config
from .extensions import db, migrate

def create_app(config_name='default'):
    # Get the base directory (project root)
    basedir = os.path.abspath(os.path.dirname(__file__))
    root_dir = os.path.dirname(basedir)

    # Create Flask app with explicit template and static folders
    app = Flask(__name__,
                template_folder=os.path.join(root_dir, 'templates'),
                static_folder=os.path.join(root_dir, 'static'))

    # Load configuration
    app.config.from_object(config.get(config_name, config['default']))

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes import main_bp, health_bp, church_bp

    # Register main blueprint (login, dashboard, etc.)
    app.register_blueprint(main_bp)

    # Register health check blueprint
    app.register_blueprint(health_bp, url_prefix='/api')

    # Register church website blueprint
    app.register_blueprint(church_bp)

    # Register error handlers
    from . import errors
    errors.register_error_handlers(app)

    # Configure logging
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('App startup')

    return app
