from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field
from typing import Optional

from sklearn.preprocessing import StandardScaler

# ==========================================================
#  CARGAR MODELO
# ==========================================================

MODEL_PATH = "../models/model_20251114_230213.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ==========================================================
#  CARGAR DATASET LIMPIO Y RECONSTRUIR PIPELINE COMPLETO
# ==========================================================

DATA_PATH = "../data/input_clean.csv" 

df = pd.read_csv(DATA_PATH)

# ======= Preprocesamiento real del entrenamiento =======

# Selección de columnas
df_pre = df.copy()
df_pre = df_pre[['l3','rooms','bathrooms','surface_total','price','property_type']]
df_pre = df_pre.dropna()

# Frequency Encoding
freq_l3 = df_pre['l3'].value_counts(normalize=True)
df_pre['l3_freq'] = df_pre['l3'].map(freq_l3)

# One Hot Encoding property_type
df_pre = pd.get_dummies(df_pre, columns=['property_type'], drop_first=True)

# Drop columna original de barrio
df_pre = df_pre.drop(columns=['l3'])

# Escalado numérico real
scaler = StandardScaler()
num_cols = ['surface_total', 'rooms', 'bathrooms']
df_pre[num_cols] = scaler.fit_transform(df_pre[num_cols])

# Columnas finales exactas
FINAL_COLUMNS = [
    c for c in df_pre.columns if c != "price"
]

# ==========================================================
#  FASTAPI
# ==========================================================

app = FastAPI(title="API Predicción Inmobiliaria")

class InputData(BaseModel):
    l3: str = Field(..., description="Nombre del barrio")
    rooms: float
    bathrooms: float
    surface_total: float
    property_type: str    # "Departamento", "PH", "Casa"


def preprocess(data: InputData):
    """
    Reproduce exactamente el preprocesamiento del entrenamiento.
    Sin PKL. Sin simulaciones.
    """

    # Frequency encoding real
    l3_freq = freq_l3.get(data.l3, 0)

    # One-hot encoding real
    pt_PH = 1 if data.property_type == "PH" else 0
    pt_Casa = 1 if data.property_type == "Casa" else 0

    # Escalado real
    rooms_s = scaler.transform([[data.surface_total, data.rooms, data.bathrooms]])[0][1]
    baths_s = scaler.transform([[data.surface_total, data.rooms, data.bathrooms]])[0][2]
    surf_s = scaler.transform([[data.surface_total, data.rooms, data.bathrooms]])[0][0]

    row = {
        "l3_freq": l3_freq,
        "rooms": rooms_s,
        "bathrooms": baths_s,
        "surface_total": surf_s,
        "property_type_PH": pt_PH,
        "property_type_Casa": pt_Casa
    }

    # Asegurar columnas finales como en entrenamiento
    for col in FINAL_COLUMNS:
        if col not in row:
            row[col] = 0

    df = pd.DataFrame([row])[FINAL_COLUMNS]

    return df

# ==========================================================
#  ENDPOINT
# ==========================================================

@app.post("/predict")
def predict(payload: InputData):
    X = preprocess(payload)
    pred = float(model.predict(X)[0])
    return {"prediction_usd": pred}

# ==========================================================
#  MAIN
# ==========================================================

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
