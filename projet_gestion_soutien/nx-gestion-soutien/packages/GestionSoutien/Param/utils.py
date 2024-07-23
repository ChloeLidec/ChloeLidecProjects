from GestionSoutien.models import EnseigneMatiere, ParticiperSoutienEleve, ParticiperSoutienProfesseur, Periode, Semaine, Matiere, Professeur, Eleve, Soutien
from GestionSoutien.utils import get_profs_dispos,get_profs_possibles
from QCM.models import QCM,ResultatQCM
from Sondages.models import Sondage,RepSondage
from .models import CreneauDef
import datetime
import csv

def get_periodes():
    """
    La fonction `get_periodes` renvoie toutes les instances du modèle `Periode`.
    :return: tous les objets du modèle Période.
    """
    return Periode.objects.all()

def get_creneau_def():
    """
    La fonction `get_creneau_def()` renvoie le premier objet du modèle `CreneauDef`.
    :return: le premier objet du modèle CreneauDef.
    """
    return CreneauDef.objects.all().first()

def get_soutiens(id_semaine:int):
    """
    La fonction `get_soutiens` renvoie un ensemble de requêtes d'objets `Soutien` filtrés par le
    paramètre `id_semaine`.
    
    :param id_semaine: Le paramètre "id_semaine" est un entier qui représente l'ID d'une semaine
    spécifique
    :type id_semaine: int
    :return: un ensemble de requêtes d'objets Soutien filtrés par l'id_semaine donné.
    """
    souts = Soutien.objects.filter(id_semaine=id_semaine).exclude(id_matiere__isnull=True,id_creneau__isnull=True)
    soutiens_liste = []
    for sout in souts:
        eleves = ParticiperSoutienEleve.objects.filter(id_soutien=sout.id_soutien)
        eleves = [part.num_etu for part in eleves]
        prof = ParticiperSoutienProfesseur.objects.filter(id_soutien=sout.id_soutien).first()
        profs_dispos = get_profs_dispos(id_semaine,sout.id_matiere.id_matiere)
        profs_possibles = get_profs_possibles(id_semaine,sout.id_matiere.id_matiere)
        soutiens_liste.append((sout,eleves,prof,profs_dispos,profs_possibles))
    return soutiens_liste

def get_soutiens_ajoutes(id_semaine:int):
    """
    La fonction `get_soutiens` renvoie un ensemble de requêtes d'objets `Soutien` filtrés par le
    paramètre `id_semaine`.
    
    :param id_semaine: Le paramètre "id_semaine" est un entier qui représente l'ID d'une semaine
    spécifique
    :type id_semaine: int
    :return: un ensemble de requêtes d'objets Soutien filtrés par l'id_semaine donné.
    """
    souts = Soutien.objects.filter(id_semaine=id_semaine,id_matiere__isnull=True,id_creneau__isnull=True)
    soutiens_liste = []
    for sout in souts:
        profs_dispos = get_profs_dispos(id_semaine,Matiere.objects.first().id_matiere)
        profs_possibles = get_profs_possibles(id_semaine,Matiere.objects.first().id_matiere)
        soutiens_liste.append((sout,[],None,profs_dispos,profs_possibles))
    return soutiens_liste

def get_matieres(numprof):
    """
    La fonction `get_matières` récupère un dictionnaire des matières enseignées par un professeur à
    chaque période.
    
    :param numprof: Le paramètre `numprof` est l'identifiant d'un professeur. Il permet de récupérer les
    informations du professeur à partir du modèle 'Professeur'
    :return: un dictionnaire appelé "resultat". Ce dictionnaire contient des informations sur les
    matières enseignées par un professeur pour chaque période. Les clés du dictionnaire sont les objets
    Matière (sujets) et les valeurs sont des dictionnaires contenant les points (P1, P2, P3, P4) comme
    clés et une valeur binaire (1 ou 0) indiquant si le professeur enseigne cette matière en
    """
    resultat = {}
    matieres = Matiere.objects.all()
    prof = Professeur.objects.get(id_prof=numprof)
    mat_prof_p1 = list(EnseigneMatiere.objects.filter(id_periode=1,id_prof=prof).values_list('id_matiere',flat=True))
    mat_prof_p2 = list(EnseigneMatiere.objects.filter(id_periode=2,id_prof=prof).values_list('id_matiere',flat=True))
    mat_prof_p3 = list(EnseigneMatiere.objects.filter(id_periode=3,id_prof=prof).values_list('id_matiere',flat=True))
    mat_prof_p4 = list(EnseigneMatiere.objects.filter(id_periode=4,id_prof=prof).values_list('id_matiere',flat=True))
    for mat in matieres:
        dico = {}
        if mat.id_matiere in mat_prof_p1:
            dico['P1'] = 1
        else:
            dico['P1'] = 0
        if mat.id_matiere in mat_prof_p2:
            dico['P2'] = 1
        else:
            dico['P2'] = 0
        if mat.id_matiere in mat_prof_p3:
            dico['P3'] = 1
        else:
            dico['P3'] = 0
        if mat.id_matiere in mat_prof_p4:
            dico['P4'] = 1
        else:
            dico['P4'] = 0
        resultat[mat] = dico
    return resultat    

def maj_periodes_semaines(periodes,form):
    """
    La fonction `maj_periodes_semaines` met à jour les dates des périodes et des semaines en fonction
    des entrées de l'utilisateur.
    
    :param periodes: Le paramètre `periodes` est une liste d'objets représentant des périodes. Chaque
    objet de période possède les attributs suivants :
    :param form: Le paramètre « formulaire » est un objet de type dictionnaire qui contient les valeurs
    soumises dans un formulaire. Il permet de récupérer les valeurs des champs 'deb' et 'fin' pour
    chaque 'période' de la liste 'périodes'
    """
    cpt_id = 1
    for periode in periodes:
        date_deb = form.get('deb'+str(periode.id_periode))
        date_fin = form.get('fin'+str(periode.id_periode))
        date_deb_dt = datetime.datetime.strptime(date_deb,"%Y-%m-%d").date()
        date_fin_dt = datetime.datetime.strptime(date_fin,"%Y-%m-%d").date()
        date_deb_dt = date_deb_dt - datetime.timedelta(days=date_deb_dt.weekday())
        periode.date_debut = datetime.datetime.strftime(date_deb_dt,"%Y-%m-%d")
        date_deb = periode.date_debut
        date_fin_dt = date_fin_dt - datetime.timedelta(days=date_fin_dt.weekday())
        date_fin_dt = date_fin_dt + datetime.timedelta(days=6)
        periode.date_fin = datetime.datetime.strftime(date_fin_dt,"%Y-%m-%d")
        date_fin = periode.date_fin
        periode.save()
        # changer les dates des semaines
        semaines = Semaine.objects.all().order_by('id_periode','date_debut')
        # + datetime.timedelta(days=...)
        cpt = 0
        date_max = datetime.datetime.strptime(date_deb,"%Y-%m-%d").date()
        while cpt < len(semaines) and datetime.datetime.strptime(date_fin,"%Y-%m-%d").date() >= semaines[cpt].date_fin:
            sem = semaines[cpt]
            sem.id_semaine = cpt_id
            sem.id_periode = periode
            sem.date_debut = date_max
            sem.date_fin = sem.date_debut + datetime.timedelta(days=6)
            sem.save()
            date_max = sem.date_fin + datetime.timedelta(days=1)
            cpt += 1
            cpt_id += 1
        # Semaine.objects.filter(id_semaine__gte=cpt_id).delete()
        while datetime.datetime.strptime(date_fin,"%Y-%m-%d").date() > date_max:
            deb = date_max
            fin = deb + datetime.timedelta(days=6)
            sem = Semaine.objects.create(id_semaine=cpt_id,id_periode=periode,date_debut=deb,date_fin=fin)
            date_max = fin + datetime.timedelta(days=1)
            cpt_id += 1
    date_min = Periode.objects.all().order_by('date_debut').first().date_debut
    date_max = Periode.objects.all().order_by('date_debut').last().date_fin
    Semaine.objects.filter(date_fin__lte=date_min).delete()
    Semaine.objects.filter(date_debut__gte=date_max).delete()

def import_donnees_eleves(fichier):
    """
    La fonction importe les données des étudiants à partir d'un fichier et met à jour les dossiers des
    étudiants existants ou en crée de nouveaux dans une base de données.
    
    :param fichier: Le paramètre "fichier" est censé être un objet fichier contenant les données des
    étudiants
    """
    contenu = [ligne.decode('utf-8', errors='ignore').split(',') for ligne in fichier]
    contenu = contenu[1:]
    for ligne in contenu:
        if len(ligne) == 4:
            num_etu,nom,prenom,groupe = ligne[0].strip('\n'),ligne[1].strip('\n'),ligne[2].strip('\n'),ligne[3].strip('\n')
            eleve = Eleve.objects.filter(num_etu=num_etu)
            if eleve.count() != 0:
                eleve = eleve.first()
                eleve.nom = nom
                eleve.prenom = prenom
                eleve.groupe = groupe
                eleve.save()
            else:
                eleve = Eleve.objects.create(num_etu=num_etu,nom=nom,prenom=prenom,groupe=groupe)
        else:
            # Gérer le cas où la ligne n'a pas la bonne longueur
            print(f"La ligne {ligne} ne contient pas les 4 valeurs attendues.")


def import_donnees_qcm(fichier,nom_matiere):
    """
    La fonction `import_donnees_qcm` importe les données d'un fichier, les traite et enregistre les
    résultats dans une base de données.
    
    :param fichier: Le paramètre "fichier" est un objet fichier qui contient les données du QCM
    (Questionnaire à Choix Multiples) au format CSV
    :param nom_matiere: Le paramètre "nom_matiere" représente le nom de la matière ou du cours pour
    lequel les données QCM (Questionnaire à Choix Multiples) sont importées
    """
    contenu = [ligne.decode().split(',') for ligne in fichier]
    colonnes = contenu[0]
    bareme = int(colonnes[8].split('/')[1])
    contenu = contenu[1:len(contenu)-1]
    date_qcm = contenu[1][5].strip('"').replace('û','u').replace('é','e')
    mois = date_qcm.split(" ")[1].lower().replace('û','u').replace('é','e')
    match mois:
        case "janvier":
            date_qcm = date_qcm.replace("janvier","january")
        case "fevrier":
            date_qcm = date_qcm.replace("fevrier","february")
        case "mars":
            date_qcm = date_qcm.replace("mars","march")
        case "avril":
            date_qcm = date_qcm.replace("avril","april")
        case "mai":
            date_qcm = date_qcm.replace("mai","may")
        case "juin":
            date_qcm = date_qcm.replace("juin","june")
        case "juillet":
            date_qcm = date_qcm.replace("juillet","july")
        case "aout":
            date_qcm = date_qcm.replace("aout","august")
        case "septembre":
            date_qcm = date_qcm.replace("septembre","september")
        case "octobre":
            date_qcm = date_qcm.replace("octobre","october")
        case "novembre":
            date_qcm = date_qcm.replace("novembre","november")
        case "decembre":
            date_qcm = date_qcm.replace("decembre","december")
    semaine = Semaine.objects.filter(date_debut__lte=datetime.datetime.strptime(date_qcm,'%d %B %Y  %H:%M').date(), date_fin__gte=datetime.datetime.strptime(date_qcm,'%d %B %Y %H:%M').date()).first()
    mat = Matiere.objects.filter(nom_matiere=nom_matiere)
    if mat.count() != 0:
        mat = mat.first()
    else:
        mat = Matiere.objects.create(nom_matiere=nom_matiere)
    qcm = QCM.objects.filter(id_semaine=semaine,id_matiere=mat)
    if qcm.count() != 0:
        qcm = qcm.first()
    else:
        qcm = QCM.objects.create(nom_qcm=fichier.name.split('.')[0],id_matiere=mat,id_semaine=semaine)
    for ligne in contenu:
        num_etu,etat,date_qcm,note = ligne[2].strip('\n'),ligne[4].strip('\n'),ligne[5].strip('\n'),ligne[8].strip('\n')
        if etat != 'Terminé':
            note = 0
        if bareme != 20:
            note = round((20*float(note.strip('"').strip("'")))/bareme,2)
        eleve = Eleve.objects.filter(num_etu=num_etu)
        if eleve.count() !=0:
            eleve = eleve.first()
            res = ResultatQCM.objects.filter(num_etu=eleve,id_qcm=qcm)
            if res.count() != 0:
                res = res.first()
                res.note = note
                res.save()
            else:
                res = ResultatQCM.objects.create(num_etu=eleve,id_qcm=qcm,note=note)

def import_donnees_sondage(fichier):
    """
    La fonction `import_donnees_sondage` importe les données d'enquête à partir d'un fichier, traite les
    données et les enregistre dans une base de données.
    
    :param fichier: Le paramètre `fichier` est un objet fichier qui contient les données d'une enquête
    """
    contenu = [ligne.decode().split(',') for ligne in fichier]
    contenu = contenu[1:]
    date_sond = contenu[1][4].strip('"')
    date_sond = " ".join(date_sond.split(" ")[1:]).replace('û','u').replace('é','e')
    mois = date_sond.split(" ")[1].lower().replace('û','u').replace('é','e')
    print(mois)
    match mois:
        case "janvier":
            date_sond = date_sond.replace("janvier","january")
        case "fevrier":
            date_sond = date_sond.replace("fevrier","february")
        case "mars":
            date_sond = date_sond.replace("mars","march")
        case "avril":
            date_sond = date_sond.replace("avril","april")
        case "mai":
            date_sond = date_sond.replace("mai","may")
        case "juin":
            date_sond = date_sond.replace("juin","june")
        case "juillet":
            date_sond = date_sond.replace("juillet","july")
        case "aout":
            date_sond = date_sond.replace("aout","august")
        case "septembre":
            date_sond = date_sond.replace("septembre","september")
        case "octobre":
            date_sond = date_sond.replace("octobre","october")
        case "novembre":
            date_sond = date_sond.replace("novembre","november")
        case "decembre":
            date_sond = date_sond.replace("decembre","december")
    print(date_sond)
    semaine = Semaine.objects.filter(date_debut__lte=datetime.datetime.strptime(date_sond,'%d %B %Y').date(), date_fin__gte=datetime.datetime.strptime(date_sond,'%d %B %Y').date()).first()
    sond = Sondage.objects.filter(id_semaine=semaine)
    if sond.count() != 0:
        sond = sond.first()
    else:
        sond = Sondage.objects.create(id_semaine=semaine)
    for ligne in contenu:
        num_etu,volontaire,souhait,commentaire = ligne[2].strip('\n'),ligne[6].strip('\n'),ligne[7].strip('\n'),ligne[8].strip('\n')
        eleve = Eleve.objects.get(num_etu=num_etu)
        res = RepSondage.objects.filter(num_etu=eleve,id_sondage=sond)
        if res.count() != 0:
            res = res.first()
            res.volontaire = volontaire
            res.commentaire = commentaire
            res.matiere_voulue = souhait
            res.save()
        else:
            res = RepSondage.objects.create(num_etu=eleve,id_sondage=sond,matiere_voulue=souhait,volontaire=volontaire,commentaire=commentaire)