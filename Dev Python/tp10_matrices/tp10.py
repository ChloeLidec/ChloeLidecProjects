"""Init Dev : TP10"""

#focntion remove_all td10

def remove_all(liste,elt):
    """supprime ttes les occurence de elt dans la liste

    Args:
        liste (list): [description]
        elt (n importe quel type) l element a supprimer
    """    
    ind = 0
    while ind >= 0 and ind < len(liste):
        if liste[ind] == elt:
            liste.pop(ind)
            #pas de +1 car on fait sauter l'elt a cet 
            #indice donc décalage donc on doit reverifier
        else:
            ind += 1
# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for (pkm, _) in pokedex:
        if pkm == pokemon:
            return True
    return False

def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    types: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    types = set()
    for (pkm, type) in pokedex:
        if pkm == pokemon:
            types.add(type)#gere les doublons tout seul
    return types

def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    resultat = 0
    for (_, type) in pokedex:
        if type == attaque:
            resultat += 1
    return resultat


def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    pref = None
    maxi = 0
    for (_, type) in pokedex:
        if maxi < nombre_de_v1(type, pokedex):
            maxi = nombre_de_v1(type, pokedex)
            pref = type
    return pref


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    return pokemon in pokedex.keys()


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    return pokedex[pokemon]


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    resultat = 0
    for type in pokedex.values():
        if attaque in type:
            resultat += 1
    return resultat


def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    types = dict()
    maxi = 0
    pref = None
    for type in pokedex.values():
        for elt in type:
            if elt in types:
                types[elt] += 1
            else:
                types[elt] = 1
    for (attaque, nombre) in types.items():
        if maxi < nombre:
            maxi = nombre
            pref = attaque
    return pref
    

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for pkm in pokedex.values():
        if pokemon in pkm:
            return True
    return False

def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    resultat = set()
    for (type, pkm) in pokedex.items():
        if pokemon in pkm:
            resultat.add(type)
    return resultat


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    resultat = 0
    if attaque in pokedex:
        resultat = len(pokedex[attaque])
    return resultat

def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    pref = None
    maxi = 0
    for type in pokedex.keys():
        if len(pokedex[type]) > maxi:
            maxi = len(pokedex[type])
            pref = type
    return pref


# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    pokedex_v2 = dict()
    for (pokemon, type) in pokedex_v1:
        if pokemon not in pokedex_v2:
            pokedex_v2[pokemon] = set()
        pokedex_v2[pokemon].add(type)
    return pokedex_v2


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    pokedex_v3 = dict()
    for (pokemon, types) in pokedex_v2.items():
        for type in types:
            if type not in pokedex_v3:
                pokedex_v3[type] = set()
            pokedex_v3[type].add(pokemon)
    return pokedex_v3


# =====================================================================
# Exercice 2 : Ecosystème
# =====================================================================

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    if ecosysteme[animal] not in ecosysteme and ecosysteme[animal] is not None :
        return True
    return False


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    etu = animal
    disp = extinction_immediate(ecosysteme, animal)
    cpt = 0
    while not disp and cpt < len(ecosysteme):
        if ecosysteme[etu] is None:
            return False
        elif extinction_immediate(ecosysteme, etu):
            disp = True
        etu = ecosysteme[etu]
        cpt += 1
    return disp


def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    danger = set()
    for animal in ecosysteme.keys():
        if extinction_immediate(ecosysteme, animal):
            danger.add(animal)
    return danger


def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    voie_disp = set()
    for animal in ecosysteme.keys():
        if en_voie_disparition(ecosysteme, animal):
            voie_disp.add(animal)
    return voie_disp