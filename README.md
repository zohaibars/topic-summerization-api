# Topic Summarization API
Topic Extraction and Summarization using LLaMA-3-70B/8B

## File Structure
```bash
app
├── api
│   ├── endpoints # all the api endpoint router are here
│   ├── __init__.py
│   └── __pycache__
├── core
│   ├── agents # LLM agents for each endpoint
│   ├── graph_builder # graph builder wrapper around langraph
│   └── prompts # all the prompts for agents
├── main.py # main entry point file for the fast api
└── utils # All the required elements for the api to function
    ├── connections.py # connections to external apis or clients 
    ├── models.py # pydantic models for the entire app are here
    └── settings.py # loading environment varibales from .env
```

### Agents content
 - Agents can range from a simple chain to a langgraph
 - summary and word cloud agents are simple chains
 - summary chain are to be replaced by the langgraph in this [repository.](https://github.com/talhaforbmax/graph-testing-repo)
 - Spell check agent is for annotation app utilized for internal use remove for Nimar and Demp
 - Agents folder consists of the core structure with chains/graph and helper functions in utils
 - Prompts are in seperate file and has a unique .py file for each agent.
 - Utils include parsers to extract from LLM responses. # TODO improve parsers using langchains in built ones.

## Setup

1. **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install Dependencies**
    ```bash
    poetry lock
    poetry install
    ```

3. **Run the Server**
    ```bash
    poetry run uvicorn app.main:app --reload --log-level debug --reload-dir app/ --host 0.0.0.0 --port 8080
    ```

## Docker Setup

1. **Build and Run with Docker Compose (First Time)**
    ```bash
    docker compose up --build
    ```

2. **Subsequent Runs**
    ```bash
    docker compose up
    ```

