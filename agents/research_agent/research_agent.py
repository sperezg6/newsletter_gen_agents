from agents import Agent, Runner, WebSearchTool


researcher_agent = Agent(
    name="Researcher Agent",
    instructions="Investigate the latest news on Tech and Data Engineering",
    tools=[
        WebSearchTool(),
    ]
)