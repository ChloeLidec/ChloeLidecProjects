from time import strftime
from GestionSoutien.models import Semaine, EnseigneMatiere, Professeur, Creneau, Matiere, ParticiperSoutienProfesseur, Soutien


def get_liste_dispos_profs(id_semaine: int, matieres_select: list) -> tuple:
    """
    La fonction `get_liste_dispos_profs` récupère une liste des professeurs disponibles ainsi que leurs
    matières et horaires d'enseignement pour une semaine donnée et les matières sélectionnées.
    
    :param id_semaine: Le paramètre `id_semaine` représente l'ID d'une semaine spécifique
    :type id_semaine: int
    :param matieres_select: Le paramètre `matières_select` est une liste de sujets sélectionnés. Il
    permet de filtrer la liste des matières enseignées par les professeurs. Si `matieres_select` est une
    liste vide, elle sera renseignée avec tous les sujets disponibles dans la base de données
    :type matieres_select: list
    :return: un dictionnaire où les clés sont des instances du modèle `Professeur` et les valeurs sont
    des listes. Chaque liste contient deux éléments : une liste de chaînes représentant les noms des
    matières enseignées par le professeur, et une chaîne représentant les plages horaires disponibles
    pour les séances de soutien du professeur.
    """
    resultats = {}
    if matieres_select == []:
        matieres_select = list(
            Matiere.objects.all().values_list('id_matiere', flat=True))
    profs = Professeur.objects.all()
    semaine = Semaine.objects.filter(id_semaine=id_semaine).first()
    # On parcourt tous les profs et on récupère les matières qu'ils enseignent pour la semaine donnée
    for prof in profs:
        # On récupère les matières enseignées par le prof pour la semaine donnée
        ids_matieres = EnseigneMatiere.objects.filter(
            id_prof=prof.id_prof, id_periode=semaine.id_periode).values('id_matiere')
        # On récupère les noms des matières enseignées par le prof pour la semaine donnée
        enseignees = list(Matiere.objects.filter(id_matiere__in=ids_matieres).filter(
            id_matiere__in=matieres_select).values_list('nom_matiere', flat=True))
        creneaux_dispos = ""
        # On récupère les créneaux de soutien auxquels le prof participe
        soutiens = Soutien.objects.filter(
            id_semaine=id_semaine).values('id_soutien')
        # On récupère les créneaux de soutien auxquels le prof participe et qui sont organisés par lui
        dispos = ParticiperSoutienProfesseur.objects.filter(
            num_prof__id_prof=prof.id_prof, id_soutien__in=(soutiens), disponibilite=True)
        orgas = ParticiperSoutienProfesseur.objects.filter(
            num_prof=prof, id_soutien__in=(soutiens), organise=True)
        dispos = dispos.union(orgas)
        # On parcourt les créneaux de soutien auxquels le prof participe et on récupère les plages
        for dispo in dispos:
            creneau = Soutien.objects.get(
                id_soutien=dispo.id_soutien.id_soutien).id_creneau
            jour = creneau.jour
            match jour:
                case 1:
                    jour = "Lundi"
                case 2:
                    jour = "Mardi"
                case 3:
                    jour = "Mercredi"
                case 4:
                    jour = "Jeudi"
                case 5:
                    jour = "Vendredi"
                case _:
                    jour = "Mardi"
            if creneaux_dispos == "" or not creneaux_dispos.find(jour + " " + creneau.heure_debut.strftime('%H:%M:%S') + "\n"):
                creneaux_dispos += jour + " " + \
                    creneau.heure_debut.strftime('%H:%M:%S') + "\n"

        if creneaux_dispos == '':
            creneaux_dispos = '--'

        resultats[prof] = [enseignees, creneaux_dispos]

    return resultats


def get_creneaux_a_inscrire(id_prof, semaine):
    """
    La fonction `get_creneaux_a_inscrire` récupère les plages horaires disponibles pour qu'un professeur
    puisse s'inscrire aux séances de soutien en fonction des matières qui lui sont attribuées et des
    inscriptions existantes.
    
    :param id_prof: Le paramètre `id_prof` est l'identifiant du professeur. Il est utilisé pour
    récupérer l'objet professeur de la base de données
    :param semaine: Le paramètre "semaine" représente une semaine. C'est un objet de la classe "Semaine"
    :return: un ensemble de requêtes de soutiens (sessions de soutien) auxquels un professeur peut
    s'inscrire.
    """
    prof = Professeur.objects.get(id_prof=id_prof)
    ids_matieres = list(EnseigneMatiere.objects.filter(
        id_prof=prof.id_prof, id_periode=semaine.id_periode).values_list('id_matiere', flat=True))
    inscriptions = ParticiperSoutienProfesseur.objects.filter(
        num_prof=prof, disponibilite=True, id_soutien__id_semaine=semaine)
    soutiens_ins = list(inscriptions.values_list('id_soutien', flat=True))
    jour_ins = list(inscriptions.values_list(
        'id_soutien__id_creneau__jour', flat=True))
    heure_ins = list(inscriptions.values_list(
        'id_soutien__id_creneau__heure_debut', flat=True))
    creneaux_vides = Soutien.objects.filter(id_semaine=semaine, id_matiere=None).exclude(
        id_soutien__in=soutiens_ins).exclude(id_creneau__jour__in=jour_ins, id_creneau__heure_debut__in=heure_ins)
    creneaux_matieres = Soutien.objects.filter(
        id_semaine=semaine, id_matiere__id_matiere__in=ids_matieres).exclude(id_soutien__in=soutiens_ins)
    soutiens = creneaux_vides.union(creneaux_matieres)
    return soutiens
