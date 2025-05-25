from agents import Agent, Runner, WebSearchTool
from ..research_agent.research_agent import researcher_agent
import asyncio


writer_agent = Agent(
    name="Newsletter Writer Agent",
    model="o4-mini",
    instructions="""
        
    You are the Writer Agent for the "Data Engineering" newsletter, which documents a personal journey from startup to Amazon Data Engineer while building a community of aspiring and current data engineers.

    """,
    tools=[
        researcher_agent.as_tool(
            tool_name = "Research Agent for Data Engineering Newsletter",
            tool_description=""" 
            This agent finds the latest, most relevant content that supports authentic storytelling about data engineering careers, big tech culture, and technical growth - focusing on content that would resonate with someone documenting their Amazon journey.
            """            
        ),

    ],
    

)



async def main():
    result = await Runner.run(
        writer_agent,
        input={
            "query": "Find the latest content on data engineering careers, big tech culture, and technical growth."
        }
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())