# 📊 Automatisation des Ventes

> Projet Python de traitement automatique des données de ventes d'une entreprise e-commerce.  
> Matière : Logiciels | Faculté des Sciences de Tunis | 2025-2026

---

## 1. 📌 Description

Ce projet consiste à développer un programme Python qui génère automatiquement un fichier CSV de ventes, effectue des calculs financiers (CA Brut, CA Net, TVA), exporte les résultats et les visualise sous forme de graphiques.

L'objectif principal est de simuler un traitement de données réel en entreprise, en suivant la chaîne : **Données → Calcul → Résultats**


#2. ⚙️ Prérequis

Python 3.x
pip
Git
VS Code (recommandé)

2.**Structure du projet :**
```
Automatisation-des-ventes-PFA/
│
├── data/
│   ├── ventes.csv              ← généré automatiquement
│   └── resultats_final.csv     ← exporté après calculs
│
├── src/
│   ├── generate_data.py        ← génération du CSV
│   ├── data_loader.py          ← chargement des données
│   ├── calculer.py             ← calculs CA, TVA, remises
│   └── graphiques.py           ← visualisation Matplotlib
│
├── .venv/                      ← environnement virtuel
├── main.py                     ← point d'entrée principal
├── requirements.txt            ← bibliothèques du projet
└── README.md

## 3. 🛠️préparation :
**Étape 1 — Créer le repository GitHub**(Hadil)

1. Aller sur [github.com](https://github.com)
2. Cliquer sur **"New"** pour créer un nouveau repository
3. Nommer le repo : `Automatisation-des-ventes-PFA`
4. Cliquer sur **"Create repository"**
5. Copier le lien du repository

**Étape 2 — Initialiser Git localement**(Hadil)
```bash
git init
git add .
git commit -m "initial commit"
git remote add origin URL
git push -u origin main
```

**Étape 3 — Cloner le projet** *(Nour et Balkiss)*
```bash
git clone https://github.com/hadiljobrani/Automatisation-des-ventes-PFA.git
cd Automatisation-des-ventes-PFA
```

**Étape 4 — Créer et activer l'environnement virtuel**
```bash
python -m venv .venv
activation :
"ctrl+shift+p"

**Étape 5 — ## 4. 📦 requirements.txt

Le fichier `requirements.txt` contient toutes les bibliothèques nécessaires :

```
matplotlib
pandas
```

Pour le générer automatiquement :
```bash
pip freeze > requirements.txt```
```

## 4. 👥 Auteurs & Répartition du travail

**Hadil Jobrani** — `feature-Hadil`
Gestion des données :
génération automatique de `ventes.csv` avec n lignes choisies par l'utilisateur
lecture et préparation des données


**Nour** — `feature-Nour`
Traitement & Calcul : 
calcul du CA Brut, CA Net après remise ,TVA
organisation des données traitées.
export du fichier `resultats_final.csv`


**Balkiss** — `feature-Balkiss`
Résultats & Visualisation :
identification des meilleurs produits
création des graphiques avec Matplotlib.

---

## 5. 🌿 Workflow Git

Règles suivies pendant le projet :
- ✅ Chaque membre travaille sur sa propre branche
- ✅ `git pull origin main` avant de commencer
- ✅ Ne jamais travailler directement sur `main`
- ✅ Communication constante entre les membres

```
feature-Hadil   →  Pull Request  →  main ✅
feature-Nour    →  Pull Request  →  main ✅
feature-Balkiss →  Pull Request  →  main ✅
```

##6. 🚀 Lancement du projet:

Lancer le projet depuis la racine :
```bash
python main.py
```

Le programme demande le nombre de lignes à générer, puis exécute automatiquement toutes les étapes.

> ⚠️ Le fichier `ventes.csv` est **généré automatiquement** par le code — il n'est pas créé manuellement.

**Exemple d'exécution :**
```
=== Automatisation des Ventes ===

Combien de lignes voulez-vous générer ? 20
✅ 'data/ventes.csv' généré automatiquement (20 lignes).
✅ 20 lignes chargées depuis 'data/ventes.csv'.
✅ Calculs effectués.
✅ Résultats exportés dans 'data/resultats_final.csv'.
📊 Graphiques affichés.
