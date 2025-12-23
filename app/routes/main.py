from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

# Note: The main blueprint routes are for future administrative features
# The church website routes are handled by church_bp

@main_bp.route('/admin/login')
def login():
    """Admin login page - future feature"""
    try:
        return render_template('pages/login.html', title='Login')
    except:
        return '<h1>Admin Login</h1><p>This feature is coming soon.</p>', 200

@main_bp.route('/admin/dashboard')
def dashboard():
    """Admin dashboard - future feature"""
    try:
        return render_template('pages/dashboard.html', title='Dashboard')
    except:
        return '<h1>Admin Dashboard</h1><p>This feature is coming soon.</p>', 200
