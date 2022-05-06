from flask import Blueprint, request, jsonify
from models import User

bpUser = Blueprint('bpUser', __name__)

@bpUser.route('/users', methods=['GET'])
def list_users():
    users = User.query.all() # [<User 1>]
    users = list(map(lambda user: user.serialize(), users)) # [{ "id": 1, "username": "lrodriguez@4geeks.co"}]
    return jsonify(users), 200

@bpUser.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User()
    user.username = username
    user.password = password
    user.save()

    return jsonify(user.serialize()), 201

@bpUser.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.get(id) # buscamos al usuario por el id
    user.username = username
    user.password = password
    user.update()

    return jsonify(user.serialize()), 200

@bpUser.route('/users/contacts', methods=['GET'])
def list_users_with_contacts():
    users = User.query.all() # [<User 1>]
    users = list(map(lambda user: user.serialize_with_contacts(), users)) # [{ "id": 1, "username": "lrodriguez@4geeks.co"}]
    return jsonify(users), 200
