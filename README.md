# hello-langchain-openai

Minimal LangChain hello-world adapted for GitHub Copilot / GitHub Models.

## Setup

```bash
# export two required tokens
export LANGSMITH_API_KEY="todo"
export GITHUB_TOKEN="todo"

# let direnv setup our python virtualenv and load environment variables from .envrc
brew install direnv
direnv allow
direnv status
which python

# install dependencies
pip install langchain langchain-openai
python -m pip install pip-system-certs -U --use-feature=truststore
```

## Run

```bash
# Run the demo
python app.py
```
