import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


api_key = os.getenv("AZURE_API_KEY")
api_base = os.getenv("AZURE_ENDPOINT")
model = os.getenv("MODEL_AZURE", "gpt-4o")

@CrewBase
class ToxicNetwork():
    """ToxicNetwork crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def user_research(self) -> Agent:

        return Agent(
            config=self.agents_config['user_research'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            memory=True,
        )

    @agent
    def user_writer(self) -> Agent:

        return Agent(
            config=self.agents_config['user_writer'], # type: ignore[index]
            verbose=True,
            llm=LLM(
                model=model,
                api_base=api_base,
                api_key=api_key,
            ),
            memory=True,
        )

    @task
    def user_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_research_task'], # type: ignore[index]
        )
    
    @task
    def user_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_writer_task'], # type: ignore[index]
            
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ToxicNetwork crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
