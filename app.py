import os
from flask import Flask, render_template
from backend.db.database import init_db
from backend.api.auth import bp as auth_bp
from backend.api.sessions import bp as sessions_bp
from backend.api.users import bp as users_bp

app = Flask(__name__)

# Secret Key Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-default-secret-key')

# Database Initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:HS3492k5$!@localhost/TFAF'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)

# Register Blueprints for API routes
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(sessions_bp, url_prefix='/api/sessions')
app.register_blueprint(users_bp, url_prefix='/api/users')

# Error Handling for Debugging
@app.errorhandler(500)
def internal_error(error):
    return "500 error"

@app.errorhandler(404)
def not_found_error(error):
    return "404 error"

# Optional: Serve Frontend Pages
@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an 'index.html' in your 'templates' folder

# Run in Debug Mode
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # host='0.0.0.0' makes the server publicly available
