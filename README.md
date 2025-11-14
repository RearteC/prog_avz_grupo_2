# Programación Avanzada para Ciencias de Datos - 2/2025

## Grupo 2 - Gradiente decadente
### - Diego Ottino
### - Cristian Persivati
### - Jorge Rearte
### - Omar Vivona

# Introducción

En este trabajo práctico analizamos un dataset de Properati que contiene información sobre precios de venta de inmuebles en Ciudad de Buenos Aires y el conurbano bonaerense. Para simplificar el análisis y concentrarnos en la región con mayor densidad de datos, trabajamos exclusivamente con las propiedades ubicadas en Capital Federal.

El objetivo principal es desarrollar un modelo capaz de predecir el precio de venta de un inmueble a partir de sus características, tales como el barrio, la superficie, la cantidad de ambientes, los m² cubiertos, la cantidad de baños, entre otras variables relevantes.

Comenzamos realizando un Análisis Exploratorio de Datos (EDA) que incluye visualizaciones como mapas, gráficos de barras y matrices de correlación. A partir de estos gráficos buscamos interpretar cómo se relacionan las variables independientes con la variable dependiente del estudio: el precio de venta del inmueble.

En una primera aproximación, variables como la cantidad de habitaciones y baños parecen tener una relación directa con el precio. Sin embargo, estas variables son discretas, lo que puede sesgar el rendimiento de modelos paramétricos como la regresión lineal.

Por este motivo, complementamos el análisis utilizando modelos no paramétricos, como árboles de decisión y K-Nearest Neighbors (KNN). Estos modelos capturan mejor las relaciones no lineales presentes en los datos. Observamos que variables como la superficie cubierta y el barrio resultan ser las que mejor explican el precio final, especialmente cuando se emplean métodos basados en distancias como kNN.

A lo largo del notebook desarrollamos cada una de estas etapas, justificando las decisiones metodológicas en función de los resultados obtenidos y evaluando la capacidad predictiva de los distintos modelos probados.
