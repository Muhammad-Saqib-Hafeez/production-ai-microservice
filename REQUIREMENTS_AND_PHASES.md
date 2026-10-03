# Project 1: Production-Ready AI Microservice Template

## Part 1: How Industry Projects Start (Requirements Gathering)

Before writing a single line of code, Senior Engineers spend time understanding the problem. If you start coding immediately, you usually end up rewriting it later. We follow the "4 W's and How" for Requirements Gathering:

1. **Why are we building this? (Business Goal)**
   - *Requirement*: We need a standardized, reusable way to deploy AI models (like LLMs or classic ML) so that future projects can be deployed in hours instead of days.
2. **Who is the user? (Stakeholders)**
   - *Requirement*: Other developers (or future you), and automated systems that will consume the API.
3. **What must it do? (Functional Requirements)**
   - Must expose REST API endpoints for model inference.
   - Must have health checks `/health` for load balancers.
   - Must validate incoming data strictly.
4. **How must it perform? (Non-Functional Requirements)**
   - *Performance*: Fast response times (using asynchronous Python).
   - *Reliability*: Must be containerized (Docker) to run consistently anywhere.
   - *Maintainability*: Code must be strictly typed, formatted, and tested.

## Part 2: Project Phases (The Roadmap)

To make your GitHub commit history look like a real professional (and not an automated bot), we will build and commit this in modular phases. 

### Phase 1: Foundation (Current)
*Goal: Set up the skeleton and make the first clean commit.*
- [ ] Initialize Git repository.
- [ ] Create `.gitignore`.
- [ ] Define Project Structure (directories).
- [ ] Set up Python environment and `pyproject.toml` (Dependency management).

### Phase 2: Core Application & Routing
*Goal: Build the FastAPI server without the AI model yet.*
- [ ] Set up FastAPI `main.py`.
- [ ] Implement robust configuration management (Pydantic Settings).
- [ ] Create `/health` endpoint.
- [ ] Setup structured logging.

### Phase 3: The AI / Business Logic Layer
*Goal: Add the actual model handling.*
- [ ] Create data validation schemas (Pydantic).
- [ ] Create a mock AI service interface (Dependency Injection).
- [ ] Add the `/predict` or `/generate` endpoint.

### Phase 4: Testing & Quality Assurance
*Goal: Prove the code works.*
- [ ] Add Pytest framework.
- [ ] Write unit tests for endpoints.
- [ ] Add linting/formatting tools (Ruff, MyPy).

### Phase 5: Containerization & CI/CD (The Senior Touch)
*Goal: Make it production-ready.*
- [ ] Write a highly optimized `Dockerfile`.
- [ ] Write a GitHub Actions `.yml` workflow for automated testing.
- [ ] Write the ultimate `README.md`.
