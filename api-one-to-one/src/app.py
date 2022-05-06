from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from models import db, User, Profile

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
Migrate(app, db)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register_user():
    # capturar los valores del request 
    # data = request.get_json()
    username = request.json.get('username')
    password = request.json.get('password')

    bio = request.json.get('bio', "")
    twitter = request.json.get('twitter', "")
    instagram = request.json.get('instagram', "")
    linkedin = request.json.get('linkedin', "")


    # creamos la instancia del usuario
    user = User()
    user.username = username
    user.password = password

    # creamos la instancia del perfil
    profile = Profile()
    profile.bio = bio
    profile.twitter = twitter
    profile.instagram = instagram
    profile.linkedin = linkedin

    # asignamos el perfil al usuario 
    user.profile = profile
    # guardamos el usuario en la base de datos
    user.save()

    return jsonify(user.serialize_with_profile()), 201

if __name__ == '__main__':
    app.run()