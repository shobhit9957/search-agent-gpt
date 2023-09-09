from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import os

user = input("enter any search related queries, you've I'll solve it: --- ")
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "45d6021e4f8b7a343558c5412992fecffe03a009dfe5a9ba1eecfa711ae32cd7"
llm = OpenAI(temperature=0)
tool_name = ["serpapi"]
tools = load_tools(tool_name)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

agent.run(user)