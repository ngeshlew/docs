---
title: "docs.crewai.com-en-tools-cloud-storage"
slug: "docs.crewai.com-en-tools-cloud-storage"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/tools/cloud-storage"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures:
  - path: "../assets/docs.crewai.com/docs.crewai.com-en-tools-cloud-storage/71bc45159c09.webp"
    caption: "light logo"
    credit_name: "docs.crewai.com"
    credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
    license: "internal-copy"
  - path: "../assets/docs.crewai.com/docs.crewai.com-en-tools-cloud-storage/71bc45159c09.webp"
    caption: "dark logo"
    credit_name: "docs.crewai.com"
    credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
    license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-tools-cloud-storage

> Synthesis: TODO

Interact with cloud services, storage systems, and cloud-based AI platforms
from crewai_tools import S3ReaderTool, S3WriterTool, BedrockInvokeAgentTool
# Create cloud tools
s3_reader = S3ReaderTool()
s3_writer = S3WriterTool()
bedrock_agent = BedrockInvokeAgentTool()
# Add to your agent
agent = Agent(
role="Cloud Operations Specialist",
tools=[s3_reader, s3_writer, bedrock_agent],
goal="Manage cloud resources and AI services"
)
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-tools-cloud-storage/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-tools-cloud-storage/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
