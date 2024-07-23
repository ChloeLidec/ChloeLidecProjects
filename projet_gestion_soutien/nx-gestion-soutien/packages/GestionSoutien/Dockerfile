# Utilisez une image de base avec Python
FROM python:3.10

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY . /app/

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel l'application fonctionnera
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
