from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LogForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw=dict(placeholder="Přihlašovací jméno"))
    password = PasswordField('Password', validators=[DataRequired()], render_kw=dict(placeholder="Heslo"))
    submit = SubmitField("Přihlásit", render_kw=dict(class_ = "btn btn-primary"))

class RegForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw=dict(class_ = "form-floating", placeholder="Přihlašovací jméno"))
    password = PasswordField('Password', validators=[DataRequired()], render_kw=dict(class_ = "form-floating", placeholder="Heslo"))
    submit = SubmitField("Registrovat", render_kw=dict(class_ = "btn btn-primary"))


