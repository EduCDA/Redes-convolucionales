# Clasificación de Dígitos Manuscritos con Redes Convolucionales (CNN)

## Objetivo

El objetivo de este repositorio es entrenar un modelo de red neuronal convolucional (CNN) capaz de reconocer y clasificar correctamente dígitos manuscritos a partir de imágenes, utilizando el popular dataset MNIST. El modelo también permite predecir números en imágenes externas, tanto individuales como secuencias de varios dígitos.

## Descripción del Proyecto

El flujo de trabajo está documentado en el notebook `cnn.ipynb` y se compone de las siguientes etapas:

### 1. Importación de Librerías
Se utilizan librerías como TensorFlow, Keras, NumPy, Matplotlib, PIL y scikit-learn para el procesamiento de datos, construcción y entrenamiento del modelo.

### 2. Carga y Visualización de Datos
- Se descarga el dataset MNIST, que contiene imágenes de dígitos manuscritos (28x28 píxeles, escala de grises).
- Se visualizan ejemplos de imágenes y sus etiquetas para comprobar la correcta carga de los datos.

### 3. Preprocesamiento de Datos
- **Normalización:** Los valores de los píxeles se escalan al rango [0, 1].
- **Reformateo:** Se añade una dimensión de canal para adaptar las imágenes a la entrada de la CNN.
- **División:** El conjunto de datos se divide en entrenamiento, validación y test.

### 4. Aumentación de Datos
Se utiliza un generador de imágenes para aplicar transformaciones aleatorias (rotación, traslación, zoom, etc.) y así mejorar la robustez del modelo.

### 5. Construcción y Entrenamiento del Modelo
- Se define una arquitectura CNN con varias capas convolucionales, de pooling, flatten, densas y dropout.
- El modelo se compila con el optimizador Adam y la función de pérdida de entropía cruzada categórica.
- Se entrena el modelo utilizando el generador de aumentación de datos.

### 6. Predicción sobre Imágenes Externas
- Se implementan funciones para cargar, preprocesar y predecir el dígito en imágenes externas.
- Se incluye una función para predecir secuencias de varios dígitos en una sola imagen, segmentando y clasificando cada uno.

### 7. Guardado del Modelo
El modelo entrenado se guarda en formato Keras (`modelo.keras`) para su reutilización o despliegue en aplicaciones.

## ¿Cómo Funciona?

1. **Entrenamiento:** El modelo aprende a identificar patrones en imágenes de dígitos manuscritos mediante capas convolucionales y de pooling.
2. **Aumentación:** Se generan variaciones de las imágenes para mejorar la generalización.
3. **Predicción:** El modelo puede recibir una imagen nueva (o una secuencia de dígitos) y predecir el número representado.

## Estructura del Repositorio

- `cnn.ipynb`: Notebook principal con todo el flujo de trabajo y visualizaciones.
- `modelo.keras`: Modelo entrenado listo para usar.
- `Imagenes/`: Carpeta con imágenes de prueba (individuales y múltiples dígitos).
- `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.

## Requisitos

- Python 3.8+
- TensorFlow
- Keras
- numpy, matplotlib, pillow, scikit-learn

Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

1. Ejecuta el notebook `cnn.ipynb` paso a paso.
2. Prueba la predicción sobre imágenes propias ubicadas en la carpeta `Imagenes/`.
3. El modelo entrenado se guarda automáticamente y puede ser reutilizado.

## Notas
- El modelo puede ser ajustado modificando la arquitectura, los hiperparámetros o el esquema de aumentación de datos.
- Las funciones incluidas permiten predecir tanto dígitos individuales como secuencias de varios números en una sola imagen.
