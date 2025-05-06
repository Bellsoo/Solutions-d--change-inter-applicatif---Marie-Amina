import requests
import json
import time

# URL de ton API locale
API_URL = "http://localhost:8000/scores"
TOKEN = "ceci_est_un_token"
FICHIER_JSON = "donnees_etl.json"

# Étape 1 : Charger les données depuis le fichier JSON
with open(FICHIER_JSON, "r", encoding="utf-8") as f:
    donnees = json.load(f)

# Étape 2 : Transformation simple : ajout d'un champ "avis"
for item in donnees:
    revenu = item.get("income_amount", 0)
    item["avis"] = "positif" if revenu > 1000000 else "neutre"

    # Ne garder que les champs utiles (tu peux adapter)
    item_nettoye = {
        "name": item.get("name", "Inconnu"),
        "city": item.get("city", "Non précisé"),
        "income_amount": revenu,
        "avis": item["avis"]
    }

    # Étape 3 : Envoi à l’API
    try:
        response = requests.post(
            API_URL,
            json=item_nettoye,
            headers={"token": TOKEN},
            timeout=10
        )

        # Vérification du résultat
        if response.status_code == 200:
            print(f"Envoyé : {item_nettoye['name']}")
        else:
            print(f"Erreur {response.status_code} pour {item_nettoye['name']}")
            print("Réponse :", response.text)

    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau pour {item_nettoye['name']} : {e}")

    # Pause entre les envois (évite surcharge serveur)
    time.sleep(0.3)
