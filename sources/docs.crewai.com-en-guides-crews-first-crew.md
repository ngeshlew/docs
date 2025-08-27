---
title: "docs.crewai.com-en-guides-crews-first-crew"
slug: "docs.crewai.com-en-guides-crews-first-crew"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/guides/crews/first-crew"
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

# docs.crewai.com-en-guides-crews-first-crew

> Synthesis: TODO

Step-by-step tutorial to create a collaborative AI team that works together to solve complex problems.
crewai create crew research_crew
cd research_crew
CrewAI Framework Overview
research_crew/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
└── src/
└── research_crew/
├── __init__.py
├── main.py
├── crew.py
├── tools/
│ ├── custom_tool.py
│ └── __init__.py
└── config/
├── agents.yaml
└── tasks.yaml
agents.yaml file to define these specialized agents. Be sure
to set
llm to the provider you are using.
# src/research_crew/config/agents.yaml
researcher:
role: >
Senior Research Specialist for {topic}
goal: >
Find comprehensive and accurate information about {topic}
with a focus on recent developments and key insights
backstory: >
You are an experienced research specialist with a talent for
finding relevant information from various sources. You excel at
organizing information in a clear and structured manner, making
complex topics accessible to others.
llm: provider/model-id # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
analyst:
role: >
Data Analyst and Report Writer for {topic}
goal: >
Analyze research findings and create a comprehensive, well-structured
report that presents insights in a clear and engaging way
backstory: >
You are a skilled analyst with a background in data interpretation
and technical writing. You have a talent for identifying patterns
and extracting meaningful insights from research data, then
communicating those insights effectively through well-crafted reports.
llm: provider/model-id # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
tasks.yaml file:
# src/research_crew/config/tasks.yaml
research_task:
description: >
Conduct thorough research on {topic}. Focus on:
1. Key concepts and definitions
2. Historical development and recent trends
3. Major challenges and opportunities
4. Notable applications or case studies
5. Future outlook and potential developments
Make sure to organize your findings in a structured format with clear sections.
expected_output: >
A comprehensive research document with well-organized sections covering
all the requested aspects of {topic}. Include specific facts, figures,
and examples where relevant.
agent: researcher
analysis_task:
description: >
Analyze the research findings and create a comprehensive report on {topic}.
Your report should:
1. Begin with an executive summary
2. Include all key information from the research
3. Provide insightful analysis of trends and patterns
4. Offer recommendations or future considerations
5. Be formatted in a professional, easy-to-read style with clear headings
expected_output: >
A polished, professional report on {topic} that presents the research
findings with added analysis and insights. The report should be well-structured
with an executive summary, main sections, and conclusion.
agent: analyst
context:
- research_task
output_file: output/report.md
context field in the analysis task - this is a powerful feature that allows the analyst to access the output of the research task. This creates a workflow where information flows naturally between agents, just as it would in a human team.
crew.py file:
# src/research_crew/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
@CrewBase
class ResearchCrew():
"""Research crew for comprehensive topic analysis and reporting"""
agents: List[BaseAgent]
tasks: List[Task]
@agent
def researcher(self) -> Agent:
return Agent(
config=self.agents_config['researcher'], # type: ignore[index]
verbose=True,
tools=[SerperDevTool()]
)
@agent
def analyst(self) -> Agent:
return Agent(
config=self.agents_config['analyst'], # type: ignore[index]
verbose=True
)
@task
def research_task(self) -> Task:
return Task(
config=self.tasks_config['research_task'] # type: ignore[index]
)
@task
def analysis_task(self) -> Task:
return Task(
config=self.tasks_config['analysis_task'], # type: ignore[index]
output_file='output/report.md'
)
@crew
def crew(self) -> Crew:
"""Creates the research crew"""
return Crew(
agents=self.agents,
tasks=self.tasks,
process=Process.sequential,
verbose=True,
)
#!/usr/bin/env python
# src/research_crew/main.py
import os
from research_crew.crew import ResearchCrew
# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)
def run():
"""
Run the research crew.
"""
inputs = {
'topic': 'Artificial Intelligence in Healthcare'
}
# Create and run the crew
result = ResearchCrew().crew().kickoff(inputs=inputs)
# Print the result
print("\n\n=== FINAL REPORT ===\n\n")
print(result.raw)
print("\n\nReport has been saved to output/report.md")
if __name__ == "__main__":
run()
.env file in your project root with your API keys:
SERPER_API_KEY=your_serper_api_key
# Add your provider's API key here too.
crewai install
crewai run
output/report.md file. The report will include:
# View all available commands
crewai --help
# Run the crew
crewai run
# Test the crew
crewai test
# Reset crew memories
crewai reset-memories
# Replay from a specific task
crewai replay -t <task_id>
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-guides-crews-first-crew/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-guides-crews-first-crew/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![CrewAI Framework Overview](../assets/docs.crewai.com/docs.crewai.com-en-guides-crews-first-crew/1b2cec88734b.webp)
<figcaption>Figure 3. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crews.png), License: internal-copy</figcaption>
