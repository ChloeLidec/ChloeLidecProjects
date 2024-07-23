import datetime
from .models import EnseigneMatiere, ParticiperSoutienProfesseur, Professeur, Semaine, Eleve,Matiere,Soutien
from django.db.models import Avg
from QCM.models import QCM,ResultatQCM
from QCM.utils import get_moyenne_generale,get_moyenne_groupe
from Sondages.models import RepSondage,Sondage

def get_semaine_actuelle():
    """
    La fonction "get_semaine_actuelle" renvoie la semaine en cours en fonction des dates de début et de
    fin stockées dans le modèle "Semaine".
    :return: l'objet semaine en cours du modèle Semaine.
    """
    # __lte : <=
    # __gte : >=
    sem = Semaine.objects.filter(date_debut__lte=datetime.date.today(), date_fin__gte=datetime.date.today())
    if sem.count == 0:
        return None
    return sem.first()


def get_matieres_qcms(id_semaine):
    """
    La fonction `get_matieres_qcms` récupère les noms des sujets pour les QCM d'une semaine donnée.
    
    :param id_semaine: Le paramètre "id_semaine" est l'ID d'une semaine spécifique. Il permet de filtrer
    les objets QCM (Questionnaire à Choix Multiples) en fonction de la semaine à laquelle ils
    appartiennent
    :return: une liste de noms de matières pour les QCM (Questionnaire à Choix Multiples) qui ont
    l'id_semaine (week id) donné.
    """
    matieres = []
    qcms = QCM.objects.filter(id_semaine=id_semaine).order_by('id_matiere')
    matieres = [qcm.id_matiere.nom_matiere for qcm in qcms]
    return matieres

def get_matieres_soutien(id_semaine):
    """
    La fonction `get_matieres_soutien` renvoie une liste de noms de sujets uniques pour une semaine
    donnée.
    
    :param id_semaine: Le paramètre "id_semaine" est l'ID d'une semaine spécifique. Il permet de filtrer
    les objets supports en fonction de la semaine à laquelle ils appartiennent
    :return: une liste de noms de matières uniques pour les supports qui ont l'id_semaine donné.
    """
    matieres = []
    soutiens = Soutien.objects.filter(id_semaine=id_semaine).order_by('id_matiere')
    for sout in soutiens:
        if sout.id_matiere.nom_matiere not in matieres:
            matieres.append(sout.id_matiere.nom_matiere)
    return matieres

def get_groupes():
    """
    La fonction `get_groupes` renvoie une liste de valeurs distinctes pour le champ "groupe" du modèle
    `Eleve`, ordonnées par le champ "groupe".
    :return: une liste de valeurs distinctes du champ 'groupe' du modèle Eleve, ordonnées par le champ
    'groupe'.
    """
    return Eleve.objects.all().order_by('groupe').values_list('groupe', flat=True).distinct()


def get_semaines():
    """
    La fonction `get_semaines` renvoie toutes les instances du modèle `Semaine` ordonnées par leur
    attribut `id_semaine`.
    :return: toutes les instances du modèle Semaine, classées par leur attribut id_semaine.
    """
    return Semaine.objects.all().order_by('id_semaine')

def get_moyenne__generale_matiere(matiere):
    """
    La fonction "get_moyenne_generale_matiere" calcule la note moyenne pour une matière donnée dans un
    système QCM (Multiple Choice Questions).
    
    :param matiere: Le paramètre « matière » représente le nom d'une matière ou d'un cours
    :return: la note moyenne (arrondie à 2 décimales) pour une matière donnée. S'il n'y a aucun résultat
    ou si la moyenne est de 0, il renvoie '--'.
    """

    res = ResultatQCM.objects.filter(id_qcm__id_matiere__nom_matiere=matiere).aggregate(Avg("note", default=0))['note__avg']
    if res != None and res != 0:
        return str(round(res,2))
    else:
        return '--'
    

def get_donnees_qcm_acceuil():
    """
    La fonction `get_donnees_qcm_acceuil` récupère les données d'un QCM (Questionnaire à Choix
    Multiples) et renvoie les scores moyens pour chaque matière et groupe.
    :return: un dictionnaire contenant les scores moyens de chaque matière au QCM (questionnaire à choix
    multiples) pour la semaine en cours. Le dictionnaire est structuré comme suit :
    """
    semaine = get_semaine_actuelle()
    #semaine = Semaine.objects.filter(id_semaine=13).first()
    gps = get_groupes()
    qcms = QCM.objects.filter(id_semaine=semaine)
    resultat = {}
    resultat["generale"] = {}
    for qcm in qcms:
        resultat["generale"][qcm.id_matiere.nom_matiere] = get_moyenne_generale(qcm.id_qcm)
        for groupe in gps:
            if not(groupe in resultat):
                resultat[groupe] = {}
            resultat[groupe][qcm.id_matiere.nom_matiere] = get_moyenne_groupe(qcm.id_qcm,groupe)
    return resultat

def get_donnees_sondage_acceuil():
    """
    La fonction `get_donnees_sondage_acceuil` récupère les données d'une enquête et calcule le nombre de
    réponses et la note moyenne pour chaque sujet demandé.
    :return: La fonction `get_donnees_sondage_acceuil` renvoie un dictionnaire contenant des
    informations sur le nombre de réponses et le score moyen pour chaque sujet demandé dans une enquête.
    Les clés du dictionnaire sont les noms des sujets, et les valeurs sont des dictionnaires avec les
    clés 'nb' (nombre de réponses) et 'moyenne' (score moyen).
    """
    semaine = get_semaine_actuelle()
    # semaine = Semaine.objects.filter(id_semaine=17).first()
    matieres_demandees = RepSondage.objects.filter(id_sondage__id_semaine=semaine).values_list('matiere_voulue',flat=True).distinct()
    resultat = {}
    for matiere in matieres_demandees:
        resultat[matiere] = {}
        resultat[matiere]['nb'] = RepSondage.objects.filter(matiere_voulue=matiere,id_sondage__id_semaine=semaine).count()
        resultat[matiere]['moyenne'] = get_moyenne__generale_matiere(matiere)
    return resultat

def get_moyenne_generale_matiere_annee(id_matiere):
    """
    La fonction calcule la note moyenne d'un étudiant spécifique dans une matière spécifique.
    
    :param id_matiere: Le paramètre "id_matiere" est l'identifiant de la matière ou du cours pour lequel
    vous souhaitez calculer la note moyenne
    :return: la note moyenne (note) pour une matière spécifique (id_matiere) et un étudiant spécifique
    (num_etu) dans le modèle ResultatQCM. La note moyenne est arrondie à deux décimales.
    """
    mat = Matiere.objects.filter(id_matiere=id_matiere).first()
    return round(ResultatQCM.objects.filter(id_qcm__id_matiere=mat).aggregate(Avg('note',default=0))['note__avg'],2)

def get_moyenne_generale_matiere_annee_etu(id_matiere,num_etu):
    """
    Cette fonction calcule la note moyenne d'un étudiant spécifique dans une matière spécifique.
    
    :param id_matiere: Le paramètre "id_matiere" est l'identifiant de la matière ou du cours pour lequel
    vous souhaitez calculer la note moyenne
    :param num_etu: Le paramètre « num_etu » représente le numéro d'identification de l'étudiant
    :return: la note moyenne (note) pour une matière (id_matiere) et un étudiant spécifiques (num_etu)
    dans le modèle ResultatQCM. La note moyenne est arrondie à deux décimales.
    """
    mat = Matiere.objects.filter(id_matiere=id_matiere).first()
    return round(ResultatQCM.objects.filter(id_qcm__id_matiere=mat,num_etu=num_etu).aggregate(Avg('note',default=0))['note__avg'],2)

def get_profs_dispos(id_semaine,id_matiere):
    """
    La fonction `get_profs_dispos` renvoie une liste de professeurs disponibles pour une matière et une
    semaine spécifiques.
    
    :param id_semaine: Le paramètre id_semaine représente l'ID d'une semaine spécifique. Il permet de
    filtrer les objets ParticiperSoutienProfesseur en fonction du champ id_semaine de id_soutien
    :param id_matiere: Le paramètre `id_matiere` représente l'ID d'un sujet ou d'un cours spécifique
    :return: a queryset of Professeur objects.
    """
    profs = list(ParticiperSoutienProfesseur.objects.filter(id_soutien__id_matiere=id_matiere,id_soutien__id_semaine=id_semaine,disponibilite=True,organise=False).values_list('num_prof',flat=True))
    return Professeur.objects.filter(id_prof__in=profs)

def get_profs_possibles(id_semaine,id_matiere):
    """
    La fonction `get_profs_possibles` renvoie une liste des professeurs qui enseignent une matière
    spécifique au cours d'une semaine donnée.
    
    :param id_semaine: Le paramètre `id_semaine` représente l'ID d'une semaine spécifique
    :param id_matiere: Le paramètre `id_matiere` représente l'ID d'un sujet ou d'un cours spécifique
    :return: a queryset of Professeur objects.
    """
    id_periode = Semaine.objects.filter(id_semaine=id_semaine).first().id_periode
    profsdispos = list(ParticiperSoutienProfesseur.objects.filter(id_soutien__id_matiere=id_matiere,id_soutien__id_semaine=id_semaine,disponibilite=True).values_list('num_prof',flat=True))
    profs = list(EnseigneMatiere.objects.filter(id_periode=id_periode,id_matiere=id_matiere).exclude(id_prof__in=profsdispos).values_list('id_prof',flat=True))
    return Professeur.objects.filter(id_prof__in=profs)