
# Importation de FastAPI
from fastapi import FastAPI

# Création d'une instance de FastAPI
app = FastAPI()

# Déclaration d'un endpoint GET accessible via l'URL /personnages
@app.get("/personnages")
def get_personnages():
    # Retour d'une liste statique de personnages (format JSON)
    return [
        {"nom": "Naruto Uzumaki", "village": "Konoha"},
        {"nom": "Sasuke Uchiha", "village": "Konoha"}
    ]



# Voici le lien pour tester dans swagger : http://localhost:8000/docs