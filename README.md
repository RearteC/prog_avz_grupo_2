# Programación Avanzada para Ciencias de Datos - 2/2025

## Grupo 2 - Gradiente decadente
### - Diego Ottino
### - Cristian Percivati
### - Jorge Rearte
### - Omar Vivona

# Introducción

En este trabajo práctico analizamos un dataset de Properati que contiene información sobre precios de venta de inmuebles en Ciudad de Buenos Aires y el conurbano bonaerense. Para simplificar el análisis y concentrarnos en la zona con mayor disponibilidad de datos, trabajamos exclusivamente con las propiedades ubicadas en Capital Federal.

El objetivo central es desarrollar un modelo capaz de predecir el precio de venta de un inmueble a partir de sus características principales, tales como el barrio, la superficie, la cantidad de ambientes, los m² cubiertos, la cantidad de baños, entre otras variables relevantes. Para ello, el dataset puede ser tomado tanto desde una fuente SQL como desde un archivo CSV, lo que permite flexibilidad en la ingestión de datos según el contexto de trabajo.

Comenzamos con un Análisis Exploratorio de Datos (EDA) que incluye mapas, gráficos de barras y estudios de correlación. A través de estas visualizaciones buscamos comprender cómo se relacionan las variables independientes con la variable dependiente del estudio: el precio de venta del inmueble. Aunque variables como la cantidad de habitaciones o baños parecen tener cierta correlación con el precio, estas relaciones pueden resultar engañosas debido a su naturaleza discreta, lo que afecta el rendimiento de modelos paramétricos como la regresión lineal.

Por este motivo incorporamos modelos no paramétricos, como árboles de decisión y K-Nearest Neighbors (KNN), que capturan de manera más efectiva las relaciones no lineales presentes en los datos. En nuestros experimentos, los árboles de regresión fueron los modelos que obtuvieron el mejor rendimiento general. Es razonable suponer que un modelo más avanzado basado en árboles, como XGBoost Regressor, podría obtener un desempeño aún superior.

Para evaluar los modelos utilizamos diversas métricas:

1. R², para obtener una visión global del poder explicativo,
2. MSE y MAE, para medir la magnitud del error y su impacto en unidades reales,
3. Cross validation, aplicada en todos los modelos salvo en árboles profundos, donde el proceso se vuelve computacionalmente muy costoso.

Finalmente, registramos todas las evaluaciones y resultados en un documento almacenado en MongoDB Atlas. Cada vez que se ejecuta el proceso, se genera un nuevo documento que permite llevar un historial de las pruebas y mejoras del modelo, facilitando el análisis comparativo y la trazabilidad del desarrollo.
