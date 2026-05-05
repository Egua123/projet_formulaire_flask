# Statuts d’une demande d’évaluation

## 1. Objectif

Ce document décrit les différents états possibles d’une demande d’évaluation client.

Il sert à déterminer :

- ce que le client peut voir ;
- ce que le client peut modifier ;
- ce que le coach peut faire ;
- quels boutons afficher dans l’interface.

## 2. Statuts prévus

Une demande d’évaluation pourra avoir les statuts suivants :

- aucune demande ;
- nouvelle ;
- en cours ;
- approuvée ;
- refusée ;
- archivée.

## 3. Description des statuts

### Aucune demande

Le client n’a pas encore rempli de demande d’évaluation.

Action client :

- remplir une demande.

Action coach :

- aucune action.

### Nouvelle

Le client a soumis une demande, mais le coach ne l’a pas encore traitée.

Action client :

- voir sa demande ;
- modifier sa demande.

Action coach :

- voir la demande ;
- commencer le traitement ;
- changer le statut à `en cours`.

### En cours

Le coach a commencé à analyser la demande.

Action client :

- voir sa demande ;
- éventuellement demander une modification.

Action coach :

- ajouter une note ;
- changer le statut ;
- approuver ou refuser la demande.

### Approuvée

La demande a été acceptée par le coach.

Action client :

- voir sa demande ;
- voir le statut ;
- accéder au programme si un programme existe ;
- demander une mise à jour plus tard.

Action coach :

- créer un programme ;
- planifier un rendez-vous ;
- archiver la demande si nécessaire.

### Refusée

La demande n’est pas acceptée.

Action client :

- voir le statut ;
- lire éventuellement un message ou une raison.

Action coach :

- ajouter une note ;
- archiver la demande.

### Archivée

La demande n’apparaît plus dans la liste principale des demandes à traiter.

Action client :

- voir éventuellement l’historique si cette fonctionnalité existe plus tard.

Action coach :

- consulter les archives plus tard ;
- réactiver la demande si une route est ajoutée plus tard.

## 4. Tableau résumé

| Statut | Signification | Actions client | Actions coach |
|---|---|---|---|
| Aucune demande | Le client n’a rien soumis | Remplir | Aucune |
| Nouvelle | Demande envoyée | Voir / Modifier | Voir / Traiter |
| En cours | Coach analyse | Voir / Demander modification | Ajouter note / Approuver / Refuser |
| Approuvée | Demande acceptée | Voir / Voir programme futur | Créer programme / Rendez-vous |
| Refusée | Demande refusée | Voir statut | Ajouter note / Archiver |
| Archivée | Demande masquée | Historique futur | Consulter archives futur |

## 5. Diagramme simple des états

```text
[Aucune demande]
        |
        | client soumet le formulaire
        v
[Nouvelle]
        |
        | coach commence l’analyse
        v
[En cours]
   |          |
   |          |
   v          v
[Approuvée] [Refusée]
   |
   | programme ou suivi futur
   v
[Programme actif futur]

Depuis plusieurs états :
[Nouvelle], [En cours], [Approuvée], [Refusée]
        |
        | coach archive
        v
[Archivée]