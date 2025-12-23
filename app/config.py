import os
from dotenv import load_dotenv

# Load .env file from the root directory
basedir = os.path.abspath(os.path.dirname(__file__))
root_dir = os.path.dirname(basedir)
load_dotenv(os.path.join(root_dir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

    # Instance folder for the database - use absolute path for SQLite
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(root_dir, 'instance')
    db_path = os.path.join(instance_path, 'app.db')

    # Ensure the instance directory exists
    os.makedirs(instance_path, exist_ok=True)

    # Use the DATABASE_URL from env or construct a proper SQLite URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
        f'sqlite:///{db_path}')

    # If DATABASE_URL is set but not a proper SQLAlchemy URI, use default
    if SQLALCHEMY_DATABASE_URI and not SQLALCHEMY_DATABASE_URI.startswith(('sqlite://', 'postgresql://', 'mysql://')):
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(root_dir, 'uploads')

    # Security headers
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # In production, ensure SECRET_KEY is set via environment variable
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
