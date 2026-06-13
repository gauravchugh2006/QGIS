# Builds a small Python image that can run the profiling toolkit in local or server environments.
FROM python:3.12-slim

WORKDIR /app

# Installs Python dependencies first so Docker layer caching stays effective.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copies the rest of the project into the container.
COPY . .

# Runs the main profiling workflow by default.
CMD ["python", "src/main.py"]
