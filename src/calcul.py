import csv
import os

def calculer_ventes(ventes: list) -> list:
    resultats = []

    for v in ventes:
        ca_brut = v["Prix"] * v["Quantite"]
        ca_net  = ca_brut * (1 - v["Remise"] / 100)
        tva     = ca_net * 0.20

        resultats.append({
            "ID"      : v["ID"],
            "Prix"    : v["Prix"],
            "Quantite": v["Quantite"],
            "Remise"  : v["Remise"],
            "CA_Brut" : round(ca_brut, 2),
            "CA_Net"  : round(ca_net, 2),
            "TVA"     : round(tva, 2)
        })

    return resultats


def afficher_resultats(resultats: list) -> None:
    print("\n=== Résultats des calculs ===")
    for r in resultats:
        print(f"ID {r['ID']} | CA Brut: {r['CA_Brut']} | CA Net: {r['CA_Net']} | TVA: {r['TVA']}")


def ca_total(resultats: list) -> float:
    total = sum(r["CA_Net"] for r in resultats)
    print(f"\n=== CA Total de l'entreprise : {round(total, 2)} TND ===")
    return round(total, 2)


def meilleur_produit(resultats: list) -> int:
    meilleur = max(resultats, key=lambda r: r["CA_Net"])
    print(f"=== Produit avec le plus gros bénéfice : ID {meilleur['ID']} ===")
    return meilleur["ID"]


def exporter_resultats(resultats: list, nom_fichier: str = "data/resultats_final.csv") -> None:
    os.makedirs(os.path.dirname(nom_fichier), exist_ok=True)

    entete = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]

    with open(nom_fichier, mode="w", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=entete)
        writer.writeheader()
        writer.writerows(resultats)

    print(f"✅ Fichier '{nom_fichier}' exporté avec succès !")