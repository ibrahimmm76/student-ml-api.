# Explicit base-image version, avoiding 'latest'
FROM python:3.11-slim

LABEL org.opencontainers.image.title="student-ml-api" \
      org.opencontainers.image.description="MLOps  Phase  API" \
      org.opencontainers.image.authors="Muhammad Ibrahim" \
      org.opencontainers.image.source="https://github.com/ibrahimmm76/student-ml-api"

# Set the working directory
WORKDIR /app

# Correct COPY ordering: Dependencies first for caching
COPY requirements.txt .

# Dependency installation with no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the required port
EXPOSE 5000

# Appropriate CMD to run FastAPI on port 5000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]