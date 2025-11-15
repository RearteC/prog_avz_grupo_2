import gradio as gr
import requests

API_URL = "http://localhost:8000/predict"

tipos_propiedad = ["Departamento", "PH", "Casa"]

def predecir(barrio, superficie, ambientes, banios, tipo_prop):

    # === VALIDACIONES BÁSICAS ===
    if not barrio or barrio.strip() == "":
        return "Error: Escribí un barrio."

    if superficie is None or ambientes is None or banios is None:
        return "Error: Completá todos los valores numéricos."

    # Normalización
    barrio = barrio.strip()
    tipo_prop = tipo_prop.strip().title()

    payload = {
        "l3": barrio,
        "rooms": float(ambientes),
        "bathrooms": float(banios),
        "surface_total": float(superficie),
        "property_type": tipo_prop
    }

    try:
        r = requests.post(API_URL, json=payload)
        r.raise_for_status()
        data = r.json()

        if "prediction_usd" in data:
            return data["prediction_usd"]
        else:
            return f"Error inesperado en API: {data}"

    except Exception as e:
        return f"Error en la API: {e}"


iface = gr.Interface(
    fn=predecir,
    inputs=[
        gr.Textbox(label="Barrio (escribí el nombre exacto)"),
        gr.Number(label="Superficie (m²)"),
        gr.Number(label="Ambientes"),
        gr.Number(label="Baños"),
        gr.Dropdown(
    choices=[
        ("Departamento", "Departamento"),
        ("PH", "PH"),
        ("Casa", "Casa"),
    ],
    label="Tipo de propiedad"
)
    ],
    outputs=gr.Number(label="Precio estimado (USD)")
)

if __name__ == "__main__":
    iface.launch()
