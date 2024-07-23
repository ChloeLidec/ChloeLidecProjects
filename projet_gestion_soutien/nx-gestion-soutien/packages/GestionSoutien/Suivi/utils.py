from django.db.models import Avg
from GestionSoutien.models import Eleve, Matiere,ParticiperSoutienEleve,Soutien
from QCM.models import ResultatQCM,QCM

def get_nb_part_soutien(numetu: str):
    """
    La fonction `get_nb_part_soutien` renvoie le nombre d'instances de `ParticiperSoutienEleve` où le
    champ `num_etu` est égal à l'entrée `numetu`.
    
    :param numetu: Le paramètre « numetu » est une chaîne représentant le numéro d'identification de
    l'étudiant
    :type numetu: str
    :return: le nombre d'objets ParticiperSoutienEleve qui ont un attribut num_etu égal au paramètre
    numetu fourni.
    """
    return ParticiperSoutienEleve.objects.filter(num_etu=numetu).count()

def get_moyenne_generale(numetu):
    """
    La fonction "get_moyenne_generale" calcule et renvoie la note moyenne d'un élève dans un QCM.
    
    :param numetu: Le paramètre "numetu" est le numéro ou identifiant de l'étudiant. Il est utilisé pour
    filtrer les objets ResultatQCM et calculer la note moyenne (note) pour cet étudiant spécifique
    :return: la moyenne du champ "note" des objets ResultatQCM qui ont une valeur "num_etu"
    correspondante. La moyenne est arrondie à 2 décimales.
    """
    return round(ResultatQCM.objects.filter(num_etu=numetu).aggregate(Avg("note", default=0))['note__avg'],2)

def get_dernier_soutien(id_semaine, numetu):
    """
    La fonction `get_dernier_soutien` récupère la dernière session de support pour une semaine et un
    élève donnés, et si elle n'existe pas, elle récupère la session de support de la semaine précédente.
    
    :param id_semaine: L'identifiant de la semaine pour laquelle vous souhaitez obtenir le dernier
    support
    :param numetu: Le paramètre « numetu » représente le numéro d'identification de l'étudiant
    :return: une instance du modèle ParticiperSoutienEleve qui correspond aux id_soutien et num_etu
    donnés.
    """
    #if soutien semaine fait on recup sinon on prend la semaine derniere
    #si pas de resultat traité auto par django
    soutien = Soutien.objects.filter(id_semaine=id_semaine).first()
    if soutien is None:
        soutien = Soutien.objects.filter(id_semaine=(id_semaine - 1)).first()
    return ParticiperSoutienEleve.objects.filter(id_soutien=soutien,num_etu=numetu).first()


def get_infos_etudiants(id_semaine, groupes_select):
    """
    La fonction `get_infos_etudiants` récupère les informations sur les étudiants en fonction des
    groupes sélectionnés et de l'ID de la semaine.
    
    :param id_semaine: Le paramètre "id_semaine" représente l'ID d'une semaine spécifique. Il est
    utilisé pour récupérer les informations relatives à la dernière séance de soutien suivie par chaque
    étudiant au cours de cette semaine
    :param groupes_select: Le paramètre "groupes_select" est une liste d'identifiants de groupe. Il est
    utilisé pour filtrer les étudiants en fonction de leur appartenance à un groupe. Si la liste est
    vide, cela signifie que tous les étudiants doivent être inclus dans le résultat. Si la liste n'est
    pas vide, seuls les étudiants appartenant à l'un des
    :return: une liste de dictionnaires. Chaque dictionnaire contient des informations sur un étudiant,
    notamment son nom, sa participation totale aux sessions de support, sa note moyenne et la date de sa
    dernière session de support.
    """
    if groupes_select == []:
        etus = Eleve.objects.all()
    else:
        etus = Eleve.objects.filter(groupe__in=groupes_select)
        
    resultat = []
    for etu in etus:
        res_eleve = {}
        res_eleve['etu'] = etu
        res_eleve['tot_part'] = get_nb_part_soutien(etu.num_etu)
        res_eleve['moy_gen'] = get_moyenne_generale(etu.num_etu)
        res_eleve['dern_sout'] = get_dernier_soutien(id_semaine, etu.num_etu)
        resultat.append(res_eleve)
    return resultat

def get_graphe(num_etu, id_semaine, semaines):
    """
    La fonction `get_graphe` récupère les données de la base de données et renvoie un dictionnaire
    contenant les résultats des QCM pour un élève et une semaine donnés, ainsi qu'une liste des noms des
    matières.
    
    :param num_etu: Le paramètre "num_etu" représente le numéro d'étudiant ou l'identifiant d'un
    étudiant particulier
    :param id_semaine: Le paramètre `id_semaine` représente l'ID d'une semaine spécifique. Il est
    utilisé pour filtrer les données et récupérer les informations relatives à cette semaine
    particulière
    :param semaines: Le paramètre "semaines" est une liste d'objets représentant des semaines. Chaque
    objet possède un attribut "id_semaine" qui représente l'ID de la semaine
    :return: un dictionnaire `data_dict` et une liste `matieres_noms`.
    """
    data_dict = {}

    matieres = Matiere.objects.all()
    matieres_noms = list(Matiere.objects.all().values_list('nom_matiere', flat=True))

    cpt = 0
    while id_semaine > semaines[cpt].id_semaine:
        res_sem = {}

        for matiere in matieres:
            qcm = QCM.objects.filter(id_semaine=semaines[cpt].id_semaine, id_matiere=matiere.id_matiere).first()

            if qcm is not None:
                try:
                    note = ResultatQCM.objects.filter(id_qcm=qcm.id_qcm, num_etu=num_etu).first().note
                    res_sem[matiere.nom_matiere] = note
                except:
                    # Si pas de note, n'ajoutez pas au dictionnaire
                    pass

        data_dict[semaines[cpt].id_semaine] = res_sem
        cpt += 1

    return data_dict, matieres_noms



def get_res_qcms_soutien(numetu,id_semaine):
    pass

def get_tableau_recap(id_semaine,numetu):
    pass