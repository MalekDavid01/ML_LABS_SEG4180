# ResNet-50 Image Classification Service

A REST API that serves a pretrained ResNet-50 image classification model from HuggingFace (microsoft/resnet-50).

The service is built with Flask, served using Waitress, and containerized with Docker.

## Docker Hub
Image: https://hub.docker.com/r/dvdmalek/resnet50-service

---

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

After executing this command, your container should be running locally. 

### Step 3: Test the API

**POST /predict** — Send an image URL, get back classification predictions.

#### Windows (cmd) / macOS / Linux:
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"image_url\": \"https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg\"}"
```

#### Windows (PowerShell):
```powershell
Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST -ContentType "application/json" -Body '{"image_url": "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg"}'
```

---

## Sample Requests

### Cat
**curl (cmd / macOS / Linux):**
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"image_url\": \"https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg\"}"
```
**PowerShell:**
```powershell
Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST -ContentType "application/json" -Body '{"image_url": "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg"}'
```

### Monkey
**curl (cmd / macOS / Linux):**
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"image_url\": \"https://api.hub.jhu.edu/factory/sites/default/files/styles/landscape/public/monkey092018.jpg\"}"
```
**PowerShell:**
```powershell
Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST -ContentType "application/json" -Body '{"image_url": "https://api.hub.jhu.edu/factory/sites/default/files/styles/landscape/public/monkey092018.jpg"}'
```

### Basketball
**curl (cmd / macOS / Linux):**
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"image_url\": \"https://images.pexels.com/photos/358042/pexels-photo-358042.jpeg\"}"
```
**PowerShell:**
```powershell
Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST -ContentType "application/json" -Body '{"image_url": "https://images.pexels.com/photos/358042/pexels-photo-358042.jpeg"}'
```

### Dog
**curl (cmd / macOS / Linux):**
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"image_url\": \"https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg\"}"
```
**PowerShell:**
```powershell
Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST -ContentType "application/json" -Body '{"image_url": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg"}'
```

---

## Notes
- The API expects a JSON body containing image_url.
- The API is built with Flask and served using Waitress.
- The model used is microsoft/resnet-50 from HuggingFace.
- Some image URLs may return errors if the hosting server blocks automated requests.
- The container exposes port 5000.