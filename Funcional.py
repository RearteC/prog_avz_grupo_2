from pathlib import Path
import yaml
from typing import List, Dict

# Ruta del archivo YAML
PROBLEMS_PATH = Path("problems.yaml")

def cargar_preguntas(nuevas: List[Dict]):
    """
    Agrega nuevas preguntas al archivo YAML, preservando las existentes.
    """
    # Leer preguntas existentes si el archivo existe
    if PROBLEMS_PATH.exists():
        with PROBLEMS_PATH.open("r", encoding="utf-8") as f:
            existentes = yaml.safe_load(f) or []
    else:
        existentes = []

    # Agregar nuevas preguntas
    existentes.extend(nuevas)

    # Guardar todas las preguntas en YAML
    with PROBLEMS_PATH.open("w", encoding="utf-8") as f:
        yaml.dump(existentes, f, sort_keys=False, allow_unicode=True)

def main():
    # Ejemplo de nuevas preguntas a agregar
    nueva_pregunta = [
        {
            "title": "Calcula factorial",
            "description": "Calcula el factorial de un número dado",
            "input": "5",
            "output": "120"
        },
        {
            "title": "Suma dos números",
            "description": "Suma dos números enteros",
            "input": [3, 4],
            "output": 7
        }
    ]

    # Agregar preguntas al YAML
    cargar_preguntas(nueva_pregunta)
    print("Preguntas agregadas correctamente.")

if __name__ == "__main__":
    main()
