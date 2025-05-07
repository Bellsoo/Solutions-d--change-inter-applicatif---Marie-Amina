import requests
import json

# URL de l'API de traitement
API_URL = "http://localhost:8000/traitement"

# Chemin vers le fichier JSON d'entrée
FICHIER_ENTREE = "donnees_filtrees.json"

# Fichier où on va sauvegarder les résultats 
FICHIER_SORTIE = "resultats_traitement.json"

# Chargement des données depuis le fichier JSON
with open(FICHIER_ENTREE, "r", encoding="utf-8") as f:
    personnages = json.load(f)

# Liste pour stocker les réponses de l'API
resultats = []

# Envoi de chaque personnage vers /traitement
for p in personnages:
    data = {
        "nom": p.get("name", "Inconnu"),      # récupère le champ name, si il n'y a pas de name => inconnu
        "score": int(p.get("income_amount", 0))  # récupère le revenu du personnage, sinon 0
    }

    try:
        response = requests.post(API_URL, json=data, timeout=10)

        if response.status_code == 200:
            print(f"Envoyé : {data['nom']}")
            resultat = response.json()
            resultats.append(resultat)
        else:
            print(f"Erreur {response.status_code} pour {data['nom']}")
    except requests.exceptions.RequestException as e:
        print(f"Problème réseau avec {data['nom']} : {e}")

# On va sauvegarder des résultats dans un fichier
with open(FICHIER_SORTIE, "w", encoding="utf-8") as f:
    json.dump(resultats, f, indent=2, ensure_ascii=False)

print(f"Traitement terminé : {len(resultats)} éléments traités")
