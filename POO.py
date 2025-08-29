from pathlib import Path
import yaml
from typing import List, Dict

PROBLEMS_PATH = Path("problems.yaml")

class Preguntas:
    def __init__(self, title, prompt, hints=None, tags=None):
        self.title = title
        self.prompt = prompt
        self.hints = hints or []
        self.tags = tags or []

    def mostrar(self):
        print(self.title, self.prompt, self.hints, self.tags)

    @classmethod
    def cargar_preguntas(cls, nuevas: List[Dict]):
        """
        Agrega nuevas preguntas al archivo YAML.
        Cada pregunta debe ser un diccionario con keys: title, prompt, hints, tags
        """
        # Leer preguntas existentes si el archivo existe
        if PROBLEMS_PATH.exists():
            with PROBLEMS_PATH.open("r", encoding="utf-8") as f:
                existentes = yaml.safe_load(f) or []
        else:
            existentes = []

        # Convertir instancias nuevas a diccionarios si vienen como objetos Preguntas
        nuevas_convertidas = []
        for p in nuevas:
            if isinstance(p, cls):
                nuevas_convertidas.append({
                    "title": p.title,
                    "prompt": p.prompt,
                    "hints": p.hints,
                    "tags": p.tags
                })
            elif isinstance(p, dict):
                nuevas_convertidas.append(p)
            else:
                raise ValueError("Cada elemento debe ser un dict o una instancia de Preguntas")

        # Agregar nuevas preguntas
        existentes.extend(nuevas_convertidas)

        # Guardar todas las preguntas en YAML
        with PROBLEMS_PATH.open("w", encoding="utf-8") as f:
            yaml.dump(existentes, f, sort_keys=False, allow_unicode=True)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de Preguntas
    p1 = Preguntas(
        title="Calcula factorial",
        prompt="Calcula el factorial de un número dado",
        hints=["Usa recursión", "Recuerda que 0! = 1"],
        tags=["matemáticas", "factorial"]
    )
    p2 = {
        "title": "Suma dos números",
        "prompt": "Suma dos números enteros",
        "hints": ["Usa el operador +"],
        "tags": ["matemáticas", "suma"]
    }

    # Cargar al YAML
    Preguntas.cargar_preguntas([p1, p2])
    print("Preguntas agregadas correctamente.")






