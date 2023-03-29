from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Uzivatele.query.get(int(user_id))


class Uzivatele(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    klienti = db.relationship('Klienti', backref='uzivatele')
    pojisteni = db.relationship('Pojisteni', backref='uzivatele')

class Klienti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uzivatel_id = db.Column(db.Integer, db.ForeignKey('uzivatele.id', ondelete='CASCADE'), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)


class Pojisteni(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.String(10), nullable=False, default="bez_klienta")
    uzivatel_id = db.Column(db.Integer, db.ForeignKey('uzivatele.id', ondelete='CASCADE'), nullable=False)
    druh = db.Column(db.String(50), nullable=False)
    pojistovna = db.Column(db.String(50), nullable=False)
    pojistna_castka = db.Column(db.Integer, nullable=False)

class KlientiPojisteni(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    klient_id = db.Column(db.Integer, db.ForeignKey('klienti.id', ondelete='CASCADE'))
    pojisteni_id = db.Column(db.Integer, db.ForeignKey('pojisteni.id', ondelete='CASCADE'))

    klient = db.relationship('Klienti', backref='klienti_pojisteni')
    pojisteni = db.relationship('Pojisteni', backref='klienti_pojisteni')
