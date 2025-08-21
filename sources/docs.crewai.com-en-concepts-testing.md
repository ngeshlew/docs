---
title: "docs.crewai.com-en-concepts-testing"
slug: "docs.crewai.com-en-concepts-testing"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/concepts/testing"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-testing/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-testing/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-concepts-testing

> Synthesis: TODO

Learn how to test your CrewAI Crew and evaluate their performance.
crewai test to make it easy to test your crew. This command will run your crew for a specified number of iterations and provide detailed performance metrics. The parameters are
n_iterations and
model, which are optional and default to 2 and
gpt-4o-mini respectively. For now, the only provider available is OpenAI.
crewai test
crewai test --n_iterations 5 --model gpt-4o
crewai test -n 5 -m gpt-4o
crewai test command, the crew will be executed for the specified number of iterations, and the performance metrics will be displayed at the end of the run.
A table of scores at the end will show the performance of the crew in terms of the following metrics:
|Tasks/Crew/Agents
|Run 1
|Run 2
|Avg. Total
|Agents
|Additional Info
|Task 1
|9.0
|9.5
9.2 |Professional Insights
|Researcher
|Task 2
|9.0
|10.0
9.5 |Company Profile Investigator
|Task 3
|9.0
|9.0
9.0 |Automation Insights
|Specialist
|Task 4
|9.0
|9.0
9.0 |Final Report Compiler
|Automation Insights Specialist
|Crew
|9.00
|9.38
9.2
|Execution Time (s)
|126
|145
135

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-testing/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-testing/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
