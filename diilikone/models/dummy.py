from diilikone.extensions import db


class Dummy(db.Model):

    __tablename__ = 'dummy'

    id = db.Column(db.Integer, primary_key=True)

    column = db.Column(db.Unicode)
