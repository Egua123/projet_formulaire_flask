# Parcours utilisateurs

## 1. Objectif

Ce document décrit les parcours principaux des utilisateurs dans l’application.

Il sert à comprendre comment un visiteur, un client ou un coach utilise l’application.

## 2. Parcours visiteur — Découverte du site

### Étapes

1. Le visiteur arrive sur la page d’accueil.
2. Il découvre le service de coaching.
3. Il peut choisir de créer un compte.
4. Il choisit entre :
   - compte client ;
   - compte coach.
5. Il remplit le formulaire d’inscription.
6. Après inscription, il peut se connecter.

### Objectif du parcours

Permettre à une personne non connectée de comprendre l’application et de créer un compte adapté à son rôle.

## 3. Parcours client — Création de compte

### Étapes

1. Le visiteur clique sur créer un compte.
2. Il choisit le rôle client.
3. Il remplit le formulaire d’inscription.
4. Le compte est créé avec le rôle `client`.
5. Il est redirigé vers la page de connexion ou connecté selon la logique actuelle.
6. Après connexion, il arrive sur le dashboard client.

### Résultat attendu

Le client possède un compte utilisateur avec le rôle `client`.

## 4. Parcours coach — Création de compte

### Étapes

1. Le visiteur clique sur créer un compte.
2. Il choisit le rôle coach.
3. Il remplit le formulaire d’inscription.
4. Le compte est créé avec le rôle `coach`.
5. Après connexion, il arrive sur le dashboard coach.

### Résultat attendu

Le coach possède un compte utilisateur avec le rôle `coach`.

## 5. Parcours client — Demande d’évaluation

### État actuel

Le client peut remplir une demande d’évaluation.

La demande contient notamment :

- prénom ;
- nom ;
- email ;
- âge ;
- sexe ;
- taille ;
- poids ;
- objectif ;
- heures de sommeil ;
- repas par jour ;
- niveau ;
- fréquence d’activité.

### Parcours prévu

1. Le client se connecte.
2. Il arrive sur son dashboard client.
3. Il clique sur “Ma demande d’évaluation”.
4. Si aucune demande n’existe :
   - le système affiche un bouton “Remplir ma demande”.
5. Le client remplit le formulaire.
6. La demande est enregistrée dans la base de données.
7. Le client peut ensuite consulter sa demande.
8. Le client peut modifier sa demande selon les règles définies.
9. Le client peut suivre le statut de sa demande.

### Résultat attendu

La demande est liée au compte du client connecté.

## 6. Parcours client — Consultation de sa demande

### Parcours prévu

1. Le client se connecte.
2. Il accède à son dashboard.
3. Il clique sur “Ma demande d’évaluation”.
4. Le système cherche la demande associée à son compte.
5. Si une demande existe :
   - le résumé de la demande est affiché ;
   - le statut est affiché ;
   - des actions sont proposées selon le statut.
6. Si aucune demande n’existe :
   - le système propose de remplir une demande.

### Actions possibles

Selon le statut de la demande, le client pourra :

- voir sa demande ;
- modifier sa demande ;
- demander une mise à jour ;
- voir son programme si un programme existe plus tard.

## 7. Parcours coach — Consultation des demandes clients

### État actuel

Le coach peut accéder à une page affichant les demandes clients sous forme de tableau.

Le tableau affiche les informations soumises par les clients.

### Parcours

1. Le coach se connecte.
2. Il arrive sur le dashboard coach.
3. Il clique sur “Demandes clients”.
4. Il voit la liste des demandes clients.
5. Il peut consulter les informations de chaque demande.

### Résultat actuel

Le coach peut lire les demandes.

## 8. Parcours coach — Traitement d’une demande

### Parcours prévu

1. Le coach se connecte.
2. Il accède à la liste des demandes clients.
3. Il clique sur une demande.
4. Il consulte les détails.
5. Il change le statut de la demande.
6. Il ajoute une note interne.
7. Il enregistre le traitement.
8. Le client peut voir le nouveau statut depuis son dashboard.

### Actions prévues pour le coach

Le coach pourra :

- voir les détails d’une demande ;
- changer son statut ;
- ajouter une note ;
- archiver la demande.

## 9. Parcours futur — Programme client

Cette fonctionnalité n’est pas encore active.

Parcours futur possible :

1. Le coach approuve une demande.
2. Le coach crée un programme personnalisé.
3. Le programme est associé au client.
4. Le client peut consulter son programme dans son dashboard.
5. Le coach peut modifier le programme.

## 10. Parcours futur — Rendez-vous

Cette fonctionnalité n’est pas encore active.

Parcours futur possible :

1. Le coach propose un rendez-vous.
2. Le client consulte ses rendez-vous.
3. Le client peut voir les informations du rendez-vous.
4. Le coach peut gérer les rendez-vous depuis son dashboard.