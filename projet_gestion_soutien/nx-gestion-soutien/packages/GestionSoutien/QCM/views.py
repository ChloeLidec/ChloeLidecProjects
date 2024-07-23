from django.shortcuts import render
from django.http import HttpResponse
from django import http
from .utils import get_res_qcm, get_bandeau_moyennes,get_suggestion_eleve
from GestionSoutien.utils import get_semaine_actuelle, get_semaines, get_matieres_qcms, get_groupes
from GestionSoutien.models import EnseigneMatiere, Semaine,Matiere,Eleve,Soutien,ParticiperSoutienEleve,ParticiperSoutienProfesseur,Professeur
from Param.models import Creneau,CreneauDef
from django.contrib.auth.decorators import login_required


def res_qcm(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction `res_qcm` est une fonction d'affichage en Python qui restitue un modèle avec des données
    liées aux résultats QCM pour une semaine et un groupe sélectionnés.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module
    `django.http`. Il représente une requête HTTP faite par un client au serveur. Il contient des
    informations telles que la méthode de requête (GET, POST, etc.), les en-têtes et toutes les données
    envoyées avec la requête
    :type request: http.HttpRequest
    :return: un objet HttpResponse.
    """
    groupes = get_groupes()
    if request.POST:
        form = request.POST.copy()
        if form.get('btn_valide'):
            semaine_select = form.get('semaine')
            groupes_select = form.getlist('groupe')
            if len(groupes_select) == 0:
                groupes_select = groupes
        elif form.get('btn_envoi'):
            eleves = form.getlist('eleve_sout')
            mats_sout = form.getlist('mat_sout')
            semaine_select = Semaine.objects.get(id_semaine=form.get('semaine_act'))
            for ind in range(len(eleves)):
                mat = Matiere.objects.get(id_matiere=mats_sout[ind])
                eleve = Eleve.objects.get(num_etu=eleves[ind])
                sout = Soutien.objects.filter(id_matiere=mats_sout[ind],id_semaine=semaine_select)
                if sout.count() > 0:
                    sout = sout.first()
                else:
                    creneau_def = Creneau.objects.get(id_creneau=CreneauDef.objects.all().first().id_creneau.id_creneau)
                    sout = Soutien.objects.create(id_matiere=mat,id_semaine=semaine_select,id_creneau=creneau_def)
                part_eleve = ParticiperSoutienEleve.objects.get_or_create(num_etu=eleve,id_soutien=sout)
                part_prof = ParticiperSoutienProfesseur.objects.filter(id_soutien=sout,disponibilite=True)
                if part_prof.count() < 1:
                    profs = EnseigneMatiere.objects.filter(id_periode=semaine_select.id_periode,id_matiere=mat).values_list('id_prof__id_prof',flat=True)
                    soutiens_cren = Soutien.objects.filter(id_semaine=semaine_select,id_creneau=sout.id_creneau).values_list('id_soutien',flat=True)
                    profs_soutiens = ParticiperSoutienProfesseur.objects.filter(id_soutien__in=soutiens_cren).values_list('num_prof__id_prof',flat=True)
                    prof = Professeur.objects.filter(id_prof__in=profs).exclude(id_prof__in=profs_soutiens).first()
                    ParticiperSoutienProfesseur.objects.create(id_soutien=sout,num_prof=prof,disponibilite=True,organise=True)
                else:
                    part_profo = part_prof.filter(organise=True)
                    if part_profo.count() < 0:
                        part_prof = part_prof.first()
                        part_prof.disponibilite = True
                        part_prof.organise = True
            semaine_select = semaine_select.id_semaine
            groupes_select = list(groupes)
    else:
        semaine_select = get_semaine_actuelle().id_semaine
        groupes_select = list(groupes)
    semaine_select = int(semaine_select)
    
    semaines = get_semaines()
    matieres = get_matieres_qcms(semaine_select)
    res_bandeau = get_bandeau_moyennes(semaine_select)
    resultats = get_res_qcm(semaine_select, groupes_select)
    groupe_act = "Generale"
    request.session['selec'] = ""
    return render(request, "ResQCM.html", context={'groupes': groupes,"groupe_act":groupe_act, 'matieres': matieres, 'res_bandeau': res_bandeau, 'semaines': semaines, 'resultats': resultats, 'semaine_select': semaine_select, 'groupes_select': groupes_select,"selec":""})

@login_required
def get_bandeau(request):
    """
    La fonction `get_bandeau` prend un objet de requête, récupère la semaine et le groupe sélectionnés à
    partir de la requête, et renvoie un modèle HTML rendu avec les scores moyens du groupe sélectionné
    pour la semaine sélectionnée.
    
    :param request: Le paramètre `request` est un objet qui représente la requête HTTP effectuée par le
    client. Il contient des informations telles que la méthode de requête, les en-têtes et les
    paramètres de requête
    :return: un modèle HTML rendu appelé 'bandeau.html' avec les variables de contexte suivantes :
    'groupes', 'semaine_select', 'res_bandeau' et 'groupe_act'.
    """
    sem = int(request.GET.get('semaine'))
    sem = Semaine.objects.get(id_semaine=sem)
    groupes = get_groupes()
    groupe_bandeau = request.GET.get('groupe-bandeau')
    res_bandeau = get_bandeau_moyennes(sem.id_semaine,groupe_bandeau)
    return render(request,'bandeau.html',{'groupes':groupes,'semaine_select':sem.id_semaine, 'res_bandeau': res_bandeau,"groupe_act":groupe_bandeau})

@login_required
def ajouter_eleve(request,num_etu):
    """
    Ajoute l eleve au tableau de soutien"""
    sem = int(request.POST.get('semaine'))
    sem = Semaine.objects.get(id_semaine=sem)
    eleve = Eleve.objects.get(num_etu=num_etu)
    if eleve.num_etu not in request.session['selec'].split('|'):
        request.session["selec"] += eleve.num_etu + "|"
        matieres_gen = Matiere.objects.all()
        suggestions = get_suggestion_eleve(sem.id_semaine,eleve)
        return render(request,'eleve-soutien.html',{'matieres_gen':matieres_gen,'eleve':eleve,'suggestions':suggestions})

@login_required
def delete_row(request):
    return HttpResponse("")
    
@login_required
def get_matiere(request):
    mat = request.GET.get("mat_sout")
    mat = Matiere.objects.get(id_matiere=mat)
    return HttpResponse("<small>"+mat.nom_matiere+"</small>")