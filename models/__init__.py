from database import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(256))
    text = db.Column(db.String)

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __repr__(self):
        return '<Contact name: {0}, email: {1}>'.format(self.name, self.email)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User name: {0}>'.format(self.username)
