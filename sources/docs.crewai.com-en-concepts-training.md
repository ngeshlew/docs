---
title: "docs.crewai.com-en-concepts-training"
slug: "docs.crewai.com-en-concepts-training"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/concepts/training"
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

# docs.crewai.com-en-concepts-training

> Synthesis: TODO

Learn how to train your CrewAI agents by giving them feedback early on and get consistent results.
crewai train -n <n_iterations>, you can specify the number of iterations for the training process.
During training, CrewAI utilizes techniques to optimize the performance of your agents along with human feedback.
This helps the agents improve their understanding, decision-making, and problem-solving abilities.
crewai train -n <n_iterations> <filename> (optional)
<n_iterations> with the desired number of training iterations and
<filename> with the appropriate filename ending with
.pkl.
n_iterations = 2
inputs = {"topic": "CrewAI Training"}
filename = "your_model.pkl"
try:
YourCrewName_Crew().crew().train(
n_iterations=n_iterations,
inputs=inputs,
filename=filename
)
except Exception as e:
raise Exception(f"An error occurred while training the crew: {e}")
n_iterations) is a positive integer. The code will raise a
ValueError if this condition is not met.
.pkl. The code will raise a
ValueError if this condition is not met.
from crewai import Agent, Crew, Task, LLM
# Recommended minimum for training evaluation
llm = LLM(model="mistral/open-mistral-7b")
# Better options for reliable training evaluation
llm = LLM(model="anthropic/claude-3-sonnet-20240229-v1:0")
llm = LLM(model="gpt-4o")
# Use this LLM with your agents
agent = Agent(
role="Training Evaluator",
goal="Provide accurate training feedback",
llm=llm
)
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-training/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-training/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
