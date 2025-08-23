# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir mysql-connector-python openai==0.28 pandas

# Command to run the script
CMD ["python", "incident_analysis.py"]
