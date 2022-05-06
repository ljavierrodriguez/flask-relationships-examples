from flask import Blueprint, request, jsonify
from models import User
from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

bpAuth = Blueprint('bpAuth', __name__)


@bpAuth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if not user: return jsonify({ "status": "fail", "message": "username/password incorrect!"}), 401
    if not check_password_hash(user.password, password): return jsonify({ "status": "fail", "message": "username/password incorrect!"}), 401

    expires = datetime.timedelta(minutes=3)
    acccess_token = create_access_token(identity=user.id, expires_delta=expires)

    data = {
        "status": "success",
        "message": "Login successfully!",
        "access_token": acccess_token,
        "user": user.serialize()
    }

    return jsonify(data), 200
    


@bpAuth.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User()
    user.username = username
    user.password = generate_password_hash(password)
    user.save()

    return jsonify({ "status": "success", "message": "Register successfully. Please login!"}), 200