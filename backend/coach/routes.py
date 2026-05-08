from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from backend import db
from backend.models import ClientFormEvaluation
from backend.coach.forms import CoachTraitementForm
from backend.utils import redirect_dashboard

coach = Blueprint("coach", __name__)


@coach.route("/dashboard-coach")
@login_required
def dashboard_coach():
    if current_user.role != "coach":
        return redirect_dashboard(current_user)

    return render_template("dashboard_coach.html")


@coach.route("/submissions")
@login_required
def submissions():
    if current_user.role not in ["coach", "admin"]:
        flash("Tu n’as pas accès à cette page.", "danger")
        return redirect_dashboard(current_user)

    filtre = request.args.get("filtre", "actives")
    page = request.args.get("page", 1, type=int)

    if filtre == "archivees":
        query = ClientFormEvaluation.query.filter_by(
            is_archived=True
        )

    elif filtre == "toutes":
        query = ClientFormEvaluation.query

    else:
        filtre = "actives"
        query = ClientFormEvaluation.query.filter_by(
            is_archived=False
        )

    query = query.order_by(ClientFormEvaluation.created_at.desc())

    demandes = query.paginate(page=page, per_page=2)

    return render_template(
        "submissions.html",
        demandes=demandes,
        filtre=filtre
    )


@coach.route("/coach/demande/<int:id>/archiver", methods=["POST"])
@login_required
def archive_demande(id):
    if current_user.role not in ["coach", "admin"]:
        flash("Tu n’as pas accès à cette action.", "danger")
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.get_or_404(id)
    demande.is_archived = True

    db.session.commit()

    flash("La demande a été archivée.", "success")
    return redirect(url_for("coach.submissions", filtre="archivees"))


@coach.route("/coach/demande/<int:id>/desarchiver", methods=["POST"])
@login_required
def desarchive_demande(id):
    if current_user.role not in ["coach", "admin"]:
        flash("Tu n’as pas accès à cette action.", "danger")
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.get_or_404(id)
    demande.is_archived = False

    db.session.commit()

    flash("La demande a été désarchivée.", "success")
    return redirect(url_for("coach.submissions", filtre="actives"))


@coach.route("/coach/demande/<int:id>/traiter", methods=["GET", "POST"])
@login_required
def traiter_demande(id):
    if current_user.role not in ["coach", "admin"]:
        flash("Tu n’as pas accès à cette action.", "danger")
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.get_or_404(id)
    form = CoachTraitementForm(obj=demande)

    if form.validate_on_submit():
        demande.status = form.status.data
        demande.coach_note = form.coach_note.data

        db.session.commit()

        flash("Le suivi de la demande a été mis à jour.", "success")
        return redirect(url_for("coach.submissions"))

    return render_template(
        "traiter_demande.html",
        form=form,
        demande=demande
    )