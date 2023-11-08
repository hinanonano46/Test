from app import db
from sqlalchemy.dialects.mysql import FLOAT,INTEGER


class Car_data(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    metro_id = db.Column(db.String(125), nullable=False)
    car_id = db.Column(db.String(125), nullable=False)
    wheel_id = db.Column(db.String(125), nullable=False)
    QR = db.Column(FLOAT(precision=4, scale=2))
    Sh = db.Column(FLOAT(precision=4, scale=2))
    Sd = db.Column(FLOAT(precision=4, scale=2))
    ddM = db.Column(FLOAT(precision=4, scale=2))
    dAR = db.Column(FLOAT(precision=4, scale=2))
    WD = db.Column(FLOAT(precision=5, scale=2))
    AR = db.Column(FLOAT(precision=6, scale=2))
    date = db.Column(db.Date)



class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    metro_id = db.Column(db.String(125), nullable=False)
    date = db.Column(db.Date)
    QR_avg = db.Column(FLOAT(precision=4, scale=2))
    Sh_avg = db.Column(FLOAT(precision=4, scale=2))
    Sd_avg = db.Column(FLOAT(precision=4, scale=2))
    WD_avg = db.Column(FLOAT(precision=5, scale=2))
    mile = db.Column(INTEGER)


class Car_data_new(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    metro_id = db.Column(db.String(125), nullable=False)
    car_id = db.Column(db.String(125), nullable=False)
    wheel_id = db.Column(db.String(125), nullable=False)
    QR = db.Column(FLOAT(precision=4, scale=2))
    Sh = db.Column(FLOAT(precision=4, scale=2))
    Sd = db.Column(FLOAT(precision=4, scale=2))
    ddM = db.Column(FLOAT(precision=4, scale=2))
    dAR = db.Column(FLOAT(precision=4, scale=2))
    WD = db.Column(FLOAT(precision=5, scale=2))
    AR = db.Column(FLOAT(precision=6, scale=2))
    date = db.Column(db.Date)
