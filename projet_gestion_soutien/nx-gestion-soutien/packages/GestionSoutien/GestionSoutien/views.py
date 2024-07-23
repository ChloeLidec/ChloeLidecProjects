from django import http
from django.shortcuts import render
from .utils import get_semaines, get_donnees_qcm_acceuil, get_donnees_sondage_acceuil, get_semaine_actuelle
from .models import Soutien
from Param.models import CreneauDef


def accueil(request: http.HttpRequest) -> http.HttpResponse:
    """
    The function "accueil" returns a rendered HTML template for the "Accueil" page in a web application.

    :param request: The request parameter is an object that represents the HTTP request made by the
    client. It contains information such as the HTTP method (GET, POST, etc.), headers, user session,
    and any data sent in the request body. In this code snippet, the request object is used to render
    the 'gest
    :return: the rendered template 'gestionSoutien/Accueil.html'.
    """
    qcms = get_donnees_qcm_acceuil()
    semaines = get_semaines()
    #matieres_demandées[r.matiere_voulue]={"nb":1,"Moyenne":None}
    sondage = get_donnees_sondage_acceuil()
    texte = ""
    if semaines.count() == 0:
        if request.user.is_superuser:
            texte = "Veuillez aller dans les paramètres afin de renseigner les périodes et de générer les semaines"
        else:
            texte = "Veuillez contacter l'administrateur afin de générer les semaines et les données"
    semaine_act = get_semaine_actuelle()
    soutiens_sem = Soutien.objects.filter(id_semaine=semaine_act)
    if soutiens_sem.count() == 0:
        crendef = CreneauDef.objects.all().first().id_creneau
        Soutien.objects.create(id_semaine=semaine_act, id_creneau=crendef)
    return render(request, "accueil.html", context={'texte': texte, 'qcm': qcms, 'sondage': sondage, 'semaines': semaines})
