# Démarrer avec Python

Cet exercice est le fil rouge du cours Démarrer avec Python, publié sur OpenClassrooms. Sentez-vous libre de le forker pour faire vos propres modifications !

## Installation 

Installation des dépendances dans un environnement virtuel :

    virtualenv venv && source venv/bin/activate
    pip install -r requirements.txt

## Parser

Lancer le scraper :

- Commencer par supprimer l'ancien fichier :
    rm -rf output_file.json

- Puis lancer le scraper :
    scrapy runspider my_spider.py -o output_file.json

Exemple avec les citations de San Antonio :
    rm -rf s_a.json
    scrapy runspider san_antonio_scraper.py -o quotes.json

Une question, une interrogation ? Ecris-moi ! => http://www.c-m-s.co/fr/contact