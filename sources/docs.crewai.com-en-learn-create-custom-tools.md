---
title: "docs.crewai.com-en-learn-create-custom-tools"
slug: "docs.crewai.com-en-learn-create-custom-tools"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/learn/create-custom-tools"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: []
- path: "../assets/docs.crewai.com/docs.crewai.com-en-learn-create-custom-tools/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-learn-create-custom-tools/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-learn-create-custom-tools

> Synthesis: TODO

Comprehensive guide on crafting, using, and managing custom tools within the CrewAI framework, including new functionalities and error handling.
BaseTool
BaseTool and define the necessary attributes, including the
args_schema for input validation, and the
_run method.
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
class MyToolInput(BaseModel):
"""Input schema for MyCustomTool."""
argument: str = Field(..., description="Description of the argument.")
class MyCustomTool(BaseTool):
name: str = "Name of my tool"
description: str = "What this tool does. It's vital for effective utilization."
args_schema: Type[BaseModel] = MyToolInput
def _run(self, argument: str) -> str:
# Your tool's logic here
return "Tool's result"
tool Decorator
@tool. This approach allows you to define the tool’s attributes and functionality directly within a function,
offering a concise and efficient way to create specialized tools tailored to your needs.
from crewai.tools import tool
@tool("Tool Name")
def my_simple_tool(question: str) -> str:
"""Tool description for clarity."""
# Tool logic here
return "Tool output"
cache_function attribute.
@tool("Tool with Caching")
def cached_tool(argument: str) -> str:
"""Tool functionality description."""
return "Cacheable result"
def my_cache_strategy(arguments: dict, result: str) -> bool:
# Define custom caching logic
return True if some_condition else False
cached_tool.cache_function = my_cache_strategy
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-learn-create-custom-tools/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-learn-create-custom-tools/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
