from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import io
import base64

# Cargar el modelo (asegúrate de tener el archivo modelo.keras en el directorio raíz)
model = load_model("modelo.keras")

app = Flask(__name__)

def preprocess_image(image):
    img = image.convert('L')
    img_inverted = ImageOps.invert(img)
    img_resized = img_inverted.resize((28, 28))
    img_array = np.array(img_resized) / 255.0
    img_expanded = np.expand_dims(img_array, axis=-1)
    img_batch = np.expand_dims(img_expanded, axis=0)
    return img_batch

@app.route('/')
def index():
    # Renderiza la página principal con la descripción y el canvas
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Obtener la imagen en formato Data URL
    img_data = data['image']
    header, encoded = img_data.split(',', 1)
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    
    # Preprocesar la imagen
    processed = preprocess_image(image)
    prediction = model.predict(processed)  # Obtiene un arreglo de probabilidades
    predicted_class = int(np.argmax(prediction))
    
    # Obtener el porcentaje de confianza para la clase predicha
    confidence = float(np.max(prediction))  # Valor en el rango [0, 1]
    confidence_percent = round(confidence * 100, 2)  # Convertir a porcentaje y redondear

    # Convertir la imagen procesada a Data URL para mostrarla en el frontend
    processed_img = processed[0, ..., 0] * 255.0
    processed_img = processed_img.astype(np.uint8)
    pil_img = Image.fromarray(processed_img, mode='L')
    buffered = io.BytesIO()
    pil_img.save(buffered, format="PNG")
    processed_image_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    processed_image_data = "data:image/png;base64," + processed_image_str
    
    # Mostrar el resultado en consola
    print(f"Número predicho: {predicted_class} con {confidence_percent}% de confianza")
    
    return jsonify({
        'predicted': predicted_class,
        'confidence': confidence_percent,
        'processed_image': processed_image_data
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
