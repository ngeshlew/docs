---
title: "docs.crewai.com-en-concepts-processes"
slug: "docs.crewai.com-en-concepts-processes"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/concepts/processes"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-processes/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-processes/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-concepts-processes

> Synthesis: TODO

Detailed guide on workflow management through processes in CrewAI, with updated implementation details.
manager_llm) or a custom manager agent (
manager_agent) must be specified in the crew to enable the hierarchical process, facilitating the creation and management of tasks by the manager.
manager_llm or
manager_agent for the manager agent.
from crewai import Crew, Process
# Example: Creating a crew with a sequential process
crew = Crew(
agents=my_agents,
tasks=my_tasks,
process=Process.sequential
)
# Example: Creating a crew with a hierarchical process
# Ensure to provide a manager_llm or manager_agent
crew = Crew(
agents=my_agents,
tasks=my_tasks,
process=Process.hierarchical,
manager_llm="gpt-4o"
# or
# manager_agent=my_manager_agent
)
my_agents and
my_tasks are defined prior to creating a
Crew object, and for the hierarchical process, either
manager_llm or
manager_agent is also required.
context parameter in the
Task class to specify outputs that should be used as context for subsequent tasks.
manager_llm). This agent oversees task execution, including planning, delegation, and validation. Tasks are not pre-assigned; the manager allocates tasks to agents based on their capabilities, reviews outputs, and assesses task completion.
Process class is implemented as an enumeration (
Enum), ensuring type safety and restricting process values to the defined types (
sequential,
hierarchical). The consensual process is planned for future inclusion, emphasizing our commitment to continuous development and innovation.
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-processes/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-processes/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
