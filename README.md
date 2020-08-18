# Réponse évaluation pour le poste Inria / AP-HP

Voici une réponse sur les Questions :

## Question 1 

- Le notebook jupyter "Question1.ipynb" met en évidence les problèmes
de qualité de données (données incohérentes, données manquantes)


## Question 2

- La fonction Python `detect_duplicates` est dans le file "Question2.py" prend en parametère le dataframe `df_patient` et renvoit un nouveau dataframe après suppression des doublons. 
Puisque les données dupliquées ne sont pas identiques nous allons garder un seul dupliquant et supprimant les autres.
La logique de choix est de garder celui qui a le moins de valeurs manquantes et incohérentes.

## Question 3

- la fonction `detect_duplicates` testée par pytest ne contient pas des erreurs.

## Question 4

Dans cette question j'ai remplacé le notebook jupyter pour l'analyse exploratoire de données(EDA exploratory data analysis) par une application "EDA_app.py". Cet outil est plus rapide, plus efficace et facile à utilser.
L'application est composé de 4 parties dans le Menu:
* Home
* "Dédupliquer&Joindre" qui utilise le dataframe `df_patient` après la déduplication utilisant la fonction `detect_duplicates` , aussi fait la jointure entre les dataframes `df_patient` et `df_pcr`.
* "Pandas Profile" méthode d'EDA qui utilise le résultat de dataframe après jointure et fait un rapport EDA complet.
* "Sweetviz" autre méthode d'EDA qui utilise le résultat de dataframe après jointure et fait un rapport EDA complet.
* Contact

## Instructions

Utilisation de l'application : 
* Les librairies python : sqlalchemy , pandas , streamlit , codecs , pandas_profiling , streamlit.components.v1 , streamlit_pandas_profiling , sweetviz
* Run de l'application : changer vers le répertoire dans le command prompt et éxécuter 'streamlit run EDA_app.py'

Merci de me contacter si vous voulez plus d'informations sur l'app ou si vous rencontrez des problèmes lors de l'éxécution de code.


