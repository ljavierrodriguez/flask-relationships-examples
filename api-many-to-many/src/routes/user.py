from flask import Blueprint, request, jsonify
from models import User, Follower, Role

bpUser = Blueprint('bpUser', __name__)

@bpUser.route('/users', methods=['GET'])
def all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200


@bpUser.route('/users/<int:user_id>/follow/<int:id>', methods=['GET'])
def follow_users(user_id, id):
    
    user = User.query.get(user_id)
    
    follow = Follower()
    follow.followed_id = id

    user.follows.append(follow)
    user.update()

    return jsonify({ "msg": "usuario seguido con exito"}), 200

@bpUser.route('/users/<int:user_id>/role/<int:id>/add', methods=['GET'])
def add_role_users(user_id, id):
    
    user = User.query.get(user_id)
    
    role = Role.query.get(id)

    user.roles.append(role)
    user.update()

    return jsonify({ "msg": "Role asignado con exito"}), 200

@bpUser.route('/users/<int:user_id>/role/<int:id>/remove', methods=['GET'])
def remove_role_users(user_id, id):
    
    user = User.query.get(user_id)
    
    role = Role.query.get(id)

    user.roles.remove(role)
    user.update()

    return jsonify({ "msg": "Role asignado con exito"}), 200