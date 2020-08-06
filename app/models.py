from app import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    invoice_id = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.email)
