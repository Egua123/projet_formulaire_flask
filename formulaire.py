from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import EvaluationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e7a7821dce87007b9d9a53d4a7b366031139242aa986025a6ed74a23fed5b953'
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
    form = EvaluationForm()
    if form.validate_on_submit():

        client = ClientFormEvaluation(
            prenom=form.prenom.data,
            nom=form.nom.data,
            email=form.email.data,
            age=form.age.data,
            sexe=form.sexe.data,
            taille=form.taille.data,
            poids=form.poids.data,
            objectif=form.objectif.data,
            heures_sommeil=form.heures_sommeil.data,
            repas_par_jour=form.repas_par_jour.data,
            niveau=form.niveau.data,
            frequence_activite=form.frequence_activite.data,
        )

        

        db.session.add(client)
        db.session.commit()
        flash("La demande a été envoyée avec succès.", "success")

        return redirect(url_for("submissions"))

    return render_template("evaluation.html", form=form)


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