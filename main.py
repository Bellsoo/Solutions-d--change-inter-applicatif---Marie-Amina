# Importation de FastAPI
from fastapi import FastAPI
# Importation d'autres outils FastAPI pour la sécurité
from fastapi import Header, HTTPException
# Importation de CORS qui est un mécanisme de sécurité des navigateurs.
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel



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


# Voici le lien pour tester dans swagger : http://localhost:8000/docs
# Pour l'exercice 2, nous avons try out le token, lorsqu'on met le bon token nous avons les informations 
# relatif aux personnages. Dans le cas d'un faux token, nous avons "token invaldie"




