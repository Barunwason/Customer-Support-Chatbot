from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from customer_support_automation.tools.scraper_tool import docs_scrape_tool


@CrewBase
class CustomerSupportAutomation():
	"""CustomerSupportAutomation crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def support_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['support_agent'],
			verbose=True
		)

	@agent
	def support_quality_assurance_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['support_quality_assurance_agent'],
			verbose=True
		)


	@task
	def inquiry_resolution(self) -> Task:
		return Task(
			config=self.tasks_config['inquiry_resolution'],
			tools=[docs_scrape_tool]
		)

	@task
	def quality_assurance_review(self) -> Task:
		return Task(
			config=self.tasks_config['quality_assurance_review'],
			output_file='final_draft.md'
		)

	@crew
	def crew(self) -> Crew:
		

		return Crew(
			agents=self.agents, 
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
