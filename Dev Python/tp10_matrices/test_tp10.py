# pylint: disable=missing-function-docstring
"""les tests pour les fonctions des exercices 1 et 2 du TP10"""
import tp10 as tp10


#test remove all
def test_ra():
    listev = []
    tp10.remove_all(listev,1)
    assert listev == []
    liste1 = [1, 2, 3, 4]
    tp10.remove_all(liste1, 1)
    assert liste1 == [2, 3, 4]
    liste2 = [3, 2, 3, 3]
    tp10.remove_all(liste2, 3)
    assert liste2 == [2]
    liste3 = [1, 4, 1, 4]
    tp10.remove_all(liste3, 4)
    assert liste3 == [1, 1]


# ==================================
# TESTS pour l'exercice 1
# ==================================

def exemples_pokedex_v1():
    """renvoie un couple de deux exemples de pokedex en utilisant la modélisation 1"""
    pokedex_anakin = {
        ('Carmache', 'Dragon'), ('Carmache', 'Sol'),
        ('Colimucus', 'Dragon'), ('Palkia', 'Dragon'),
        ('Palkia', 'Eau')}
    pokedex_romain = {('Maraiste', 'Eau'), ('Maraiste', 'Sol'),
                      ('Racaillou', 'Sol'), ('Racaillou', 'Roche')}    
    return (pokedex_anakin, pokedex_romain)

def exemples_pokedex_v2():
    """renvoie un couple de deux exemples de pokedex en utilisant la modélisation 2"""
    pokedex_anakin = {
        'Carmache': {'Dragon','Sol'},
        'Colimucus': {'Dragon'},
        'Palkia': {'Dragon', 'Eau'}}
    pokedex_romain = {
        'Maraiste': {'Eau', 'Sol'},
        'Racaillou': {'Sol', 'Roche'}
    }
    return (pokedex_anakin, pokedex_romain)

def exemples_pokedex_v3():
    """renvoie un couple de deux exemples de pokedex en utilisant la modélisation 3"""
    pokedex_anakin = {
        'Dragon': {'Carmache','Colimucus', 'Palkia'},
        'Sol': {'Carmache'},
        'Eau': {'Palkia'}}
    pokedex_romain = {
        'Eau': {'Maraiste'},
        'Sol': {'Maraiste', 'Racaillou'},
        'Roche': {'Racaillou'}
    }
    return (pokedex_anakin, pokedex_romain)


# ==================================
# Exercice 1 : Modélisation n°1
# ==================================

def test_appartient_v1():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v1()
    assert not tp10.appartient_v1("Racaillou", pokedex_anakin)
    assert tp10.appartient_v1("Racaillou", pokedex_romain)


def test_toutes_les_attaques_v1():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v1()
    assert tp10.toutes_les_attaques_v1("Palkia", pokedex_anakin) == {'Eau', 'Dragon'}
    assert tp10.toutes_les_attaques_v1("Colimucus", pokedex_anakin) == {'Dragon'}


def test_nombre_de_v1():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v1()
    assert tp10.nombre_de_v1("Dragon", pokedex_anakin) == 3
    assert tp10.nombre_de_v1("Dragon", pokedex_romain) == 0

def test_attaque_preferee_v1():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v1()
    assert tp10.attaque_preferee_v1(pokedex_anakin) == "Dragon"
    assert tp10.attaque_preferee_v1(pokedex_romain) == "Sol"

# ==================================
# Exercice 1 : Modélisation n°2
# ==================================

def test_appartient_v2():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v2()
    assert not tp10.appartient_v2("Racaillou", pokedex_anakin)
    assert tp10.appartient_v2("Racaillou", pokedex_romain)


def test_toutes_les_attaques_v2():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v2()
    assert tp10.toutes_les_attaques_v2("Palkia", pokedex_anakin) == {'Eau', 'Dragon'}
    assert tp10.toutes_les_attaques_v2("Colimucus", pokedex_anakin) == {'Dragon'}


def test_nombre_de_v2():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v2()
    assert tp10.nombre_de_v2("Dragon", pokedex_anakin) == 3
    assert tp10.nombre_de_v2("Dragon", pokedex_romain) == 0

def test_attaque_preferee_v2():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v2()
    assert tp10.attaque_preferee_v2(pokedex_anakin) == "Dragon"
    assert tp10.attaque_preferee_v2(pokedex_romain) == "Sol"


# ==================================
# Exercice 1 : Modélisation n°3
# ==================================


def test_appartient_v3():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v3()
    assert not tp10.appartient_v3("Racaillou", pokedex_anakin)
    assert tp10.appartient_v3("Racaillou", pokedex_romain)


def test_toutes_les_attaques_v3():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v3()
    assert tp10.toutes_les_attaques_v3("Palkia", pokedex_anakin) == {'Eau', 'Dragon'}
    assert tp10.toutes_les_attaques_v3("Colimucus", pokedex_anakin) == {'Dragon'}


def test_nombre_de_v3():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v3()
    assert tp10.nombre_de_v3("Dragon", pokedex_anakin) == 3
    assert tp10.nombre_de_v3("Dragon", pokedex_romain) == 0

def test_attaque_preferee_v3():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v3()
    assert tp10.attaque_preferee_v3(pokedex_anakin) == "Dragon"
    assert tp10.attaque_preferee_v3(pokedex_romain) == "Sol"

# ==================================
# Exercice 1 : Transformations
# ==================================

def test_v1_to_v2():
    (pokedex_anakin_v1, pokedex_romain_v1) = exemples_pokedex_v1()
    (pokedex_anakin_v2, pokedex_romain_v2) = exemples_pokedex_v2()    
    assert tp10.v1_to_v2(pokedex_anakin_v1) == pokedex_anakin_v2
    assert tp10.v1_to_v2(pokedex_romain_v1) == pokedex_romain_v2

def test_v2_to_v3():
    (pokedex_anakin_v3, pokedex_romain_v3) = exemples_pokedex_v3()
    (pokedex_anakin_v2, pokedex_romain_v2) = exemples_pokedex_v2()    
    assert tp10.v2_to_v3(pokedex_anakin_v2) == pokedex_anakin_v3
    assert tp10.v2_to_v3(pokedex_romain_v2) == pokedex_romain_v3

# ==================================
# TESTS pour l'exercice 2
# ==================================

def test_extinction_immediate():
    ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
    ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
    assert tp10.extinction_immediate(ecosysteme_1, 'Lapin')
    assert tp10.extinction_immediate(ecosysteme_1, 'Requin')
    assert not tp10.extinction_immediate(ecosysteme_1, 'Mouton')
    assert not tp10.extinction_immediate(ecosysteme_1, 'Dragon')
    assert not tp10.extinction_immediate(ecosysteme_2, 'Poule')


def test_en_voie_disparition():
    ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
    ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
    ecosysteme_3 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard' }
    assert tp10.en_voie_disparition(ecosysteme_1, 'Lapin')
    assert tp10.en_voie_disparition(ecosysteme_1, 'Requin')
    assert tp10.en_voie_disparition(ecosysteme_1, 'Dragon')
    assert not tp10.en_voie_disparition(ecosysteme_1, 'Loup')
    assert not tp10.en_voie_disparition(ecosysteme_1, 'Mouton')
    assert not tp10.en_voie_disparition(ecosysteme_1, 'Herbe')
    assert not tp10.en_voie_disparition(ecosysteme_2, 'Poule')
    assert not tp10.en_voie_disparition(ecosysteme_2, 'Ours')
    assert not tp10.en_voie_disparition(ecosysteme_3, 'Poule')


def test_animaux_en_danger():
    ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
    ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
    eco = {1:2, 2:3, 3:4, 4:5, 5:17, 6:4, 7:6, 8:9, 9:10, 10:11, 11:8}
    assert tp10.animaux_en_danger(ecosysteme_1) =={'Lapin', 'Requin'}
    assert tp10.animaux_en_danger(ecosysteme_2) == set()
    assert tp10.animaux_en_danger(eco) == {5}


def test_especes_en_voie_disparition():
    ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
    ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
    eco = {1:2, 2:3, 3:4, 4:5, 5:17, 6:4, 7:6, 8:9, 9:10, 10:11, 11:8}
    assert tp10.especes_en_voie_disparition(ecosysteme_1) == {'Lapin', 'Requin', 'Lion', 'Dragon'}
    assert tp10.especes_en_voie_disparition(ecosysteme_2) == set()
    assert tp10.especes_en_voie_disparition(eco) == {1, 2, 3, 4, 5, 6, 7}