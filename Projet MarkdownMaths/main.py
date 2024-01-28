import subprocess
import sys
from os import listdir
from os.path import isfile, join
import shutil
from difflib import SequenceMatcher # Pour la compilation d'un seul doc et permettre de taper n'importe quel bout éloigné du nom du fichier, la lib permet de calculer une distance entre mots 


# Pre-processeur
def convert_md(f_name, file_path):
	print(f'\nConstruction du document {f_name}')
	markdown = None
	
	with open(file_path, encoding='utf-8') as f:
		markdown = f.read()
	
	# Remplacement automatique de certains débuts de lignes par des codes clefs.
	markdown = markdown.replace('\nDéfinition', '\n\\shortcutDefinition{}')
	markdown = markdown.replace('\nPropriétés', '\n\\shortcutProprietes{}')
	markdown = markdown.replace('\nPropriété',  '\n\\shortcutPropriete{}')
	markdown = markdown.replace('\nProposition', '\n\\shortcutProposition{}')
	markdown = markdown.replace('\nThéorème',   '\n\\shortcutTheoreme{}')
	markdown = markdown.replace('\nLemme',      '\n\\shortcutLemme{}')
	markdown = markdown.replace('\nCorollaire', '\n\\shortcutCorollaire{}')
	markdown = markdown.replace('\nMéthode',    '\n\\shortcutMethode{}')
	markdown = markdown.replace('\nExemples',   '\n\\shortcutExemples{}')
	markdown = markdown.replace('\nExemple',    '\n\\shortcutExemple{}')
	markdown = markdown.replace('\nApplications',    '\n\\shortcutApplications{}')
	markdown = markdown.replace('\nApplication',    '\n\\shortcutApplication{}')
	
	# Surcharge de l'implémentation du package markdown pour les citations.
	# La surcharge est écrite en Python par flemme, je trouve cela pour le
	# moment beaucoup plus simple et plus facile à éditer.
	
	comment_styles = [
						['🧩', 'puzzle-piece', 'shadeGreen'],
						['🚨', 'police-car-light', 'shadeRed'],
						['💶', 'euro-banknote', 'shadeBlue'],
					]
	
	PLOTTEMPLATE = r"""
	\documentclass{standalone}

	\usepackage{../../utilities}

	\begin{document}
	\begin{tikzpicture}
		\begin{axis}[
			grid = major,
			axis line style = very thick,
			grid style={line width=1pt, draw=gray!50},
			axis equal image,
			xmin=$XMIN,xmax=$XMAX,
			ymin=$YMIN,ymax=$YMAX,
			xtick = {$XMIN,...,$XMAX},
			ytick = {$YMIN,...,$YMAX},
			axis lines=middle,
			axis line style={-Latex},
			ticks=none]
				$PLOTDATA
		\end{axis}
	\end{tikzpicture}
	\end{document}
	"""
	PLOTCURVETEMPLATE = r"""
	\addplot[
		domain=$XMIN:$XMAX,
		samples=200,
		color=blue,
		thick
		] {$EXPR};
	"""
	
	
	print('Pré-processing du markdown.')
	
	# "Pre-processor"
	
	plotnum = 1
	
	lines = markdown.split('\n')
	for li in range(len(lines)):
		if len(lines[li]) > 2 and lines[li][0] == '|' and lines[li][2] == ' ':
			emoji = lines[li][1]
			for comment_style in comment_styles:
				if comment_style[0] == emoji:
					lines[li] = r'\begin{boitecitation}['+comment_style[2]+r']\tikz[overlay]{\node at (-0.7,0.1) {\emoji{'+comment_style[1]+'}}}' + lines[li][3:] + r'\end{boitecitation}'
		elif len(lines[li]) > 2 and lines[li][0:2] == '! ':
			lines[li] = r'\docpart{'+lines[li][2:]+'}'
		elif len(lines[li]) > 1 and lines[li][0] == '📈':
			plotparams = lines[li][1:].split(';')
			plot_expr = plotparams[0]
			plot_xmin = plotparams[1]
			plot_xmax = plotparams[2]
			plot_ymin = plotparams[3]
			plot_ymax = plotparams[4]
			
			# TODO : plusieurs courbes sur un même schéma.
			latex_curve_form = PLOTCURVETEMPLATE.replace('$EXPR', plot_expr).replace('$XMIN', plot_xmin).replace('$XMAX', plot_xmax)
			latex_plot_form = PLOTTEMPLATE.replace('$PLOTDATA', latex_curve_form).replace('$XMIN', plot_xmin).replace('$XMAX', plot_xmax).replace('$YMIN', plot_ymin).replace('$YMAX', plot_ymax)
			
			fname = f'plot{plotnum}.tex'
			plotnum += 1
			
			with open('plots/'+fname, 'w+', encoding='utf-8') as f:
				f.write(latex_plot_form)
			
			lines[li] = r'\begin{figure}[H] \center \includegraphics{plots/'+fname+r'} \end{figure}'
	
	markdown = '\n'.join(lines)
	
	with open('PROCESSED.md', 'w', encoding='utf-8') as f:
		f.write(markdown)
	
	print('Compilation du LaTeX.')
	
	# Compilation
	subprocess.run(['lualatex','--output-directory=./output/', '--interaction=batchmode', 'main.tex'])
	
	print('Déplacement du pdf.')
	# Déplacement du résultat vers le dossier hôte des pdfs
	shutil.move(f'./output/main.pdf', f'./documents conv/{f_name}.pdf')




# Lister les documents à exporter
# Patch pour Maxence (avec le .DS_Store)
md_files = [f for f in listdir('./documents/') if isfile(join('./documents/', f)) and not ".DS" in f]

# On ne compile qu'un seul fichier
if len(sys.argv) > 1:
	f_name_closeform = sys.argv[1]
	
	best_match_fname = None
	best_match_ratio = -1
	for fname in md_files:
		sim = SequenceMatcher(None, f_name_closeform.upper(), fname.upper()).ratio()
		if sim > best_match_ratio:
			best_match_fname = fname
			best_match_ratio = sim
	
	# Si a bien trouvé un match
	if best_match_fname != None:
		convert_md('.'.join(best_match_fname.split('.')[:-1]),join('./documents/', best_match_fname))
	else:
		print(f"Aucun fichier dont le nom se rapproche suffisament de '{f_name_closeform}' n'a été trouvé.")
else:
	# On les compile tous
	for fname in md_files:
		convert_md('.'.join(fname.split('.')[:-1]),join('./documents/', fname))


# Liste d'émojis selon le paquet emojis latex
# https://distrib-coffee.ipsl.jussieu.fr/pub/mirrors/ctan/macros/luatex/latex/emoji/emoji-doc.pdf