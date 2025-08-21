---
title: "docs.crewai.com-en-tools-file-document"
slug: "docs.crewai.com-en-tools-file-document"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/tools/file-document"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-tools-file-document/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-tools-file-document/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-tools-file-document

> Synthesis: TODO

Read, write, and search through various file formats with CrewAI’s document processing tools
from crewai_tools import FileReadTool, PDFSearchTool, JSONSearchTool
# Create tools
file_reader = FileReadTool()
pdf_searcher = PDFSearchTool()
json_processor = JSONSearchTool()
# Add to your agent
agent = Agent(
role="Document Analyst",
tools=[file_reader, pdf_searcher, json_processor],
goal="Process and analyze various document types"
)
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-tools-file-document/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-tools-file-document/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
