#!/bin/bash

# Fonction pour afficher un message d'erreur et quitter le script avec un code d'erreur
exit_with_error() {
  echo "$1"
  exit 1
}

# Fonction pour vérifier la branche actuelle
check_branch() {
  target_branch="main"

  current_branch=$(git symbolic-ref --short -q HEAD)
  [ "$current_branch" == "$target_branch" ] || exit_with_error "Vous n'êtes pas sur la branche $target_branch. Veuillez changer de branche."
  
  echo "Vous êtes actuellement sur la branche $target_branch."
}

# Fonction pour vérifier si nous sommes à la racine du projet
check_root() {
  project_root="gestion_soutien_iut"

  [ "$(basename "$(pwd)")" == "$project_root" ] || exit_with_error "Veuillez vous déplacer à la racine du projet."
  
  echo "Vous vous situez bien à la racine du projet."
}

# Fonction pour vérifier l'absence du fichier db.sqlite3
check_db_file() {
  db_file="nx-gestion-soutien/packages/GestionSoutien/db.sqlite3"

  if [ -e "$db_file" ]; then
    echo "Le fichier $db_file existe déjà. Vous pouvez continuer sans le supprimer."
  else
    echo "Le fichier $db_file n'existe pas. Vous pouvez continuer."
  fi
}

# Fonction qui permet de faire la migration
make_migrations() {
  cd "nx-gestion-soutien/packages/GestionSoutien" || exit_with_error "Impossible de changer de répertoire."
  python3 manage.py makemigrations
  cd - || exit_with_error "Impossible de revenir au répertoire précédent."
}

# Fonction qui permet de faire le migrate
make_migrate() {
  cd "nx-gestion-soutien/packages/GestionSoutien" || exit_with_error "Impossible de changer de répertoire."
  python3 manage.py migrate
  cd - || exit_with_error "Impossible de revenir au répertoire précédent."
}

# Fonction pour charger les données
load_data() {
  cd "nx-gestion-soutien/packages/GestionSoutien" || exit_with_error "Impossible de changer de répertoire."
  python3 manage.py loaddata static/db.json
  cd - || exit_with_error "Impossible de revenir au répertoire précédent."
}

# Fonction pour lancer le serveur et ouvrir la page
start_server() {
  local project_path="nx-gestion-soutien/packages/GestionSoutien"
  local server_url="http://127.0.0.1:8000/"
  
  cd "$project_path" || exit_with_error "Impossible de changer de répertoire vers $project_path."

  # Vérification si le serveur est déjà en cours d'exécution
  if pgrep -f "python3 manage.py runserver" > /dev/null; then
    echo "Le serveur est déjà en cours d'exécution à l'adresse $server_url."
  else
    echo "Lancement du serveur..."
    python3 manage.py runserver &
    sleep 2 # Attente de quelques secondes pour s'assurer que le serveur est bien démarré
    xdg-open "$server_url" 2>/dev/null || open "$server_url" 2>/dev/null || echo "Ouvrez votre navigateur et accédez à : $server_url"
  fi

  cd - || exit_with_error "Impossible de revenir au répertoire précédent."
}




#Appel des fonctions
check_branch
check_root
check_db_file
make_migrations
make_migrate
load_data
start_server
