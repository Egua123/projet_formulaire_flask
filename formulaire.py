from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///one.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/evaluation", methods=["GET", "POST"])
def evaluation():
    if request.method == "POST":
        prenom = request.form.get("prenom")
        nom = request.form.get("nom")
        email = request.form.get("email")
        sexe = request.form.get("sexe")
        niveau = request.form.get("niveau")
        objectif = request.form.get("objectif")
        frequence_activite = request.form.get("frequence_activite")

        try:
            age = int(request.form.get("age"))
            taille = float(request.form.get("taille"))
            poids = float(request.form.get("poids"))
            heures_sommeil = float(request.form.get("heures_sommeil"))
            repas_par_jour = int(request.form.get("repas_par_jour"))

            if age < 0 or age >=120 :
                return "Erreur : valeurs invalides"
            if taille < 0 or taille > 290 :
                return "Erreur : valeurs invalides"
            if poids < 0  :
                return "Erreur : valeurs invalides"

            if heures_sommeil < 0 :
                return "Erreur : valeurs invalides"
            

            if repas_par_jour < 0 :
                return "Erreur : valeurs invalides"
            
            

        except (TypeError, ValueError):
            return "Erreur : un ou plusieurs champs numériques sont invalides."

        client = ClientFormEvaluation(
            prenom=prenom,
            nom=nom,
            email=email,
            age=age,
            sexe=sexe,
            taille=taille,
            poids=poids,
            objectif=objectif,
            heures_sommeil=heures_sommeil,   
            repas_par_jour=repas_par_jour,
            niveau=niveau,
            frequence_activite=frequence_activite,
        )

        db.session.add(client)
        db.session.commit()

        return redirect(url_for("submissions"))

    return render_template("evaluation.html")


@app.route("/submissions")
def submissions():
    demandes = ClientFormEvaluation.query.order_by(ClientFormEvaluation.id.desc()).all()
    return render_template("submissions.html", demandes=demandes)


@app.route("/appointment")
def appointment():
    return render_template("appointment.html")


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Base de données créée.")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)