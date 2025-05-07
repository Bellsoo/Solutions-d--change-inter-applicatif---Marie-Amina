# Importation de FastAPI
from fastapi import FastAPI
# Importation d'autres outils FastAPI pour la sécurité
from fastapi import Header, HTTPException
# Importation de CORS qui est un mécanisme de sécurité des navigateurs.
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import json
import os




# Création d'une instance de FastAPI
app = FastAPI()

# Configuration CORS : autorise les appels depuis tous les domaines
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, il faut remplacer l'étoile par une URL précise, dite "autorisée"
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les headers, y compris le token
)


# ---------------------
# GET /personnages
# ---------------------


# Déclaration d'un endpoint GET accessible via l'URL /personnages écurisé avec un token en header HTTP
@app.get("/personnages")
# Nous ajoutons la règle du token
def get_personnages(token: str = Header(...)):
    # Vérifie si le token est correct
    if token != "ceci_est_un_token":
        # Si ce n'est pas le bon token, renvoie une erreur 401
        raise HTTPException(status_code=401, detail="Token invalide")
    # Si le token est bon, renvoie la liste de personnages
    return [
        {"nom": "Naruto Uzumaki", "village": "Konoha"},
        {"nom": "Sasuke Uchiha", "village": "Konoha"}
    ]

# ---------------------
# POST /scores
# ---------------------
class Score(BaseModel):
    name: str
    city: str
    income_amount: float
    avis: str
    
# Sécurité par token
SECURE_TOKEN = "ceci_est_un_token"

# Endpoint POST sécurisé
@app.post("/scores")
def add_score(score: Score, token: str = Header(...)):
    if token != SECURE_TOKEN:
        raise HTTPException(status_code=401, detail="Token invalide")
    
    print(f"Nouveau score reçu : {score}")
    return {"message": "Score reçu avec succès", "data": score}




# ---------------------
# POST /webhook/personnage
# ---------------------

# Modèle pour recevoir un personnage via webhook
class WebhookPersonnage(BaseModel):
    nom: str
    score: int

# Endpoint webhook qui reçoit un personnage + calcule son niveau
@app.post("/webhook/personnage")
async def recevoir_personnage(data: WebhookPersonnage):
    nom = data.nom
    score = data.score

    # Calcul du niveau en fonction du score
    if score >= 90:
        niveau = "master"
    elif score >= 75:
        niveau = "expert"
    elif score >= 50:
        niveau = "intermédiaire"
    else:
        niveau = "débutant"

    # Création du dictionnaire enrichi
    personnage = {
        "nom": nom,
        "score": score,
        "niveau": niveau
    }


    # Chemin du fichier d'enregistrement
    chemin_fichier = "webhook_log.json"

    # Lecture ou création du fichier
    if os.path.exists(chemin_fichier):
        try:
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                contenu = json.load(f)
        except json.JSONDecodeError:
            contenu = []  # fichier vide ou corrompu
    else:
        contenu = []

    # Ajout du nouveau personnage
    contenu.append(personnage)

    # Écriture dans le fichier (en réécrivant toute la liste)
    with open(chemin_fichier, "w", encoding="utf-8") as f:
        json.dump(contenu, f, indent=2, ensure_ascii=False)
        
        
    print("Personnage reçu :", personnage)

    return {
        "status": "ok",
        "personnage": personnage
    }


# Voici le lien pour tester dans swagger : http://localhost:8000/docs
# Pour l'exercice 2, nous avons try out le token, lorsqu'on met le bon token nous avons les informations 
# relatif aux personnages. Dans le cas d'un faux token, nous avons "token invaldie"




