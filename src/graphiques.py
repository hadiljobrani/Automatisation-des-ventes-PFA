import matplotlib.pyplot as plt

def afficher_graphiques(resultats: list) -> None:
    ids      = [str(r["ID"]) for r in resultats]
    ca_bruts = [r["CA_Brut"] for r in resultats]
    ca_nets  = [r["CA_Net"]  for r in resultats]
    tvas     = [r["TVA"]     for r in resultats]
    remises  = [r["Remise"]  for r in resultats]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Analyse des Ventes", fontsize=16, fontweight="bold")

    # ── Graphique 1 : CA Brut vs CA Net (barres groupées) ──
    x, width = range(len(ids)), 0.35
    axes[0,0].bar([i - width/2 for i in x], ca_bruts, width, label="CA Brut", color="#4C72B0")
    axes[0,0].bar([i + width/2 for i in x], ca_nets,  width, label="CA Net",  color="#55A868")
    axes[0,0].set_title("CA Brut vs CA Net par Produit")
    axes[0,0].set_xlabel("ID Produit")
    axes[0,0].set_ylabel("Montant (TND)")
    axes[0,0].set_xticks(list(x))
    axes[0,0].set_xticklabels(ids)
    axes[0,0].legend()
    axes[0,0].grid(axis="y", linestyle="--", alpha=0.5)

    # ── Graphique 2 : Répartition CA Net (camembert) ──
    axes[0,1].pie(
        ca_nets,
        labels=[f"ID {i}" for i in ids],
        autopct="%1.1f%%",
        startangle=140,
        colors=["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974"]
    )
    axes[0,1].set_title("Répartition du CA Net")

    # ── Graphique 3 : TVA par produit (barres horizontales) ──
    axes[1,0].barh(ids, tvas, color="#C44E52")
    axes[1,0].set_title("TVA par Produit")
    axes[1,0].set_xlabel("Montant TVA (TND)")
    axes[1,0].set_ylabel("ID Produit")
    axes[1,0].grid(axis="x", linestyle="--", alpha=0.5)

    # ── Graphique 4 : Remise par produit (courbe) ──
    axes[1,1].plot(ids, remises, marker="o", color="#8172B2", linewidth=2, markersize=8)
    axes[1,1].fill_between(ids, remises, alpha=0.2, color="#8172B2")
    axes[1,1].set_title("Remise (%) par Produit")
    axes[1,1].set_xlabel("ID Produit")
    axes[1,1].set_ylabel("Remise (%)")
    axes[1,1].grid(linestyle="--", alpha=0.5)
    for xi, yi in zip(ids, remises):
        axes[1,1].annotate(f"{yi}%", (xi, yi), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=9)

    plt.tight_layout()
    plt.savefig("data/graphiques_ventes.png", dpi=150)
    plt.show()
    print("✅ Graphique sauvegardé dans 'data/graphiques_ventes.png'")