FROM python:3.8-slim

# Installer dépendances système
RUN apt-get update && apt-get install -y build-essential

# Installer BentoML et dépendances
RUN pip install --upgrade pip && pip install bentoml scikit-learn xgboost pandas

WORKDIR /bento

# Copier les fichiers du projet et le modèle enregistré localement
COPY . /bento
COPY saved_model /bento/saved_model

# Installer les dépendances python
RUN pip install -r requirements.txt

# NE PAS faire bentoml build, car le modèle n’est pas dans le BentoML store ici

# Exposer le port pour le service BentoML
EXPOSE 3000

# Démarrer le service avec python
CMD ["python", "service.py"]
