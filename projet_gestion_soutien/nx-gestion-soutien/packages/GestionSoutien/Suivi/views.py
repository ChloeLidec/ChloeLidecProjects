import json
from django.shortcuts import render
from django import http
from django.shortcuts import render
from GestionSoutien.utils import get_semaines, get_groupes,get_semaine_actuelle
from GestionSoutien.models import Eleve,Matiere, ParticiperSoutienEleve
from .utils import get_infos_etudiants,get_graphe
from Sondages.utils import get_sondage_etudiant
from QCM.utils import get_res_qcm_etudiant
from django.http import JsonResponse


def suivi_etu(request: http.HttpRequest,num_etu) -> http.HttpResponse:
    """
    La fonction `suivi_etu` est une fonction d'affichage dans Django qui restitue un modèle et lui
    transmet diverses données, notamment une liste de sujets, des QCM, des enquêtes, des semaines, des
    informations sur les étudiants et un graphique des notes des étudiants.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest`, qui représente
    une requête HTTP effectuée par un client. Il contient des informations sur la requête, telles que la
    méthode HTTP (GET, POST, etc.), les en-têtes et le corps
    :type request: http.HttpRequest
    :param num_etu: Le paramètre `num_etu` représente le numéro d'étudiant ou l'identifiant de
    l'étudiant pour lequel le suivi est effectué
    :return: un objet HttpResponse.
    """
    if request.POST:
        form = request.POST.copy()
        semaine_select = form.get('semaine')
        
    else:
        semaine_select = get_semaine_actuelle().id_semaine
    
    semaine_select = int(semaine_select)
    
    semaines = get_semaines()
    
    eleve = Eleve.objects.filter(num_etu=num_etu).first()
    # liste_matieres=["Python","Java","C++","BDD","Reseau","IHM","Web"]
    liste_matieres = Matiere.objects.all()
    semaines= get_semaines()
    semaine_actu = get_semaine_actuelle()
    qcms = get_res_qcm_etudiant(num_etu,semaine_actu)
    sondage = get_sondage_etudiant(num_etu,semaine_actu)
    data, matieres_nom = get_graphe(num_etu, 43, semaines)
    context = {
        'matieres': liste_matieres,
        'qcms': qcms,
        'sondage': sondage,
        'semaines': semaines,
        'eleve': eleve,
        'semaine_actu': semaine_actu,
    }
    context = crea_liste_notes(data,matieres_nom,context)
    return render(request,"Suivi_etu.html",context=context)

def crea_liste_notes(data,matieres_nom,context):
    """
    La fonction "crea_liste_notes" crée une liste de notes pour chaque sujet en fonction des données
    fournies et des noms de sujets.
    
    :param data: Le paramètre « data » est un dictionnaire qui contient les informations sur les notes
    de chaque matière. Les clés du dictionnaire représentent les semaines et les valeurs sont des
    dictionnaires qui contiennent les notes de chaque matière
    :param matieres_nom: Une liste de chaînes représentant les noms des matières ou des cours
    :param context: Le paramètre `context` est un dictionnaire qui stocke des informations et des
    variables accessibles et modifiables tout au long de l'exécution du code. Il est utilisé pour
    transmettre des données entre différentes parties du programme
    :return: le dictionnaire contextuel mis à jour, qui inclut désormais les clés 'liste_noms_matières'
    et 'liste_notes'.
    """
    liste_notes = []
    for i in range(len(matieres_nom)):
        liste_notes.append([matieres_nom[i]])
    # On parcours les semaines
    for key,value in data.items():
        if value == {}:
            # On ajoute -1 dans chaque liste de notes
            for i in range(len(liste_notes)):
                liste_notes[i].append(-1)
        else:
            # On récupère la liste de clés du dico de valeurs
            matieres_notes = value.keys()
            # Si la matière n'est pas dans le dico de valeurs, on ajoute -1 dans la liste de notes sinon on ajoute la note
            for i in range(len(liste_notes)):
                if matieres_nom[i] not in matieres_notes:
                    liste_notes[i].append(-1)
                else:
                    liste_notes[i].append(value[matieres_nom[i]])
    liste_noms_matieres = []
    for matiere_data in liste_notes:
        nom_matiere = matiere_data[0]
        liste_noms_matieres.append(nom_matiere)
    context['liste_noms_matieres'] = liste_noms_matieres
    context['liste_notes'] = liste_notes
    return context     

def suivi_gen(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction `suivi_gen` est une fonction de vue Python qui gère une requête HTTP et renvoie une
    réponse HTTP avec un modèle rendu, en transmettant certaines données de contexte.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module
    `django.http`. Il représente une requête HTTP faite par un client au serveur. Il contient des
    informations sur la requête, telles que la méthode HTTP (GET, POST, etc.), les en-têtes et toutes
    les données envoyées
    :type request: http.HttpRequest
    :return: une réponse HTTP, qui est généralement un modèle HTML rendu. Le modèle HTML en cours de
    rendu est "SuiviGenEtu.html" et un dictionnaire de contexte lui est transmis contenant diverses
    variables telles que "suivi_gen", "groupes", "semaines", "jours", "semaine_select" et
    "groupes_select".
    """
    groupes = get_groupes()
    if request.POST:
        form = request.POST.copy()
        if request.POST.get('envoi-comm'):
            coms = form.getlist("commsout")
            souts = form.getlist("sout")
            etus = form.getlist("etu")
            for ind in range(len(souts)):
                etu = Eleve.objects.get(num_etu=etus[ind])
                comm = coms[ind]
                part = ParticiperSoutienEleve.objects.get(num_etu=etu,id_soutien__id_soutien=int(souts[ind]))
                part.commentaire = comm
                part.save()
            semaine_select = form.get('semaine_act')
            groupes_select = list(groupes)
        else:
            semaine_select = form.get('semaine')
            groupes_select = form.getlist('groupe')
            if len(groupes_select) == 0:
                groupes_select = groupes
    else:
        semaine_select = get_semaine_actuelle().id_semaine
        groupes_select = list(groupes)
    
    semaine_select = int(semaine_select)

    semaines = get_semaines()
    
    jours = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi']
    
    # return render_template("SuiviGenEtu.html",title="Suivi général étudiant", admin=True,suivi_gen=eleves,semaine_act=semaine_act,semaines=semaines,groupes=groupes)
    return render(request,"SuiviGenEtu.html",context={'suivi_gen':get_infos_etudiants(semaine_select, groupes_select), 'groupes':groupes, 'semaines':semaines, 'jours':jours, 'semaine_select':semaine_select, 'groupes_select':groupes_select})