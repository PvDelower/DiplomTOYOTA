# services/users/src/api/users/models.py

import datetime
import os


from flask import current_app
from sqlalchemy.sql import func

from src import db


class User(db.Model):

    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Brand = db.Column(db.String(128), nullable=False)
    Model = db.Column(db.String(128), nullable=False)
    Year = db.Column(db.String(255), nullable=False)
    Price = db.Column(db.String(128), nullable=False)
    probeg = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, Brand="", Model="", password=""):
        self.Brand = Brand
        self.Model = Model
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode()
#  ЦЕНА + ПРОБЕГ + ГОД

