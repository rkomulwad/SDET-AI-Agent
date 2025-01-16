from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff
from .tools.openapi_spec_parser import openapi_spec_parser
from .tools.testcases_markdown_reader import testcases_markdown_reader

@CrewBase
class SDETAIAgent():
	"""SDETAIAgent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@before_kickoff
	def before_kickoff_function(self, inputs):
		print(f"******* Before kickoff function with inputs: {inputs}")
		return inputs

	@agent
	def test_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['test_designer'],
			verbose=True,
			tools=[openapi_spec_parser]
		)
	
	@task
	def generate_test_cases(self) -> Task:
		return Task(
			config=self.tasks_config['generate_test_cases'],
			output_file='output/testcases.md'
		)

	@task
	def identify_edge_cases(self) -> Task:
		return Task(
			config=self.tasks_config['generate_edge_test_cases'],
			output_file='output/edgecases.md'
		)

	@agent
	def test_case_coder(self) -> Agent:
		return Agent(
			config=self.agents_config['test_case_coder'],
			verbose=True,
			tools=[openapi_spec_parser, testcases_markdown_reader]
		)
		
	@task
	def generate_test_code(self) -> Task:
		return Task(
			config=self.tasks_config['generate_test_code'],
			output_file='output/postman_collection.json'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the SDETAIAgent crew"""
		return Crew(
			agents=self.agents, 
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical,
		)
