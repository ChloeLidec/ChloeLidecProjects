"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module matrice.py
    Ce module de gestion des matrices
"""


def creer_matrice(nb_lig, nb_col, val_defaut=None):
    """créer une matrice contenant nb_lig lignes et nb_col colonnes avec
       pour valeur par défaut val_defaut

    Args:
        nb_lig (int): un entier strictement positif
        nb_col (int): un entier strictement positif
        val_defaut (Any, optional): La valeur par défaut des éléments de la matrice.
                                    Defaults to None.
    Returns:
        dict: la matrice
    """
    mat = []
    ligne = []
    for _ in range(nb_lig):
        for _ in range(nb_col):
            ligne.append(val_defaut)
        mat.append(ligne)
        ligne = []
    return mat


def get_nb_lignes(matrice):
    """retourne le nombre de lignes de la matrice

    Args:
        matrice (dict): une matrice

    Returns:
        int: le nombre de lignes de la matrice
    """
    return len(matrice)


def get_nb_colonnes(matrice):
    """retourne le nombre de colonnes de la matrice

    Args:
        matrice (dict): une matrice

    Returns:
        int: le nombre de colonnes de la matrice
    """
    return len(matrice[0])


def get_val(matrice, lig, col):
    """retourne la valeur en lig, col de la matrice

    Args:
        matrice (dict): une matrice
        lig (int): numéro de la ligne (en commençant par 0)
        col (int): numéro de la colonne (en commençant par 0)

    Returns:
        Any: la valeur en lig, col de la matrice
    """
    return matrice[lig][col]


def set_val(matrice, lig, col, val):
    """stocke la valeur val en lig, col de la matrice

    Args:
        matrice (dict): une matrice
        lig (int): numéro de la ligne (en commençant par 0)
        col (int): numéro de la colonne (en commençant par 0)
        val (Any): la valeur à stocker
    """
    matrice[lig][col] = val

def max_matrice(matrice, interdits=None):
    """retourne la liste des coordonnées des cases contenant la valeur la plus grande de la matrice
        Ces case ne doivent pas être parmi les interdits.

    Args:
        matrice (dict): une matrice
        interdits (set): un ensemble de tuples (ligne,colonne) de case interdites. Defaults to None

    Returns:
        list: la liste des coordonnées de cases de valeur maximale dans la matrice
        (hors cases interdites)
    """
    val_max = None
    liste_coord = []
    for ligne in range(get_nb_lignes(matrice)):
        for colonne in range(get_nb_colonnes(matrice)):
            if val_max is None or get_val(matrice, ligne, colonne) > val_max:
                if interdits is None or (ligne, colonne) not in interdits:
                    val_max = get_val(matrice, ligne, colonne)
                    liste_coord = [(ligne, colonne)]
            elif get_val(matrice, ligne, colonne) == val_max:
                if interdits is None or (ligne, colonne) not in interdits:
                    liste_coord.append((ligne, colonne))
    return liste_coord

DICO_DIR = {(-1, -1): 'HD', (-1, 0): 'HH', (-1, 1): 'HG', (0, -1): 'GG',
            (0, 1): 'DD', (1, -1): 'BG', (1, 0): 'BB', (1, 1): 'BD', (0, 0): 'BB'}

def direction_max_voisin(matrice, ligne, colonne):
    """retourne la liste des directions qui permettent d'aller vers la case voisine de
       la case (ligne,colonne) la plus grande. Le résultat doit aussi contenir la
       direction qui permet de se rapprocher du milieu de la matrice
       si ligne,colonne n'est pas le milieu de la matrice

    Args:
        matrice (dict): une matrice
        ligne (int): le numéro de la ligne de la case considérée
        colonne (int): le numéro de la colonne de la case considérée

    Returns:
        str: deux lettres indiquant la direction DD -> droite , HD -> Haut Droite,
                                                 HH -> Haut, HG -> Haut gauche,
                                                 GG -> Gauche, BG -> Bas Gauche, BB -> Bas
    """
    voisins = []
    milieu = (get_nb_lignes(matrice) // 2, get_nb_colonnes(matrice) // 2)
    for lig in range(ligne - 1, ligne + 2):
        for col in range(colonne - 1, colonne + 2):
            if (lig, col) != (ligne, colonne):
                voisins.append((lig, col))
    val_max = None
    directions = []
    for (li_vois, co_vois) in voisins:
        if val_max is None or val_max < get_val(matrice, li_vois, co_vois):
            val_max = get_val(matrice, li_vois, co_vois)
            directions = [(DICO_DIR[(li_vois - ligne, co_vois - colonne)])]
        elif val_max == get_val(matrice, li_vois, co_vois):
            directions.append((DICO_DIR[(li_vois - ligne, co_vois - colonne)]))
    if milieu in voisins:
        (mil_ligne, mil_colonne) = milieu
        directions.append((DICO_DIR[(mil_ligne - ligne, mil_colonne - colonne)]))
    return directions
