from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from backend import db
from backend.models import ClientFormEvaluation
from backend.client.forms import EvaluationForm
from backend.utils import redirect_dashboard

client = Blueprint("client", __name__)


@client.route("/dashboard-client")
@login_required
def dashboard_client():
    if current_user.role != "client":
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.filter_by(
        user_id=current_user.id
    ).first()

    return render_template("dashboard_client.html", demande=demande)


@client.route("/evaluation", methods=["GET", "POST"])
@login_required
def evaluation():
    if current_user.role != "client":
        flash("Seuls les clients peuvent remplir une demande d’évaluation.", "danger")
        return redirect_dashboard(current_user)

    demande_existante = ClientFormEvaluation.query.filter_by(
        user_id=current_user.id
    ).first()

    if demande_existante:
        flash(
            "Tu as déjà une demande d’évaluation. Tu peux la consulter ou la modifier.",
            "info"
        )
        return redirect(url_for("client.client_evaluation"))

    form = EvaluationForm()

    if request.method == "GET":
        form.email.data = current_user.email

    if form.validate_on_submit():
        demande = ClientFormEvaluation(
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
            user_id=current_user.id,
            status="nouvelle"
        )

        db.session.add(demande)
        db.session.commit()

        flash("La demande a été envoyée avec succès.", "success")
        return redirect(url_for("client.client_evaluation"))

    return render_template(
        "evaluation.html",
        form=form,
        form_action=url_for("client.evaluation")
    )


@client.route("/client/evaluation")
@login_required
def client_evaluation():
    if current_user.role != "client":
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.filter_by(
        user_id=current_user.id
    ).first()

    return render_template("client_evaluation.html", demande=demande)


@client.route("/client/evaluation/update", methods=["GET", "POST"])
@login_required
def client_evaluation_update():
    if current_user.role != "client":
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.filter_by(
        user_id=current_user.id
    ).first()

    if not demande:
        flash("Tu dois d’abord remplir une demande avant de pouvoir la modifier.", "info")
        return redirect(url_for("client.evaluation"))

    if demande.is_archived:
        flash("Cette demande est archivée et ne peut plus être modifiée.", "warning")
        return redirect(url_for("client.client_evaluation"))

    form = EvaluationForm(obj=demande)

    if form.validate_on_submit():
        demande.prenom = form.prenom.data
        demande.nom = form.nom.data
        demande.email = form.email.data
        demande.age = form.age.data
        demande.sexe = form.sexe.data
        demande.taille = form.taille.data
        demande.poids = form.poids.data
        demande.objectif = form.objectif.data
        demande.heures_sommeil = form.heures_sommeil.data
        demande.repas_par_jour = form.repas_par_jour.data
        demande.niveau = form.niveau.data
        demande.frequence_activite = form.frequence_activite.data

        if demande.status in ["approuvee", "refusee"]:
            demande.status = "nouvelle"

        db.session.commit()

        flash("Ta demande a été mise à jour.", "success")
        return redirect(url_for("client.client_evaluation"))

    return render_template(
        "evaluation.html",
        form=form,
        form_action=url_for("client.client_evaluation_update")
    )