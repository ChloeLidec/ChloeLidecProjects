"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module test_joueur.py
Module de test des joueurs
"""
# pylint: disable=missing-function-docstring
import joueur

def creer_4_joueur():
    j1=joueur.creer_joueur(1,"joueur 1",50)
    j2=joueur.creer_joueur(2,"joueur 2",0)
    j3=joueur.creer_joueur(3,"joueur 3",150)
    j4=joueur.creer_joueur(4,"joueur 4",47)
    return j1,j2,j3,j4


def test_get_id():
    j1,j2,j3,j4=creer_4_joueur()
    assert joueur.get_id(j1)==1
    assert joueur.get_id(j2)==2
    assert joueur.get_id(j3)==3
    assert joueur.get_id(j4)==4

def test_get_nom():
    j1,j2,j3,j4=creer_4_joueur()
    assert joueur.get_nom(j1)=="joueur 1"
    assert joueur.get_nom(j2)=="joueur 2"
    assert joueur.get_nom(j3)=="joueur 3"
    assert joueur.get_nom(j4)=="joueur 4"

def test_get_points():
    j1,j2,j3,j4=creer_4_joueur()
    assert joueur.get_points(j1)==50
    assert joueur.get_points(j2)==0
    assert joueur.get_points(j3)==150
    assert joueur.get_points(j4)==47


def test_ajouter_points():
    j1,j2,j3,j4=creer_4_joueur()
    assert joueur.ajouter_points(j1,10)==60 and joueur.get_id(j1)==1 and\
        joueur.get_nom(j1)=="joueur 1" and joueur.get_points(j1)==60
    assert joueur.ajouter_points(j2,25)==25 and joueur.get_id(j2)==2 and\
        joueur.get_nom(j2)=="joueur 2" and joueur.get_points(j2)==25
    assert joueur.ajouter_points(j3,-53)==97 and joueur.get_id(j3)==3 and\
        joueur.get_nom(j3)=="joueur 3" and joueur.get_points(j3)==97
    assert joueur.ajouter_points(j4,-50)==-3 and joueur.get_id(j4)==4 and\
        joueur.get_nom(j4)=="joueur 4" and joueur.get_points(j4)==-3


def test_id_joueur_droite():
    j1,j2,j3,j4=creer_4_joueur()
    assert joueur.id_joueur_droite(j1)==2
    assert joueur.id_joueur_droite(j2)==3
    assert joueur.id_joueur_droite(j3)==4
    assert joueur.id_joueur_droite(j4)==1

def id_joueur_gauche():
    j1,j2,j3,j4=creer_4_joueur()
    assert joueur.id_joueur_gauche(j1)==4
    assert joueur.id_joueur_gauche(j2)==1
    assert joueur.id_joueur_gauche(j3)==2
    assert joueur.id_joueur_gauche(j4)==3


def test_id_joueur_haut():
    j1,j2,j3,j4=creer_4_joueur()
    assert joueur.id_joueur_haut(j1)==3
    assert joueur.id_joueur_haut(j2)==4
    assert joueur.id_joueur_haut(j3)==1
    assert joueur.id_joueur_haut(j4)==2
