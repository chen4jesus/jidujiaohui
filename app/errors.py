from flask import render_template

def register_error_handlers(app):
    @app.errorhandler(403)
    def forbidden(e):
        try:
            return render_template('pages/403.html'), 403
        except:
            return '<h1>403 Forbidden</h1><p>You do not have permission to access this resource.</p>', 403

    @app.errorhandler(404)
    def page_not_found(e):
        try:
            return render_template('pages/404.html'), 404
        except:
            return '<h1>404 Not Found</h1><p>The page you are looking for does not exist.</p>', 404

    @app.errorhandler(500)
    def internal_server_error(e):
        try:
            return render_template('pages/500.html'), 500
        except:
            return '<h1>500 Internal Server Error</h1><p>An unexpected error occurred. Please try again later.</p>', 500
