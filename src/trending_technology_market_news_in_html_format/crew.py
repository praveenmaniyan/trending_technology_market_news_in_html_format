from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import FileReadTool

@CrewBase
class TrendingTechnologyMarketNewsInHtmlFormatCrew():
    """TrendingTechnologyMarketNewsInHtmlFormat crew"""

    @agent
    def news_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['news_search_agent'],
            tools=[WebsiteSearchTool()],
        )

    @agent
    def news_scrape_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['news_scrape_agent'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def html_compile_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['html_compile_agent'],
            tools=[FileReadTool()],
        )


    @task
    def search_news_websites_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_news_websites_task'],
            tools=[WebsiteSearchTool()],
        )

    @task
    def scrape_news_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['scrape_news_data_task'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def compile_html_task(self) -> Task:
        return Task(
            config=self.tasks_config['compile_html_task'],
            tools=[FileReadTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the TrendingTechnologyMarketNewsInHtmlFormat crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
