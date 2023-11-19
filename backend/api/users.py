from flask import Blueprint, jsonify
from backend.db.models import User, db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"username": user.username, "email": user.email}), 200
