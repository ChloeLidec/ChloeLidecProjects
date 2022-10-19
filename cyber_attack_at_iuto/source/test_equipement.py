"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module equipement.py
    ce module gère les équipements ordinateurs et serveurs
"""
# pylint: disable=missing-function-docstring
import equipement

def creer_4_equipements():
    e1=equipement.creer_equipement(equipement.ORDINATEUR,10)
    e2=equipement.creer_equipement(equipement.SERVEUR,8)
    e3=equipement.creer_equipement(equipement.ORDINATEUR,0)
    e4=equipement.creer_equipement(equipement.SERVEUR,1)
    return e1,e2,e3,e4

def test_attaque():
    e1,e2,e3,e4=creer_4_equipements()
    assert equipement.attaque(e1)==9 and\
        equipement.get_type(e1)==equipement.ORDINATEUR and equipement.get_resistance(e1)==9
    assert equipement.attaque(e2)==7 and\
        equipement.get_type(e2)==equipement.SERVEUR and equipement.get_resistance(e2)==7
    assert equipement.attaque(e3)==0 and\
        equipement.get_type(e3)==equipement.ORDINATEUR and equipement.get_resistance(e3)==0
    assert equipement.attaque(e4)==0 and\
        equipement.get_type(e4)==equipement.SERVEUR and equipement.get_resistance(e4)==0

def test_est_detruit():
    e1,e2,e3,e4=creer_4_equipements()
    assert not equipement.est_detruit(e1)
    assert not equipement.est_detruit(e2)
    assert equipement.est_detruit(e3)
    assert not equipement.est_detruit(e4)

def test_get_resistance():
    e1,e2,e3,e4=creer_4_equipements()
    assert equipement.get_resistance(e1)==10
    assert equipement.get_resistance(e2)==8
    assert equipement.get_resistance(e3)==0
    assert equipement.get_resistance(e4)==1
    
def test_get_type():
    e1,e2,e3,e4=creer_4_equipements()
    assert equipement.get_type(e1)==equipement.ORDINATEUR
    assert equipement.get_type(e2)==equipement.SERVEUR
    assert equipement.get_type(e3)==equipement.ORDINATEUR
    assert equipement.get_type(e4)==equipement.SERVEUR

def test_set_resistance():
    e1,e2,e3,e4=creer_4_equipements()
    equipement.set_resistance(e1,20)
    assert equipement.get_resistance(e1)==20 and equipement.get_type(e1)==equipement.ORDINATEUR
    equipement.set_resistance(e2,3)
    assert equipement.get_resistance(e2)==3 and equipement.get_type(e2)==equipement.SERVEUR
    equipement.set_resistance(e3,7)
    assert equipement.get_resistance(e3)==7 and equipement.get_type(e3)==equipement.ORDINATEUR
    equipement.set_resistance(e4,4)
    assert equipement.get_resistance(e4)==4 and equipement.get_type(e4)==equipement.SERVEUR