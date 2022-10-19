"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module joueur.py
Module de gestion des joueurs
"""


def creer_joueur(id_joueur, nom_joueur, nb_points=0):
    """créer un nouveau joueur

    Args:
        id_joueur (int): l'identifiant du joueur (un entier de 1 à 4)
        nom_joueur (str): le nom du joueur
        nb_points (int, optional): le nombre de points du joueur. Defaults to 0.

    Returns:
        dict: le joueur
    """
    joueur = {"ID": id_joueur, "nom": nom_joueur, "points": nb_points}
    return joueur


def get_id(joueur):
    """retourne l'identifiant du joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: l'identifiant du joueur
    """
    return joueur["ID"]


def get_nom(joueur):
    """retourne le nom du joueur

    Args:
        joueur (dict): un joueur

    Returns:
        str: nom du joueur
    """
    return joueur["nom"]


def get_points(joueur):
    """retourne le nombre de points du joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: le nombre de points du joueur
    """
    return joueur["points"]


def ajouter_points(joueur, points):
    """ajoute des points au joueur

    Args:
        joueur (dict): un joueur
        points (int): le nombre de points à ajouter

    Returns:
        int: le nombre de points du joueur
    """
    joueur["points"] += points
    return joueur["points"]


def id_joueur_droite(joueur):
    """retourne l'identifiant du joueur à droite d'un joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: l'identifiant du joueur de droite
    """
    if (get_id(joueur) + 1) % 4 == 0:
        #si on arrive a un reste de 0 c'est que l'on est a 4 pour l'id
        return 4
    return (get_id(joueur) + 1) % 4


def id_joueur_gauche(joueur):
    """retourne l'identifiant du joueur à gauche d'un joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: l'identifiant du joueur de gauche
    """
    if (get_id(joueur) + 3) % 4 == 0:
        #si on arrive a un reste de 0 c'est que l'on est a 4 pour l'id
        return 4
    return (get_id(joueur) + 3) % 4


def id_joueur_haut(joueur):
    """retourne l'identifiant du joueur au dessus d'un joueur

    Args:
        joueur (dict): un joueur

    Returns:
        int: l'identifiant du joueur du haut
    """
    if (get_id(joueur) + 2) % 4 == 0:
        #si on arrive a un reste de 0 c'est que l'on est a 4 pour l'id
        return 4
    return (get_id(joueur) + 2) % 4
