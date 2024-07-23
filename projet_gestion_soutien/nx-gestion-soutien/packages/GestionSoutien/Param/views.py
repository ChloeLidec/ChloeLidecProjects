from django.shortcuts import render
import numpy as np
from .utils import get_creneau_def,get_periodes,get_soutiens,get_matieres,get_soutiens_ajoutes
from GestionSoutien.utils import get_semaines,get_semaine_actuelle,get_profs_dispos,get_profs_possibles
from GestionSoutien.models import Eleve, ParticiperSoutienEleve, ParticiperSoutienProfesseur, Semaine,Creneau, Periode,Matiere,EnseigneMatiere,Professeur, Soutien
from .models import ParamDef, CreneauDef
from .utils import maj_periodes_semaines, import_donnees_eleves, import_donnees_qcm, import_donnees_sondage
from django.core.mail import send_mail
from datetime import time


def param(request):
    """
    La fonction `param` est une fonction d'affichage de Django qui gère les requêtes liées aux
    paramètres, telles que l'enregistrement des paramètres, l'importation de fichiers et la gestion des
    périodes et des sujets pour les professeurs et les superutilisateurs.

    :param request: Le paramètre `request` est un objet qui représente la requête HTTP effectuée par le
    client. Il contient des informations telles que l'utilisateur effectuant la demande, la méthode
    utilisée (GET ou POST) et toutes les données envoyées avec la demande
    """
    if request.user.is_superuser:
        semaine_act = get_semaine_actuelle()
        if request.POST and request.POST.get('paramsave'):
            # request.POST.get('nom_input')
            # request.POST.copy().getlist('nom_champ')
            form = request.POST.copy()
            creneaudef = CreneauDef.objects.all().first()
            jour_def = form.get('jour_default_sout')
            match jour_def:
                case "Lundi":
                    jour_def = 1
                case "Mardi":
                    jour_def = 2
                case "Mercredi":
                    jour_def = 3
                case "Jeudi":
                    jour_def = 4
                case "Vendredi":
                    jour_def = 5
                case _:
                    jour_def = 2
            heure_def = form.get('heure_default_sout')
            creneaubase = CreneauDef.objects.all().first().id_creneau
            soutiens = Soutien.objects.filter(id_creneau=creneaubase)
            nv_creneau = Creneau.objects.filter(
                jour=jour_def, heure_debut=heure_def).first()
            if nv_creneau is None:
                nv_creneau = Creneau.objects.create(
                    jour=jour_def, heure_debut=heure_def)
            creneaudef.id_creneau = nv_creneau
            creneaudef.save()
            for soutien in soutiens:
                soutien.id_creneau = creneaubase
                soutien.save()
            periodes = Periode.objects.all()
            maj_periodes_semaines(periodes, form)
            
            profs_coches = request.POST.getlist('prof_mail')
            param_mails = ""
            for prof in profs_coches:
                param_mails += prof + " "
            param_mails = param_mails[:-1]
            param = ParamDef.objects.all().first()
            param.profs_mails = param_mails
            param.save()
                        
        # elif request.POST and request.POST.get('creneausave'):
        elif request.POST and request.POST.get('envoifichiers'):
            if 'formFileEtu' in request.FILES:
                files_etu = request.FILES.getlist('formFileEtu')
                if len(files_etu) >= 1:
                    for file_etu in files_etu:
                        import_donnees_eleves(file_etu)

            if 'formFileQCM' in request.FILES:
                matieres_qcm = request.POST.getlist('nonmatQCM')
                files_qcm = request.FILES.getlist('formFileQCM')
                if len(files_qcm) >= 1 and len(matieres_qcm) >= 1:
                    # On parcours la liste des fichiers et on ajoute la matière au même index
                    for index, file_qcm in enumerate(files_qcm):
                        import_donnees_qcm(file_qcm, matieres_qcm[index])

            if 'formFileSond' in request.FILES:
                files_sond = request.FILES.getlist('formFileSond')
                if len(files_sond) >= 1:
                    for file_sond in files_sond:
                        import_donnees_sondage(file_sond)
        elif request.POST and request.POST.get('creneausave'):
            
            contenu_mail = dict() # Nécessaire à l'envoi de mail
            jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
            destinataires_mail = ParamDef.objects.all().first().profs_mails
            if destinataires_mail != "":
                destinataires_mail = destinataires_mail.split(" ")
            else:
                destinataires_mail = []
            form = request.POST.copy()
            semaine_sout = Semaine.objects.get(id_semaine=int(form.get('semaine_sout')))
            listdates = form.getlist('datesout') + form.getlist('datesoutaj')
            heures_list = form.getlist('h_deb') + form.getlist('h_debaj')
            mats_list = form.getlist('matsout') + form.getlist('matsoutaj')
            soutiens_list = form.getlist('soutien') + form.getlist('soutienaj')
            profs_list = form.getlist('profsout') + form.getlist('profsoutaj')
            for ind in range(len(soutiens_list)):
                soutien = Soutien.objects.get(id_soutien=int(soutiens_list[ind]))
                prof = Professeur.objects.get(id_prof=profs_list[ind])
                jour = listdates[ind]
                match jour:
                    case "Lundi":
                        jour = 1
                    case "Mardi":
                        jour = 2
                    case "Mercredi":
                        jour = 3
                    case "Jeudi":
                        jour = 4
                    case "Vendredi":
                        jour = 5
                    case _:
                        jour = 2
                creneau = Creneau.objects.get_or_create(jour=jour,heure_debut=heures_list[ind])[0]
                mat = Matiere.objects.get(id_matiere=mats_list[ind])
                soutien.id_creneau = creneau
                soutien.id_matiere = mat
                soutien.save()
                prof_soutien = ParticiperSoutienProfesseur.objects.get_or_create(num_prof=prof,id_soutien=soutien)
                prof_soutien = prof_soutien[0]
                prof_soutien.organise = True
                prof_soutien.disponibilite = True
                prof_soutien.save()
                souts_sem_mat = Soutien.objects.filter(id_matiere=mat,id_semaine=semaine_sout)
                
                eleves_soutien = ParticiperSoutienEleve.objects.filter(id_soutien=soutien)
                eleves = []
                for eleve in eleves_soutien:
                    eleves.append(Eleve.objects.get(num_etu=eleve.num_etu_id))
                # Collecte d'informations pour le mail
                contenu_mail[(jours_semaine[creneau.jour-1], creneau.heure_debut, mat.nom_matiere)] = (prof, eleves)
                if prof.id_prof != "" and prof.id_prof not in destinataires_mail:
                    destinataires_mail.append(prof.id_prof)
                if souts_sem_mat.count() > 1:
                    eleves = ParticiperSoutienEleve.objects.filter(id_soutien__id_matiere=mat,id_soutien__id_semaine=semaine_sout)
                    eleves = np.array_split(eleves,souts_sem_mat.count())
                    for ind_sout in range(souts_sem_mat.count()):
                        for eleve in eleves[ind_sout]:
                            eleve.id_soutien = souts_sem_mat[ind_sout]
                            eleve.save()
    
                                      
            # Envoi de mail
            from_email = 'gestionsoutien883@gmail.com'
            subject = 'Convocation Soutien Semaine '+str(semaine_sout.id_semaine)
            emails_profs = []
            print(destinataires_mail)
            for prof in destinataires_mail:
                emails_profs.append(Professeur.objects.get(id_prof=prof).email_prof)

            message = f'Bonjour,\n\nVoici les soutiens de la semaine {semaine_sout.id_semaine} :\n'
            
            for (jour, heure, mat), (prof, eleves) in contenu_mail.items():
                message += f'\n- {jour} à {str(heure)[:-3]} => {mat} :\n'
                message += f'  - Professeur : {prof.nom_prof} {prof.prenom_prof}\n'
                message += '  - Elèves :\n'
                for eleve in eleves:
                    message += f'    - {eleve.nom} {eleve.prenom}\n'
                
            message += '\nCordialement,\nL\'équipe de gestion des soutiens.'
            
            send_mail(subject, message, from_email, emails_profs, fail_silently=False)

                            
        if request.POST and not request.POST.get('envoifichiers'):
            semaine = request.POST.get('Semaine')
            semaine_act = Semaine.objects.get(id_semaine=semaine)
        semaines = get_semaines()
        soutiens = get_soutiens(semaine_act.id_semaine) + get_soutiens_ajoutes(semaine_act.id_semaine)
        creneau = get_creneau_def()
        periodes = get_periodes()
        # semaine_act = Semaine.objects.all().first()
        liste_creneau = [tuples[0].id_creneau for tuples in soutiens]
        defnotpris = creneau.id_creneau not in liste_creneau
        jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
        matieres = Matiere.objects.all()
        nom_matiere = matieres.values_list('nom_matiere',flat=True)
        # Récupérer l'id de tous les profs
        profs = Professeur.objects.all()
        
        # Récupérer les profs qui reçoivent les mails par défaut
        profs_defaut = ParamDef.objects.all().first().profs_mails.split(' ')
        return render(request, 'param.html', context={'nom_matiere':nom_matiere,'defnotpris': defnotpris, 'semaines': semaines, 'soutiens': soutiens, 'creneau': creneau, 'periodes': periodes, 'semaine_act': semaine_act, 'jours': jours, 'matieres': matieres, 'profs': profs , 'profs_defaut': profs_defaut})
    else:
        if request.POST:
            form = request.POST.copy()
            prof = Professeur.objects.get(id_prof=request.user.username)
            periodes = []
            periodes.append(form.getlist('P1'))
            periodes.append(form.getlist('P2'))
            periodes.append(form.getlist('P3'))
            periodes.append(form.getlist('P4'))
            for id_p, periode in enumerate(periodes):
                cpt = 0
                periode_obj = Periode.objects.get(id_periode=id_p+1)
                list_mat = []
                while cpt < len(periode):
                    mat = Matiere.objects.get(
                        id_matiere=int(periode[cpt].split('-')[0]))
                    list_mat.append(mat.id_matiere)
                    ens = EnseigneMatiere.objects.filter(
                        id_prof=prof, id_matiere=mat, id_periode=periode_obj).first()
                    if ens is None:
                        EnseigneMatiere.objects.create(
                            id_prof=prof, id_matiere=mat, id_periode=periode_obj)
                    cpt += 1
                mats_non_ens = EnseigneMatiere.objects.filter(
                    id_prof=prof, id_periode=periode_obj).exclude(id_matiere__in=list_mat)
                mats_non_ens.delete()
        matieres = get_matieres(request.user.username)
        return render(request,'param.html',context={'matieres':matieres})

def creneau(request):
    soutien = Soutien.objects.create(id_semaine= Semaine.objects.get(id_semaine=int(request.GET.get('semaine_act'))))
    semaine_act = Semaine.objects.get(id_semaine=int(request.GET.get('semaine_act')))
    matieres = Matiere.objects.all()
    jours = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi']
    profs_dispos = get_profs_dispos(semaine_act.id_semaine,matieres.first().id_matiere)
    profs_possibles = get_profs_possibles(semaine_act.id_semaine,matieres.first().id_matiere)
    return render(request,'creneau-soutien.html',{'soutien':soutien,'matieres':matieres,'jours':jours,'semaine_act':semaine_act,'profsd':profs_dispos,'profsp':profs_possibles})

def suppr_soutien(request,pk):
    soutien = Soutien.objects.get(id_soutien=pk)
    eleves = ParticiperSoutienEleve.objects.filter(id_soutien=soutien)
    sout_mat = Soutien.objects.filter(id_semaine=soutien.id_semaine,id_matiere=soutien.id_matiere).first()
    for eleve in eleves:
        eleve.id_soutien = sout_mat
        eleve.save()
    soutien.delete()
    semaine_act = Semaine.objects.get(id_semaine=int(request.POST.get('semaine_act')))
    soutiens = get_soutiens(semaine_act.id_semaine)
    soutiens += get_soutiens_ajoutes(semaine_act.id_semaine)
    jours = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi']
    return render(request,'liste-soutiens.html',{'soutiens':soutiens,'semaine_act':semaine_act,'jours':jours})

def get_profs(request):
    semaine_act = Semaine.objects.get(id_semaine=int(request.GET.get('semaine')))
    mat = Matiere.objects.get(id_matiere=int(request.GET.get('matsoutaj')))
    profs_dispos = get_profs_dispos(semaine_act.id_semaine,mat.id_matiere)
    profs_possibles = get_profs_possibles(semaine_act.id_semaine,mat.id_matiere)
    return render(request,'profs.html',{'profsd':profs_dispos,'profsp':profs_possibles})





