# IncomeInference Project

## Descripción General

Este proyecto tiene como objetivo predecir los sueldos brutos de empleados utilizando diferentes algoritmos de regresión. Los modelos se entrenan y evalúan utilizando un conjunto de datos que ha sido preprocesado y escalado adecuadamente. Los algoritmos utilizados incluyen regresiones lineales, métodos basados en árboles, redes neuronales y técnicas de ensamble.

## Estructura del Proyecto

El proyecto está organizado en varias carpetas y archivos, cada uno dedicado a una parte específica del flujo de trabajo de machine learning.

### Descripción de los Directorios y Archivos

- **data/**: Contiene los conjuntos de datos utilizados en el proyecto.
  - **clean/**: Archivos de datos preprocesados y escalados.
  - **train_test_split/**: Conjuntos de datos divididos en entrenamiento y prueba.
  - **csv/**: Archivos CSV con nuevos datos para pruebas.

- **models/**: Contiene cuadernos de Jupyter para cada modelo de regresión utilizado.
  - **ordinary_least_squares_regression/**: Cuadernos específicos para el modelo de regresión lineal ordinaria.
    - `entrenamiento_modelo.ipynb`: Entrenamiento del modelo.
    - `validacion_modelo.ipynb`: Validación del modelo.
    - `analisis_resultados.ipynb`: Análisis de resultados.
    - `pruebas_nuevos_datos.ipynb`: Pruebas con nuevos datos.
  - **(otras carpetas de modelos)**: Estructura similar para otros modelos.

- **results/**: Contiene los resultados de los modelos entrenados y validados.

- **notebooks/**: Cuadernos de Jupyter generales.
  - `preparacion_datos.ipynb`: Preprocesamiento y preparación de datos.
  - `comparacion_modelos.ipynb`: Comparación de modelos para seleccionar el más óptimo.

- **requirements.txt**: Lista de bibliotecas necesarias para ejecutar el proyecto.

- **README.md**: Descripción general del proyecto.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/IncomeInference.git
