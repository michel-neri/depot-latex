Dépôt personnel de certains répertoires de projets persos (un projet pouvant désigner une simple fiche de correction).

Le fichier `utilities.sty` est le document le plus important sur ce dépôt : c'est le paquet auquel je me réfère dans tous mes projets. Il contient pléthore de commandes fondamentales et d'importations d'autres paquets utiles et succintement commentés.
Il est à noter que la quantité de paquets importés dans `utilities.sty` induit une compilation particulièrement longue.

:heavy_exclamation_mark: Pour le moment tous les répertoires et fichiers contenus sur cet espace sont rédigés plus ou moins proprement. Aucune tenue rédactionnelle n'est à ce jour (28/01/2024) garantie.

L'arborescence n'est pour le moment pas non plus celle d'origine des fichiers.

:hammer: Je compile mes `main.tex` (nom qu'ont presque tous mes fichiers sources) via un micro script batch dont voici le contenu :
```bat
cls
lualatex --output-directory=./output/ main.tex
```
Tous mes projets sont situés dans des répertoires eux-mêmes situés dans un répertoire commun nommé `workspace`. Ce super-répertoire porte le `utilities.sty` ainsi commun à tous les projets.

Voici quelques captures d'écrans de ce que comporte ce dépôt :

<p align='center'>
  <img src='Modèle%20corrigé%20DS/icon.png' width='400'>
</p>

<p align='center'>Projet <code>Modèle corrigé DS</code></p>

