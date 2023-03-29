from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Length, NumberRange


class KlientiForm(FlaskForm):
    first_name = StringField("Jméno", validators=[DataRequired(), Length(min=2, max=50)],render_kw=dict(class_ = "form-control", placeholder="Zadejte celé jméno klienta (min. 2 znaky)"))
    last_name = StringField("Příjmení", validators=[DataRequired(), Length(min=2, max=50)], render_kw=dict(class_ = "form-control", placeholder="Zadejte příjmení klienta (min. 2 znaky)"))
    email = StringField("Email", validators=[DataRequired(), Length(min=6, max=50)], render_kw=dict(class_ = "form-control", placeholder="Zadejte platný email klienta (min. 6 znaků)"))
    phone_number = StringField("Telefonní číslo", validators=[DataRequired(), Length(min=9, max=15)], render_kw=dict(class_ = "form-control", placeholder="Formát 00420-123456789"))
    birth_year = IntegerField("Rok narození", validators=[DataRequired(), NumberRange(min=1922, max=2022)], render_kw=dict(class_ = "form-control", placeholder="Zadejte rok narození klienta (max. 2022)"))
    street = StringField("Ulice", validators=[DataRequired(), Length(min=2, max=50)], render_kw=dict(class_ = "form-control", placeholder="Zadejte ulici (min. 2 znaky)"))
    city = StringField("Město", validators=[DataRequired(), Length(min=2, max=50)], render_kw=dict(class_ = "form-control", placeholder="Zadejte město (min. 2 znaky)"))
    postal_code = StringField("PSČ", validators=[DataRequired(), Length(min=5, max=6)], render_kw=dict(class_ = "form-control", placeholder="Zadejte PSČ (5 až 6 znaků)"))
    submit = SubmitField("Potvrdit", render_kw=dict(class_="btn btn-primary"))


class PojisteniForm(FlaskForm):
    druh = StringField("Druh", validators=[DataRequired(), Length(min=2, max=50)], render_kw=dict(class_="form-control", placeholder="Zadejte druh pojistení (min. 2 znaky)"))
    pojistovna = StringField("Pojišťovna", validators=[DataRequired(), Length(min=2, max=50)], render_kw=dict(class_="form-control", placeholder="Zadejte název pojišťovny (min. 2 znaky)"))
    pojistna_castka = IntegerField("Pojištná částka", validators=[DataRequired(), NumberRange(min=1000, max=1000000)], render_kw=dict(class_="form-control", placeholder="Zadejte pojištnou částku (1000 až 1000000)"))
    submit = SubmitField("Potvrdit", render_kw=dict(class_="btn btn-primary"))