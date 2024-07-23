from django.shortcuts import render
from django import http
from GestionSoutien.utils import get_semaine_actuelle, get_semaines, get_matieres_soutien
from GestionSoutien.models import Matiere, Semaine,Professeur,Soutien,ParticiperSoutienProfesseur
from .utils import get_liste_dispos_profs,get_creneaux_a_inscrire

def dispo(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction `dispo` prend une requête HTTP, récupère les choix de semaine et de sujet sélectionnés
    dans la requête, et renvoie un modèle HTML rendu avec les choix sélectionnés et une liste des plages
    horaires disponibles pour les professeurs.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module
    `django.http`. Il représente une requête HTTP faite par un client au serveur. Il contient des
    informations sur la requête, telles que la méthode HTTP (GET, POST, etc.), les en-têtes et toutes
    les données envoyées
    :type request: http.HttpRequest
    :return: un objet HttpResponse.
    """
    if request.POST:
        form = request.POST.copy()
        semaine_select = form.get('semaine')
        semaine_select = int(semaine_select)
        matieres_select = form.getlist('matiere')
        
    else:
        semaine_select = get_semaine_actuelle().id_semaine
        matieres_select = []
    if matieres_select != []:
        matieres_select = list(Matiere.objects.filter(nom_matiere__in=matieres_select).values_list('id_matiere',flat=True))
    
    else:
        matieres_select = list(Matiere.objects.all().values_list('id_matiere',flat=True))
    
    
    semaines = get_semaines()
    dispos = get_liste_dispos_profs(semaine_select, matieres_select)
    matieres = list(Matiere.objects.all().values_list('nom_matiere',flat=True))
    matieres_select = list(Matiere.objects.filter(id_matiere__in=matieres_select).values_list('nom_matiere',flat=True))
    return render(request,"Dispo.html",context={'admin':False, 'dispos':dispos, 'matieres':matieres, 'matieres_select':matieres_select, 'semaines':semaines, 'semaine_select':semaine_select})



def gerer_dispos(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction `gerer_dispos` gère la disponibilité des professeurs pour les sessions de support et
    affiche les sessions de support et les jours de la semaine en cours.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module
    `django.http`. Il représente une requête HTTP effectuée par un client vers un serveur
    :type request: http.HttpRequest
    :return: un objet HttpResponse.
    """
    if request.POST:
        prof = request.user.username
        sout = request.POST.get('soutien')
        prof = Professeur.objects.get(id_prof=prof)
        sout = Soutien.objects.get(id_soutien=sout)
        part = ParticiperSoutienProfesseur.objects.filter(id_soutien=sout,num_prof=prof)
        if part.count() != 0:
            part = part.first()
            part.disponibilite = True
            part.save()
        else:
            ParticiperSoutienProfesseur.objects.create(id_soutien=sout,num_prof=prof,disponibilite=True)
    semaine = get_semaine_actuelle()
    oraux = get_creneaux_a_inscrire(request.user.username,semaine)
    jours = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi']
    orgas = ParticiperSoutienProfesseur.objects.filter(num_prof=request.user.username, organise=True)
    inscrits = ParticiperSoutienProfesseur.objects.filter(num_prof=request.user.username, organise=False ,disponibilite=True)
    return render(request,"GererDispos.html", context={'soutiens':oraux, 'semaine_act':semaine,'jours':jours ,'orgas':orgas, 'inscrits':inscrits})
