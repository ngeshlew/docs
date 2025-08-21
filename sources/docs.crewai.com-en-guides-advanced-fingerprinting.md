---
title: "docs.crewai.com-en-guides-advanced-fingerprinting"
slug: "docs.crewai.com-en-guides-advanced-fingerprinting"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/guides/advanced/fingerprinting"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-guides-advanced-fingerprinting/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-guides-advanced-fingerprinting/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-guides-advanced-fingerprinting

> Synthesis: TODO

Learn how to use CrewAI’s fingerprinting system to uniquely identify and track components throughout their lifecycle.
Agent,
Crew, and
Task automatically receives a unique fingerprint when created, which cannot be manually overridden.
These fingerprints can be used for:
Fingerprint class from the
crewai.security module. Each fingerprint contains:
from crewai import Agent, Crew, Task
# Create components - fingerprints are automatically generated
agent = Agent(
role="Data Scientist",
goal="Analyze data",
backstory="Expert in data analysis"
)
crew = Crew(
agents=[agent],
tasks=[]
)
task = Task(
description="Analyze customer data",
expected_output="Insights from data analysis",
agent=agent
)
# Access the fingerprints
agent_fingerprint = agent.fingerprint
crew_fingerprint = crew.fingerprint
task_fingerprint = task.fingerprint
# Print the UUID strings
print(f"Agent fingerprint: {agent_fingerprint.uuid_str}")
print(f"Crew fingerprint: {crew_fingerprint.uuid_str}")
print(f"Task fingerprint: {task_fingerprint.uuid_str}")
# Add metadata to the agent's fingerprint
agent.security_config.fingerprint.metadata = {
"version": "1.0",
"department": "Data Science",
"project": "Customer Analysis"
}
# Access the metadata
print(f"Agent metadata: {agent.fingerprint.metadata}")
original_fingerprint = agent.fingerprint.uuid_str
# Modify the agent
agent.goal = "New goal for analysis"
# The fingerprint remains unchanged
assert agent.fingerprint.uuid_str == original_fingerprint
generate method with a seed:
from crewai.security import Fingerprint
# Create a deterministic fingerprint using a seed string
deterministic_fingerprint = Fingerprint.generate(seed="my-agent-id")
# The same seed always produces the same fingerprint
same_fingerprint = Fingerprint.generate(seed="my-agent-id")
assert deterministic_fingerprint.uuid_str == same_fingerprint.uuid_str
# You can also set metadata
custom_fingerprint = Fingerprint.generate(
seed="my-agent-id",
metadata={"version": "1.0"}
)
from crewai.security import Fingerprint
fingerprint = agent.fingerprint
# UUID string - the unique identifier (auto-generated)
uuid_str = fingerprint.uuid_str # e.g., "123e4567-e89b-12d3-a456-426614174000"
# Creation timestamp (auto-generated)
created_at = fingerprint.created_at # A datetime object
# Metadata - for additional information (can be customized)
metadata = fingerprint.metadata # A dictionary, defaults to {}
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-guides-advanced-fingerprinting/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-guides-advanced-fingerprinting/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
