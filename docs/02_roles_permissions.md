# Rôles et permissions

## 1. Objectif

Ce document définit les différents rôles de l’application et les actions autorisées pour chaque rôle.

L’objectif est d’éviter qu’un utilisateur puisse accéder à des pages ou actions qui ne correspondent pas à son rôle.

## 2. Rôles actuels

L’application utilise actuellement deux rôles principaux :

- Client
- Coach

Un rôle administrateur pourra être ajouté plus tard.

## 3. Rôle : Visiteur

Un visiteur est une personne non connectée.

### Permissions du visiteur

Le visiteur peut :

- voir la page d’accueil ;
- créer un compte client ;
- créer un compte coach ;
- accéder à la page de connexion.

Le visiteur ne peut pas :

- accéder au dashboard client ;
- accéder au dashboard coach ;
- voir les demandes clients ;
- modifier une demande ;
- traiter une demande ;
- accéder à la page compte.

## 4. Rôle : Client

Un client est un utilisateur connecté avec le rôle `client`.

### Permissions du client

Le client peut :

- se connecter ;
- se déconnecter ;
- accéder à son dashboard client ;
- accéder à son compte ;
- remplir une demande d’évaluation ;
- voir sa propre demande d’évaluation ;
- modifier sa propre demande d’évaluation ;
- voir le statut de sa demande.

### Restrictions du client

Le client ne peut pas :

- accéder au dashboard coach ;
- consulter toutes les demandes clients ;
- modifier les demandes d’autres clients ;
- supprimer une demande d’un autre client ;
- traiter une demande comme un coach ;
- archiver une demande comme un coach.

## 5. Rôle : Coach

Un coach est un utilisateur connecté avec le rôle `coach`.

### Permissions du coach

Le coach peut :

- se connecter ;
- se déconnecter ;
- accéder à son dashboard coach ;
- accéder à son compte ;
- consulter les demandes clients ;
- voir les détails d’une demande ;
- traiter une demande ;
- ajouter une note de suivi ;
- changer le statut d’une demande ;
- archiver une demande.

### Restrictions du coach

Le coach ne devrait pas :

- modifier directement les informations personnelles soumises par un client ;
- supprimer définitivement une demande ;
- modifier le compte personnel d’un client ;
- accéder au dashboard client comme s’il était client.

## 6. Rôle futur : Admin

Le rôle administrateur n’est pas encore implémenté.

À terme, l’administrateur pourrait :

- voir tous les utilisateurs ;
- gérer les comptes ;
- supprimer définitivement des données ;
- réactiver des demandes archivées ;
- gérer les rôles ;
- superviser les coachs.

## 7. Tableau résumé des permissions

| Fonctionnalité | Visiteur | Client | Coach | Admin futur |
|---|---:|---:|---:|---:|
| Voir la page d’accueil | Oui | Oui | Oui | Oui |
| Créer un compte client | Oui | Non | Non | Oui |
| Créer un compte coach | Oui | Non | Non | Oui |
| Se connecter | Oui | Oui | Oui | Oui |
| Se déconnecter | Non | Oui | Oui | Oui |
| Accéder au dashboard client | Non | Oui | Non | Oui |
| Accéder au dashboard coach | Non | Non | Oui | Oui |
| Accéder à son compte | Non | Oui | Oui | Oui |
| Remplir une demande d’évaluation | Non | Oui | Non | Non |
| Voir sa propre demande | Non | Oui | Non | Oui |
| Modifier sa propre demande | Non | Oui | Non | Oui |
| Voir toutes les demandes clients | Non | Non | Oui | Oui |
| Traiter une demande | Non | Non | Oui | Oui |
| Ajouter une note coach | Non | Non | Oui | Oui |
| Archiver une demande | Non | Non | Oui | Oui |
| Supprimer définitivement une demande | Non | Non | Non | Oui |

## 8. Règles importantes

### Règle 1

Un client doit voir uniquement sa propre demande d’évaluation.

### Règle 2

Un coach peut voir les demandes clients, mais ne doit pas modifier directement les informations personnelles soumises par le client.

### Règle 3

Le coach peut modifier les informations de suivi :

- statut ;
- note coach ;
- archivage.

### Règle 4

La suppression définitive doit être réservée à un futur rôle administrateur.

### Règle 5

Toutes les routes sensibles doivent être protégées par :

- connexion obligatoire ;
- vérification du rôle ;
- vérification de propriété des données quand nécessaire.