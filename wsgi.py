# Flask App
import os
import sys

# Try to capture all errors during startup, including imports
try:
    from app import create_app
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    if __name__ == '__main__':
        # PORT is set by the preview manager to the dynamically assigned preview port
        port = int(os.environ.get('PORT', 3000))
        # Bind specifically to 0.0.0.0 for consistent behavior on Windows
        # Disable reloader to prevent forking issues
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', port)), debug=True, use_reloader=False)

except Exception as e:
    import traceback
    print(f"CRITICAL: Failed to start Flask app: {e}", file=sys.stderr)
    traceback.print_exc()
    sys.exit(1)

