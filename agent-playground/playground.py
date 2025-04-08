from agno.playground import Playground, serve_playground_app
from agents.finance_agent import finance_agent
from agents.web_agent import web_agent

app = Playground(agents=[web_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True, host='0.0.0.0')