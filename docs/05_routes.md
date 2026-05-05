# Routes de l’application

## 1. Objectif

Ce document liste les routes actuelles et les routes prévues pour l’application.

Il sert de référence avant d’ajouter de nouvelles fonctionnalités.

## 2. Routes publiques

| Route | Méthode | Rôle autorisé | Description |
|---|---|---|---|
| `/` | GET | Tous | Page d’accueil |
| `/register/<role>` | GET/POST | Visiteur | Création d’un compte client ou coach |
| `/login` | GET/POST | Visiteur | Connexion |
| `/logout` | GET | Utilisateur connecté | Déconnexion |

## 3. Routes client

| Route | Méthode | Rôle autorisé | Description |
|---|---|---|---|
| `/dashboard/client` | GET | Client | Dashboard client |
| `/account` | GET/POST | Client / Coach | Page compte utilisateur |
| `/evaluation` | GET/POST | Client | Formulaire de demande d’évaluation |
| `/client/evaluation` | GET | Client | Page “Ma demande d’évaluation” |
| `/client/evaluation/update` | GET/POST | Client | Modifier sa propre demande |

## 4. Routes coach

| Route | Méthode | Rôle autorisé | Description |
|---|---|---|---|
| `/dashboard/coach` | GET | Coach | Dashboard coach |
| `/submissions` ou `/coach/demandes` | GET | Coach | Liste des demandes clients |
| `/coach/demande/<int:demande_id>` | GET | Coach | Voir les détails d’une demande |
| `/coach/demande/<int:demande_id>/traiter` | GET/POST | Coach | Changer le statut et ajouter une note |
| `/coach/demande/<int:demande_id>/archiver` | POST | Coach | Archiver une demande |

## 5. Routes futures

| Route | Méthode | Rôle autorisé | Description |
|---|---|---|---|
| `/coach/programmes` | GET | Coach | Gérer les programmes |
| `/coach/programme/new` | GET/POST | Coach | Créer un programme |
| `/client/programme` | GET | Client | Voir son programme |
| `/coach/rendez-vous` | GET | Coach | Gérer les rendez-vous |
| `/client/rendez-vous` | GET | Client | Voir ses rendez-vous |
| `/admin/dashboard` | GET | Admin | Dashboard administrateur futur |

## 6. Règles de protection des routes

### Règle 1

Les dashboards doivent être accessibles uniquement aux utilisateurs connectés.

### Règle 2

Un client ne doit pas accéder aux routes du coach.

### Règle 3

Un coach ne doit pas accéder aux routes réservées au client comme s’il était client.

### Règle 4

Une route qui modifie des données doit vérifier :

- l’utilisateur est connecté ;
- le rôle est correct ;
- la donnée appartient au bon utilisateur quand nécessaire.

### Règle 5

Les routes de suppression ou d’archivage doivent utiliser idéalement `POST`, pas seulement `GET`.

## 7. Remarque sur `/submissions`

La route `/submissions` existe ou a existé pour afficher les demandes soumises.

À terme, il serait plus clair de la renommer ou de l’organiser comme une route coach :

```text
/coach/demandes