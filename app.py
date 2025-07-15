from flask import Flask, render_template, request
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Load the trained model
with open('classifier1.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    Nitrogen = float(request.form.get('Nitrogen'))
    Potassium = float(request.form.get('Potassium'))
    Phosphorous = float(request.form.get('Phosphorous'))

    # Perform prediction
    result = model.predict(np.array([[Nitrogen, Potassium, Phosphorous]]))

    # Map prediction result to fertilizer names
    fertilizer_map = {
        0: "10:10:10 NPK",
        1: "10:26:26 NPK",
        2: "12:32:16 NPK",
        3: "18:46:00 NPK",
        4: "19:19:19 NPK",
        5: "20:20:20 NPK",
        6: "20:20:20 NPK",
        7: "50:26:26 NPK",
        8: "Ammonium Sulphate",
        9: "Chilated Micronutrient",
        10: "DAP",
        11: "Ferrous Sulphate",
        12: "Hydrated Lime",
        13: "MOP",
        14: "SSP",
        15: "Sulphur",
        16: "UREA",
        17: "13:32:26 NPK",
        18: "White Potash"
    }

    # Get the fertilizer name based on the prediction
    fertilizer_name = fertilizer_map.get(result[0], "Unknown Fertilizer")

    # Pass the result to the template
    return render_template('index.html', result=fertilizer_name)

if __name__ == '__main__':
    app.run(debug=True)