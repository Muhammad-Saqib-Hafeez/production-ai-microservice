# Use the official Python slim image for a smaller footprint
FROM python:3.10-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Set working directory
WORKDIR /app

# We use uv instead of pip for lightning-fast Docker builds
RUN pip install --no-cache-dir uv

# Copy only the dependency definitions first (for Docker layer caching)
COPY pyproject.toml .

# Install dependencies system-wide (Standard practice inside a container)
RUN uv pip install --system -e .

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
