from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from models import db
from routes_user import bpUser
from routes_contact import bpContact

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
Migrate(app, db)

app.register_blueprint(bpUser, url_prefix='/api')
app.register_blueprint(bpContact, url_prefix='/api')

@app.route('/')
def root():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()