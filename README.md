<div align="center">
  <h1>🚀 Production AI Microservice Template</h1>
  <p><i>The ultimate skeleton for taking Machine Learning models from Jupyter Notebooks to Production.</i></p>
  
  [![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com)
  [![Pydantic v2](https://img.shields.io/badge/Pydantic-v2-e92063.svg)](https://docs.pydantic.dev/latest/)
  [![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF.svg)]()
  [![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)]()
  [![uv](https://img.shields.io/badge/Package_Manager-uv-purple.svg)](https://github.com/astral-sh/uv)
</div>

---

## 📖 Table of Contents
- [The "Last Mile" Problem](#-the-last-mile-problem)
- [✨ Key Features](#-key-features)
- [🏗️ Architecture (DDD)](#️-architecture-ddd)
- [🚀 Quick Start (Local)](#-quick-start-local)
- [🐳 Docker Deployment](#-docker-deployment)
- [🧪 Testing & QA](#-testing--qa)
- [🤝 Contributing](#-contributing)

---

## 💡 The "Last Mile" Problem
Most AI/ML projects fail because they never leave the Jupyter Notebook. Deploying a model requires more than just calling `model.predict()`. You need strict data validation, memory-efficient dependency injection, automated testing, and CI/CD. 

This repository serves as a **cookiecutter template** that handles all the software engineering boilerplate, allowing you to focus on the AI.

---

## ✨ Key Features

*   **Domain-Driven Design (DDD):** Clean separation of routing, business logic, and configuration.
*   **Dependency Injection:** Models are loaded into memory exactly *once* as singletons to prevent out-of-memory crashes on concurrent requests.
*   **Strict Validation:** Pydantic V2 ensures that malformed requests are blocked *before* they reach your heavy ML models.
*   **Blazing Fast Docker Builds:** Utilizes Astral's `uv` inside the container for 10x-100x faster dependency resolution.
*   **Zero-GPU Testing:** Tests use dependency overriding to swap massive ML models for instant mocks.
*   **CI/CD Ready:** Automated GitHub Actions pipeline enforcing strict MyPy typing and Pytest coverage.

---

## 🏗️ Architecture & Data Flow

### Directory Structure (Domain-Driven Design)
```text
.
├── src/
│   ├── api/            # FastAPI Routers & HTTP Endpoints
│   ├── core/           # Pydantic BaseSettings & App Configuration
│   ├── schemas/        # Pydantic Data Validation Models
│   ├── services/       # AI Model Loading & Business Logic
│   └── main.py         # Application Factory & CORS
├── tests/              # Pytest Suite & Fixtures
├── .github/workflows/  # CI/CD Pipelines
├── Dockerfile          # Optimized Container Definition
└── pyproject.toml      # Modern Dependency Management
```

### Request Lifecycle Diagram
GitHub natively renders this diagram so you can visualize exactly how data moves through the microservice.

```mermaid
graph TD
    Client([Client Request]) -->|HTTP POST JSON| Router(FastAPI Router <br> <code>src/api</code>)
    Router -->|1. Validate Input| Schema{Pydantic Schema <br> <code>src/schemas</code>}
    
    Schema -- Valid --> DI[Dependency Injection <br> <code>Depends()</code>]
    Schema -. Invalid .-> Error([422 Unprocessable Entity])
    
    DI -->|2. Inject Singleton| Service(AI Service <br> <code>src/services</code>)
    Service -->|3. Run Inference| Model[(Heavy ML Model)]
    Model -->|4. Return Result| Service
    Service -->|5. Format Output| Response{Response Schema}
    Response -->|HTTP 200 OK| Client
```

---

## 🧠 How It Works (Educational Walkthrough)

If you are using this repository to learn how production systems are built, here is the exact lifecycle of a single API request:

1. **The Request Arrives (`src/api/predict.py`)**: A client sends a JSON payload to `/api/v1/predict`.
2. **The Bouncer (`src/schemas/prediction.py`)**: Before the route function even executes, FastAPI intercepts the data and passes it to Pydantic. Pydantic checks if the data matches our strict rules (e.g., *is the text between 5 and 5000 characters?*). If it fails, the user gets a 422 error immediately, protecting the heavy AI model from processing garbage data.
3. **The Injector (`src/services/ai_service.py`)**: Loading an AI model (like PyTorch or an LLM) takes massive memory and time. To prevent loading it on every request, we use `Depends(get_ai_service)`. This tells FastAPI to grab the *already running* instance of our AI model (the Singleton pattern) and hand it to the route.
4. **The Brain (`src/services/ai_service.py`)**: The `AIService` processes the text (this is where you place your HuggingFace/PyTorch code) and returns the raw prediction.
5. **The Formatter (`src/schemas/prediction.py`)**: The route takes the raw prediction, packages it into our `PredictionResponse` Pydantic schema, and sends it back to the client as clean, validated JSON.

---

## 🚀 Quick Start (Local)

1. **Clone and Install:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/production-ai-microservice.git
   cd production-ai-microservice
   pip install -e .[dev]
   ```

2. **Boot the Server:**
   ```bash
   uvicorn src.main:app --reload
   ```

3. **Explore the Docs:**
   Navigate to `http://127.0.0.1:8000/api/v1/docs` to test the endpoints in the auto-generated Swagger UI.

---

## 🐳 Docker Deployment

For production (AWS ECS, Kubernetes, etc.), use the pre-configured, heavily optimized Dockerfile.

```bash
# Build the image (Powered by Astral's uv)
docker build -t ai-microservice .

# Run the container
docker run -p 8000:8000 ai-microservice
```

---

## 🧪 Testing & QA

Run the test suite instantly (no GPUs required due to DI overriding):
```bash
pytest -v
```

Enforce strict static typing:
```bash
mypy src/
```

---

## 🤝 Contributing
If you found this template helpful for deploying your models, **please consider leaving a ⭐ Star!** It helps others find the repository. Pull requests for architectural improvements are always welcome.
