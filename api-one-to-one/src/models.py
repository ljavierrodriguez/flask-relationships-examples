from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    profile = db.relationship('Profile', backref="user", uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
        }

    def serialize_with_profile(self):
        return {
            "id": self.id,
            "username": self.username,
            "profile": self.profile.serialize()
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String, default="")
    twitter = db.Column(db.String, default="")
    instagram = db.Column(db.String, default="")
    linkedin = db.Column(db.String, default="")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "bio": self.bio,
            "twitter": self.twitter,
            "instagram": self.instagram,
            "linkedin": self.linkedin,
            "user": self.user.username
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()