# KachaniOS Public

A privacy-safe public edition of **KachaniOS**, a modular Python assistant architecture built around topic routing, specialized domain agents, short-term context, and one final response layer.

> The original KachaniOS development repository remains private because it contains personal runtime history and experimental internal components. This repository preserves the core engineering ideas without conversations, credentials, personal memory, private prompts, or sensitive Git history.

## What this repository demonstrates

- Multilingual topic-lane routing for English, French, Arabic, and Moroccan Darija signals
- Primary and secondary domain selection with confidence and routing reasons
- Specialized agents for studies, productivity, software engineering, finance, health habits, relationships, and general support
- Privacy-safe in-memory conversation context
- Multi-agent execution for mixed-domain requests
- A **Final Speaker** layer that combines agent outputs into one coherent response
- Typed request, route, context, agent-output, and final-response models
- Automated tests for multilingual routing, orchestration, and input validation
- Installable Python package and interactive command-line interface

## Architecture

```text
User message
     |
     v
TopicRouter
     |
     +--> Primary domain agent
     +--> Optional secondary agent
     |
     v
Privacy-safe context store
     |
     v
FinalSpeaker
     |
     v
One coherent response
```

## Project structure

```text
kachanios-public/
├── kachanios/
│   ├── __init__.py
│   ├── agents.py
│   ├── cli.py
│   ├── memory.py
│   ├── models.py
│   ├── orchestrator.py
│   └── router.py
├── tests/
│   └── test_public_architecture.py
├── .github/workflows/tests.yml
├── .gitignore
├── LICENSE
├── main.py
├── pyproject.toml
└── README.md
```

## Run locally

Requirements: Python 3.10 or newer.

```bash
git clone https://github.com/kachaniabdellah86/kachanios-public.git
cd kachanios-public
python -m pip install -e .
kachanios
```

You can also run:

```bash
python main.py
```

## Run the tests

```bash
python -m unittest discover -s tests
```

## Example

Input:

```text
Plan my budget and organize the tasks for my business.
```

The router can identify finance as the primary domain and productivity as a secondary domain. Both agents contribute structured actions, while the Final Speaker removes repetition and returns one answer.

## Privacy and security decisions

This public repository deliberately excludes:

- Personal conversations and memory files
- Telegram chat identifiers and bot tokens
- API keys, `.env` files, cookies, and credentials
- Health, relationship, task, and life-state records
- Production system prompts containing personal context
- Autonomous code-editing capabilities from the experimental private system
- Local model files and generated logs

The public context store is ephemeral and does not write user messages to disk.

## Scope

This repository is a portfolio-safe architectural edition, not a hosted medical, financial, or emergency service. Its health and finance modules provide general planning structure and include explicit limitations.

## Author

**Abdellah Kachani**  
Computer engineering student focused on AI-agent architectures, Python, full-stack development, and reliable software systems.
