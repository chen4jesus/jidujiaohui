# Church Website - Project Structure Documentation

## Overview

This is a Flask-based church website application that has been refactored to follow standard Flask project structure patterns. The application uses the Flask application factory pattern with blueprints for modular organization.

## Project Structure

```
.
├── app/                          # Application package
│   ├── __init__.py               # Application factory
│   ├── config.py                 # Configuration classes
│   ├── extensions.py             # Flask extensions (db, migrate)
│   ├── errors.py                 # Error handlers
│   ├── models/                   # Database models
│   │   ├── __init__.py
│   │   └── user.py               # User model example
│   ├── routes/                   # Blueprint routes
│   │   ├── __init__.py
│   │   ├── church.py             # Church website blueprint (main site)
│   │   ├── main.py               # Admin routes (future features)
│   │   └── health.py             # Health check endpoint
│   ├── services/                 # Business logic
│   │   ├── __init__.py
│   │   └── user_service.py       # User service example
│   ├── static/                   # NOTE: Not used - using root static/
│   └── templates/                # NOTE: Not used - using root templates/
├── instance/                     # Instance folder (database, etc.)
│   └── app.db                    # SQLite database (created on first run)
├── migrations/                   # Flask-Migrate migration files
├── static/                       # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css             # Main stylesheet
│   └── js/
│       └── script.js             # Main JavaScript file
├── templates/                    # Jinja2 templates
│   ├── base.html                 # Base template
│   ├── index.html                # Home page
│   ├── about.html                # About page
│   ├── ministries.html           # Ministries page
│   ├── sermons.html              # Sermons page
│   └── contact.html              # Contact page
├── tests/                        # Test suite
│   ├── conftest.py
│   └── test_health.py
├── uploads/                      # User uploaded files
├── .env                          # Environment configuration
├── .gitignore
├── app.py.bak                    # Backup of original monolithic app
├── wsgi.py                       # WSGI entry point
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker configuration
└── docker-compose.yml            # Docker Compose configuration

```

## Key Features

### 1. Application Factory Pattern

The application uses the factory pattern via `create_app()` function in `app/__init__.py`:

```python
from app import create_app
app = create_app()
```

This allows for:
- Easy testing with different configurations
- Multiple application instances
- Better configuration management

### 2. Blueprint Organization

The application is organized into three blueprints:

#### Church Blueprint (`church_bp`)
- **Purpose**: Main church website pages and API
- **Routes**:
  - `/` - Home page
  - `/about` - About page
  - `/ministries` - Ministries page
  - `/sermons` - Sermons page
  - `/contact` - Contact page
  - `/api/sermons` - Sermons API (GET)
  - `/api/ministries` - Ministries API (GET)
  - `/api/events` - Events API (GET)
  - `/api/contact` - Contact form submission (POST)
  - `/api/newsletter` - Newsletter subscription (POST)

#### Main Blueprint (`main_bp`)
- **Purpose**: Future administrative features
- **Routes**:
  - `/admin/login` - Admin login (coming soon)
  - `/admin/dashboard` - Admin dashboard (coming soon)

#### Health Blueprint (`health_bp`)
- **Purpose**: API health checks
- **Routes**:
  - `/api/health` - Health check endpoint

### 3. Configuration Management

Configuration is handled through classes in `app/config.py`:

- `Config` - Base configuration
- `DevelopmentConfig` - Development environment
- `ProductionConfig` - Production environment
- `TestingConfig` - Testing environment

Configuration is loaded from:
1. `.env` file in the project root
2. Environment variables
3. Default values

### 4. Database Integration

The application uses Flask-SQLAlchemy with SQLite:

- **Database location**: `instance/app.db`
- **ORM**: SQLAlchemy
- **Migrations**: Flask-Migrate
- **Models**: Located in `app/models/`

### 5. Static Files & Templates

Static files and templates are stored in the project root (not inside `app/` package):

- **Static files**: `static/` directory (CSS, JS, images)
- **Templates**: `templates/` directory (HTML templates)

This is configured in `app/__init__.py`:
```python
app = Flask(__name__,
            template_folder=os.path.join(root_dir, 'templates'),
            static_folder=os.path.join(root_dir, 'static'))
```

## Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Edit `.env` file:
```
FLASK_APP=wsgi.py
FLASK_DEBUG=true
FLASK_CONFIG=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///instance/app.db
```

### 3. Run the Application

```bash
python wsgi.py
```

The application will start on `http://localhost:3000` (or the PORT specified in environment).

## Running with Docker

```bash
docker-compose up
```

## Testing

Run tests using pytest:

```bash
pytest tests/
```

## API Endpoints

### Public Pages
- `GET /` - Home page
- `GET /about` - About page
- `GET /ministries` - Ministries page
- `GET /sermons` - Sermons page
- `GET /contact` - Contact page

### API Endpoints
- `GET /api/health` - Health check
- `GET /api/sermons?page=1&per_page=10` - Get sermons with pagination
- `GET /api/ministries` - Get all ministries
- `GET /api/events` - Get all events
- `POST /api/contact` - Submit contact form
- `POST /api/newsletter` - Subscribe to newsletter

## Refactoring Changes

The following changes were made to refactor this project:

1. **Created `app/routes/church.py`**: Moved all church website routes from root `app.py`
2. **Updated `app/__init__.py`**: Configured proper template/static folders and registered church blueprint
3. **Updated `app/routes/__init__.py`**: Added church blueprint export
4. **Updated `app/routes/main.py`**: Moved admin routes to `/admin/*` to avoid conflicts
5. **Updated `app/config.py`**: Fixed DATABASE_URL handling and added validation
6. **Updated `app/errors.py`**: Added fallback error pages
7. **Updated `requirements.txt`**: Added Flask-SQLAlchemy and Flask-Migrate
8. **Renamed `app.py` → `app.py.bak`**: Backed up original monolithic file

## Notes

- The original `app.py` has been backed up as `app.py.bak`
- All routes have been tested and verified working
- The application follows Flask best practices and conventions
- Templates use Jinja2 templating with `base.html` as the parent template
