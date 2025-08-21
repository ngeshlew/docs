---
title: "docs.crewai.com-en-tools-database-data"
slug: "docs.crewai.com-en-tools-database-data"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/tools/database-data"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-tools-database-data/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-tools-database-data/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-tools-database-data

> Synthesis: TODO

Connect to databases, vector stores, and data warehouses for comprehensive data access
from crewai_tools import MySQLTool, QdrantVectorSearchTool, NL2SQLTool
# Create database tools
mysql_db = MySQLTool()
vector_search = QdrantVectorSearchTool()
nl_to_sql = NL2SQLTool()
# Add to your agent
agent = Agent(
role="Data Analyst",
tools=[mysql_db, vector_search, nl_to_sql],
goal="Extract insights from various data sources"
)
Was this page helpful?

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-tools-database-data/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-tools-database-data/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
