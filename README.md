# App Coaching

App Coaching est une application web développée avec Flask pour gérer une plateforme de coaching sportif.

Le projet permet actuellement à deux types d’utilisateurs, les clients et les coachs, de créer un compte, de se connecter et d’accéder à un espace adapté à leur rôle.

## Fonctionnalités actuelles

- Création de compte client
- Création de compte coach
- Connexion et déconnexion
- Redirection selon le rôle utilisateur
- Dashboard client
- Dashboard coach
- Page de compte utilisateur
- Upload et modification de l’image de profil
- Formulaire de demande d’évaluation client
- Association d’une demande d’évaluation à un compte client
- Consultation de sa demande côté client
- Modification de sa demande côté client
- Consultation des demandes clients côté coach
- Filtrage des demandes actives, archivées ou toutes
- Traitement d’une demande par le coach
- Ajout d’une note de suivi par le coach
- Modification du statut d’une demande
- Archivage et désarchivage des demandes
- Protection des routes selon le rôle utilisateur

## Technologies utilisées

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- Flask-WTF / WTForms
- SQLite
- Jinja2
- HTML
- CSS
- Bootstrap
- Pillow

## Structure du projet

```text
projet_formulaire_flask/
│-- run.py
│-- README.md
│
├── backend/
│   │-- __init__.py
│   │-- routes.py
│   │-- models.py
│   │-- forms.py
│   │
│   ├── templates/
│   │   │-- base.html
│   │   │-- index.html
│   │   │-- login.html
│   │   │-- register.html
│   │   │-- dashboard_client.html
│   │   │-- dashboard_coach.html
│   │   │-- account.html
│   │   │-- evaluation.html
│   │   │-- client_evaluation.html
│   │   │-- submissions.html
│   │   │-- traiter_demande.html
│   │
│   └── static/
│       │-- main.css
│       └── profile_pics/
│
└── docs/
    │-- 00_vue_ensemble.md
    │-- 01_structure_projet.md
    │-- 02_roles_permissions.md
    │-- 03_parcours_utilisateurs.md
    │-- 04_statuts_demande.md
    │-- 05_routes.md
    │-- 06_decisions_conception.md
    │-- 07_prochaines_etapes.md