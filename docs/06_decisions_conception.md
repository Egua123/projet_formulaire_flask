# Décisions de conception

## 1. Objectif

Ce document garde une trace des décisions importantes prises pendant la conception de l’application.

Il permet de comprendre pourquoi certaines fonctionnalités sont organisées d’une certaine manière.

## 2. Décision 1 — Séparer les rôles client et coach

### Décision

L’application distingue les comptes clients et les comptes coachs.

### Raison

Les deux rôles n’ont pas les mêmes besoins.

Un client doit pouvoir :

- remplir une demande ;
- voir ses informations ;
- consulter son statut ;
- accéder à son programme futur.

Un coach doit pouvoir :

- consulter les demandes clients ;
- traiter les demandes ;
- ajouter des notes ;
- gérer les programmes futurs.

## 3. Décision 2 — Redirection selon le rôle

### Décision

Après connexion, l’utilisateur est redirigé selon son rôle :

- client vers le dashboard client ;
- coach vers le dashboard coach.

### Raison

Cela évite d’afficher la même interface à tous les utilisateurs.

Chaque rôle obtient un espace adapté.

## 4. Décision 3 — Garder une demande d’évaluation accessible

### Décision

La demande d’évaluation doit rester accessible au client même après approbation.

### Raison

La demande représente les informations initiales du client :

- objectif de départ ;
- niveau de départ ;
- habitudes de vie ;
- données physiques ;
- besoins initiaux.

Ces informations peuvent être utiles plus tard pour comparer l’évolution du client.

## 5. Décision 4 — Le client peut modifier sa propre demande

### Décision

Le client pourra modifier sa propre demande d’évaluation.

### Raison

Un client peut faire une erreur ou vouloir mettre à jour certaines informations.

### Condition importante

Le client doit uniquement pouvoir modifier sa propre demande.

Il ne doit jamais pouvoir modifier la demande d’un autre client.

## 6. Décision 5 — Le coach ne modifie pas directement les données personnelles du client

### Décision

Le coach ne doit pas modifier directement les informations personnelles soumises par le client.

### Raison

Les informations soumises par le client représentent sa déclaration initiale.

Le coach doit plutôt modifier des champs de suivi.

Exemples de champs coach :

- statut ;
- note coach ;
- archivage ;
- programme associé plus tard.

## 7. Décision 6 — Remplacer Delete par Archive

### Décision

Le coach ne doit pas supprimer définitivement une demande.

Le coach doit plutôt pouvoir archiver une demande.

### Raison

Une suppression définitive peut causer une perte de données importante.

L’archivage permet de masquer une demande sans la supprimer réellement.

## 8. Décision 7 — Suppression définitive réservée à un admin futur

### Décision

La suppression définitive des données sera réservée à un rôle administrateur futur.

### Raison

La suppression est une action sensible.

Elle doit être limitée à un rôle ayant plus de responsabilités.

## 9. Décision 8 — Une demande doit être liée à un compte client

### Décision

Une demande d’évaluation doit être reliée au compte `User` du client.

### Raison

Sans lien entre la demande et l’utilisateur, il est impossible de garantir qu’un client voit ou modifie uniquement sa propre demande.

### Conséquence technique

Le modèle `ClientFormEvaluation` devra contenir une clé étrangère vers `User`.

Exemple conceptuel :

```python
user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)