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
    try:
        data = request.get_json()
        image_url = data.get("image_url")

        if not image_url:
            return jsonify({"error": "Missing 'image_url' in request"}), 400

        predictions = model(image_url)

        return jsonify({
            "input": image_url,
            "predictions": predictions
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 415

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)