from flask import render_template, request, redirect, url_for, flash, abort
from backend import app, db, bcrypt
from backend.forms import EvaluationForm, RegistrationForm, LoginForm
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


@app.route("/evaluation", methods=["GET", "POST"])
@login_required
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

        return redirect(url_for("dashboard_client"))

    return render_template("evaluation.html", form=form, form_action=url_for("evaluation"))


@app.route("/submissions")
@login_required
def submissions():
    if current_user.role not in ["coach", "admin"]:
        flash("Tu n’as pas accès à cette page.", "danger")
        return redirect_dashboard(current_user)

    demandes = ClientFormEvaluation.query.order_by(ClientFormEvaluation.id.desc()).all()
    return render_template("submissions.html", demandes=demandes)



@app.route("/appointment")
def appointment():
    return render_template("appointment.html")


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

    return render_template("dashboard_client.html")


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

@app.route("/account")
@login_required
def account():
    return render_template("account.html")

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Base de données créée.")

