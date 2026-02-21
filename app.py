from flask import Flask, request, jsonify
from transformers import pipeline
from waitress import serve
import requests
from PIL import Image
from io import BytesIO

# Initialize Flask
app = Flask(__name__)

# Load pretrained ResNet-50 from HuggingFace
print("Loading model...")
classifier = pipeline("image-classification", model="microsoft/resnet-50")
print("Model loaded successfully!")


@app.route("/", methods=["GET"])
def home():
    """Health check endpoint."""
    return jsonify({"status": "running", "model": "ResNet-50 Image Classification"})


@app.route("/predict", methods=["POST"])
def predict():
    """
    POST /predict
    Accepts JSON body: {"image_url": "https://..."}
    Returns top 5 predictions in JSON format.
    """
    data = request.get_json()

    if not data or "image_url" not in data:
        return jsonify({"error": "Please provide an 'image_url' field in your JSON body."}), 400

    image_url = data["image_url"]

    # Download the image (with browser-like headers to avoid 403 blocks)
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        response = requests.get(image_url, timeout=10, headers=headers)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert("RGB")
    except Exception as e:
        return jsonify({"error": f"Could not load image from URL: {str(e)}"}), 400

    # Run ResNet-50 classification
    results = classifier(image, top_k=5)

    # Format predictions
    predictions = [
        {"label": r["label"], "confidence": round(r["score"], 4)}
        for r in results
    ]

    return jsonify({
        "image_url": image_url,
        "predictions": predictions
    }), 200


if __name__ == "__main__":
    # Serve with Waitress (production-grade WSGI server)
    print("Starting Waitress server on port 5000...")
    serve(app, host="0.0.0.0", port=5000)