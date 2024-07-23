from .models import ResultatQCM, QCM
from GestionSoutien.models import Eleve, Matiere, Semaine
from Sondages.utils import get_sondage_etudiant


def get_res_qcm_etudiant(num_etu,id_semaine):
    """
    La fonction `get_res_qcm_etudiant` récupère les résultats des QCM d'un étudiant pour une semaine
    donnée.
    
    :param num_etu: Le paramètre « num_etu » représente le numéro d'identification de l'étudiant. Il est
    utilisé pour filtrer les résultats et récupérer les résultats QCM pour un étudiant spécifique
    :param id_semaine: Le paramètre "id_semaine" représente l'ID d'une semaine spécifique. Il permet de
    filtrer les objets QCM (Questionnaire à Choix Multiples) en fonction de la semaine à laquelle ils
    appartiennent
    :return: une liste d’objets ResultatQCM.
    """
    notes = []
    qcms = QCM.objects.filter(id_semaine=id_semaine).order_by('id_matiere')
    for qcm in qcms:
        try:
            notes.append(ResultatQCM.objects.filter(
                id_qcm=qcm.id_qcm, num_etu=num_etu).first())
        except:
            notes.append(ResultatQCM.objects.create(id_qcm=qcm.id_qcm,num_etu=num_etu,note=0))
    return notes

def get_res_qcm(id_semaine: int, groupe_filtre):
    """
    La fonction `get_res_qcm` récupère les résultats des questions à choix multiples (QCM) pour une
    semaine donnée et filtrés par un groupe spécifique.
    
    :param id_semaine: Le paramètre `id_semaine` représente l'ID de la semaine pour laquelle vous
    souhaitez récupérer les résultats
    :type id_semaine: int
    :param groupe_filtre: Le paramètre "groupe_filtre" est une liste de groupes selon lesquels vous
    souhaitez filtrer les étudiants. Si la liste est vide, cela signifie que vous souhaitez obtenir des
    résultats pour tous les élèves. Si la liste n'est pas vide, cela signifie que vous souhaitez obtenir
    uniquement les résultats des étudiants appartenant au
    :return: une liste de résultats à un QCM (quiz à choix multiples) pour une semaine donnée et filtrés
    par groupe. Chaque résultat comprend l'étudiant, ses scores pour chaque QCM et ses réponses à une
    enquête (si disponible).
    """
    resultats = []
    if groupe_filtre == []:
        etudiants = Eleve.objects.all()
    else:
        etudiants = Eleve.objects.filter(groupe__in=groupe_filtre)
    qcms = QCM.objects.filter(id_semaine=id_semaine).order_by('id_matiere')
    for etudiant in etudiants:
        resultat_etudiant = [etudiant]
        # On récupère toutes les notes aux QCMS de la semaine, si il n'y a pas de note, on met 0
        notes = []
        for qcm in qcms:
            try:
                notes.append(ResultatQCM.objects.filter(
                    id_qcm=qcm.id_qcm, num_etu=etudiant.num_etu).first().note)
            except:
                notes.append('--')
        resultat_etudiant.append(notes)
        rep_sondage = get_sondage_etudiant(etudiant.num_etu, id_semaine)
        if rep_sondage is not None:
            resultat_etudiant.append(rep_sondage.volontaire)
            resultat_etudiant.append(rep_sondage.matiere_voulue)
        else:
            resultat_etudiant.append('--')
            resultat_etudiant.append('--')
        suggestion = get_suggestion_eleve(id_semaine,etudiant)
        resultat_etudiant.append(suggestion)
        if len(notes) != 0:
            resultats.append(resultat_etudiant)
    return resultats


def get_moyenne_generale(id_qcm):
    """
    La fonction calcule le score moyen pour un QCM (Questionnaire à Choix Multiples) donné en
    additionnant tous les scores et en divisant par le nombre de résultats.
    
    :param id_qcm: Le paramètre "id_qcm" représente l'ID d'un QCM (Questionnaire à Choix Multiples) pour
    lequel on souhaite calculer le score moyen
    :return: la moyenne moyenne d'un QCM (questionnaire à choix multiple) identifié par son id_qcm. S'il
    n'y a aucun résultat pour le QCM, il renvoie « -- » comme espace réservé.
    """

    moyenne = 0
    resultats = ResultatQCM.objects.filter(id_qcm=id_qcm)
    for resultat in resultats:
        moyenne += resultat.note
    if len(resultats) != 0:
        moyenne /= len(resultats)
        return round(moyenne,2)
    return '--'

def get_moyenne_groupe(id_qcm,groupe):
    """
    La fonction `get_moyenne_groupe` calcule le score moyen d'un groupe dans un QCM (Questionnaire à
    Choix Multiples) en filtrant les résultats en fonction de l'ID QCM et du numéro de groupe.
    
    :param id_qcm: Le paramètre "id_qcm" représente l'ID du QCM (Questionnaire à Choix Multiples) dont
    vous souhaitez calculer la moyenne
    :param groupe: Le paramètre "groupe" représente le groupe pour lequel vous souhaitez calculer la
    moyenne. Il peut s'agir d'une chaîne ou d'un entier identifiant le groupe
    :return: le score moyen d'un groupe à un QCM (quiz à choix multiples). S'il n'y a aucun résultat
    pour le groupe, il renvoie '--'.
    """
    moyenne = 0
    resultats = ResultatQCM.objects.filter(id_qcm=id_qcm,num_etu__groupe=groupe)
    for resultat in resultats:
        moyenne += resultat.note
    if len(resultats) != 0:
        moyenne /= len(resultats)
        return round(moyenne,2)
    return '--'

def get_bandeau_moyennes(id_semaine, filtre="generale"):
    """
    La fonction `get_bandeau_moyennes` récupère les scores moyens d'une semaine et d'un filtre donnés.
    
    :param id_semaine: Le paramètre "id_semaine" représente l'ID d'une semaine spécifique. Il permet de
    filtrer les QCM (questionnaires à choix multiples) en fonction de la semaine à laquelle ils
    appartiennent
    :param filtre: Le paramètre « filtre » permet de préciser le type de filtrage à appliquer lors du
    calcul des moyennes. Il peut avoir deux valeurs possibles :, defaults to generale (optional)
    :return: une liste de moyennes.
    """
    moyennes = []
    qcms = QCM.objects.filter(id_semaine=id_semaine).order_by('id_matiere')
    for qcm in qcms:
        if filtre == "generale":
            moyenne = get_moyenne_generale(qcm.id_qcm)
            moyennes.append((moyenne))
        else:
            moyenne = get_moyenne_groupe(qcm.id_qcm,filtre)
            moyennes.append(moyenne)
    return moyennes


def get_suggestion_eleve(id_semaine,etudiant):
    """
    La fonction renvoie les éventuelles matières ou l'élève
    a eu sur au moins 5 semaines consécutives des notes qui baissent

    :param id_semaine:id de la semaine choisie
    :param num_etu: Le numéro d'étudiant
    :return: une liste de suggestions
    """
    suggestions = []
    matieres = Matiere.objects.all()
    semaine = Semaine.objects.get(id_semaine=id_semaine)
    for matiere in matieres:
        diff = -1
        res_qcm = ResultatQCM.objects.filter(id_qcm__id_matiere=matiere,num_etu=etudiant.num_etu,\
        id_qcm__id_semaine__id_semaine__lte=semaine.id_semaine).order_by('-id_qcm__id_semaine').values_list('note',flat=True)[:3]
        ind = 0
        while diff < 0 and ind+1 < len(res_qcm):
            diff = res_qcm[ind] - res_qcm[ind+1]
            ind += 1
        if diff < 0:
            suggestions.append(matiere.nom_matiere)
    return suggestions