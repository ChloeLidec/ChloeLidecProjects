rm nx-gestion-soutien/packages/GestionSoutien/db.sqlite3
cd nx-gestion-soutien/packages/GestionSoutien
python3 manage.py migrate
python3 manage.py loaddata static/db.json

