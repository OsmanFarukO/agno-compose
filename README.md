
# AGNO agent UI-Playground Orchestrate

This project created for orchestrate agent-ui with playground locally on docker-compose environment.

## Installation

```bash
git clone https://github.com/OsmanFarukO/agno-compose.git
cd agno-compose
git clone https://github.com/OsmanFarukO/agent-ui-dockerized.git

docker compose build .
docker compose up -d
```
Add your agents to `agent-playground/agents/ ` directory.

Import agents to `agent-playground/playground.py`
```python
from agents.my_perfect_agent import my_perfect_agent
```
Add your imported agents to app object
```python
app = Playground(agents=[my_perfect_agent]).get_app()
```
Playground will reload itself. You can observe playground log with `docker compose logs -f agent-playground`
