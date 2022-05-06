from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    follows = db.relationship('Follower', foreign_keys="[Follower.user_id]", primaryjoin="User.id==Follower.user_id")
    followers = db.relationship('Follower', foreign_keys="[Follower.followed_id]", primaryjoin="User.id==Follower.followed_id")

    roles = db.relationship('Role', secondary="roles_users")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "follows": self.get_follows(),
            "follewers": self.get_followers(),
            "roles": self.get_roles()
        }

    def get_follows(self):
        return list(map(lambda user: user.serialize(), self.follows))

    def get_followers(self):
        return list(map(lambda user: user.serialize(), self.followers))

    def get_roles(self):
        return list(map(lambda role: role.serialize(), self.roles))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Follower(db.Model):
    __tablename__ = 'followers'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    user = db.relationship('User', foreign_keys="[Follower.user_id]", primaryjoin="User.id==Follower.user_id")
    follow = db.relationship('User', foreign_keys="[Follower.followed_id]", primaryjoin="User.id==Follower.followed_id")

    def serialize(self):
        return {
            "user": {
                "username": self.user.username
            },
            "follow": {
                "username": self.follow.username
            },
        }


class RoleUser(db.Model):
    __tablename__ = 'roles_users'
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, primary_key=True)