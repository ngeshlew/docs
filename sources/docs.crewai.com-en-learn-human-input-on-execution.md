---
title: "docs.crewai.com-en-learn-human-input-on-execution"
slug: "docs.crewai.com-en-learn-human-input-on-execution"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/learn/human-input-on-execution"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-learn-human-input-on-execution/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-learn-human-input-on-execution/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-learn-human-input-on-execution

> Synthesis: TODO

Integrating CrewAI with human input during execution in complex decision-making processes and leveraging the full capabilities of the agent’s attributes and tools.
human_input flag in the task definition. When enabled, the agent prompts the user for input before delivering its final answer.
This input can provide extra context, clarify ambiguities, or validate the agent’s output.
pip install crewai
import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"
# Loading Tools
search_tool = SerperDevTool()
# Define your agents with roles, goals, tools, and additional attributes
researcher = Agent(
role='Senior Research Analyst',
goal='Uncover cutting-edge developments in AI and data science',
backstory=(
"You are a Senior Research Analyst at a leading tech think tank. "
"Your expertise lies in identifying emerging trends and technologies in AI and data science. "
"You have a knack for dissecting complex data and presenting actionable insights."
),
verbose=True,
allow_delegation=False,
tools=[search_tool]
)
writer = Agent(
role='Tech Content Strategist',
goal='Craft compelling content on tech advancements',
backstory=(
"You are a renowned Tech Content Strategist, known for your insightful and engaging articles on technology and innovation. "
"With a deep understanding of the tech industry, you transform complex concepts into compelling narratives."
),
verbose=True,
allow_delegation=True,
tools=[search_tool],
cache=False, # Disable cache for this agent
)
# Create tasks for your agents
task1 = Task(
description=(
"Conduct a comprehensive analysis of the latest advancements in AI in 2025. "
"Identify key trends, breakthrough technologies, and potential industry impacts. "
"Compile your findings in a detailed report. "
"Make sure to check with a human if the draft is good before finalizing your answer."
),
expected_output='A comprehensive full report on the latest AI advancements in 2025, leave nothing out',
agent=researcher,
human_input=True
)
task2 = Task(
description=(
"Using the insights from the researcher\'s report, develop an engaging blog post that highlights the most significant AI advancements. "
"Your post should be informative yet accessible, catering to a tech-savvy audience. "
"Aim for a narrative that captures the essence of these breakthroughs and their implications for the future."
),
expected_output='A compelling 3 paragraphs blog post formatted as markdown about the latest AI advancements in 2025',
agent=writer,
human_input=True
)
# Instantiate your crew with a sequential process
crew = Crew(
agents=[researcher, writer],
tasks=[task1, task2],
verbose=True,
memory=True,
planning=True # Enable planning feature for the crew
)
# Get your crew to work!
result = crew.kickoff()
print("######################")
print(result)
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-learn-human-input-on-execution/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-learn-human-input-on-execution/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
