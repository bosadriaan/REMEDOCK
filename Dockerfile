# Use an official Python runtime as a base image
FROM tiangolo/uvicorn-gunicorn:python3.11

# Create model directory
RUN mkdir -p /app/models

# Install sentence_transformers
RUN pip install sentence_transformers

# Pre-download Sentence Transformer model
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('distiluse-base-multilingual-cased-v1').save('/app/models/distiluse-base-multilingual-cased-v1')"

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
