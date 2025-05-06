
# Importation de FastAPI
from fastapi import FastAPI
# Importation d'autres outils FastAPI pour la sécurité
from fastapi import Header, HTTPException

# Création d'une instance de FastAPI
app = FastAPI()

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



# Voici le lien pour tester dans swagger : http://localhost:8000/docs
# Pour l'exercice 2, nous avons try out le token, lorsqu'on met le bon token nous avons les informations 
# relatif aux personnages. Dans le cas d'un faux token, nous avons "token invaldie"
