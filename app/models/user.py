from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(1000), nullable=True)
    prognosticoins = db.Column(db.Integer())
    pick_wins = db.Column(db.Integer())
    pick_losses = db.Column(db.Integer())
    pick_ties = db.Column(db.Integer())
    elim_wins = db.Column(db.Integer())
    elim_losses = db.Column(db.Integer())
    elim_ties = db.Column(db.Integer())
    sp_elim_wins = db.Column(db.Integer())
    sp_elim_losses = db.Column(db.Integer())
    sp_elim_pushes = db.Column(db.Integer())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profile_image': self.profile_image,
            'prognosticoins': self.prognosticoins,
            'pick_wins': self.pick_wins,
            'pick_losses': self.pick_losses,
            'pick_ties': self.pick_ties,
            'elim_wins': self.elim_wins,
            'elim_losses': self.elim_losses,
            'elim_ties': self.elim_ties,
            'sp_elim_wins': self.sp_elim_wins,
            'sp_elim_losses': self.sp_elim_losses,
            'sp_elim_pushes': self.sp_elim_pushes,
            'created_at': self.created_at,
            'updated_at': self.updated_at,

        }
