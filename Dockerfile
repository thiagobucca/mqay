FROM python:3.9-alpine

# Install system packages required by psutil and other dependencies
RUN apk add --no-cache gcc libc-dev

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt and the script files into the container
COPY requirements.txt .
COPY mqay.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the MQTT port
EXPOSE 1883

# Set up the container to monitor the host systemd services
VOLUME /run/systemd

# Start the script
CMD ["python", "mqay.py"]
