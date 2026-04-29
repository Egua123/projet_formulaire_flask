from backend import db
from datetime import datetime

class ClientFormEvaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(50), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    sexe = db.Column(db.String(20), nullable=False)
    taille = db.Column(db.Float, nullable=False)
    poids = db.Column(db.Float, nullable=False)
    objectif = db.Column(db.Text, nullable=False)
    heures_sommeil = db.Column(db.Float, nullable=False)
    repas_par_jour = db.Column(db.Integer, nullable=False)
    niveau = db.Column(db.String(20), nullable=False)
    frequence_activite = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return (
            f"ClientFormEvaluation('{self.prenom}', '{self.nom}', '{self.email}')"
        )

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(160), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    role = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}','{self.role}')"
