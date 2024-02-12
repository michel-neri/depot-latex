
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
    <td colspan='2'><img src='Pages%20de%20garde%20LaTeX%20TikZ/icone.png' align='center' width='800'></td>
  </tr>
  <tr>
    <td colspan='2' align='center'>Projet <code>Modèles de pages de gardes</code></td>
  </tr>
  <tr>
    <td colspan='2'><img src='Projet%20MarkdownMaths/icone.png' align='center' width='800'></td>
  </tr>
  <tr>
    <td colspan='2' align='center'>Projet <code>MarkdownMaths</code></td>
  </tr>
  <tr>
    <td colspan='2'><img src='Modele%20fiche%20resume/icon.png' align='center' width='800'></td>
  </tr>
  <tr>
    <td colspan='2' align='center'>Projet <code>Modele fiche resume</code></td>
  </tr>
  
 </table>



Dépôt personnel de certains répertoires de projets persos (un projet pouvant désigner une simple fiche de correction).

Projets sur ce dépôt :
- Exemple de correction de DS (avec les commandes et environnements correspondants).
- Exemple de cours (Tle Complémentaire : Limites et continuité de fonctions).
- Un document qui comprend trois modèles de pages de gardes / couverture. Les modèles sont décalqués d'internet et servent surtout de modèles d'un point de vue LaTeX et TikZ, mais sont sufissament paramétrés pour pouvoir être réutilisés à souhait.
- Pré-processeur markdown permettant de rédiger des cours, fiches synthèses et autre en markdown. Le pré-processeur compile le tout et donne un rendu très satisfaisant, assurant un gain de temps considérable pour la rédaction de certains types de documents.
- Modèle de fiche résumée de quelque chose (avec en-tête légèrement stylisée, filigrane à chaque page et petit tableau vite fait avec des couleurs).

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

