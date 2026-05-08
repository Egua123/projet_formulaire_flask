from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CoachTraitementForm(FlaskForm):
    status = SelectField(
        "Statut",
        choices=[
            ("nouvelle", "Nouvelle"),
            ("en_cours", "En cours"),
            ("approuvee", "Approuvée"),
            ("refusee", "Refusée")
        ],
        validators=[DataRequired()]
    )

    coach_note = TextAreaField(
        "Note du coach",
        validators=[
            Length(max=1000, message="La note ne doit pas dépasser 1000 caractères.")
        ]
    )

    submit = SubmitField("Enregistrer le suivi")