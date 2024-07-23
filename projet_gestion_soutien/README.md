# Gestion Soutien IUT

Ce projet a pour but de créer une application web avec le framework django afin de gérer le soutien pour les élèves à l'IUT d'Orléans.

## Notre groupe

* Axel Jacquet
* Chloé Lidec
* Tom Germain
* Téo Mikulic
* IUT Informatique Orléans / 31A

## Liens divers

- Maquette(utilité):
    - https://www.figma.com/proto/r6hDMhnmvFoz5PxU2a6BOu/Maquettes-Projet-Soutien?node-id=103%3A29&scaling=scale-down&page-id=0%3A1&starting-point-node-id=103%3A29
    - https://www.figma.com/file/r6hDMhnmvFoz5PxU2a6BOu/Maquettes-Projet-Soutien?node-id=0%3A1
- Dossier docs google:
    - https://drive.google.com/drive/folders/14aOGY54dxc9G4fCnoDl-OzbdYvK74Ao5?usp=drive_link

## Gestion GIT

N'ayant eu les cours de GIT que plus tard dans l'année, nous avons débuté notre projet avec nos propres normes:

- Commit sous la forme "[ADD UPDATE DELETE] #numero de l'issue message" ou "#numero de l'issue [ADD UPDATE DELETE]  message"
- branches fusionnées ensuite sur la branche dev

par la suite, les noms des branches ont été adaptées pour suivre la forme:
hotfix fix feature/numero issue/nom

aussi, nous avons découvert les taches que plus tard sur github donc seuleument les issues les plus récentes ont des issues enfants liées.

## Installation et lancement du projet

- Clonez le projet sur votre machine

Deux solutions possibles:
- Ouvrez un terminal dan gestion_soutien_iut/nx-gestion-soutien/packages/GestionSoutien
- Lancez la commande python3 manage.py loaddata static/db.json ( si première utilisation)
- Lancez python3 manage.py runserver


ou bien:
- Ouvrez un terminal dans gestion_soutien_iut/nx-gestion-soutien
- Lancez la commande npm install --save-dev @nx/cypress
- Ouvrez VSCode et avec l'extension NX Console lancez serve

Accedez au site sur localhost:8000

