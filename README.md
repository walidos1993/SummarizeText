# SummarizeText

Le projet a été fait avec Angular 7 comme interface , et Python comme API (FLASK)

Pour tester l'application faudra avoir nodejs + npm et angular installé et Python + quelque librairies (Flask aussi).

# Mise en place

Après installation des outils nécessaire, on doit démarrer les serveurs: pour l'interface Angular la commande est : ng serve
Pour l'api : se déplacer dans le dossier api et executer les deux commandes : export FLASK_APP=main.py (une seule fois durant l'instance) et  python -m flask run faudra avoir un fichier "output.txt" contenant les mots qui va servir pour résumer le texte (https://nlp.stanford.edu/projects/glove/ version anglaise ... il existe aussi en francais http://fauconnier.github.io/) faudra juste nommer le fichier en output.txt

# Fonctionnement

Fonctionnement par étape:

 1- On saisit le texte  sur le textarea:
on aura deux choix: soit compresser le texte c'est à dire d'enlever les mots inutils et  diminuer les mots
ou bien de résumer les texte en gardant que les phrases les plus importants
2- Dans les deux cas  angular va pouvoir transmettre le texte à l'api (serveur flask doit être executé) avec le taux de compression/résumer, puis ensuite en fonction de la tâche et les paramètre l'api va renvoyer le résultat pour que angular l'affiche.

# Description des fonctions de l'API
main.py> fonction summ est la fonction qui compresse le texte Paramètre (texte et le niveau :0 1 2) return text compressé
          Niveau 0: aucun changement
          Niveau 1: Nettoyer le texte et en enlevant les stopword (ou mot vide) des mots qui sont tellement commun qu'ils sont inutiles de l'indexer  ("ce" "avec" "que" ....)
          Niveau 2: Effectuer ee processus de « lemmatisation » qui consiste à représenter les mots (ou « lemmes ») sous leur forme canonique. Par exemple pour un verbe, ce sera son infinitif. Pour un nom, son masculin singulier. En conservant le sens des mots.

main.py> fonction resum est la fonction qui résume  le texte Paramètre (texte et le pourcentage :1 ->100) return text résumé
          Cette partie qui va utiliser le fichier contenant le vecteur des mots (output.txt) le but c'est d'associer un ensemble de mots à des mots qui rapproche le plus de leurs sense (similarité) pour en savoir plus : https://scoms.hypotheses.org/657

      
