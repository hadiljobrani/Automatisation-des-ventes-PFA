import csv
import random
import os

def generer_ventes_csv(n: int, nom_fichier: str = "data/ventes.csv") -> None:
    os.makedirs(os.path.dirname(nom_fichier), exist_ok=True)

    entete = ["ID", "Prix", "Quantite", "Remise"]

    with open(nom_fichier, mode="w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(entete)

        for i in range(n):
            id_produit = 100 + i + 1
            prix       = round(random.uniform(5.0, 100.0), 2)
            quantite   = random.randint(1, 20)
            remise     = random.choice([0, 5, 10, 15, 20])
            writer.writerow([id_produit, prix, quantite, remise])

    print(f" ✅'{nom_fichier}' généré ({n} lignes).")