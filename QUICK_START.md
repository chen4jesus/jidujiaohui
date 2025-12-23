# Quick Start Guide - Church Website

## Running the Application

### Option 1: Direct Python (Recommended for Development)

```bash
python wsgi.py
```

The application will start on `http://localhost:3000` by default.

### Option 2: Using Flask CLI

```bash
# Set the Flask app environment variable
set FLASK_APP=wsgi.py
set FLASK_ENV=development

# Run the application
flask run
```

### Option 3: Using Docker

```bash
docker-compose up
```

## Available Pages

Once the application is running, you can access:

- **Home Page**: http://localhost:3000/
- **About**: http://localhost:3000/about
- **Ministries**: http://localhost:3000/ministries
- **Sermons**: http://localhost:3000/sermons
- **Contact**: http://localhost:3000/contact

## API Endpoints

- **Health Check**: http://localhost:3000/api/health
- **Sermons API**: http://localhost:3000/api/sermons
- **Ministries API**: http://localhost:3000/api/ministries
- **Events API**: http://localhost:3000/api/events

## Environment Configuration

Edit `.env` file to configure:

```env
FLASK_APP=wsgi.py
FLASK_DEBUG=true
FLASK_CONFIG=development
SECRET_KEY=dev-secret-key-change-in-production
DATABASE_URL=sqlite:///instance/app.db
```

## Project Structure

```
church-website/
├── app/                    # Application package
│   ├── routes/            # Blueprint routes
│   │   ├── church.py      # Church website routes
│   │   ├── main.py        # Admin routes
│   │   └── health.py      # Health check
│   ├── config.py          # Configuration
│   └── extensions.py      # Flask extensions
├── static/                # CSS, JS, images
├── templates/             # HTML templates
├── instance/              # Database (auto-created)
└── wsgi.py               # Application entry point
```

## Troubleshooting

### Port Already in Use

If port 3000 is already in use, set a different port:

```bash
# Windows
set PORT=5000
python wsgi.py

# Linux/Mac
PORT=5000 python wsgi.py
```

### Database Issues

The SQLite database will be automatically created in the `instance/` folder on first run. If you encounter database issues:

1. Delete `instance/app.db`
2. Restart the application
3. The database will be recreated

### Import Errors

If you encounter import errors, make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

## Development Tips

1. **Debug Mode**: Enabled by default in development
2. **Auto-reload**: The application will reload when you save changes
3. **Logging**: Check `logs/app.log` for application logs
4. **Testing**: Run `pytest tests/` to execute tests

## Support

For detailed documentation, see `PROJECT_STRUCTURE.md`.
