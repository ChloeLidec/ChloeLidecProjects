"""
              Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module case.py
    ce module gère les cases du plateau
"""
import trojan
import protection

AVATAR = 1

def creer_case(fleche, la_protection, serveur, liste_trojans):
    """créer une case du plateau

    Args:
        fleche(str): une des quatre directions 'H' 'B' 'G' 'D' ou '' si pas de flèche sur la case
        la_protection(dict): l'objet de protection posé sur la case (None si pas d'objet)
        serveur(dict): le serveur posé sur la case (None si pas de serveur)
        liste_trojans(list): la liste des trojans présents sur le case
    Returns:
        dict: la représentation d'une case
    """
    case = {"fleche": fleche, "protection": la_protection,
            "serveur": serveur, "trojans_presents": liste_trojans,
            "trojans_entrants": [], "avatar": None}
            #on met d'avance une liste vide de trojans entrants ainsi qu'un avatar à None
            #pour pouvoir gérer ensuite les cas plus facilement
    return case

def get_fleche(case):
    """retourne la direction de la flèche de la case

    Args:
        case (dict): une case

    Returns:
        str: la direction 'H', 'B', 'G', 'D' ou '' si pas de flèche sur la case
    """
    return case["fleche"]


def get_protection(case):
    """retourne l'objet de protection qui se trouve sur la case

    Args:
        case (dict): une case

    Returns:
        dict: l'objet de protection présent sur la case (None si pas d'objet)
    """
    return case["protection"]


def get_serveur(case):
    """retourne le serveur qui se trouve sur la case

    Args:
        case (dict): une case

    Returns:
        dict: le serveur présent sur la case (None si pas d'objet)
    """
    return case["serveur"]


def get_trojans(case):
    """retourne la liste des trojans présents sur la case

    Args:
        case (dict): une case

    Returns:
        list: la liste des trojans présents sur la case
    """
    return case["trojans_presents"]


def get_trojans_entrants(case):
    """retourne la liste des trojans qui vont arriver sur la case

    Args:
        case (dict): une case

    Returns:
        list: la liste des trojans qui vont arriver sur la case
    """
    return case["trojans_entrants"]


def set_fleche(case, direction):
    """affecte une direction à la case

    Args:
        case (dict): une case
        direction (dict): 'H', 'B', 'G', 'D' ou '' si pas de flèche sur la case
    """
    case["fleche"] = direction


def set_serveur(case, serveur):
    """affecte un serveur à la case

    Args:
        case (dict): une case
        serveur (str): le serveur
    """
    case["serveur"] = serveur


def set_protection(case, la_protection):
    """affecte une protection à la case

    Args:
        case (dict): une case
        la_protection (dict): la protection
    """
    case["protection"] = la_protection


def set_les_trojans(case, trojans_presents, trojans_entrants):
    """fixe la liste des trojans présents et les trojans arrivant sur la case

    Args:
        case (dict): une case
        trojans_presents (list): une liste de trojans
        trojans_entrants ([type]): une liste de trojans
    """
    case["trojans_presents"] = trojans_presents
    case["trojans_entrants"] = trojans_entrants


def ajouter_trojan(case, un_trojan):
    """ajouter un nouveau trojan arrivant à une case

    Args:
        case (dict): la case
        un_trojan (dict): le trojan à ajouter
    """
    case["trojans_entrants"].append(un_trojan)

def reinit_trojans_entrants(case):
    """reinitialise la liste des trojans entrants à la liste vide

    Args:
        case (dict): la case
    """
    case["trojans_entrants"] = []

def mettre_a_jour_case(case):
    """met les trojans arrivants comme présents et réinitialise les trojans arrivants
       change la direction du trojan si nécessaire (si la case comporte une flèche)
       la fonction retourne un dictionnaire qui indique pour chaque numéro de joueur
       le nombre de trojans qui vient d'arriver sur la case.
       La fonction enlève une resistance à protection qui se trouve sur elle et la détruit si
       la protection est arrivée à 0.

    Args:
        case (dict): la case

    Returns:
        dict: un dictionnaire dont les clés sont les numéros de joueur et les valeurs
              le nombre de trojans arrivés sur la case pour ce joueur
    """
    dico_joueur = dict()
    for trojan_arr in get_trojans_entrants(case):
        #ajout du tro aux troj presents; redirection si il y a fleche
        #et création du dico de freq des joueurs
        get_trojans(case).append(trojan_arr)
        if get_fleche(case) != '':
            trojan.set_direction(trojan_arr, get_fleche(case))
        if trojan.get_createur(trojan_arr) not in dico_joueur.keys():
            dico_joueur[trojan.get_createur(trojan_arr)] = 0
        dico_joueur[trojan.get_createur(trojan_arr)] += 1
    reinit_trojans_entrants(case)
    protection.enlever_resistance(get_protection(case))
    if protection.get_resistance(get_protection(case)) == 0:
        case["protection"] = None
    return dico_joueur

def poser_avatar(case):
    """pose l'avatar sur cette case et élimines les trojans présents sur la case.
       la fonction indique combien de trojans ont été éliminés

    Args:
        case (dict): une case

    Returns:
        dict: un dictionnaire dont les clés sont les numéros de joueur et les valeurs le nombre
        de trojans éliminés pour ce joueur.
    """
    dico_joueur = {1: 0, 2: 0, 3: 0, 4: 0}
    while len(get_trojans(case)) > 0:
        trojan_act = get_trojans(case).pop(-1)
        dico_joueur[trojan.get_createur(trojan_act)] += 1
    case["avatar"] = AVATAR # utilisation d'une variable globale pour gerer si
    #changement de valeur
    return dico_joueur


def enlever_avatar(case):
    """enlève l'avatar de la case

    Args:
        case (dict): une case
    """
    case["avatar"] = None


def contient_avatar(case):
    """vérifie si l'avatar se trouve sur la case

    Args:
        case (dict): une case

    Returns:
        bool: True si l'avatar est sur la case et False sinon[type]: [description]
    """
    return case["avatar"] is not None #True si il y a avatar False si non
