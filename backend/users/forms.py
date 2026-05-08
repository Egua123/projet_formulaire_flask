from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flask_login import current_user

from backend.models import User


class UpdateAccountForm(FlaskForm):
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

    picture = FileField(
        "Image de profil",
        validators=[
            FileAllowed(["jpg", "jpeg", "png", "svg"])
        ]
    )

    submit = SubmitField("Mettre à jour")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError(
                    "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre."
                )

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError(
                    "Cet email est déjà utilisé. Veuillez en choisir un autre."
                )