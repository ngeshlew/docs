---
title: "docs.crewai.com-en-learn-custom-manager-agent"
slug: "docs.crewai.com-en-learn-custom-manager-agent"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/learn/custom-manager-agent"
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

# docs.crewai.com-en-learn-custom-manager-agent

> Synthesis: TODO

Learn how to set a custom agent as the manager in CrewAI, providing more control over task management and coordination.
manager_agent Attribute
manager_agent attribute allows you to define a custom agent to manage the crew. This agent will oversee the entire process, ensuring that tasks are completed efficiently and to the highest standard.
import os
from crewai import Agent, Task, Crew, Process
# Define your agents
researcher = Agent(
role="Researcher",
goal="Conduct thorough research and analysis on AI and AI agents",
backstory="You're an expert researcher, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently researching for a new client.",
allow_delegation=False,
)
writer = Agent(
role="Senior Writer",
goal="Create compelling content about AI and AI agents",
backstory="You're a senior writer, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently writing content for a new client.",
allow_delegation=False,
)
# Define your task
task = Task(
description="Generate a list of 5 interesting ideas for an article, then write one captivating paragraph for each idea that showcases the potential of a full article on this topic. Return the list of ideas with their paragraphs and your notes.",
expected_output="5 bullet points, each with a paragraph and accompanying notes.",
)
# Define the manager agent
manager = Agent(
role="Project Manager",
goal="Efficiently manage the crew and ensure high-quality task completion",
backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
allow_delegation=True,
)
# Instantiate your crew with a custom manager
crew = Crew(
agents=[researcher, writer],
tasks=[task],
manager_agent=manager,
process=Process.hierarchical,
)
# Start the crew's work
result = crew.kickoff()
from crewai import LLM
manager_llm = LLM(model="gpt-4o")
crew = Crew(
agents=[researcher, writer],
tasks=[task],
process=Process.hierarchical,
manager_llm=manager_llm
)
manager_agent or
manager_llm must be set when using the hierarchical process.
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-learn-custom-manager-agent/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-learn-custom-manager-agent/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
