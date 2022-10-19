"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module test_joueur.py
Module de test des deux fonctions de matrice
"""
# pylint: disable=missing-function-docstring
import matrice

def creer_3_matrices():
    m1 = matrice.creer_matrice(5, 5, 0)
    matrice.set_val(m1, 0, 2, 1)
    matrice.set_val(m1, 1, 2, 2)
    matrice.set_val(m1, 1, 3, 1)
    matrice.set_val(m1, 2, 1, 2)
    matrice.set_val(m1, 2, 0, 2)
    matrice.set_val(m1, 4, 2, 1)
    m2 = matrice.creer_matrice(5, 5, 0)
    matrice.set_val(m2, 0, 2, 1)
    matrice.set_val(m2, 1, 1, 2)
    matrice.set_val(m2, 1, 3, 5)
    matrice.set_val(m2, 3, 1, 4)
    matrice.set_val(m2, 2, 0, 2)
    matrice.set_val(m2, 2, 1, 2)
    matrice.set_val(m2, 4, 2, 1)
    m3 = matrice.creer_matrice(5, 5, 0)
    matrice.set_val(m3, 0, 4, 5)
    matrice.set_val(m3, 2, 1, 5)
    matrice.set_val(m3, 1, 0, 5)
    matrice.set_val(m3, 3, 3, 2)
    matrice.set_val(m3, 3, 0, 2)
    matrice.set_val(m3, 4, 4, 1)
    return m1, m2, m3

def test_max_matrice():
    m1, m2, m3 = creer_3_matrices()
    l1 = [(1, 2), (2, 0), (2, 1)]
    l1bis = [(2, 0)]
    l2 = [(1, 3)]
    l2bis = [(3, 1)]
    l3 = [(0, 4), (1, 0), (2, 1)]
    l3bis = [(3, 0), (3, 3)]
    res1 = matrice.max_matrice(m1)
    res1.sort()
    assert res1 == l1
    res2 = matrice.max_matrice(m2)
    res2.sort()
    assert res2 == l2
    res3 = matrice.max_matrice(m3)
    res3.sort()
    assert res3 == l3
    res1bis = matrice.max_matrice(m1, {(1, 2), (2, 1)})
    res1bis.sort()
    assert res1bis == l1bis
    res2bis = matrice.max_matrice(m2, {(1, 3)})
    res2bis.sort()
    assert res2bis == l2bis
    res3bis = matrice.max_matrice(m3, set(l3))
    res3bis.sort()
    assert res3bis == l3bis

def test_direction_max_voisin():
    m1, m2, m3 = creer_3_matrices()
    assert matrice.direction_max_voisin(m1,0,3)==['BG']
    res2=matrice.direction_max_voisin(m1,1,0)
    res2.sort()
    assert res2==['BB','BD']
    res3=matrice.direction_max_voisin(m1,2,2)
    res3.sort()
    assert res3==['GG','HH']
    res4=matrice.direction_max_voisin(m2,3,1)
    res4.sort()
    assert res4==['HD','HG','HH']
