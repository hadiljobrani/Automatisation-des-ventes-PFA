from src.generate_data import generer_ventes_csv
from src.data_loader   import charger_ventes

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