# Charte de la rédaction — Le Mag du Rolly's

Le mag publie **un article par jour** sur rollyspub.com/mag : billard (snooker, pool, blackball, carambole) et fléchettes (steel et électroniques). Il est signé « L'équipe du Rolly's Pub ». Le ton est celui d'un journaliste sportif passionné qui écrit pour des joueurs de bar : précis, vivant, accessible, jamais condescendant.

## 1. Choisir le sujet du jour

1. **L'actualité prime toujours.** S'il y a eu une finale importante dans les dernières 48 h, c'est le sujet du jour. Par exemple : un major PDC, un tournoi classé WST, la Mosconi Cup, une Coupe du monde UMB, un titre français FFB/FFD ou un 9-darter/147 historique.
2. Sinon, on suit la **grille de la semaine** :

| Jour | Rubrique | Exemples |
|---|---|---|
| Lundi | Résultats du week-end | Résumé darts + billard des tournois terminés |
| Mardi | Guide billard | Règles 8-ball / 9-ball / blackball, effets, casse, choix de queue |
| Mercredi | Portrait ou analyse | Joueur en forme, tendance, chiffre marquant |
| Jeudi | Guide fléchettes | Checkouts, cricket, grip, matériel, cibles électroniques |
| Vendredi | Avant-programme | Enjeux des compétitions du week-end, horaires |
| Samedi | France & local | FFB, FFD, AFEBAS, ligues de fléchettes électroniques, Côte d'Azur |
| Dimanche | Grand format | Histoire, légendes, records, culture du jeu |

3. **Jamais deux fois le même sujet.** Vérifier `index.json` (titres déjà publiés) et `suivi.md` (fils rouges en cours) avant de choisir.

## 2. Vérifier avant d'écrire

- Recouper chaque résultat, score, date et lieu sur **au moins une source fiable et datée**. Les sources de référence :
  - circuits et fédérations : PDC, WDF, WST, UMB, Matchroom/WNT, FFB, FFD, AFEBAS ;
  - médias spécialisés : Sky Sports, Sporting Life, BBC Sport, Dartsnews, SnookerHQ, Totally Snookered, AZBilliards, Kozoom.
- Une information non confirmée **n'est pas publiée**, ou elle l'est avec la mention explicite « selon … » / « à confirmer ».
- Les dates sont absolues (« dimanche 4 octobre »), jamais « hier ».
- Les citations : aucune citation inventée. On ne cite un joueur que si la citation est publiée par une source, et on la traduit fidèlement.
- Pas de copie : on résume avec ses propres mots, au plus une courte citation par article.

## 3. Écrire

- **Titre** : informatif et accrocheur, avec le nom du joueur ou du tournoi. Maximum 110 caractères.
- **seo_title** : moins de 65 caractères, contenant le mot-clé principal.
- **description** (chapô) : 110 à 260 caractères. Il répond à « qui, quoi, où, quand ».
- **Corps** : 450 à 900 mots, en HTML simple. Balises autorisées : `<p>`, `<h2>`, `<h3>`, `<ul>`, `<ol>`, `<li>`, `<strong>`, `<em>`, `<a>`, `<blockquote>`, `<table>`, `<div class="encadre">`, `<div class="table-scroll">`. Pas de `<h1>`, pas de script.
- Structure type pour une actu :
  - attaque ;
  - le récit du match ;
  - un encadré pédagogique (une règle, un terme, un chiffre) ;
  - la suite du calendrier ;
  - une section **« Et au bar ? »** qui relie le sujet à la pratique amateur.
- **Liens internes** : 1 à 3 liens vers d'autres articles du mag (`/mag/slug`) ou vers les pages du Rolly's quand c'est naturel (`/billard-nice`, `/flechettes-nice`, `/mag/agenda`). Pas plus d'un lien commercial par article.
- **FAQ** (facultative, pour les guides) : 2 ou 3 questions-réponses courtes.
- **Typographie française** : espace avant `:` `;` `?` `!` ; guillemets « » ; noms de tournois en anglais quand c'est l'usage (World Grand Prix, UK Championship).

## 4. Format du fichier

Chaque article est un fichier `articles/<slug>.json` :

```json
{
  "slug": "mots-cles-en-minuscules-avec-tirets",
  "title": "…",
  "seo_title": "…",
  "description": "…",
  "category": "billard | flechettes | guides",
  "tags": ["actu", "pdc"],
  "type": "news | guide",
  "date": "2026-10-06T08:00:00+02:00",
  "updated": "2026-10-06T08:00:00+02:00",
  "image": "/images/img-flechette.jpg",
  "image_alt": "…",
  "body": "<p>…</p>",
  "faq": [{"q": "…", "a": "…"}],
  "sources": [{"title": "Média — titre (date)", "url": "https://…"}]
}
```

- `type: "news"` exige des `sources`.
- **Images disponibles** (photos du Rolly's, libres d'usage) : `/images/img-billard.jpg`, `/images/img-billard2.jpg`, `/images/img-billard3.jpg`, `/images/img-flechette.jpg`, `/images/img-flechette2.jpg`, `/images/img-flechette-bar.webp`, `/images/img-flechette-joueur.webp`, `/images/img-bar-match.webp`, `/images/img-salle.webp`, `/images/img-salle2.webp`, `/images/img-interieur.webp`, `/images/img-terrasse.webp`. Alterner pour ne pas reprendre l'image de l'article précédent. Le `image_alt` décrit la photo réelle, jamais le joueur dont parle l'article.
- Corriger un article publié : modifier le fichier et mettre à jour `updated`. Le site affichera « mis à jour le … ».

## 5. Publier

1. Écrire `articles/<slug>.json`.
2. Mettre à jour `agenda.json` si de nouvelles dates sont connues ; retirer les événements passés au besoin. Le site masque automatiquement ceux qui sont terminés.
3. Mettre à jour `suivi.md` : fils rouges, résultats à suivre, idées de sujets.
4. Lancer `python3 tools/build_index.py`. Il doit afficher `OK`, sinon corriger.
5. Commit puis push sur `main`. Le site récupère le nouvel article dans les 30 minutes.
