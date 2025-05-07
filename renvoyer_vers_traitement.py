import requests
import json

# Fichier contenant les données enrichies
fichier_entree = "resultats_enrichis.json"

# URL de l’API de traitement
url = "http://localhost:8000/traitement"

# Charger les données enrichies
with open(fichier_entree, "r", encoding="utf-8") as f:
    personnages = json.load(f)

# Liste pour stocker les réponses de l’API
reponses = []

# Envoi un par un vers /traitement
for p in personnages:
    # On garde seulement les champs attendus par l’API
    data = {
        "nom": p.get("nom"),
        "score": p.get("score")
    }

    try:
        response = requests.post(url, json=data, timeout=10)

        if response.status_code == 200:
            print(f"Envoyé à /traitement : {data['nom']}")
            reponses.append(response.json())
        else:
            print(f"Erreur {response.status_code} pour {data['nom']}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau avec {data['nom']} : {e}")

# Sauvegarde dans un nouveau fichier
with open("reponses_depuis_enrichis.json", "w", encoding="utf-8") as f:
    json.dump(reponses, f, indent=2, ensure_ascii=False)

print(f"\n{len(reponses)} éléments renvoyés à /traitement et sauvegardés.")
