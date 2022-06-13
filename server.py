import tensorflow as tf
from tensorflow import keras
import numpy as np

from flask import Flask, request, jsonify

model = keras.models.load_model("locasee_model_final.h5")

def classify(nearest_office, nearest_school):
    arr = np.array([[nearest_office, nearest_school]]) # Convert to numpy array
    arr = arr.astype(np.float64) # Change the data type to float
    prediction = np.argmax(model.predict(arr), axis=1) # Retrieve from dictionary
    if prediction == 4:
        prediction = "A"
    elif prediction == 3:
        prediction = "B"
    elif prediction == 2:
        prediction = "C"
    elif prediction == 1:
        prediction = "D"
    elif prediction == 0:
        prediction = "E"
    return prediction # Return the prediction

app = Flask(__name__)

@app.route("/classify", methods=["GET"])
def classify_type():
    try:
        nearest_office = request.args.get('nearest_office')
        nearest_school = request.args.get('nearest_school')
        prediction = classify(nearest_office, nearest_school)
        data = {"prediction": prediction}
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run()