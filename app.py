# Serve model as a flask application

import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

model = pickle.load(open('iris_trained_model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        init_features = [float(x) for x in request.form.values()]
        data = [np.array(init_features)]
        prediction = model.predict(data)  
    if prediction[0] == 0:
        final_value = 'Setosa'
    if prediction[0] == 1:
        final_value = 'Versicolor'
    if prediction[0] == 2:
        final_value = 'Virginica'
    return render_template('index.html', prediction_text='Predicted Class: {}'.format(final_value)) # rendering the predicted result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


    