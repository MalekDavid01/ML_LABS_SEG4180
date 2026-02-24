# ResNet-50 Image Classification Service

## Overview
This project deploys a pretrained ResNet-50 image classification model from Hugging Face using Flask and Waitress.  
The service exposes a REST API endpoint (`POST /predict`) that accepts image input in JSON format and returns classification predictions in JSON.

Model used: microsoft/resnet-50 (HuggingFace Transformers)  
Framework: Flask  
Application Server: Waitress  
Port: 5000


## Docker Hub
Image: https://hub.docker.com/r/dvdmalek/model-service

## Instructions for Running the Container Locally

### Prerequisites
- Docker Desktop installed and running

### Step 1: Pull the image from Docker Hub
```
docker pull dvdmalek/resnet50-service:latest
```

### Step 2: Run the container
```
docker run -p 5000:5000 dvdmalek/resnet50-service:latest
```

### Step 3: Send a prediction request

Using curl (Command Prompt):
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"image_url\": \"https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg\"}"
```

Using PowerShell:
```
Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST -ContentType "application/json" -Body '{"image_url": "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg"}'
```

### Alternative: Run using docker-compose
```
docker-compose up
```

---

## Files Included

- app.py
- Dockerfile
- requirements.txt
- docker-compose.yml
- README.md

---

## Notes
- The application uses Waitress as the production WSGI server.
- Port 5000 is exposed in the Docker container.
- The model is automatically downloaded from HuggingFace when the container starts.
- The API expects image input via URL (JSON format).