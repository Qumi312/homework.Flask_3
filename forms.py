from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegForm(FlaskForm):
    firstname = StringField('username', validators=[DataRequired(), Length(min=6)])
    lastname = StringField('lastname', validators=[DataRequired(), Length(min=6)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('password', validators=[DataRequired(), EqualTo('password')])

class LogForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password')