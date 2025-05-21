# API de Reconocimiento de Dígitos con Red Neuronal Convolucional

Esta aplicación web permite reconocer dígitos escritos a mano utilizando una red neuronal convolucional (CNN) entrenada con TensorFlow/Keras. El usuario puede dibujar un número en un canvas web y la aplicación mostrará la predicción del modelo junto con el porcentaje de confianza de la predicción.

## Características principales
- Interfaz web sencilla para dibujar dígitos.
- Procesamiento de la imagen y predicción en tiempo real usando un modelo CNN.
- Muestra el número predicho y el porcentaje de exactitud (confianza) de la predicción.
- Visualización de la imagen procesada que se envía al modelo.

## ¿Cómo funciona?
1. El usuario dibuja un número en el canvas de la página principal.
2. Al enviar la imagen, esta se convierte y preprocesa para adaptarse al formato de entrada del modelo (escala de grises, inversión de colores, redimensionado a 28x28 píxeles, normalización).
3. El modelo CNN predice el dígito y calcula la probabilidad asociada a la predicción.
4. Se muestra el resultado en la web: el número predicho y el porcentaje de confianza.

## Requisitos
- Python 3.x
- Flask
- TensorFlow
- Pillow
- Numpy

Instala las dependencias con:
```
pip install -r requirements.txt
```

## Ejecución
1. Asegúrate de tener el archivo `modelo.keras` en el directorio `API_Cnn`.
2. Ejecuta la aplicación:
```
python app.py
```
3. Abre tu navegador en [http://localhost:5000](http://localhost:5000)

## Estructura del proyecto
- `app.py`: Código principal de la API Flask.
- `modelo.keras`: Modelo CNN entrenado para reconocimiento de dígitos.
- `templates/index.html`: Interfaz web para dibujar y enviar el dígito.

## Notas
- El modelo debe estar entrenado para reconocer dígitos (por ejemplo, usando el dataset MNIST).
- El porcentaje de exactitud indica la confianza del modelo en la predicción realizada.

---
Desarrollado para fines educativos y de demostración de redes neuronales convolucionales en aplicaciones web.
