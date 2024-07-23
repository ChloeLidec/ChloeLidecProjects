from django.shortcuts import render
from django import http
from django.shortcuts import render
from GestionSoutien.utils import get_semaines, get_groupes
from .utils import get_sondages, get_semaine_actuelle
# Create your views here.


def res_sond(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction `res_sond` récupère et affiche les résultats de l'enquête en fonction de la semaine et
    des groupes sélectionnés.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module `http`.
    Il représente une requête HTTP faite par un client au serveur. Il contient des informations telles
    que la méthode de requête (GET, POST, etc.), les en-têtes et toutes les données envoyées avec la
    requête
    :type request: http.HttpRequest
    :return: un objet HttpResponse.
    """
    groupes = get_groupes()
    if request.POST:
        form = request.POST.copy()
        semaine_select = form.get('semaine')
        groupes_select = form.getlist('groupe')
        if len(groupes_select) == 0:
            groupes_select = groupes
    else:
        semaine_select = get_semaine_actuelle().id_semaine
        groupes_select = list(groupes)
        
    
    semaine_select = int(semaine_select)
    semaines = get_semaines()
    resultats = get_sondages(semaine_select, groupes_select)
    return render(request, "res_sond.html", context={'admin': True, 'groupes': groupes, 'resultats': resultats, 'semaines': semaines, 'semaine_select': semaine_select, 'groupe_select': groupes_select})
