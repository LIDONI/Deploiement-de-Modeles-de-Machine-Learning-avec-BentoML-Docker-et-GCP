import bentoml
import joblib

# Charge ton modèle localement depuis le fichier joblib ou pkl
model = joblib.load("xgb_multioutput_model.pkl")

# Enregistre-le avec un nom clair
bentoml.sklearn.save_model("xgb_multioutput_model", model)
