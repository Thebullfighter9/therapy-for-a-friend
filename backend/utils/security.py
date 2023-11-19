from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

def generate_token(user_id, expiration=3600):
    """
    Generate a token for a given user ID with a specified expiration time.
    """
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'user_id': user_id}).decode('utf-8')

def verify_token(token):
    """
    Verify a token and return the user ID if valid.
    """
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return None
    return data['user_id']

def hash_password(password):
    """
    Hash a password for storing.
    """
    return generate_password_hash(password)

def check_password(hashed_password, password):
    """
    Check a hashed password. Returns True if matches, else False.
    """
    return check_password_hash(hashed_password, password)
