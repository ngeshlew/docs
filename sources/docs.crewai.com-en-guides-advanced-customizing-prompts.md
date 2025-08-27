---
title: "docs.crewai.com-en-guides-advanced-customizing-prompts"
slug: "docs.crewai.com-en-guides-advanced-customizing-prompts"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/guides/advanced/customizing-prompts"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures:
  - path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-collaboration/71bc45159c09.webp"
    caption: "light logo"
    credit_name: "docs.crewai.com"
    credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
    license: "internal-copy"
  - path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-collaboration/71bc45159c09.webp"
    caption: "dark logo"
    credit_name: "docs.crewai.com"
    credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
    license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-guides-advanced-customizing-prompts

> Synthesis: TODO

Dive deeper into low-level prompt customization for CrewAI, enabling super custom and complex use cases for different models and languages.
role,
goal, and
backstory, CrewAI automatically adds additional system instructions that control formatting and behavior. Understanding these default injections is crucial for production systems where you need full prompt transparency.
"I MUST use these formats, my job depends on it!"
"IMPORTANT: Use the following format in your response:
Thought: you should always think about what to do
Action: the action to take, only one name of [tool_names]
Action Input: the input to the action, just a simple JSON object...
"Ensure your final answer contains only the content in the following format: {output_format}
Ensure the final output does not include any code block markers like ```json or ```python."
from crewai import Agent, Crew, Task
from crewai.utilities.prompts import Prompts
# Create your agent
agent = Agent(
role="Data Analyst",
goal="Analyze data and provide insights",
backstory="You are an expert data analyst with 10 years of experience.",
verbose=True
)
# Create a sample task
task = Task(
description="Analyze the sales data and identify trends",
expected_output="A detailed analysis with key insights and trends",
agent=agent
)
# Create the prompt generator
prompt_generator = Prompts(
agent=agent,
has_tools=len(agent.tools) > 0,
use_system_prompt=agent.use_system_prompt
)
# Generate and inspect the actual prompt
generated_prompt = prompt_generator.task_execution()
# Print the complete system prompt that will be sent to the LLM
if "system" in generated_prompt:
print("=== SYSTEM PROMPT ===")
print(generated_prompt["system"])
print("\n=== USER PROMPT ===")
print(generated_prompt["user"])
else:
print("=== COMPLETE PROMPT ===")
print(generated_prompt["prompt"])
# You can also see how the task description gets formatted
print("\n=== TASK CONTEXT ===")
print(f"Task Description: {task.description}")
print(f"Expected Output: {task.expected_output}")
from crewai import Agent
# Define your own system template without default instructions
custom_system_template = """You are {role}. {backstory}
Your goal is: {goal}
Respond naturally and conversationally. Focus on providing helpful, accurate information."""
custom_prompt_template = """Task: {input}
Please complete this task thoughtfully."""
agent = Agent(
role="Research Assistant",
goal="Help users find accurate information",
backstory="You are a helpful research assistant.",
system_template=custom_system_template,
prompt_template=custom_prompt_template,
use_system_prompt=True # Use separate system/user messages
)
custom_prompts.json file to override specific prompt slices:
{
"slices": {
"no_tools": "\nProvide your best answer in a natural, conversational way.",
"tools": "\nYou have access to these tools: {tools}\n\nUse them when helpful, but respond naturally.",
"formatted_task_instructions": "Format your response as: {output_format}"
}
}
crew = Crew(
agents=[agent],
tasks=[task],
prompt_file="custom_prompts.json",
verbose=True
)
agent = Agent(
role="Analyst",
goal="Analyze data",
backstory="Expert analyst",
use_system_prompt=False # Disables system prompt separation
)
prompts_llama.json or
prompts_es.json to quickly identify specialized configurations.
prompt_file parameter in your Crew.
custom_prompts.json file with the prompts you want to modify. Ensure you list all top-level prompts it should contain, not just your changes:
{
"slices": {
"format": "When responding, follow this structure:\n\nTHOUGHTS: Your step-by-step thinking\nACTION: Any tool you're using\nRESULT: Your final answer or conclusion"
}
}
from crewai import Agent, Crew, Task, Process
# Create agents and tasks as normal
researcher = Agent(
role="Research Specialist",
goal="Find information on quantum computing",
backstory="You are a quantum physics expert",
verbose=True
)
research_task = Task(
description="Research quantum computing applications",
expected_output="A summary of practical applications",
agent=researcher
)
# Create a crew with your custom prompt file
crew = Crew(
agents=[researcher],
tasks=[research_task],
prompt_file="path/to/custom_prompts.json",
verbose=True
)
# Run the crew
result = crew.kickoff()
from crewai import Agent, Crew, Task, Process
from crewai_tools import DirectoryReadTool, FileReadTool
# Define templates for system, user (prompt), and assistant (response) messages
system_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>{{ .System }}<|eot_id|>"""
prompt_template = """<|start_header_id|>user<|end_header_id|>{{ .Prompt }}<|eot_id|>"""
response_template = """<|start_header_id|>assistant<|end_header_id|>{{ .Response }}<|eot_id|>"""
# Create an Agent using Llama-specific layouts
principal_engineer = Agent(
role="Principal Engineer",
goal="Oversee AI architecture and make high-level decisions",
backstory="You are the lead engineer responsible for critical AI systems",
verbose=True,
llm="groq/llama-3.3-70b-versatile", # Using the Llama 3 model
system_template=system_template,
prompt_template=prompt_template,
response_template=response_template,
tools=[DirectoryReadTool(), FileReadTool()]
)
# Define a sample task
engineering_task = Task(
description="Review AI implementation files for potential improvements",
expected_output="A summary of key findings and recommendations",
agent=principal_engineer
)
# Create a Crew for the task
llama_crew = Crew(
agents=[principal_engineer],
tasks=[engineering_task],
process=Process.sequential,
verbose=True
)
# Execute the crew
result = llama_crew.kickoff()
print(result.raw)
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-guides-advanced-customizing-prompts/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-guides-advanced-customizing-prompts/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
