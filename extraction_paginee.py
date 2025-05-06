import requests
import json
import time

# URL de base de l'API 
API_URL = "https://projects.propublica.org/nonprofits/api/v2/search.json?q=chat&page="

# Liste où on va stocker toutes les données récupérées
toutes_donnees = []

# On commence à la page 0
page = 0

while True:
    print(f"Appel de la page {page}...")
    url = API_URL + str(page)

    try:
        # On envoie une requête GET à l'API
        response = requests.get(url, timeout=10)

        # Si le code retour est 200, on continue
        if response.status_code == 200:
            data = response.json()

            # On récupère la liste des organisations (résultats de cette page)
            organisations = data.get("organizations", [])

            # S'il n'y a plus de résultats → on sort de la boucle
            if not organisations:
                print(" Fin de pagination.")
                break

            # On filtre les résultats : ici, on garde ceux avec une ville définie
            organisations_filtrees = [
                org for org in organisations if org.get("city") and org.get("income_amount", 0) > 0
            ]

            # On ajoute les résultats filtrés à notre liste principale
            toutes_donnees.extend(organisations_filtrees)

            # Petite pause pour ne pas surcharger l'API
            time.sleep(0.5)

            # On passe à la page suivante
            page += 1

        else:
            print(f"Erreur HTTP {response.status_code}")
            break

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        break

# On enregistre toutes les données récupérées dans un fichier JSON
with open("donnees_filtrees.json", "w", encoding="utf-8") as f:
    json.dump(toutes_donnees, f, indent=2, ensure_ascii=False)

print(f"Terminé ! {len(toutes_donnees)} organisations enregistrées dans donnees_filtrees.json")
