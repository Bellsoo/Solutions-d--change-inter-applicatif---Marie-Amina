import requests
import json
import time

# URL de base de l'API ProPublica (recherche sur "chat")
API_URL = "https://projects.propublica.org/nonprofits/api/v2/search.json?q=chat&page="

# Nom du fichier dans lequel on va enregistrer les données filtrées
fichier_sortie = "donnees_filtrees.json"

# Liste où on stocke les résultats
toutes_donnees = []

# On démarre à la page 0
page = 0

# On limite à 10 pages maximum pour ne pas surcharger l'API
MAX_PAGES = 10

while page < MAX_PAGES:
    print(f"Appel de la page {page}...")
    url = API_URL + str(page)

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            # Correction ici : la clé s'appelle "organizations"
            organisations = data.get("organizations", [])

            if not organisations:
                print("Fin de pagination.")
                break

            # Pas de filtrage temporairement
            filtres = organisations

            # Ajout à la liste principale
            toutes_donnees.extend(filtres)

            page += 1
            time.sleep(0.5)

        else:
            print(f"Erreur HTTP {response.status_code}")
            break

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        break

# Sauvegarde des résultats dans un fichier JSON
with open(fichier_sortie, "w", encoding="utf-8") as f:
    json.dump(toutes_donnees, f, indent=2, ensure_ascii=False)

print(f"Terminé ! {len(toutes_donnees)} organisations enregistrées dans {fichier_sortie}")
