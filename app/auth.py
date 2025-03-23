import datetime

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

# Dummy user database
USERS = {
    'free_user': {'password': '1234', 'tier': 'free'},
    'pro_user': {'password': '1234', 'tier': 'pro'},
    'enterprise_user': {'password': '1234', 'tier': 'enterprise'}
}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username, password = data.get('username'), data.get('password')

    if username in USERS and USERS[username]['password'] == password:
        token = create_access_token(
            identity=username,
            additional_claims={'tier': USERS[username]['tier']}, 
            expires_delta=datetime.timedelta(hours=2),
        )
        return jsonify(access_token=token), 200
    return jsonify({'msg': 'Invalid credentials'}), 401
