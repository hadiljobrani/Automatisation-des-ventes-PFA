from src.generate_data import generer_ventes_csv
from src.data_loader   import charger_ventes
from src.generate_data import generer_ventes_csv
from src.data_loader   import charger_ventes
from src.calcul      import calculer_ventes, afficher_resultats, ca_total, meilleur_produit, exporter_resultats

def main():
    print("=== Automatisation des Ventes ===\n")

    try:
        n = int(input("Combien de lignes voulez-vous générer ? "))
        if n <= 0:
            print("❌ Entrez un nombre positif.")
            return
    except ValueError:
        print("❌ Entrée invalide.")
        return

    # Étape 1 : Générer le CSV
    generer_ventes_csv(n=n)

    # Étape 2 : Charger le CSV
    ventes = charger_ventes()

    # Étape 3 : calculer.py sera appelé ici ensuite
    print(f"\n 📦 Données prêtes : {len(ventes)} produits chargés.")

if __name__ == "__main__":
    main()


def main():
    print("=== Automatisation des Ventes ===\n")

    try:
        n = int(input("Combien de lignes voulez-vous générer ? "))
        if n <= 0:
            print("❌ Entrez un nombre positif.")
            return
    except ValueError:
        print("❌ Entrée invalide.")
        return

    # Étape 1 : Générer le CSV
    generer_ventes_csv(n=n)

    # Étape 2 : Charger le CSV
    ventes = charger_ventes()

    # Étape 3 : Calculer
    resultats = calculer_ventes(ventes)
    afficher_resultats(resultats)
    ca_total(resultats)
    meilleur_produit(resultats)
    exporter_resultats(resultats)

if __name__ == "__main__":
    main()


# Partie des graphiques 
import sys
sys.path.insert(0, "src")

from data_loader import charger_ventes
from calcul        import calculer_ventes
from graphiques    import afficher_graphiques

if __name__ == "__main__":

    # ── Chargement + Calculs + Graphiques ──
    ventes    = charger_ventes()
    resultats = calculer_ventes(ventes)
    afficher_graphiques(resultats)