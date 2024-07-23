from .models import User

def load_user(username):
    """
    La fonction `load_user` tente de récupérer un objet utilisateur 
    de la base de données en fonction du
    nom d'utilisateur fourni et renvoie 
    l'objet utilisateur s'il est trouvé, ou Aucun si l'utilisateur
    n'existe pas.
    
    :param username: Le paramètre `username` est une chaîne qui représente le nom d'utilisateur de
    l'utilisateur que nous voulons charger
    :return: une instance du modèle User si un utilisateur avec le nom d'utilisateur spécifié existe. Si
    l'utilisateur n'existe pas, il renvoie Aucun.
    """
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None  # L'utilisateur n'existe pas
