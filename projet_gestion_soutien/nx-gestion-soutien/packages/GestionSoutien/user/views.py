from django import http
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.
from GestionSoutien.models import Professeur
from random import randint


def connexion(request):
    """
    La fonction `connexion` gère l'authentification 
    de l'utilisateur en vérifiant le nom d'utilisateur
    et le mot de passe fournis dans une requête POST, 
    et redirige l'utilisateur vers la vue appropriée
    si l'authentification est réussie.
    
    :param request: Le paramètre `request` est un objet 
    qui représente la requête HTTP effectuée par le
    client. Il contient des informations telles que la méthode de requête (GET, POST, etc.), les
    en-têtes, les cookies et le corps de la requête
    :return: La fonction `connexion` renvoie un objet réponse. 
    Si la méthode de requête est "POST" et
    que l'utilisateur est authentifié avec succès, il redirige vers la vue "accueil". Si
    l'authentification échoue, le modèle "connexion.html" est affiché avec un message d'erreur. Si la
    méthode de requête n'est pas "POST", elle restitue simplement le modèle "connexion.html".
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger vers une vue appropriée après la connexion
            return redirect('accueil')
        
        # On affiche dans le template réutilisé une erreur contextuelle
        messages.error(
            request, "Nom d'utilisateur ou mot de passe incorrect.")

        return render(request, 'connexion.html')
    return render(request, 'connexion.html')


def index(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction renvoie une réponse HTTP avec le modèle « index.html » rendu.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module
    `django.http`. Il représente la requête HTTP faite par le client au serveur. Il contient des
    informations telles que la méthode de requête (GET, POST, etc.), les en-têtes, la session
    utilisateur et toutes les données envoyées avec
    :type request: http.HttpRequest
    :return: un objet HttpResponse.
    """
    return render(request, 'index.html')
    # return render_template("index.html",title="Projet soutien", admin=True)


def deconnexion(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction déconnecte l'utilisateur et le redirige vers la page de connexion.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module
    `django.http`. Il représente une requête HTTP faite par un client au serveur. Il contient des
    informations sur la requête, telles que la méthode HTTP, les en-têtes et le corps
    :type request: http.HttpRequest
    :return: le résultat de l'appel de la fonction `connexion` avec le paramètre `request`.
    """
    logout(request)
    return connexion(request)


def register(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction register permet à l'utilisateur de s'inscrire et 
    le redirige vers la page de connexion.
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module
    `django.http`. Il représente une requête HTTP faite par un client au serveur. Il contient des
    informations sur la requête, telles que la méthode HTTP, les en-têtes et le corps
    :type request: http.HttpRequest
    :return: le résultat de l'appel de la fonction `register` avec le paramètre `request`.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")

        if password == password2:
            user = User.objects.create_user(username=username,
                                            password=password)
            user.save()
            prof = Professeur(id_prof=username, nom_prof=nom,
                              prenom_prof=prenom, email_prof=email)
            prof.save()
            return connexion(request)
        
        messages.error(
            request, "Les mots de passe ne correspondent pas.")
        return render(request, 'register.html')
    return render(request, 'register.html')

def new_mdp(request: http.HttpRequest) -> http.HttpResponse:
    """
    La fonction oubli_mdp permet à l'utilisateur de réinitialiser son mot de passe et 
    le redirige vers la page de connexion.
    L'application envoie un mail à l'utilisateur avec un code à 6 chiffres pour réinitialiser son mot de passe.
    step1 : on demande l'email de l'utilisateur
    step2 : on demande le code à 6 chiffres
    step3 : on demande le nouveau mot de passe
    
    :param request: Le paramètre `request` est une instance de la classe `HttpRequest` du module
    `django.http`. Il représente une requête HTTP faite par un client au serveur. Il contient des
    informations sur la requête, telles que la méthode HTTP, les en-têtes et le corps
    :type request: http.HttpRequest
    :return: le résultat de l'appel de la fonction `oubli_mdp` avec le paramètre `request`.
    """
    if request.method == "POST":
        email = request.POST.get("email")
        code_genere = request.POST.get("code_genere")
        code = request.POST.get("code")
        mdp = request.POST.get("mdp")
        mdp2 = request.POST.get("mdp2")
        if email is not None and code is None and mdp is None:
            # On vérifie que l'email existe dans la base de données
            if Professeur.objects.filter(email_prof=email).exists():                
                # On envoie un mail au prof avec un code à 6 chiffres
                from_email = 'gestionsoutien883@gmail.com'
                prof_email = email
                code_genere = randint(100000, 999999)
                subject = "Réinitialisation du mot de passe - Gestion Soutien"
                
                prof = Professeur.objects.get(email_prof=email)
                message = "Bonjour,\n\nVoici ci-dessous votre code de réinitialisation de mot de passe :\n" + str(code_genere) + "\n\nCordialement,\nL'équipe Gestion Soutien"
                
                prof.mdp_provisoire_prof = code_genere
                prof.save()
                
                send_mail(subject, message, from_email, [prof_email], fail_silently=False)
                
                # On redirige vers la même page mais avec un champs pour le code
                return render(request, 'new_mdp.html', {'step1': False, 'step2': True, 'step3': False, 'email': email, 'code_genere': code_genere})
            else:
                # On affiche une erreur contextuelle
                return render(request, 'new_mdp.html', {'step1': True, 'step2': False, 'step3': False, 'message_error': "L'adresse e-mail renseignée n'est associée à aucun professeur."})

        elif code is not None and mdp is None:
            action = request.POST.get('action')
            prof = Professeur.objects.get(email_prof=email)
            
            if action == 'verifier_code':
                if code_genere == code:
                    return render(request, 'new_mdp.html', {'step1': False, 'step2': False, 'step3': True, 'email': email})
                else:
                    return render(request, 'new_mdp.html', {'step1': False, 'step2': True, 'step3': False, 'email': email, 'code_genere': code_genere, 'message_error': "Le code renseigné est incorrect."})
            
            elif action == 'envoyer_code':
                # On envoie un mail au prof avec un code à 6 chiffres
                from_email = 'gestionsoutien883@gmail.com'
                prof_email = email
                code_genere = randint(100000, 999999)
                subject = "Réinitialisation du mot de passe - Gestion Soutien"
                
                prof = Professeur.objects.get(email_prof=email)
                message = "Bonjour,\n\nVoici votre code de réinitialisation de mot de passe : " + str(code_genere) + "\n\nCordialement,\nL'équipe Gestion Soutien"
                
                prof.mdp_provisoire_prof = code_genere
                prof.save()
                
                send_mail(subject, message, from_email, [prof_email], fail_silently=False)
                
                # On redirige vers la même page mais avec un champs pour le code
                return render(request, 'new_mdp.html', {'step1': False, 'step2': True, 'step3': False, 'email': email, 'code_genere': code_genere, 'message_nv_code': "Un nouveau code vous a été envoyé."})
        
        elif mdp is not None and mdp2 is not None:
            if mdp == mdp2:
                prof = Professeur.objects.get(email_prof=email)
                prof.mdp_provisoire_prof = ""
                prof.save()
                user = User.objects.get(username=prof.id_prof)
                user.set_password(mdp)
                user.save()
                return connexion(request)
            else:
                return render(request, 'new_mdp.html', {'step1': False, 'step2': False, 'step3': True, 'email': email, 'message_error': "Les mots de passe ne correspondent pas."})
            
    return render(request, 'new_mdp.html', {'step1': True, 'step2': False, 'step3': False})