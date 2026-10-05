# Le Mag du Rolly's — contenus

Ce dépôt contient les articles du magazine billard & fléchettes publié sur **https://rollyspub.com/mag/**.

Le site récupère automatiquement `index.json`, les fichiers `articles/*.json` et `agenda.json` toutes les 30 minutes environ (voir `mag/lib.php` côté site).

- Règles éditoriales et format des articles : [REDACTION.md](REDACTION.md)
- Fils rouges et idées de sujets : [suivi.md](suivi.md)
- Validation + génération de l'index : `python3 tools/build_index.py`
