# TP Svelte Mikulic Lidec

## Commandes

npm install (depuis ./sonicapp)

npm run prepare

npm run dev -- --open

## Site

### Pages présentes

- Home
    - Une checkbox pour faire disparaitre et réafficher un texte avec une transition 
    - Deux boutons pour gérer la taille de l'image de Shadow

- Characters
    - Pour chacun des personnages chargé depuis un json (dans data.js pour l'exporter), on a une interface changeante lorsqu'on passe la souris sur celle-ci. Les couleurs du texte, les images et les textes viennent des données.
    - On peut voir les différents personnages grâce au drawer de navigation refermable sur la gauche

- Games
    - Les jeux sont également chargés depuis un json dans data.js
    - Il y a un menu présentant de manière générale les jeux dans des cards qui changent au passage de la souris
    - Pour chaque jeu, le bouton read more permet d'aller vers une page de détail

- Additional content
    - Différentes vidéos (urls depuis data.js) sont intégrés grâce à des composants iframe

### Composants créés

#### Souris (sur acceuil et games) 
Fait en sorte que le svg de sanic suive le curseur de la souris sauf sur la top bar car clic désactivé pour permettre de naviguer
Lorsque l'on clique, l'image grossi

#### Iframe (dans additional content)
Permet d'inclure un player de vidéo youtube

#### GameCard (dans games)
Affiche un recap des jeux -> change sur hover

#### Character (dans characters)
Affiche le personnage -> sur hover on a les détails

### Composants intégrés

#### TopAppBar (layout)
Affiche la barre de nav

#### Form Field et Button a (acceuil)
La checkbox permet de cacher et afficher un texte (avec transi perso)
Les boutons peuvent grandir ou retrecir l image de Shadow

#### Drawer (characters)
Le menu de selection dans characters
