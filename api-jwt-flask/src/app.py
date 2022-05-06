from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from routes.user import bpUser
from routes.auth import bpAuth

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = '33b9b3de94a42d19f47df7021954eaa8' #secret-key

db.init_app(app)
Migrate(app, db)

jwt = JWTManager(app)

app.register_blueprint(bpAuth, url_prefix='/api')
app.register_blueprint(bpUser, url_prefix='/api')

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()