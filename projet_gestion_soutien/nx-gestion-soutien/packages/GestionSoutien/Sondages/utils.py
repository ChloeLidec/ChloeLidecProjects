import datetime
from .models import  RepSondage, Sondage, Eleve, Semaine


def get_semaine_actuelle():
    """
    La fonction `get_semaine_actuelle` renvoie la semaine en cours en fonction des dates de début et de
    fin stockées dans le modèle `Semaine`.
    :return: la première instance du modèle Semaine où date_debut est inférieur ou égal à la date
    d'aujourd'hui et date_fin est supérieur ou égal à la date d'aujourd'hui.
    """
    # __lte : <=
    # __gte : >=                </div>

    return Semaine.objects.filter(date_debut__lte=datetime.date.today(), date_fin__gte=datetime.date.today()).first()

def get_sondage_etudiant(num_etudiant, id_semaine):
    """
    La fonction `get_sondage_etudiant` récupère la réponse d'un étudiant à une enquête pour un numéro
    d'étudiant et un identifiant de semaine donnés.
    
    :param num_etudiant: Le paramètre "num_etudiant" représente le numéro d'étudiant ou identifiant de
    l'étudiant pour lequel on souhaite récupérer la réponse à l'enquête
    :param id_semaine: Le paramètre `id_semaine` est l'ID de la semaine pour laquelle vous souhaitez
    récupérer la réponse à l'enquête de l'étudiant. Il permet de filtrer les objets `Sondage` et de
    retrouver l'enquête de cette semaine spécifique
    :return: l'objet rep_sondage, qui est la réponse à l'enquête pour un élève et une semaine
    spécifiques.
    """
    sondage = Sondage.objects.filter(id_semaine=id_semaine).first()
    rep_sondage = None
    if sondage is not None:
        rep_sondage = RepSondage.objects.filter(
            id_sondage=sondage.id_sond, num_etu=num_etudiant).first()
    return rep_sondage


def get_sondages(id_semaine, groupe_filtre):
    """
    La fonction `get_sondages` récupère les réponses à l'enquête des étudiants en fonction d'un
    identifiant de semaine donné et d'un filtre pour les groupes d'étudiants.
    
    :param id_semaine: Le paramètre "id_semaine" représente l'ID de la semaine pour laquelle vous
    souhaitez récupérer les enquêtes
    :param groupe_filtre: Le paramètre "groupe_filtre" est une liste de groupes selon lesquels vous
    souhaitez filtrer les étudiants. Si la liste est vide, cela signifie que vous souhaitez récupérer
    tous les étudiants. Si la liste n'est pas vide, cela signifie que vous souhaitez uniquement obtenir
    les étudiants appartenant aux groupes spécifiés
    :return: une liste de listes, où chaque liste interne représente la réponse à l'enquête d'un
    étudiant. Chaque liste interne contient les éléments suivants : eleve (objet étudiant), volontaire
    (booléen), matiere_voulue (chaîne) et commentaire (chaîne).
    """
    sondages = []
    if groupe_filtre == []:
        eleves = Eleve.objects.all()
    else:
        eleves = Eleve.objects.filter(groupe__in=groupe_filtre)

    for eleve in eleves:
        rep_eleve = []
        reps = get_sondage_etudiant(eleve.num_etu, id_semaine)
        if reps != None:
            rep_eleve.append(eleve)
            rep_eleve.append(reps.volontaire)
            rep_eleve.append(reps.matiere_voulue)
            rep_eleve.append(reps.commentaire)
            sondages.append(rep_eleve)
    return sondages
