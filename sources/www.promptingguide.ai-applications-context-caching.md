---
title: "www.promptingguide.ai-applications-context-caching"
slug: "www.promptingguide.ai-applications-context-caching"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://www.promptingguide.ai/applications/context-caching"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: []
updatedAt: "'2025-08-18'"
completed: false
---

# www.promptingguide.ai-applications-context-caching

> Synthesis: TODO

# Context Caching with Gemini 1.5 Flash
Google recently released a new feature called context-caching (opens in a new tab) which is available via the Gemini APIs through the Gemini 1.5 Pro and Gemini 1.5 Flash models. This guide provides a basic example of how to use context-caching with Gemini 1.5 Flash.
https://youtu.be/987Pd89EDPs?si=j43isgNb0uwH5AeI (opens in a new tab)
### The Use Case: Analyzing a Year's Worth of ML Papers
The guide demonstrates how you can use context caching to analyze the summaries of all the ML papers we've documented over the past year (opens in a new tab). We store these summaries in a text file, which can now be fed to the Gemini 1.5 Flash model and query efficiently.
### The Process: Uploading, Caching, and Querying
**Data Preparation:**First convert the readme file (containing the summaries) into a plain text file. **Utilizing the Gemini API:**You can upload the text file using the Google
generativeailibrary.
**Implementing Context Caching:**A cache is created using the
caching.CachedContent.create()function. This involves:
- Specifying the Gemini Flash 1.5 model.
- Providing a name for the cache.
- Defining an instruction for the model (e.g., "You are an expert AI researcher...").
- Setting a time-to-live (TTL) for the cache (e.g., 15 minutes).
**Creating the Model:**We then create a generative model instance using the cached content. **Querying:**We can start querying the model with natural language questions like:
- "Can you please tell me the latest AI papers of the week?"
- "Can you list the papers that mention Mamba? List the title of the paper and summary."
- "What are some of the innovations around long-context LLMs? List the title of the paper and summary."
The results were promising. The model accurately retrieved and summarized information from the text file. Context caching proved highly efficient, eliminating the need to repeatedly send the entire text file with each query.
This workflow has the potential to be a valuable tool for researchers, allowing them to:
- Quickly analyze and query large amounts of research data.
- Retrieve specific findings without manually searching through documents.
- Conduct interactive research sessions without wasting prompt tokens.
We are excited to explore further applications of context caching, especially within more complex scenarios like agentic workflows.
The notebook can be found below:
Learn more about caching methods in our new AI courses. Join now! (opens in a new tab) Use code PROMPTING20 to get an extra 20% off.


