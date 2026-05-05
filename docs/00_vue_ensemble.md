# Vue d’ensemble du projet — App Coaching

## 1. Nom du projet

App Coaching

## 2. Objectif général

L’objectif du projet est de développer une application web de coaching sportif permettant à des utilisateurs de créer un compte, de remplir une demande d’évaluation, puis d’être suivis par un coach.

L’application distingue principalement deux types d’utilisateurs :

- Client
- Coach

À terme, un rôle administrateur pourra être ajouté pour gérer les utilisateurs, les demandes et les données sensibles.

## 3. Objectif de la première version

La première version vise à mettre en place les bases fonctionnelles suivantes :

- Page d’accueil
- Formulaire d’évaluation client
- Création de compte client
- Création de compte coach
- Connexion
- Déconnexion
- Dashboard client
- Dashboard coach
- Accès à un compte utilisateur
- Consultation des demandes clients par le coach
- Protection des routes selon le rôle
- Préparation des futures opérations CRUD

## 4. Technologies utilisées

Le projet utilise actuellement :

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

## 5. État actuel du projet

À l’état actuel, l’application permet :

- de créer un compte client ;
- de créer un compte coach ;
- de se connecter avec les deux types de comptes ;
- de rediriger chaque utilisateur vers son dashboard selon son rôle ;
- d’afficher un dashboard différent pour le client et le coach ;
- d’accéder à une page de compte utilisateur ;
- d’afficher les demandes clients dans l’espace coach ;
- de voir les informations soumises par les clients dans un tableau.

Certaines fonctionnalités sont visibles dans l’interface mais pas encore actives :

- gestion des programmes ;
- gestion des rendez-vous ;
- bouton de modification ou suppression réelle des demandes ;
- consultation détaillée avancée d’une demande ;
- traitement complet d’une demande par un coach.

## 6. Vision future

À terme, l’application pourrait inclure :

- un suivi complet des clients ;
- des programmes personnalisés ;
- des rendez-vous ;
- un système de notes du coach ;
- un statut de traitement des demandes ;
- un historique des évaluations ;
- une messagerie ;
- un espace administrateur ;
- une interface plus avancée avec React ;
- une API Flask ;
- un déploiement avec Docker.


## Structure générale

Le projet est organisé autour d’un package Flask principal nommé `backend`.

```text
projet_formulaire_flask/
│-- run.py
│
├── backend/
│   │-- __init__.py
│   │-- routes.py
│   │-- models.py
│   │-- forms.py
│   ├── templates/
│   └── static/
│
└── docs/
```