#  Prédiction de la consommation d’énergie des bâtiments de Seattle  
### Déploiement de modèles de Machine Learning avec **BentoML**, **Docker** et **Google Cloud Platform (GCP)**  

---

##  Contexte du projet  
La ville de **Seattle** vise la neutralité carbone d’ici **2050**.  
Pour y parvenir, la municipalité souhaite mieux comprendre et anticiper la **consommation d’énergie** et les **émissions de CO₂** des bâtiments **non résidentiels**.  

Les données collectées en 2016 servent de base pour construire un **modèle prédictif** capable d’estimer la consommation énergétique à partir des caractéristiques structurelles des bâtiments (taille, usage, année de construction, localisation, etc.).  

Ce projet s’inscrit dans une démarche de **valorisation de la donnée urbaine** pour la **transition énergétique**.

---

##  Objectifs

- Réaliser une **analyse exploratoire** (EDA) pour identifier les variables clés influençant la consommation énergétique.  
- Entraîner plusieurs **modèles supervisés** et sélectionner le plus performant.  
- Déterminer les **facteurs principaux** influençant la prédiction (feature importance, SHAP).  
- **Industrialiser** le modèle avec **BentoML** et le **déployer dans un conteneur Docker** sur **GCP**.  

---

## Stack technique

| Domaine | Technologies |
|----------|---------------|
| Langage principal | Python 3.10 |
| Data Science | Pandas, NumPy, Scikit-learn, XGBoost |
| Visualisation | Matplotlib, Seaborn |
| MLOps / Déploiement | BentoML, Docker, Google Cloud Run |
| Cloud | Google Cloud Platform (GCP) |
| APIs / Backend | Flask / FastAPI via BentoML Service |
| Autres | Git, GitHub Actions |

---

## Structure du projet

├── Dockerfile # Image Docker pour le déploiement

├── bentofile.yaml # Configuration BentoML du service

├── energy_pred.ipynb # Notebook d'analyse et d'entraînement du modèle

├── import_model.py # Script d'import et d'enregistrement du modèle

├── service.py # Service BentoML exposant l'API de prédiction

├── input.json # Exemple de requête d'entrée

├── requirements.txt # Dépendances Python

├── README.md # Ce fichier 

└── .gitignore


## Auteur

👤 Khalid OURO-ADOYI
Data Analyst & Data Engineer 

Email : khalidouroadoyi@gmail.com
LinkedIn :(https://www.linkedin.com/in/khalid-ouro-adoyi/) | 
[GitHub](https://github.com/LIDONI)
