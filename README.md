# KachaniOS Public

A privacy-safe portfolio demonstration of a modular personal AI-agent architecture built in Python.

> This repository is a sanitized showcase inspired by the private KachaniOS project. It contains no personal conversations, production credentials, private memory, or proprietary prompts.

## Why this project exists

KachaniOS explores how one assistant can classify a user request, route it to a specialized domain, preserve structured context, and return one coherent final response.

The private production project includes additional integrations and personal data that are intentionally excluded from this public demonstration.

## Architecture

```text
User message
     |
     v
Intent Router
     |
     +--> Studies
     +--> Productivity
     +--> Software Engineering
     +--> Finance
     +--> General Support
     |
     v
Specialized Agent Result
     |
     v
Final Response Orchestrator
     |
     v
One consistent answer
```

## Demonstrated concepts

- Domain-based intent routing
- Typed request and response models
- Deterministic orchestration
- Separation between routing, agent logic, and final response composition
- Safe mock context instead of personal memory
- Unit testing of routing behaviour
- Extensible Python project structure

## Project structure

```text
kachanios-public/
├── main.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── router.py
│   └── orchestrator.py
└── tests/
    └── test_router.py
```

## Run locally

Requirements:

- Python 3.10 or newer

```bash
git clone https://github.com/kachaniabdellah86/kachanios-public.git
cd kachanios-public
python main.py
```

Run tests:

```bash
python -m unittest discover -s tests
```

## Example

Input:

```text
Help me organize my revision plan for the SQL exam.
```

Output:

```text
Domain: studies
Response: I classified this request as studies and prepared a structured next step.
```

## Privacy design

This public repository deliberately excludes:

- Personal memory and conversation logs
- Telegram chat identifiers
- API keys and environment files
- Production prompts
- Autonomous self-modification logic
- Private user state

The original KachaniOS repository remains private.

## Future improvements

- Optional LLM provider interface
- Persistent mock session state
- More specialized domains
- Evaluation dataset for router accuracy
- CLI and Telegram demo adapters

## Author

**Abdellah Kachani**  
Computer engineering student focused on AI agents, Python, full-stack development, and reliable software systems.
