# Explicit base-image version, avoiding 'latest'
FROM python:3.11-slim

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