"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module equipement.py
    ce module gère les équipements ordinateurs et serveurs
"""

SERVEUR = 0
ORDINATEUR = 1


def creer_equipement(type_e, resistance):
    """créer un équipement avec resistance

    Args:
        type_e (int): type de l'équipement
        resistance (int): le nombre d'attaques nécessaires pour détruire l'équipement

    Returns:
        dict: une structure représentant l'équipement
    """
    equipement = {"type": type_e, "resistance": resistance}
    return equipement


def attaque(equipement):
    """Enlève une protection à l'équipement

    Args:
        equipement (dict): un équipement
    """
    equipement["resistance"] -= 1
    return get_resistance(equipement)

def est_detruit(equipement):
    """Indique si l'équipement est détruit (n'a plus de resistance)

    Args:
        equipement (dict): un équipement

    Returns:
        bool: True si l'équipement n'a plus de résistance et False sinon
    """
    if equipement["resistance"] <= 0:
        #inferieur ou égal comme ca on gère les cas ou enlève plus que 1
        return True
    return False


def get_resistance(equipement):
    """retourne la resistance de l'équipement

    Args:
        equipement (dict): un équipement

    Returns:
        int: la resistance restante de l'équipement
    """
    if equipement["resistance"] > 0:
        return equipement["resistance"]
    return 0

def get_type(equipement):
    """retourne le type de l'équipement

    Args:
        equipement (dict): un équipement

    Returns:
        int: le type de l'équipement
    """
    return equipement["type"]


def set_resistance(equipement, resistance):
    """positionne la résistance d'un équipement à une valeur donnée

    Args:
        equipement (dict): un équipement
        resistance (int): la résistance restante de l'équipement
    """
    equipement["resistance"] = resistance
