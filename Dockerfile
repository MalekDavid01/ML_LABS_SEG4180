# Lightweight official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies first (for Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose the port Waitress will serve on
EXPOSE 5000

# Start the app (Waitress is launched from within app.py)
CMD ["python", "app.py"]