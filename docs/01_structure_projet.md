# Structure du projet

## 1. Structure générale actuelle

Le projet suit une structure Flask organisée en package.

Structure approximative :

```text
projet_formulaire_flask/
│-- run.py
│-- requirements.txt
│-- README.md
│-- .gitignore
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
│   │   │-- evaluation.html
│   │   │-- submissions.html
│   │   │-- login.html
│   │   │-- register.html
│   │   │-- dashboard_client.html
│   │   │-- dashboard_coach.html
│   │   │-- account.html
│   │
│   └── static/
│       │-- main.css
│       └── images/
│
└── docs/