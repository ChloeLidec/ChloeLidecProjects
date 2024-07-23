cd nx-gestion-soutien/packages/GestionSoutien
python3 manage.py dumpdata --natural-foreign --exclude contenttypes --exclude auth.permission > static/db.json 
