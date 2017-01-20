from flask_wtf import FlaskForm as BaseForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(BaseForm):
    """Login form to access writing and settings pages"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
