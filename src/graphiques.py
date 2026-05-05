import matplotlib.pyplot as plt
import csv

def charger_resultats(nom_fichier: str = "data/resultats_final.csv") -> list:
    resultats = []
    with open(nom_fichier, mode="r", encoding="utf-8") as fichier:
        reader = csv.DictReader(fichier)
        for ligne in reader:
            resultats.append({
                "ID"      : int(ligne["ID"]),
                "Prix"    : float(ligne["Prix"]),
                "Quantite": int(ligne["Quantite"]),
                "CA_Net"  : float(ligne["CA_Net"]),
                "TVA"     : float(ligne["TVA"])
            })
    return resultats


def afficher_graphiques(resultats: list) -> None:
    ids = [str(r["ID"]) for r in resultats]
    ca_nets = [r["CA_Net"] for r in resultats]
    quantites = [r["Quantite"] for r in resultats]
    tvas = [r["TVA"] for r in resultats]
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("📊 Analyse des Ventes", fontsize=16, fontweight='bold')
    
    # Graphique 1 : CA Net par produit
    ax1.bar(ids, ca_nets, color='steelblue', edgecolor='black')
    ax1.set_title("CA Net par Produit")
    ax1.set_xlabel("ID Produit")
    ax1.set_ylabel("CA Net (TND)")
    ax1.tick_params(axis='x', rotation=45)
    
    # Graphique 2 : Quantités vendues
    ax2.bar(ids, quantites, color='coral', edgecolor='black')
    ax2.set_title("Quantités Vendues par Produit")
    ax2.set_xlabel("ID Produit")
    ax2.set_ylabel("Quantité")
    ax2.tick_params(axis='x', rotation=45)
    
    # Graphique 3 : TVA par produit
    ax3.bar(ids, tvas, color='lightgreen', edgecolor='black')
    ax3.set_title("TVA par Produit")
    ax3.set_xlabel("ID Produit")
    ax3.set_ylabel("TVA (TND)")
    ax3.tick_params(axis='x', rotation=45)
    
    # Graphique 4 : Répartition CA Net (Pie Chart)
    colors = plt.cm.Set3(range(len(ids)))
    ax4.pie(ca_nets, labels=ids, autopct='%1.1f%%', colors=colors, startangle=90)
    ax4.set_title("Répartition du CA Net")
    
    plt.tight_layout()
    plt.savefig("data/graphiques_ventes.png", dpi=300, bbox_inches='tight')
    print("✅ Graphiques sauvegardés dans 'data/graphiques_ventes.png'")
    plt.show()
