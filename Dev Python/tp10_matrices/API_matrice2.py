""" Matrices : API n 2 """


def construire_matrice(nb_lignes, nb_colonnes, valeur_par_defaut = 0):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.
        si aucune valeur par défaut en paramètre on met 0
    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    mat = []
    ligne = []
    for lig in range(nb_lignes):
        for col in range(nb_colonnes):
            ligne.append(valeur_par_defaut)
        mat.append(ligne)
        ligne = []
    return mat

def set_val(matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    matrice[ligne][colonne] = nouvelle_valeur


def get_nb_lignes(matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return len(matrice)


def get_nb_colonnes(matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return len(matrice[0])


def get_val(matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    return matrice[ligne][colonne]

# Fonctions pour l'affichage 

def affiche_ligne_separatrice(matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(matrice)
    nb_lignes = get_nb_lignes(matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

def get_ligne(matrice,ligne):
    """renvoie la liste des valeurs de la ligne

    Args:
        matrice une matrice
        ligne int la ligne demandée

    Returns:
        list: liste contenant les valeurs de la ligne
    """
    liste = []
    for col in range(get_nb_colonnes(matrice)):
        liste.append(get_val(matrice, ligne, col))
    return liste

def get_colonne(matrice,colonne):
    """renvoie la liste des valeurs de la colonne

    Args:
        matrice une matrice
        colonne int la colonne demandée

    Returns:
        list: liste contenant les valeurs de la colonne
    """
    liste = []
    for ligne in range(get_nb_lignes(matrice)):
        liste.append(get_val(matrice, ligne, colonne))
    return liste


def charge_matrice_str(nom_fichier):
    """permet créer une matrice de str à partir d'un fichier CSV.

    Args:
        nom_fichier (str): le nom d'un fichier CSV (séparateur  ',')

    Returns:
        une matrice de str
    """
    fic=open(nom_fichier,"r")
    fst_l = fic.readline()
    fst_l = fst_l.split(",")
    mat = construire_matrice(int(fst_l[0]), int(fst_l[1]), None)
    lig = 0
    for ligne in fic:
        l_champs=ligne.split(",")
        print(l_champs)
        col = 0
        l_champs = l_champs[:len(l_champs) - 1]
        print(l_champs, "indice ligne ", lig)
        for val in l_champs:
            if val.isdecimal():
                set_val(mat, lig, col, int(val))
                col += 1
            else:
                set_val(mat, lig, col, val)
                col += 1
        lig +=1
    fic.close()
    return mat
#print(charge_matrice_str("test.csv"))

def sauve_matrice(matrice, nom_fichier):
    """permet sauvegarder une matrice dans un fichier CSV.
    Attention, avec cette fonction, on perd l'information sur le type des éléments

    Args:
        matrice : une matrice
        nom_fichier (str): le nom du fichier CSV que l'on veut créer (écraser)

    Returns:
        None
    """
    
    fic=open(nom_fichier,"w")
    fic.write(str(get_nb_lignes(matrice)) + "," + str(get_nb_colonnes(matrice)) + "\n")
    for nbl in range(get_nb_lignes(matrice)):
        for nbc in range(get_nb_colonnes(matrice)):
            fic.write(str(get_val(matrice, nbl, nbc)) + ",")
        fic.write("\n")
    fic.close()
#sauve_matrice((3, 4, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]),"test.csv")

def get_diagonale_principale(matrice):
    """renvoie la diagonale princiaple (haut gauche vers bas droite)
    d'une matrice carree

    Args:
        matrice une matrice carree
    returns:
        list la liste des valeurs de la diagonale
    """
    diago = []
    ind_ij = 0
    col = get_nb_colonnes(matrice)#matr carree donc ca ira pas plus loin que ca
    while ind_ij < col:
        val = get_val(matrice, ind_ij, ind_ij)
        diago.append(val)
        ind_ij += 1
    return diago

def get_diagonale_secondaire(matrice):
    """renvoie la diagonale secondaire(haut droite vers bas gauche)
    d'une matrice carree

    Args:
        matrice une matrice carree
    returns:
        list la liste des valeurs de la diagonale
    """
    diago = []
    ind_i = 0#ind ligne
    ind_j = get_nb_colonnes(matrice) - 1#-1 pour avoir le dernier indice
    while ind_j >= 0:
        val = get_val(matrice, ind_i, ind_j)
        diago.append(val)
        ind_i += 1
        ind_j -= 1
    return diago

def transpose(matrice):
    """renvoie la transposée d'une matrice
    Args:
        matrice une matrice
    returns:
        la transposee
    """
    lig = get_nb_lignes(matrice)
    col = get_nb_colonnes(matrice)
    tr = construire_matrice(col, lig, None)
    for ind_i in range(col):
        for ind_j in range(lig):
            val = get_val(matrice, ind_j, ind_i)#sur la premiere mat
            set_val(tr, ind_i, ind_j, val)#nvlle mat
    return tr

def is_triangulaire_inf(matrice):
    """renvoie si la matrice est triangualire inf
    Args:
        matrice une matrice
    returns:
        bool
    """
    lig = get_nb_lignes(matrice)
    col = get_nb_colonnes(matrice)
    for ind_i in range(lig):
        for ind_j in range(ind_i + 1, col):
            if get_val(matrice, ind_i, ind_j) != 0:
                return False
    return True

def is_triangulaire_sup(matrice):
    """renvoie si la matrice est triangualire inf
    Args:
        matrice une matrice
    returns:
        bool
    """
    lig = get_nb_lignes(matrice)
    col = get_nb_colonnes(matrice)
    for ind_i in range(col):
        for ind_j in range(ind_i +1, lig):
            if get_val(matrice, ind_j, ind_i) != 0:
                return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    """renvoie la sous matrice de matrice qui part de ligne colonne

    Args:
        matrice (matrice)
        ligne (int): ligne de debut
        colonne (int): colonne de debut
        hauteur (int): hauteur de la nouvelle matrice
        largeur (int): largeur de la nouvelle matrice

    Returns:
        bloc_mat: la sous matrice
    """
    bloc_mat = construire_matrice(hauteur, largeur, None)
    lig = 0
    col = 0
    for ind_i in range(ligne, ligne + hauteur):
        for ind_j in range(colonne, colonne + largeur):
            valeur = get_val(matrice, ind_i, ind_j)
            set_val(bloc_mat, lig, col, valeur)
            col += 1
        col = 0
        lig += 1
    return bloc_mat

def somme(m1, m2):
    """renvoie la matrice de la somme de m1 et m2

    Args:
        m1 (matrice): [description]
        m2 (matrice): [description]

    Returns:
        [matrice]: [description]
    """
    mat_som = construire_matrice(get_nb_lignes(m1), get_nb_colonnes(m1), None)
    for ind_i in range(get_nb_lignes(mat_som)):
        for ind_j in range(get_nb_colonnes(mat_som)):
            val1 = get_val(m1, ind_i, ind_j)
            val2 = get_val(m2, ind_i, ind_j)
            set_val(mat_som, ind_i, ind_j, val1 + val2)
    return mat_som

def produit(m1, m2):
    """renvoie le produit de m1 par m2

    Args:
        m1 et m2 des matrices

    Returns:
        [matrice]"""
   
    mat_pro = construire_matrice(get_nb_lignes(m1), get_nb_colonnes(m2))
    val = 0
    for ind_i in range(get_nb_lignes(mat_pro)): #parcours de lignes de produit
        for ind_j in range(get_nb_colonnes(mat_pro)): # col produit
            for ind_m1 in range(get_nb_colonnes(m1)):
                val += get_val(m1, ind_i, ind_m1) * get_val(m2, ind_m1, ind_j)
                #on prend toutes les valeurs de la lig m1 et col m2 et on add
            set_val(mat_pro, ind_i, ind_j, val)
            val = 0
    return mat_pro
