from flask import Blueprint, request, jsonify
from models import Contact

bpContact = Blueprint('bpContact', __name__)

@bpContact.route('/contacts', methods=['GET'])
def list_contacts():
    contacts = Contact.query.all() # [<User 1>]
    contacts = list(map(lambda contact: contact.serialize(), contacts)) # [{ "id": 1, "username": "lrodriguez@4geeks.co"}]
    return jsonify(contacts), 200

@bpContact.route('/contacts', methods=['POST'])
def create_contact():
    
    name = request.json.get('name')
    email = request.json.get('email', "")
    phone = request.json.get('phone')
    user_id = request.json.get('user_id')


    contact = Contact()
    contact.name = name
    contact.email = email
    contact.phone = phone
    contact.user_id = user_id
    contact.save()

    return jsonify(contact.serialize()), 200

@bpContact.route('/contacts/full', methods=['GET'])
def list_contacts_with_user():
    contacts = Contact.query.all() # [<User 1>]
    contacts = list(map(lambda contact: contact.serialize_with_user(), contacts)) # [{ "id": 1, "username": "lrodriguez@4geeks.co"}]
    return jsonify(contacts), 200