import json
from transformers import pipeline
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

# Load pretrained ResNet-50
model = pipeline("image-classification", model="microsoft/resnet-50")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    image_url = request.data.decode("utf-8")

    try:
        output = model(image_url)
        return jsonify(output), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 415

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)