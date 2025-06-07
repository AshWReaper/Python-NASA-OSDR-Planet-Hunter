# Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY planet_hunter.py ./
COPY planet_filters.py ./

# Install dependencies
RUN pip install --no-cache-dir requests

# Run the script
CMD ["python", "planet_hunter.py"]
