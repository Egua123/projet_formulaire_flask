
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

from backend.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "Nom d'utilisateur",
        validators=[
            DataRequired(),
            Length(min=2, max=20)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Mot de passe",
        validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        "Confirmer le mot de passe",
        validators=[
            DataRequired(),
            EqualTo("password")
        ]
    )

    submit = SubmitField("Créer le compte")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError(
                "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre."
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError(
                "Cet email est déjà utilisé. Veuillez en choisir un autre."
            )


class LoginForm(FlaskForm):
    username_or_email = StringField(
        "Email ou nom d'utilisateur",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Mot de passe",
        validators=[DataRequired()]
    )

    remember = BooleanField("Se souvenir de moi")

    submit = SubmitField("Connexion")