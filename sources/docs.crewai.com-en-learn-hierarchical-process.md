---
title: "docs.crewai.com-en-learn-hierarchical-process"
slug: "docs.crewai.com-en-learn-hierarchical-process"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/learn/hierarchical-process"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-learn-hierarchical-process/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-learn-hierarchical-process/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-learn-hierarchical-process

> Synthesis: TODO

A comprehensive guide to understanding and applying the hierarchical process within your CrewAI projects, updated to reflect the latest coding practices and functionalities.
Process.hierarchical, as the default behavior is
Process.sequential.
Define a crew with a designated manager and establish a clear chain of command.
manager_llm parameter is crucial for the hierarchical process.
The system requires a manager LLM to be set up for proper function, ensuring tailored decision-making.
from crewai import Crew, Process, Agent
# Agents are defined with attributes for backstory, cache, and verbose mode
researcher = Agent(
role='Researcher',
goal='Conduct in-depth analysis',
backstory='Experienced data analyst with a knack for uncovering hidden trends.',
)
writer = Agent(
role='Writer',
goal='Create engaging content',
backstory='Creative writer passionate about storytelling in technical domains.',
)
# Establishing the crew with a hierarchical process and additional configurations
project_crew = Crew(
tasks=[...], # Tasks to be delegated and executed under the manager's supervision
agents=[researcher, writer],
manager_llm="gpt-4o", # Specify which LLM the manager should use
process=Process.hierarchical,
planning=True,
)
# Define a custom manager agent
manager = Agent(
role="Project Manager",
goal="Efficiently manage the crew and ensure high-quality task completion",
backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success.",
allow_delegation=True,
)
# Use the custom manager in your crew
project_crew = Crew(
tasks=[...],
agents=[researcher, writer],
manager_agent=manager, # Use your custom manager agent
process=Process.hierarchical,
planning=True,
)
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-learn-hierarchical-process/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-learn-hierarchical-process/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
