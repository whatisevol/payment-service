import datetime
from app import db


class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.Integer)
    amount = db.Column(db.Float)
    datetime = db.Column(db.DateTime, default=datetime.datetime.now())
    description = db.Column(db.Text)

    def __repr__(self):
        return f"currency: ({self.currency}, " \
               f"amount: {self.amount}, " \
               f"datetime: {self.datetime})"
