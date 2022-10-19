"""
              Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module test_protection.py
    teste les protections que les joueurs peuvent utiliser
"""
# pylint: disable=missing-function-docstring
import protection

def creer_6_protections():
    p1=protection.creer_protection(protection.DONNEES_PERSONNELLES,2)
    p2=protection.creer_protection(protection.DPO,1)
    p3=protection.creer_protection(protection.ANTIVIRUS,0)
    p4=protection.creer_protection(protection.FIREWALL_BDHG,2)
    p5=protection.creer_protection(protection.FIREWALL_BGHD,1)
    p6=protection.creer_protection(protection.PAS_DE_PROTECTION,0)
    return p1,p2,p3,p4,p5,p6
    


def test_get_type():
    p1,p2,p3,p4,p5,p6=creer_6_protections()
    assert protection.get_type(p1)==protection.DONNEES_PERSONNELLES
    assert protection.get_type(p2)==protection.DPO
    assert protection.get_type(p3)==protection.ANTIVIRUS
    assert protection.get_type(p4)==protection.FIREWALL_BDHG
    assert protection.get_type(p5)==protection.FIREWALL_BGHD
    assert protection.get_type(p6)==protection.PAS_DE_PROTECTION
    

def test_get_resistance():
    p1,p2,p3,p4,p5,p6=creer_6_protections()
    assert protection.get_resistance(p1)==2
    assert protection.get_resistance(p2)==1
    assert protection.get_resistance(p3)==0
    assert protection.get_resistance(p4)==2
    assert protection.get_resistance(p5)==1
    assert protection.get_resistance(p6)==0


def test_enlever_resistance():
    p1,p2,p3,p4,p5,p6=creer_6_protections()
    assert protection.enlever_resistance(p1)==1 and\
        protection.get_resistance(p1)==1 and protection.get_type(p1)==protection.DONNEES_PERSONNELLES
    assert protection.enlever_resistance(p2)==0 and\
        protection.get_resistance(p2)==0 and protection.get_type(p2)==protection.DPO
    assert protection.enlever_resistance(p3)==0 and\
        protection.get_resistance(p3)==0 and protection.get_type(p3)==protection.ANTIVIRUS
    assert protection.enlever_resistance(p4)==1 and\
        protection.get_resistance(p4)==1 and protection.get_type(p4)==protection.FIREWALL_BDHG
    assert protection.enlever_resistance(p5)==0 and\
        protection.get_resistance(p5)==0 and protection.get_type(p5)==protection.FIREWALL_BGHD
    assert protection.enlever_resistance(p6)==0 and\
        protection.get_resistance(p6)==0 and protection.get_type(p6)==protection.PAS_DE_PROTECTION
