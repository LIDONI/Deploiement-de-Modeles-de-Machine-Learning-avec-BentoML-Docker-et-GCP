import bentoml
import pandas as pd
from typing import Dict, List, Union
from bentoml.io import JSON

# Charger le modèle
model_ref = bentoml.sklearn.get("xgb_multioutput_model:latest")
model_runner = model_ref.to_runner()

# Déclarer le service
svc = bentoml.Service("energy_predictor", runners=[model_runner])

# API avec le nouveau style
@svc.api(input=JSON(), output=JSON())
async def predict(input_data: Union[Dict, List[Dict]]):
    df = pd.DataFrame([input_data]) if isinstance(input_data, dict) else pd.DataFrame(input_data)
    predictions = await model_runner.predict.async_run(df)

    def format_prediction(pred):
        return {
            "SiteEnergyUse": max(0, float(pred[0])),
            "TotalGHGEmissions": max(0, float(pred[1])),
        }

    if len(predictions) == 1:
        return format_prediction(predictions[0])
    else:
        return [format_prediction(p) for p in predictions]
