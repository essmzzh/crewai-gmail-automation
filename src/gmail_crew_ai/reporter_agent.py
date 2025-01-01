import os
from crewai import Agent, LLM
from crewai.project import CrewBase, agent
from crewai_tools import FileReadTool
from gmail_crew_ai.tools.reporter_tools import ReportExportTool


@CrewBase
class ReporterCrew:
    """Reporter agent crew defined in its own file."""

    llm = LLM(
        model="openai/gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    @agent
    def report_generator(self) -> Agent:
        """The email report generator agent."""
        return Agent(
            role="Email Report Specialist",
            goal="Compile and export structured reports on processed emails",
            backstory="An automated reporting specialist summarizing executive metrics.",
            tools=[ReportExportTool(), FileReadTool()],
            llm=self.llm,
            verbose=True,
        )
