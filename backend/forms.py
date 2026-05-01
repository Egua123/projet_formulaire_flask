from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, NumberRange, Length, EqualTo, ValidationError
from backend.models import User


class EvaluationForm(FlaskForm):
    prenom = StringField(
        "Prénom",
        validators=[
            DataRequired(message="Le prénom est obligatoire."),
            Length(max=50, message="Le prénom ne doit pas dépasser 50 caractères.")
        ]
    )

    nom = StringField(
        "Nom",
        validators=[
            DataRequired(message="Le nom est obligatoire."),
            Length(max=50, message="Le nom ne doit pas dépasser 50 caractères.")
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="L'email est obligatoire."),
            Email(message="Veuillez entrer une adresse email valide."),
            Length(max=120, message="L'email ne doit pas dépasser 120 caractères.")
        ]
    )

    age = IntegerField(
        "Âge",
        validators=[
            DataRequired(message="L'âge est obligatoire."),
            NumberRange(min=0, max=120, message="L'âge doit être entre 0 et 120.")
        ]
    )

    sexe = SelectField(
        "Sexe",
        choices=[
            ("", "Choisir"),
            ("M", "Masculin"),
            ("F", "Féminin"),
            ("Autre", "Autre")
        ],
        validators=[DataRequired(message="Le sexe est obligatoire.")]
    )

    taille = FloatField(
        "Taille (cm)",
        validators=[
            DataRequired(message="La taille est obligatoire."),
            NumberRange(min=0, max=290, message="La taille doit être entre 0 et 290 cm.")
        ]
    )

    poids = FloatField(
        "Poids (kg)",
        validators=[
            DataRequired(message="Le poids est obligatoire."),
            NumberRange(min=0, message="Le poids doit être positif ou nul.")
        ]
    )

    heures_sommeil = FloatField(
        "Heures de sommeil par nuit",
        validators=[
            DataRequired(message="Les heures de sommeil sont obligatoires."),
            NumberRange(min=0, max=24, message="Les heures de sommeil doivent être entre 0 et 24.")
        ]
    )

    repas_par_jour = IntegerField(
        "Repas par jour",
        validators=[
            DataRequired(message="Le nombre de repas est obligatoire."),
            NumberRange(min=0, max=15, message="Le nombre de repas doit être entre 0 et 15.")
        ]
    )

    niveau = SelectField(
        "Niveau",
        choices=[
            ("", "Choisir"),
            ("debutant", "Débutant"),
            ("intermediaire", "Intermédiaire"),
            ("avance", "Avancé")
        ],
        validators=[DataRequired(message="Le niveau est obligatoire.")]
    )

    frequence_activite = SelectField(
        "Fréquence d'activité",
        choices=[
            ("", "Choisir"),
            ("faible", "Faible"),
            ("moderee", "Modérée"),
            ("elevee", "Élevée")
        ],
        validators=[DataRequired(message="La fréquence d'activité est obligatoire.")]
    )

    objectif = TextAreaField(
        "Objectif",
        validators=[
            DataRequired(message="L'objectif est obligatoire."),
            Length(max=1000, message="L'objectif ne doit pas dépasser 1000 caractères.")
        ]
    )

    submit = SubmitField("Envoyer la demande")

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This userame is taken. Please choose a different one')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken. Please choose a different one')    

class LoginForm(FlaskForm):
    username_or_email = StringField('Email or Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
