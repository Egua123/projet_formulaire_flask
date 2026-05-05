# Prochaines étapes du projet

## 1. Objectif

Ce document liste les prochaines étapes techniques et fonctionnelles du projet.

Il sert à éviter de coder au hasard et à avancer progressivement.

## 2. État actuel résumé

Le projet permet actuellement :

- la création de comptes clients ;
- la création de comptes coachs ;
- la connexion ;
- la déconnexion ;
- la redirection selon le rôle ;
- l’affichage d’un dashboard client ;
- l’affichage d’un dashboard coach ;
- l’accès à la page compte ;
- l’accès coach aux demandes clients ;
- l’affichage des demandes clients dans un tableau.

## 3. Prochaine étape prioritaire

La prochaine étape prioritaire est de relier les demandes d’évaluation aux comptes clients.

### Pourquoi ?

Actuellement, une demande contient les informations remplies par un client, mais il faut s’assurer qu’elle est clairement associée à un compte utilisateur.

Sans ce lien, il est difficile de permettre au client de voir ou modifier uniquement sa propre demande.

## 4. Étape 1 — Lier `ClientFormEvaluation` à `User`

### Fichier concerné

```text
backend/models.py