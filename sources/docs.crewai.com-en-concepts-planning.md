---
title: "docs.crewai.com-en-concepts-planning"
slug: "docs.crewai.com-en-concepts-planning"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/concepts/planning"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-planning/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-planning/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-concepts-planning

> Synthesis: TODO

Learn how to add planning to your CrewAI Crew and improve their performance.
planning=True to your Crew:
from crewai import Crew, Agent, Task, Process
# Assemble your crew with planning capabilities
my_crew = Crew(
agents=self.agents,
tasks=self.tasks,
process=Process.sequential,
planning=True,
)
gpt-4o-mini as the default LLM for planning, which requires a valid OpenAI API key. Since your agents might be using different LLMs, this could cause confusion if you don’t have an OpenAI API key configured or if you’re experiencing unexpected behavior related to LLM API calls.
AgentPlanner
responsible for creating the step-by-step logic to add to the Agents’ tasks.
from crewai import Crew, Agent, Task, Process
# Assemble your crew with planning capabilities and custom LLM
my_crew = Crew(
agents=self.agents,
tasks=self.tasks,
process=Process.sequential,
planning=True,
planning_llm="gpt-4o"
)
# Run the crew
my_crew.kickoff()

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-planning/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-planning/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
