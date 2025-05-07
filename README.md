# Solutions d’échange inter-applicatif – Projet FastAPI

Ce projet a été réalisé dans le cadre d'exercices pratiques visant à manipuler des échanges inter-applicatifs à l’aide de FastAPI, en simulant l’envoi, le traitement et la visualisation de données JSON.

## 🗂️ Structure générale des fichiers

```
📁 projet/
│
├── main.py                         # API FastAPI avec endpoints GET et POST
├── extraction_paginee.py          # Récupère les données depuis l’API ProPublica
├── send_traitement.py             # Envoie les données vers l’API /traitement
├── enrichir_resultats.py          # Ajoute des champs comme score_doublé et avis
├── renvoyer_vers_traitement.py    # Renvoie les données enrichies vers l’API
│
├── resultats_traitement.json      # Réponses initiales de l’API
├── resultats_enrichis.json        # Résultats enrichis (niveau + avis + score doublé)
├── donnees_filtrees.json          # Données extraites depuis l’API ProPublica
│
├── index.html                     # Interface pour tester /personnages
├── style.css                      # Style associé à la page HTML
```

## ⚙️ Environnement requis

- Windows
- Visual Studio Code
- Terminal PowerShell
- Python installé avec le launcher `py`
- FastAPI et Uvicorn installés (`pip install fastapi uvicorn`)

## ▶️ Lancer l’API FastAPI

```bash
uvicorn main:app --reload
```

Documentation Swagger :
```
http://localhost:8000/docs
```

## 📘 Partie 1 à 3 – Mise en place de l’API et test des endpoints

### `main.py`

Ce fichier contient :

- `GET /personnages` → sécurisé avec token
- `POST /scores` → reçoit un score
- `POST /traitement` → calcule un niveau
- `POST /webhook/personnage` → écrit dans un fichier
- CORS activé

## 📗 Partie 4 – Publier des données

### Exercice 1 – Endpoint `/traitement`
- Reçoit `{ nom, score }` → retourne `{ nom, score, niveau }`

### Exercice 2 – Envoyer des données

```bash
py extraction_paginee.py
py send_traitement.py
```

Résultats sauvegardés dans `resultats_traitement.json`

### Exercice 3 – Enrichissement et affichage

```bash
py enrichir_resultats.py
```

Ajoute un champ `score_doublé` et `avis`, puis affiche `nom + niveau + avis`

### Bonus – Repost des résultats enrichis

```bash
py renvoyer_vers_traitement.py
```

## 🌐 Interface HTML

`index.html` permet de tester `/personnages` avec un token depuis le navigateur.

## 🔐 Token requis

```
ceci_est_un_token
```

## ✅ Ordre d’exécution conseillé

1. `uvicorn main:app --reload`
2. `py extraction_paginee.py`
3. `py send_traitement.py`
4. `py enrichir_resultats.py`
5. `py renvoyer_vers_traitement.py`
