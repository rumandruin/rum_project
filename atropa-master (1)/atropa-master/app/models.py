from app import db
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_authenticated = True

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def avatar(self, size):
        h = md5(self.email.encode('utf-8')).hexdigest()
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (h, size)
