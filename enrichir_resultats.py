import json

# Fichier d'entrée (résultats existants)
fichier_entree = "resultats_traitement.json"

# Fichier de sortie (résultats enrichis)
fichier_sortie = "resultats_enrichis.json"

# Ouvrir les résultats existants
with open(fichier_entree, "r", encoding="utf-8") as f:
    personnages = json.load(f)

# Nouvelle liste enrichie
enrichis = []

# Règles d’avis selon niveau
avis_par_niveau = {
    "élite": "Excellent travail !",
    "expert": "Bravo !",
    "intermédiaire": "Continue comme ça.",
    "débutant": "À améliorer."
}

for p in personnages:
    nom = p.get("nom")
    niveau = p.get("niveau")
    score = p.get("score")

    # Calcul du score doublé
    score_double = score * 2

    # Récupération de l'avis
    avis = avis_par_niveau.get(niveau, "Aucun avis")

    # Affichage résumé
    print(f"{nom} → niveau : {niveau} → avis : {avis}")

    # Ajout à la liste enrichie
    enrichis.append({
        "nom": nom,
        "score": score,
        "niveau": niveau,
        "score_doublé": score_double,
        "avis": avis
    })

# Sauvegarde dans un nouveau fichier
with open(fichier_sortie, "w", encoding="utf-8") as f:
    json.dump(enrichis, f, indent=2, ensure_ascii=False)

print(f"\nRésultats enrichis enregistrés dans {fichier_sortie}")
