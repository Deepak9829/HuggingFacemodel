# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY fetch_huggingface_top_models.py /app/

# Install any needed packages specified in requirements.txt
RUN pip install requests

# Create a directory for the report
RUN mkdir -p /report

# Run fetch_huggingface_top_models.py when the container launches
CMD ["python", "fetch_huggingface_top_models.py"]