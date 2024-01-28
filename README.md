
<table align='center'>
  <tr>
    <td><img src='Modèle%20corrigé%20DS/icon.png' align='center' width='400'></td>
    <td><img src='Modèle cours Tle Compl/icone.png' align='center' width='400'></td>
  </tr>
  <tr>
     <td align='center'>Projet <code>Modèle corrigé DS</code></td>
     <td align='center'>Projet <code>Modèle cours Tle Compl</code></td>
  </tr>
  <tr>
    <td colspan='2'><img src='Projet%20MarkdownMaths/icone.png' align='center' width='800'></td>
  </tr>
  <tr>
    <td colspan='2' align='center'>Projet <code>MarkdownMaths</code></td>
  </tr>
 </table>



Dépôt personnel de certains répertoires de projets persos (un projet pouvant désigner une simple fiche de correction).

Projets sur ce dépôt :
- Exemple de correction de DS (avec les commandes et environnements correspondants).
- Exemple de cours (Tle Complémentaire : Limites et continuité de fonctions).
- Pré-processeur markdown permettant de rédiger des cours, fiches synthèses et autre en markdown. Le pré-processeur compile le tout et donne un rendu très satisfaisant, assurant un gain de temps considérable pour la rédaction de certains types de documents.

---

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

:x: Il reste énormément de choses à améliorer et à ajouter. Certains fichiers sont longs, trop longs et pourraient bénéficier d'une réduction de contenu d'un facteur 5 à l'aide d'outils que je projette de m'écrire (e.g. paquet de construction de tableaux de signe / vars, paquet de construction de schéma très simplifiée).

