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
    # Préparation des données au format attendu par l'API
    data = {
        "nom": p.get("name", "inconnu"),
        "score": int(p.get("income_amount", 0))
    }

    try:
        response = requests.post(API_URL, json=data, timeout=10)

        if response.status_code == 200:
            resultat = response.json()
            nom = resultat.get("nom")
            niveau = resultat.get("niveau")

            # Résumé affiché dans la console
            print(f"{nom} → niveau calculé : {niveau}")

            resultats.append(resultat)
        else:
            print(f"Erreur {response.status_code} pour {data.get('nom', 'inconnu')}")

    except requests.exceptions.RequestException as e:
        print(f"Problème réseau avec {data.get('nom', 'inconnu')} : {e}")

# Sauvegarde des résultats dans un fichier
with open(FICHIER_SORTIE, "w", encoding="utf-8") as f:
    json.dump(resultats, f, indent=2, ensure_ascii=False)

print(f"\nTraitement terminé : {len(resultats)} éléments traités et enregistrés dans {FICHIER_SORTIE}")
