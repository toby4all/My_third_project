# Use a more recent Python Alpine image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the Python source files and requirements.txt
COPY rest_app.py db_connector.py requirements.txt ./

# Update and upgrade Alpine packages, and install required system dependencies
RUN apk update && apk upgrade && \
    apk add --no-cache build-base libffi-dev openssl-dev && \  # Add libffi-dev and openssl-dev for cryptography
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install the 'cryptography' package
RUN pip install cryptography

# Expose the port
EXPOSE 5000

# Define a volume for logs
VOLUME /app/logs

# Run the Python application
CMD ["python3", "rest_app.py"]

