import os

from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from pydantic import SecretStr


# Define the tool using the @tool decorator
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# Initialize the GitHub Copilot LLM
# GitHub Models uses an OpenAI-compatible API
llm = ChatOpenAI(
    model="gpt-4o-mini", # GitHub supports models like gpt-4o, gpt-4o-mini, etc.
    api_key=SecretStr(os.environ["GITHUB_TOKEN"]),
    base_url="https://models.inference.ai.azure.com"
)

# Create the agent
# We use the 'llm' object configured for GitHub instead of a string provider
agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)

# Run the agent
inputs = {"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]}
config=RunnableConfig(run_name="hello-langchain-openai")
response = agent.invoke(
    inputs,
    config=config
)

# Display the result
print(response["messages"][-1].content)

