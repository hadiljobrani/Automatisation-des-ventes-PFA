import csv

def charger_ventes(nom_fichier: str = "data/ventes.csv") -> list:
    ventes = []

    with open(nom_fichier, mode="r", encoding="utf-8") as fichier:
        reader = csv.DictReader(fichier)
        for ligne in reader:
            ventes.append({
                "ID"      : int(ligne["ID"]),
                "Prix"    : float(ligne["Prix"]),
                "Quantite": int(ligne["Quantite"]),
                "Remise"  : float(ligne["Remise"])
            })

    print(f" ✅ {len(ventes)} lignes chargées depuis '{nom_fichier}'.")
    return ventes