Routes de l'API 

# TODO 
- Ajouter les formats attendus pour chaque requête et réponse (exemple : login = {"email":"aEmail@com","password":"password"}).
- Stratégies de connexion twitter, instagram, facebook.
- Rajouter le middleware d'authentification au modèle.

# Home

## GET /

Informations principales de l'application. (Concept, locations récentes, cours du SèviCoin, informations sur WestWizards).

# Authentification

## POST /login

## POST /signup
### return 201

## POST /admin

Connexion d'un client à l'api à l'aide d'un jwt.

# User

## GET /users/
### return 200

Collection des utilisateurs (propriétaires, loueurs, admins).

## POST /users/
### return 201

Ajout d'un utilisateur à la collection.

## GET /users/:idUser

Informations d'un utilisateur.

## PATCH /users/:idUser

Mise à jour des informations d'un utilisateur.

## DELETE /users/:idUser

Suppression d'un utilisateur.

# Object

## GET /objects/

Collection des objets enregistrés.

## POST /objects/
### return 201

Ajout d'un objet.

## GET /objects/:idObject

Informations d'un objet.

## PATCH /objects/:idObject

Mise à jour des informations d'un objet.

## DELETE /objects/:idObject

Suppression d'un objet.

# Rent

## GET /rents/

Collection des locations.

## POST /rents/
### return 201

Ajout d'une location.

## GET /rents/:idRent

Informations d'une location.

## PATCH /rents/:idRent

Mise à jour des informations d'une location.

## DELETE /rents/:idRent

Suppression d'une location.

# Coin

## GET /sevicoin

Informations sur le SèviCoin, la cryptomonnaie des locations de l'application.


