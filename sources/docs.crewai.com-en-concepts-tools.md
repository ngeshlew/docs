---
title: "docs.crewai.com-en-concepts-tools"
slug: "docs.crewai.com-en-concepts-tools"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/concepts/tools"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: []
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-tools/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-tools/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-concepts-tools

> Synthesis: TODO

Understanding and leveraging tools within the CrewAI framework for agent collaboration and task execution.
pip install 'crewai[tools]'
import os
from crewai import Agent, Task, Crew
# Importing crewAI tools
from crewai_tools import (
DirectoryReadTool,
FileReadTool,
SerperDevTool,
WebsiteSearchTool
)
# Set up API keys
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"
# Instantiate tools
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()
# Create agents
researcher = Agent(
role='Market Research Analyst',
goal='Provide up-to-date market analysis of the AI industry',
backstory='An expert analyst with a keen eye for market trends.',
tools=[search_tool, web_rag_tool],
verbose=True
)
writer = Agent(
role='Content Writer',
goal='Craft engaging blog posts about the AI industry',
backstory='A skilled writer with a passion for technology.',
tools=[docs_tool, file_tool],
verbose=True
)
# Define tasks
research = Task(
description='Research the latest trends in the AI industry and provide a summary.',
expected_output='A summary of the top 3 trending developments in the AI industry with a unique perspective on their significance.',
agent=researcher
)
write = Task(
description='Write an engaging blog post about the AI industry, based on the research analyst's summary. Draw inspiration from the latest blog posts in the directory.',
expected_output='A 4-paragraph blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
agent=writer,
output_file='blog-posts/new_post.md' # The final blog post will be saved here
)
# Assemble a crew with planning enabled
crew = Crew(
agents=[researcher, writer],
tasks=[research, write],
verbose=True,
planning=True, # Enable planning feature
)
# Execute tasks
crew.kickoff()
cache_function attribute on the tool.
|Tool
|Description
ApifyActorsTool |A tool that integrates Apify Actors with your workflows for web scraping and automation tasks.
BrowserbaseLoadTool |A tool for interacting with and extracting data from web browsers.
CodeDocsSearchTool |A RAG tool optimized for searching through code documentation and related technical documents.
CodeInterpreterTool |A tool for interpreting python code.
ComposioTool |Enables use of Composio tools.
CSVSearchTool |A RAG tool designed for searching within CSV files, tailored to handle structured data.
DALL-E Tool |A tool for generating images using the DALL-E API.
DirectorySearchTool |A RAG tool for searching within directories, useful for navigating through file systems.
DOCXSearchTool |A RAG tool aimed at searching within DOCX documents, ideal for processing Word files.
DirectoryReadTool |Facilitates reading and processing of directory structures and their contents.
EXASearchTool |A tool designed for performing exhaustive searches across various data sources.
FileReadTool |Enables reading and extracting data from files, supporting various file formats.
FirecrawlSearchTool |A tool to search webpages using Firecrawl and return the results.
FirecrawlCrawlWebsiteTool |A tool for crawling webpages using Firecrawl.
FirecrawlScrapeWebsiteTool |A tool for scraping webpages URL using Firecrawl and returning its contents.
GithubSearchTool |A RAG tool for searching within GitHub repositories, useful for code and documentation search.
SerperDevTool |A specialized tool for development purposes, with specific functionalities under development.
TXTSearchTool |A RAG tool focused on searching within text (.txt) files, suitable for unstructured data.
JSONSearchTool |A RAG tool designed for searching within JSON files, catering to structured data handling.
LlamaIndexTool |Enables the use of LlamaIndex tools.
MDXSearchTool |A RAG tool tailored for searching within Markdown (MDX) files, useful for documentation.
PDFSearchTool |A RAG tool aimed at searching within PDF documents, ideal for processing scanned documents.
PGSearchTool |A RAG tool optimized for searching within PostgreSQL databases, suitable for database queries.
Vision Tool |A tool for generating images using the DALL-E API.
RagTool |A general-purpose RAG tool capable of handling various data sources and types.
ScrapeElementFromWebsiteTool |Enables scraping specific elements from websites, useful for targeted data extraction.
ScrapeWebsiteTool |Facilitates scraping entire websites, ideal for comprehensive data collection.
WebsiteSearchTool |A RAG tool for searching website content, optimized for web data extraction.
XMLSearchTool |A RAG tool designed for searching within XML files, suitable for structured data formats.
YoutubeChannelSearchTool |A RAG tool for searching within YouTube channels, useful for video content analysis.
YoutubeVideoSearchTool |A RAG tool aimed at searching within YouTube videos, ideal for video data extraction.
custom tools tailored for their agent’s needs or
utilize pre-built options.
BaseTool
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
tool Decorator with Async Functions
from crewai.tools import tool
@tool("fetch_data_async")
async def fetch_data_async(query: str) -> str:
"""Asynchronously fetch data based on the query."""
# Simulate async operation
await asyncio.sleep(1)
return f"Data retrieved for {query}"
from crewai.tools import BaseTool
class AsyncCustomTool(BaseTool):
name: str = "async_custom_tool"
description: str = "An asynchronous custom tool"
async def _run(self, query: str = "") -> str:
"""Asynchronously run the tool"""
# Your async implementation here
await asyncio.sleep(1)
return f"Processed {query} asynchronously"
# In standard Crew
agent = Agent(role="researcher", tools=[async_custom_tool])
# In Flow
class MyFlow(Flow):
@start()
async def begin(self):
crew = Crew(agents=[agent])
result = await crew.kickoff_async()
return result
tool Decorator
from crewai.tools import tool
@tool("Name of my tool")
def my_tool(question: str) -> str:
"""Clear description for what this tool is useful for, your agent will need this information to use it."""
# Function logic here
return "Result from your custom tool"
cache_function to fine-tune caching
behavior. This function determines when to cache results based on specific
conditions, offering granular control over caching logic.
from crewai.tools import tool
@tool
def multiplication_tool(first_number: int, second_number: int) -> str:
"""Useful for when you need to multiply two numbers together."""
return first_number * second_number
def cache_func(args, result):
# In this case, we only cache the result if it's a multiple of 2
cache = result % 2 == 0
return cache
multiplication_tool.cache_function = cache_func
writer1 = Agent(
role="Writer",
goal="You write lessons of math for kids.",
backstory="You're an expert in writing and you love to teach kids but you know nothing of math.",
tools=[multiplication_tool],
allow_delegation=False,
)
#...
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-tools/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-tools/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
