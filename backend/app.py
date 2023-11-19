from flask import Flask
from backend.db.database import init_db
from backend.api.auth import bp as auth_bp
from backend.api.sessions import bp as sessions_bp
from backend.api.users import bp as users_bp
import os

app = Flask(__name__)

# Secret Key Configuration
# For development, you can use a generated key. For production, use a secure key.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-default-secret-key')

# Database Initialization
# Make sure to set the correct database URI
# Database Initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:HS3492k5$!@localhost/TFAF'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)
# Register Blueprints for API routes
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(sessions_bp, url_prefix='/api/sessions')
app.register_blueprint(users_bp, url_prefix='/api/users')

# Optional: Configure additional components like logging, error handlers, etc.

@app.route('/')
def index():
    return "Welcome to the Therapy for a Friend API!"

if __name__ == '__main__':
    app.run(debug=True)
