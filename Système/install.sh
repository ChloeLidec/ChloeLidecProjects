#!/bin/bash
#Fichier donnant les droits et executant les sous fichiers
chmod u+x code.sh java.sh python.sh docker.sh oracle.sh test.sh
./code.sh
./java.sh
./python.sh
# ./docker.sh
./oracle.sh
# newgrp docker
