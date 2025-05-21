# Proyecto: Reconocimiento de Dígitos con Red Neuronal Convolucional

Este repositorio contiene dos componentes principales:

## 1. Notebook de Entrenamiento de la Red Neuronal Convolucional
- **Ubicación:** `Redes_convolucionales/cnn.ipynb`
- En este notebook se desarrolla todo el proceso de entrenamiento de una red neuronal convolucional (CNN) para el reconocimiento de dígitos escritos a mano.
- Incluye la carga de datos, preprocesamiento, definición y entrenamiento del modelo, así como la evaluación de su desempeño.
- Al finalizar, se guarda el modelo entrenado en el archivo `modelo.keras` para su uso posterior.

## 2. Aplicación Web para Predicción de Dígitos
- **Ubicación:** `Redes_convolucionales/API_Cnn/`
- Esta carpeta contiene una aplicación web desarrollada con Flask.
- Permite al usuario dibujar un número en un canvas desde el navegador web.
- La imagen dibujada se envía al backend, donde el modelo previamente entrenado (guardado como `modelo.keras`) realiza la predicción del dígito.
- La aplicación muestra el número predicho junto con el porcentaje de exactitud (confianza) del modelo.
- El archivo principal de la aplicación es `app.py` y la interfaz web se encuentra en `templates/index.html`.

---

**Resumen:**
- Entrena tu propio modelo CNN en el notebook y pruébalo fácilmente desde la web integrada.
- Ideal para experimentar con reconocimiento de dígitos y despliegue de modelos de deep learning en aplicaciones web.
