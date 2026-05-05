import os
import secrets
from PIL import Image
from flask import render_template, request, redirect, url_for, flash, abort
from backend import app, db, bcrypt
from backend.forms import EvaluationForm, RegistrationForm, LoginForm, UpdateAccountForm, CoachTraitementForm
from backend.models import ClientFormEvaluation, User
from flask_login import login_user, current_user, logout_user, login_required





def redirect_dashboard(user):
    if user.role == "admin":
        return redirect(url_for("dashboard_admin"))
    elif user.role == "coach":
        return redirect(url_for("dashboard_coach"))
    else:
        return redirect(url_for("dashboard_client"))
@app.route("/")
def index():
    return render_template("index.html")





@app.route("/submissions")
@login_required
def submissions():
    if current_user.role not in ["coach", "admin"]:
        flash("Tu n’as pas accès à cette page.", "danger")
        return redirect_dashboard(current_user)

    filtre = request.args.get("filtre", "actives")

    if filtre == "archivees":
        demandes = ClientFormEvaluation.query.filter_by(
            is_archived=True
        ).order_by(ClientFormEvaluation.id.desc()).all()

    elif filtre == "toutes":
        demandes = ClientFormEvaluation.query.order_by(
            ClientFormEvaluation.id.desc()
        ).all()

    else:
        filtre = "actives"
        demandes = ClientFormEvaluation.query.filter_by(
            is_archived=False
        ).order_by(ClientFormEvaluation.id.desc()).all()

    return render_template(
        "submissions.html",
        demandes=demandes,
        filtre=filtre
    )



@app.route("/appointment")
def appointment():
    return render_template("appointment.html")

"""
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    demande = ClientFormEvaluation.query.get_or_404(id)
    nom_complet = f"{demande.prenom} {demande.nom}."
    db.session.delete(demande)
    db.session.commit()
    flash(f"{nom_complet} a été supprimé.", "Success")

    return redirect(url_for("submissions"))




@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    demande = ClientFormEvaluation.query.get_or_404(id)
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

        db.session.commit()
        flash("La demande a été mise à jour.", "success")

        return redirect(url_for("submissions"))

    return render_template("evaluation.html", form=form, form_action=url_for("edit", id=demande.id))



"""


@app.route("/coach/demande/<int:id>/archiver", methods=["POST"])
@login_required
def archive_demande(id):
    if current_user.role not in ["coach", "admin"]:
        flash("Tu n’as pas accès à cette action.", "danger")
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.get_or_404(id)
    demande.is_archived = True

    db.session.commit()
    flash("La demande a été archivée.", "success")

    return redirect(url_for("submissions", filtre="archivees"))



@app.route("/coach/demande/<int:id>/desarchiver", methods=["POST"])
@login_required
def desarchive_demande(id):
    if current_user.role not in ["coach", "admin"]:
        flash("Tu n’as pas accès à cette action.", "danger")
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.get_or_404(id)
    demande.is_archived = False

    db.session.commit()
    flash("La demande a été désarchivée.", "success")

    return redirect(url_for("submissions", filtre="actives"))


@app.route("/coach/demande/<int:id>/traiter", methods=["GET", "POST"])
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
        return redirect(url_for("submissions"))

    return render_template(
        "traiter_demande.html",
        form=form,
        demande=demande
    )






@app.route("/register/<role>", methods=['GET','POST'])
def register_role(role):

    if role not in ["client", "coach"]:
        abort(404)


    if current_user.is_authenticated:
        return redirect_dashboard(current_user)
        
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username= form.username.data, email=form.email.data, password = hashed_password, role=role)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("login"))
    return render_template("register.html", form= form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect_dashboard(current_user)

    
    form = LoginForm()
    if form.validate_on_submit():
        identifier = form.username_or_email.data

        user = User.query.filter(
            (User.email == identifier) | (User.username == identifier)
        ).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page= request.args.get('next')
            return redirect(next_page) if next_page else redirect_dashboard(current_user)
        

        else:
            flash('Login Unsuccessful. Please check username/email or password', 'danger')
    return render_template("login.html", form=form)



@app.route("/dashboard-client")
@login_required
def dashboard_client():
    if current_user.role != "client":
        return redirect_dashboard(current_user)
    
    demande = ClientFormEvaluation.query.filter_by(
        user_id=current_user.id
    ).first()

    return render_template("dashboard_client.html", demande=demande)


@app.route("/dashboard-coach")
@login_required
def dashboard_coach():
    if current_user.role != "coach":
        return redirect_dashboard(current_user)

    return render_template("dashboard_coach.html")

@app.route("/dashboard-admin")
@login_required
def dashboard_admin():
    return render_template("dashboard_admin.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))





def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size =(125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account",  methods=['GET', 'POST'] )
@login_required
def account():
        form =  UpdateAccountForm()
        if form.validate_on_submit():
            if form.picture.data:
                pictue_file = save_picture(form.picture.data)
                current_user.image_file = pictue_file


            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash('your account has been updated!', 'succes')
            return redirect(url_for('account'))
        elif request.method =='GET':
            form.username.data = current_user.username
            form.email.data = current_user.email

        image_file = url_for('static', filename='profile_pics/'+ current_user.image_file)
        return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route("/evaluation", methods=["GET", "POST"])
@login_required
def evaluation():
    if current_user.role != "client":
        flash("Seuls les clients peuvent remplir une demande d’évaluation.", "danger")
        return redirect_dashboard(current_user)

    demande_existante = ClientFormEvaluation.query.filter_by(
        user_id=current_user.id
    ).first()

    if demande_existante:
        flash("Tu as déjà une demande d’évaluation. Tu peux la consulter ou la modifier.", "info")
        return redirect(url_for("client_evaluation"))

    form = EvaluationForm()

    if request.method == "GET":
        form.email.data = current_user.email

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
            user_id=current_user.id,
            status="nouvelle"
        )

        db.session.add(client)
        db.session.commit()

        flash("La demande a été envoyée avec succès.", "success")
        return redirect(url_for("client_evaluation"))

    return render_template(
        "evaluation.html",
        form=form,
        form_action=url_for("evaluation")
    )


@app.route("/client/evaluation")
@login_required
def client_evaluation():
    if current_user.role != "client":
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.filter_by(
        user_id=current_user.id
    ).first()

    return render_template("client_evaluation.html", demande=demande)


@app.route("/client/evaluation/update", methods=["GET", "POST"])
@login_required
def client_evaluation_update():
    if current_user.role != "client":
        return redirect_dashboard(current_user)

    demande = ClientFormEvaluation.query.filter_by(
        user_id=current_user.id
    ).first()

    if not demande:
        flash("Tu dois d’abord remplir une demande avant de pouvoir la modifier.", "info")
        return redirect(url_for("evaluation"))


    # 4. Si la demande est archivée
    if demande.is_archived:
        flash("Cette demande est archivée et ne peut plus être modifiée.", "warning")
        return redirect(url_for("client_evaluation"))


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
        return redirect(url_for("client_evaluation"))

    return render_template(
        "evaluation.html",
        form=form,
        form_action=url_for("client_evaluation_update")
    )





@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Base de données créée.")

