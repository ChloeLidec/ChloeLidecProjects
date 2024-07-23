def lecture_parametre_def(id_recherche):
    """Lis le fichier par_def.txt et retourne
    la valeur correspondant à l'id recherché
    Si l'id n'est pas trouvé, retourne None
    Args:
        id_recherche : id du paramètre à rechercher
    """
    fichier = open("../static/donnees/par_def.txt", "r")
    for ligne in fichier:
        if ligne[0] != "#":
            id, valeur = ligne.split(":")
            if id == id_recherche:
                fichier.close()
                return valeur.strip()
    fichier.close()
    return None