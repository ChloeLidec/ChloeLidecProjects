"""
             Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module jeu.py
"""

import random
import plateau
import protection
import matrice


def creer_jeu(liste_joueurs, taille_plateau=5, resistance_serveur=4, resistance_pc=5,
              resistance_protection=2, humain=False, nb_tours_max=-1):
    """Créer un nouveau jeu avec 4 joueurs

    Args:
        liste_joueurs (list): la liste des noms de joueur
        taille_plateau (int, optional): le coté du plateau. Defaults to 5.
        resistance_serveur (int, optional): la resistance du serveur. Defaults to 4.
        resistance_pc (int, optional): la resistance des PC. Defaults to 5.
        resistance_protection (int, optional): la resistance des protections. Defaults to 2.
        humain (bool, optional): indique si le joueur 1 est humain. Defaults to False.
        nb_tours_max (int, optional): indique le nombre de tours de la partie
                                      (-1 pour indiquer pas de limite). Defaults -1.

    Returns:
        dict: le jeu
    """
    ...


def get_taille_plateau(jeu):
    """Retourne la taille des plateau

    Args:
        jeu (dict): un jeu

    Returns:
        int: la taille des plateau
    """
    ...

def get_plateau(jeu, id_joueur):
    """ retour le plateau de joueur indenfié par id_joueur

    Args:
        jeu (dict): un jeu
        id_joueur (int): l'identifiant du joueur (entre 1 et 4)

    Returns:
        dict: le plateau du joueur
    """
    ...


def est_fini(jeu):
    """indique si la partie est terminée

    Args:
        jeu (dict): un jeu

    Returns:
        bool: un booléen à True si au moins trois joueur sont éliminés ou
              que le nombre de tours max est atteint
    """
    ...


def get_num_tour(jeu):
    """retourne le numéro du tour en cours

    Args:
        jeu (dict): un jeu

    Returns:
        int: le numéro du tour
    """
    ...


def echange_trojans(jeu):
    """Effectue les échanges de trojans entre les joueurs (des sorties vers les entrées)

    Args:
        jeu (dict): un jeu
    """
    ...


def diriger_trojan(jeu):
    """Applique la protection DONNEES_PERSONNELLES sur les quatre plateaux

    Args:
        jeu (dict): un jeu
    """
    ...


def phase1(jeu):
    """Effectue les déplacements des trojans sur les 4 plateaux

    Args:
        jeu ((dict): un jeu
    """
    ...


def phase2(jeu):
    """Finalise les déplacements des trojans sur les 4 plateaux.
       cette fonction doit augementer le numero du tour de jeu de 1

    Args:
        jeu ((dict): un jeu
    """
    ...


def joueur_humain():
    """

    Returns:
        str: une chaine de caractères indiquant les ordres donnés par la personne
    """
    print("indiquez le direction de votre avatar")
    res = input()

    rep = input(
        "Souhaitez vous (P)oser une protection ou (A)ttaquer les adversaires? (P/A)")
    res += rep
    if rep == 'P':
        print(
            "indiquez le type de protection [O"+str(protection.PAS_DE_PROTECTION)+"]")
        type_protection = input()
        try:
            type_protection = int(type_protection)
        except:
            type_protection = protection.PAS_DE_PROTECTION
        if type_protection != protection.PAS_DE_PROTECTION:
            print("indiquez la position de votre protection")
            ligne = input("numero de la ligne ")
            colonne = input("numero de la colonne")
            try:
                ligne = int(ligne)
                colonne = int(colonne)
            except:
                type_protection = protection.PAS_DE_PROTECTION
        res += str(type_protection)+str(ligne)+str(colonne)
    elif rep == 'A':
        for direction in "GHD":
            print("indiquez le type de virus à envoyer vers "+direction)
            try:
                type_vir = int(input())
            except:
                type_vir = -1
            res += direction+str(type_vir)
    return res


def joueur_aleatoire(le_plateau):
    """produit des ordres aléatoires

    Args:
        le_plateau (dict): un plateau

    Returns:
        str: une chaine de caractères donnant des ordres compatibles mais aléatoires
        Les ordres sont donnés sous la forme
        d'une chaine de caractères dont les deux premiers indique le déplacement de l'avatar
        le troisième caractère est
        soit un A pour une attaque
        soit un P pour une protection
        En cas d'attaque, les caractères suivants sont GxHyDz où
                    x y et z sont des chiffres entre 0 et 4 indiquant le numéro de la
                             ligne ou de la colonne où sera envoyé le trojan
        En cas de pose d'une protection les caractère suivants seront trois chiffre tlc où
                    t est le type de la protection
                    l la ligne où poser la protection
                    c la colonne où poser la protection
    """
    # choix du déplacement de l'avatar
    res = random.choice(list(plateau.DIRECTIONS_AVATAR))
    taille = plateau.get_taille(le_plateau)
    # choix entre poser une protection ou attaquer les adversaires
    if random.randint(0, 1) == 0:
        ligne = random.randint(0, taille-1)
        colonne = random.randint(0, taille-1)
        ind_protect = random.randint(0, protection.PAS_DE_PROTECTION-1)
        if ligne != taille//2 or colonne != taille//2:
            res += 'P'+str(ind_protect)+str(ligne)+str(colonne)
    else:  # on attaque les adversaires
        res += 'A'
        les_voisins = ['G', 'H', 'D']
        for direct in les_voisins:
            res += direct+str(random.randint(0, 4))
    return res



def actions_joueur(jeu):
    """Récolte et exécute les actions choisies par chacun des joueurs

    Args:
        jeu (dict): un jeu
    """
    for id_joueur in range(1, 5):
        if plateau.a_perdu(jeu[id_joueur]):
            continue
        if id_joueur == 1 and jeu['humain']:
            ordres = joueur_humain()
        else:
            ordres = joueur_aleatoire(jeu[id_joueur])
        
        plateau.executer_ordres(jeu[id_joueur], ordres)
    echange_trojans(jeu)


