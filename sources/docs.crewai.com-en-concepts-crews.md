---
title: "docs.crewai.com-en-concepts-crews"
slug: "docs.crewai.com-en-concepts-crews"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/concepts/crews"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-crews/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-crews/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-concepts-crews

> Synthesis: TODO

Understanding and utilizing crews in the crewAI framework with comprehensive attributes and functionalities.
|Attribute
|Parameters
|Description
Tasks
tasks
|A list of tasks assigned to the crew.
Agents
agents
|A list of agents that are part of the crew.
Process (optional)
process
|The process flow (e.g., sequential, hierarchical) the crew follows. Default is
sequential.
Verbose (optional)
verbose
|The verbosity level for logging during execution. Defaults to
False.
Manager LLM (optional)
manager_llm
|The language model used by the manager agent in a hierarchical process.
Required when using a hierarchical process.
Function Calling LLM (optional)
function_calling_llm
|If passed, the crew will use this LLM to do function calling for tools for all agents in the crew. Each agent can have its own LLM, which overrides the crew’s LLM for function calling.
Config (optional)
config
|Optional configuration settings for the crew, in
Json or
Dict[str, Any] format.
Max RPM (optional)
max_rpm
|Maximum requests per minute the crew adheres to during execution. Defaults to
None.
Memory (optional)
memory
|Utilized for storing execution memories (short-term, long-term, entity memory).
Cache (optional)
cache
|Specifies whether to use a cache for storing the results of tools’ execution. Defaults to
True.
Embedder (optional)
embedder
|Configuration for the embedder to be used by the crew. Mostly used by memory for now. Default is
{"provider": "openai"}.
Step Callback (optional)
step_callback
|A function that is called after each step of every agent. This can be used to log the agent’s actions or to perform other operations; it won’t override the agent-specific
step_callback.
Task Callback (optional)
task_callback
|A function that is called after the completion of each task. Useful for monitoring or additional operations post-task execution.
Share Crew (optional)
share_crew
|Whether you want to share the complete crew information and execution with the crewAI team to make the library better, and allow us to train models.
Output Log File (optional)
output_log_file
|Set to True to save logs as logs.txt in the current directory or provide a file path. Logs will be in JSON format if the filename ends in .json, otherwise .txt. Defaults to
None.
Manager Agent (optional)
manager_agent
manager sets a custom agent that will be used as a manager.
Prompt File (optional)
prompt_file
|Path to the prompt JSON file to be used for the crew.
Planning (optional)
planning
|Adds planning ability to the Crew. When activated before each Crew iteration, all Crew data is sent to an AgentPlanner that will plan the tasks and this plan will be added to each task description.
Planning LLM (optional)
planning_llm
|The language model used by the AgentPlanner in a planning process.
Knowledge Sources (optional)
knowledge_sources
|Knowledge sources available at the crew level, accessible to all the agents.
max_rpm attribute sets the maximum number of requests per minute the crew can perform to avoid rate limits and will override individual agents’
max_rpm settings if you set it.
CrewBase and uses decorators to define agents, tasks, and the crew itself.
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew, before_kickoff, after_kickoff
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
@CrewBase
class YourCrewName:
"""Description of your crew"""
agents: List[BaseAgent]
tasks: List[Task]
# Paths to your YAML configuration files
# To see an example agent and task defined in YAML, checkout the following:
# - Task: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
# - Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
agents_config = 'config/agents.yaml'
tasks_config = 'config/tasks.yaml'
@before_kickoff
def prepare_inputs(self, inputs):
# Modify inputs before the crew starts
inputs['additional_data'] = "Some extra information"
return inputs
@after_kickoff
def process_output(self, output):
# Modify output after the crew finishes
output.raw += "\nProcessed after kickoff."
return output
@agent
def agent_one(self) -> Agent:
return Agent(
config=self.agents_config['agent_one'], # type: ignore[index]
verbose=True
)
@agent
def agent_two(self) -> Agent:
return Agent(
config=self.agents_config['agent_two'], # type: ignore[index]
verbose=True
)
@task
def task_one(self) -> Task:
return Task(
config=self.tasks_config['task_one'] # type: ignore[index]
)
@task
def task_two(self) -> Task:
return Task(
config=self.tasks_config['task_two'] # type: ignore[index]
)
@crew
def crew(self) -> Crew:
return Crew(
agents=self.agents, # Automatically collected by the @agent decorator
tasks=self.tasks, # Automatically collected by the @task decorator.
process=Process.sequential,
verbose=True,
)
YourCrewName().crew().kickoff(inputs={"any": "input here"})
CrewBase class, along with these decorators, automates the collection of agents and tasks, reducing the need for manual management.
annotations.py
annotations.py file that are used to mark methods within your crew class for special handling:
@CrewBase: Marks the class as a crew base class.
@agent: Denotes a method that returns an
Agent object.
@task: Denotes a method that returns a
Task object.
@crew: Denotes the method that returns the
Crew object.
@before_kickoff: (Optional) Marks a method to be executed before the crew starts.
@after_kickoff: (Optional) Marks a method to be executed after the crew finishes.
from crewai import Agent, Crew, Task, Process
from crewai_tools import YourCustomTool
class YourCrewName:
def agent_one(self) -> Agent:
return Agent(
role="Data Analyst",
goal="Analyze data trends in the market",
backstory="An experienced data analyst with a background in economics",
verbose=True,
tools=[YourCustomTool()]
)
def agent_two(self) -> Agent:
return Agent(
role="Market Researcher",
goal="Gather information on market dynamics",
backstory="A diligent researcher with a keen eye for detail",
verbose=True
)
def task_one(self) -> Task:
return Task(
description="Collect recent market data and identify trends.",
expected_output="A report summarizing key trends in the market.",
agent=self.agent_one()
)
def task_two(self) -> Task:
return Task(
description="Research factors affecting market dynamics.",
expected_output="An analysis of factors influencing the market.",
agent=self.agent_two()
)
def crew(self) -> Crew:
return Crew(
agents=[self.agent_one(), self.agent_two()],
tasks=[self.task_one(), self.task_two()],
process=Process.sequential,
verbose=True
)
YourCrewName().crew().kickoff(inputs={})
CrewOutput class.
This class provides a structured way to access results of the crew’s execution, including various formats such as raw strings, JSON, and Pydantic models.
The
CrewOutput includes the results from the final task output, token usage, and individual task outputs.
|Attribute
|Parameters
|Type
|Description
Raw
raw
str
|The raw output of the crew. This is the default format for the output.
Pydantic
pydantic
Optional[BaseModel]
|A Pydantic model object representing the structured output of the crew.
JSON Dict
json_dict
Optional[Dict[str, Any]]
|A dictionary representing the JSON output of the crew.
Tasks Output
tasks_output
List[TaskOutput]
|A list of
TaskOutput objects, each representing the output of a task in the crew.
Token Usage
token_usage
Dict[str, Any]
|A summary of token usage, providing insights into the language model’s performance during execution.
|Method/Property
|Description
json |Returns the JSON string representation of the crew output if the output format is JSON.
to_dict |Converts the JSON and Pydantic outputs to a dictionary.
|*
*str** |Returns the string representation of the crew output, prioritizing Pydantic, then JSON, then raw.
output attribute of the
Crew object. The
CrewOutput class provides various ways to interact with and present this output.
# Example crew execution
crew = Crew(
agents=[research_agent, writer_agent],
tasks=[research_task, write_article_task],
verbose=True
)
crew_output = crew.kickoff()
# Accessing the crew output
print(f"Raw Output: {crew_output.raw}")
if crew_output.json_dict:
print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
if crew_output.pydantic:
print(f"Pydantic Output: {crew_output.pydantic}")
print(f"Tasks Output: {crew_output.tasks_output}")
print(f"Token Usage: {crew_output.token_usage}")
output_log_file as a
True(Boolean) or a
file_name(str). Supports logging of events as both
file_name.txt and
file_name.json.
In case of
True(Boolean) will save as
logs.txt.
In case of
output_log_file is set as
False(Boolean) or
None, the logs will not be populated.
# Save crew logs
crew = Crew(output_log_file = True) # Logs will be saved as logs.txt
crew = Crew(output_log_file = file_name) # Logs will be saved as file_name.txt
crew = Crew(output_log_file = file_name.txt) # Logs will be saved as file_name.txt
crew = Crew(output_log_file = file_name.json) # Logs will be saved as file_name.json
usage_metrics attribute to view the language model (LLM) usage metrics for all tasks executed by the crew. This provides insights into operational efficiency and areas for improvement.
# Access the crew's usage metrics
crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
crew.kickoff()
print(crew.usage_metrics)
manager_llm or
manager_agent is required for this process and it’s essential for validating the process flow.
kickoff() method. This starts the execution process according to the defined process flow.
# Start the crew's task execution
result = my_crew.kickoff()
print(result)
kickoff(),
kickoff_for_each(),
kickoff_async(), and
kickoff_for_each_async().
kickoff(): Starts the execution process according to the defined process flow.
kickoff_for_each(): Executes tasks sequentially for each provided input event or item in the collection.
kickoff_async(): Initiates the workflow asynchronously.
kickoff_for_each_async(): Executes tasks concurrently for each provided input event or item, leveraging asynchronous processing.
# Start the crew's task execution
result = my_crew.kickoff()
print(result)
# Example of using kickoff_for_each
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
results = my_crew.kickoff_for_each(inputs=inputs_array)
for result in results:
print(result)
# Example of using kickoff_async
inputs = {'topic': 'AI in healthcare'}
async_result = await my_crew.kickoff_async(inputs=inputs)
print(async_result)
# Example of using kickoff_for_each_async
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
async_results = await my_crew.kickoff_for_each_async(inputs=inputs_array)
for async_result in async_results:
print(async_result)
replay.
The replay feature in CrewAI allows you to replay from a specific task using the command-line interface (CLI). By running the command
crewai replay -t <task_id>, you can specify the
task_id for the replay process.
Kickoffs will now save the latest kickoffs returned task outputs locally for you to be able to replay from.
crewai log-tasks-outputs
crewai replay -t <task_id>

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-crews/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-crews/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
