---
title: "docs.crewai.com-en-concepts-memory"
slug: "docs.crewai.com-en-concepts-memory"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/concepts/memory"
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

# docs.crewai.com-en-concepts-memory

> Synthesis: TODO

Leveraging memory systems in the CrewAI framework to enhance agent capabilities.
|Component
|Description
Short-Term Memory |Temporarily stores recent interactions and outcomes using
RAG, enabling agents to recall and utilize information relevant to their current context during the current executions.
Long-Term Memory |Preserves valuable insights and learnings from past executions, allowing agents to build and refine their knowledge over time.
Entity Memory |Captures and organizes information about entities (people, places, concepts) encountered during tasks, facilitating deeper understanding and relationship mapping. Uses
RAG for storing entity information.
Contextual Memory |Maintains the context of interactions by combining
ShortTermMemory,
LongTermMemory,
ExternalMemory and
EntityMemory, aiding in the coherence and relevance of agent responses over a sequence of tasks or a conversation.
from crewai import Crew, Agent, Task, Process
# Enable basic memory system
crew = Crew(
agents=[...],
tasks=[...],
process=Process.sequential,
memory=True, # Enables short-term, long-term, and entity memory
verbose=True
)
appdirs package
CREWAI_STORAGE_DIR environment variable
appdirs library to determine storage locations following platform conventions. Here’s exactly where your files are stored:
~/Library/Application Support/CrewAI/{project_name}/
├── knowledge/ # Knowledge base ChromaDB files
├── short_term_memory/ # Short-term memory ChromaDB files
├── long_term_memory/ # Long-term memory ChromaDB files
├── entities/ # Entity memory ChromaDB files
└── long_term_memory_storage.db # SQLite database
~/.local/share/CrewAI/{project_name}/
├── knowledge/
├── short_term_memory/
├── long_term_memory/
├── entities/
└── long_term_memory_storage.db
C:\Users\{username}\AppData\Local\CrewAI\{project_name}\
├── knowledge\
├── short_term_memory\
├── long_term_memory\
├── entities\
└── long_term_memory_storage.db
from crewai.utilities.paths import db_storage_path
import os
# Get the base storage path
storage_path = db_storage_path()
print(f"CrewAI storage location: {storage_path}")
# List all CrewAI storage directories
if os.path.exists(storage_path):
print("\nStored files and directories:")
for item in os.listdir(storage_path):
item_path = os.path.join(storage_path, item)
if os.path.isdir(item_path):
print(f"📁 {item}/")
# Show ChromaDB collections
if os.path.exists(item_path):
for subitem in os.listdir(item_path):
print(f" └── {subitem}")
else:
print(f"📄 {item}")
else:
print("No CrewAI storage directory found yet.")
import os
from crewai import Crew
# Set custom storage location
os.environ["CREWAI_STORAGE_DIR"] = "./my_project_storage"
# All memory and knowledge will now be stored in ./my_project_storage/
crew = Crew(
agents=[...],
tasks=[...],
memory=True
)
import os
from crewai import Crew
from crewai.memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
# Configure custom storage location
custom_storage_path = "./storage"
os.makedirs(custom_storage_path, exist_ok=True)
crew = Crew(
memory=True,
long_term_memory=LongTermMemory(
storage=LTMSQLiteStorage(
db_path=f"{custom_storage_path}/memory.db"
)
)
)
import os
from pathlib import Path
# Store in project directory
project_root = Path(__file__).parent
storage_dir = project_root / "crewai_storage"
os.environ["CREWAI_STORAGE_DIR"] = str(storage_dir)
# Now all storage will be in your project directory
# When using Claude as your LLM...
from crewai import Agent, LLM
agent = Agent(
role="Analyst",
goal="Analyze data",
backstory="Expert analyst",
llm=LLM(provider="anthropic", model="claude-3-sonnet") # Using Claude
)
# CrewAI will use OpenAI embeddings by default for consistency
# You can easily customize this to match your preferred provider
from crewai import Crew
# Option 1: Match your LLM provider
crew = Crew(
agents=[agent],
tasks=[task],
memory=True,
embedder={
"provider": "anthropic", # Match your LLM provider
"config": {
"api_key": "your-anthropic-key",
"model": "text-embedding-3-small"
}
}
)
# Option 2: Use local embeddings (no external API calls)
crew = Crew(
agents=[agent],
tasks=[task],
memory=True,
embedder={
"provider": "ollama",
"config": {"model": "mxbai-embed-large"}
}
)
import os
from crewai.utilities.paths import db_storage_path
storage_path = db_storage_path()
print(f"Storage path: {storage_path}")
print(f"Path exists: {os.path.exists(storage_path)}")
print(f"Is writable: {os.access(storage_path, os.W_OK) if os.path.exists(storage_path) else 'Path does not exist'}")
# Create with proper permissions
if not os.path.exists(storage_path):
os.makedirs(storage_path, mode=0o755, exist_ok=True)
print(f"Created storage directory: {storage_path}")
import chromadb
from crewai.utilities.paths import db_storage_path
# Connect to CrewAI's ChromaDB
storage_path = db_storage_path()
chroma_path = os.path.join(storage_path, "knowledge")
if os.path.exists(chroma_path):
client = chromadb.PersistentClient(path=chroma_path)
collections = client.list_collections()
print("ChromaDB Collections:")
for collection in collections:
print(f" - {collection.name}: {collection.count()} documents")
else:
print("No ChromaDB storage found")
from crewai import Crew
# Reset all memory storage
crew = Crew(agents=[...], tasks=[...], memory=True)
# Reset specific memory types
crew.reset_memories(command_type='short') # Short-term memory
crew.reset_memories(command_type='long') # Long-term memory
crew.reset_memories(command_type='entity') # Entity memory
crew.reset_memories(command_type='knowledge') # Knowledge storage
CREWAI_STORAGE_DIR
# Fix permissions
chmod -R 755 ~/.local/share/CrewAI/
# Ensure only one CrewAI instance accesses storage
import fcntl
import os
storage_path = db_storage_path()
lock_file = os.path.join(storage_path, ".crewai.lock")
with open(lock_file, 'w') as f:
fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
# Your CrewAI code here
# Verify storage location is consistent
import os
print("CREWAI_STORAGE_DIR:", os.getenv("CREWAI_STORAGE_DIR"))
print("Current working directory:", os.getcwd())
print("Computed storage path:", db_storage_path())
from crewai import Crew
# Basic OpenAI configuration (uses environment OPENAI_API_KEY)
crew = Crew(
agents=[...],
tasks=[...],
memory=True,
embedder={
"provider": "openai",
"config": {
"model": "text-embedding-3-small" # or "text-embedding-3-large"
}
}
)
# Advanced OpenAI configuration
crew = Crew(
memory=True,
embedder={
"provider": "openai",
"config": {
"api_key": "your-openai-api-key", # Optional: override env var
"model": "text-embedding-3-large",
"dimensions": 1536, # Optional: reduce dimensions for smaller storage
"organization_id": "your-org-id" # Optional: for organization accounts
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "openai", # Use openai provider for Azure
"config": {
"api_key": "your-azure-api-key",
"api_base": "https://your-resource.openai.azure.com/",
"api_type": "azure",
"api_version": "2023-05-15",
"model": "text-embedding-3-small",
"deployment_id": "your-deployment-name" # Azure deployment name
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "google",
"config": {
"api_key": "your-google-api-key",
"model": "text-embedding-004" # or "text-embedding-preview-0409"
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "vertexai",
"config": {
"project_id": "your-gcp-project-id",
"region": "us-central1", # or your preferred region
"api_key": "your-service-account-key",
"model_name": "textembedding-gecko"
}
}
)
# First, install and run Ollama locally, then pull an embedding model:
# ollama pull mxbai-embed-large
crew = Crew(
memory=True,
embedder={
"provider": "ollama",
"config": {
"model": "mxbai-embed-large", # or "nomic-embed-text"
"url": "http://localhost:11434/api/embeddings" # Default Ollama URL
}
}
)
# For custom Ollama installations
crew = Crew(
memory=True,
embedder={
"provider": "ollama",
"config": {
"model": "mxbai-embed-large",
"url": "http://your-ollama-server:11434/api/embeddings"
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "cohere",
"config": {
"api_key": "your-cohere-api-key",
"model": "embed-english-v3.0" # or "embed-multilingual-v3.0"
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "voyageai",
"config": {
"api_key": "your-voyage-api-key",
"model": "voyage-large-2", # or "voyage-code-2" for code
"input_type": "document" # or "query"
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "bedrock",
"config": {
"aws_access_key_id": "your-access-key",
"aws_secret_access_key": "your-secret-key",
"region_name": "us-east-1",
"model": "amazon.titan-embed-text-v1"
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "huggingface",
"config": {
"api_key": "your-hf-token", # Optional for public models
"model": "sentence-transformers/all-MiniLM-L6-v2",
"api_url": "https://api-inference.huggingface.co" # or your custom endpoint
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "watson",
"config": {
"api_key": "your-watson-api-key",
"url": "your-watson-instance-url",
"model": "ibm/slate-125m-english-rtrvr"
}
}
)
from crewai.memory.short_term.short_term_memory import ShortTermMemory
from crewai.memory.entity_entity_memory import EntityMemory
mem0_oss_embedder_config = {
"provider": "mem0",
"config": {
"user_id": "john",
"local_mem0_config": {
"vector_store": {"provider": "qdrant","config": {"host": "localhost", "port": 6333}},
"llm": {"provider": "openai","config": {"api_key": "your-api-key", "model": "gpt-4"}},
"embedder": {"provider": "openai","config": {"api_key": "your-api-key", "model": "text-embedding-3-small"}}
},
"infer": True # Optional defaults to True
},
}
mem0_client_embedder_config = {
"provider": "mem0",
"config": {
"user_id": "john",
"org_id": "my_org_id", # Optional
"project_id": "my_project_id", # Optional
"api_key": "custom-api-key" # Optional - overrides env var
"run_id": "my_run_id", # Optional - for short-term memory
"includes": "include1", # Optional
"excludes": "exclude1", # Optional
"infer": True # Optional defaults to True
"custom_categories": new_categories # Optional - custom categories for user memory
},
}
short_term_memory_mem0_oss = ShortTermMemory(embedder_config=mem0_oss_embedder_config) # Short Term Memory with Mem0 OSS
short_term_memory_mem0_client = ShortTermMemory(embedder_config=mem0_client_embedder_config) # Short Term Memory with Mem0 Client
entity_memory_mem0_oss = EntityMemory(embedder_config=mem0_oss_embedder_config) # Entity Memory with Mem0 OSS
entity_memory_mem0_client = EntityMemory(embedder_config=mem0_client_embedder_config) # Short Term Memory with Mem0 Client
crew = Crew(
memory=True,
short_term_memory=short_term_memory_mem0_oss, # or short_term_memory_mem0_client
entity_memory=entity_memory_mem0_oss # or entity_memory_mem0_client
)
|Provider
|Best For
|Pros
|Cons
OpenAI |General use, high reliability
|High quality, widely tested
|Paid service, API key required
Ollama |Privacy-focused, cost savings
|Free, runs locally, fully private
|Requires local installation/setup
Google AI |Integration in Google ecosystem
|Strong performance, good support
|Google account required
Azure OpenAI |Enterprise & compliance needs
|Enterprise-grade features, security
|More complex setup process
Cohere |Multilingual content handling
|Excellent language support
|More niche use cases
VoyageAI |Information retrieval & search
|Optimized for retrieval tasks
|Relatively new provider
Mem0 |Per-user personalization
|Search-optimized embeddings
|Paid service, API key required
import os
# Set environment variables
os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["GOOGLE_API_KEY"] = "your-google-key"
os.environ["COHERE_API_KEY"] = "your-cohere-key"
# Use without exposing keys in code
crew = Crew(
memory=True,
embedder={
"provider": "openai",
"config": {
"model": "text-embedding-3-small"
# API key automatically loaded from environment
}
}
)
from crewai import Crew
from crewai.utilities.paths import db_storage_path
# Test different providers with the same data
providers_to_test = [
{
"name": "OpenAI",
"config": {
"provider": "openai",
"config": {"model": "text-embedding-3-small"}
}
},
{
"name": "Ollama",
"config": {
"provider": "ollama",
"config": {"model": "mxbai-embed-large"}
}
}
]
for provider in providers_to_test:
print(f"\nTesting {provider['name']} embeddings...")
# Create crew with specific embedder
crew = Crew(
agents=[...],
tasks=[...],
memory=True,
embedder=provider['config']
)
# Run your test and measure performance
result = crew.kickoff()
print(f"{provider['name']} completed successfully")
# Verify model availability
from crewai.rag.embeddings.configurator import EmbeddingConfigurator
configurator = EmbeddingConfigurator()
try:
embedder = configurator.configure_embedder({
"provider": "ollama",
"config": {"model": "mxbai-embed-large"}
})
print("Embedder configured successfully")
except Exception as e:
print(f"Configuration error: {e}")
import os
# Check if API keys are set
required_keys = ["OPENAI_API_KEY", "GOOGLE_API_KEY", "COHERE_API_KEY"]
for key in required_keys:
if os.getenv(key):
print(f"✅ {key} is set")
else:
print(f"❌ {key} is not set")
import time
def test_embedding_performance(embedder_config, test_text="This is a test document"):
start_time = time.time()
crew = Crew(
agents=[...],
tasks=[...],
memory=True,
embedder=embedder_config
)
# Simulate memory operation
crew.kickoff()
end_time = time.time()
return end_time - start_time
# Compare performance
openai_time = test_embedding_performance({
"provider": "openai",
"config": {"model": "text-embedding-3-small"}
})
ollama_time = test_embedding_performance({
"provider": "ollama",
"config": {"model": "mxbai-embed-large"}
})
print(f"OpenAI: {openai_time:.2f}s")
print(f"Ollama: {ollama_time:.2f}s")
import os
from crewai import Agent, Crew, Process, Task
from crewai.memory.external.external_memory import ExternalMemory
# Create external memory instance with local Mem0 Configuration
external_memory = ExternalMemory(
embedder_config={
"provider": "mem0",
"config": {
"user_id": "john",
"local_mem0_config": {
"vector_store": {
"provider": "qdrant",
"config": {"host": "localhost", "port": 6333}
},
"llm": {
"provider": "openai",
"config": {"api_key": "your-api-key", "model": "gpt-4"}
},
"embedder": {
"provider": "openai",
"config": {"api_key": "your-api-key", "model": "text-embedding-3-small"}
}
},
"infer": True # Optional defaults to True
},
}
)
crew = Crew(
agents=[...],
tasks=[...],
external_memory=external_memory, # Separate from basic memory
process=Process.sequential,
verbose=True
)
import os
from crewai import Agent, Crew, Process, Task
from crewai.memory.external.external_memory import ExternalMemory
new_categories = [
{"lifestyle_management_concerns": "Tracks daily routines, habits, hobbies and interests including cooking, time management and work-life balance"},
{"seeking_structure": "Documents goals around creating routines, schedules, and organized systems in various life areas"},
{"personal_information": "Basic information about the user including name, preferences, and personality traits"}
]
os.environ["MEM0_API_KEY"] = "your-api-key"
# Create external memory instance with Mem0 Client
external_memory = ExternalMemory(
embedder_config={
"provider": "mem0",
"config": {
"user_id": "john",
"org_id": "my_org_id", # Optional
"project_id": "my_project_id", # Optional
"api_key": "custom-api-key" # Optional - overrides env var
"run_id": "my_run_id", # Optional - for short-term memory
"includes": "include1", # Optional
"excludes": "exclude1", # Optional
"infer": True # Optional defaults to True
"custom_categories": new_categories # Optional - custom categories for user memory
},
}
)
crew = Crew(
agents=[...],
tasks=[...],
external_memory=external_memory, # Separate from basic memory
process=Process.sequential,
verbose=True
)
from crewai.memory.external.external_memory import ExternalMemory
from crewai.memory.storage.interface import Storage
class CustomStorage(Storage):
def __init__(self):
self.memories = []
def save(self, value, metadata=None, agent=None):
self.memories.append({
"value": value,
"metadata": metadata,
"agent": agent
})
def search(self, query, limit=10, score_threshold=0.5):
# Implement your search logic here
return [m for m in self.memories if query.lower() in str(m["value"]).lower()]
def reset(self):
self.memories = []
# Use custom storage
external_memory = ExternalMemory(storage=CustomStorage())
crew = Crew(
agents=[...],
tasks=[...],
external_memory=external_memory
)
Category Feature Basic Memory External Memory
Ease of Use |Setup Complexity
|Simple
|Moderate
|Integration
|Built-in (contextual)
|Standalone
Persistence |Storage
|Local files
|Custom / Mem0
|Cross-session Support
|✅
|✅
Personalization |User-specific Memory
|❌
|✅
|Custom Providers
|Limited
|Any provider
Use Case Fit |Recommended For
|Most general use cases
|Specialized / custom needs
crew = Crew(
memory=True,
embedder={
"provider": "openai",
"config": {"model": "text-embedding-3-small"}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "ollama",
"config": {"model": "mxbai-embed-large"}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "google",
"config": {
"api_key": "your-api-key",
"model": "text-embedding-004"
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "openai",
"config": {
"api_key": "your-api-key",
"api_base": "https://your-resource.openai.azure.com/",
"api_version": "2023-05-15",
"model_name": "text-embedding-3-small"
}
}
)
crew = Crew(
memory=True,
embedder={
"provider": "vertexai",
"config": {
"project_id": "your-project-id",
"region": "your-region",
"api_key": "your-api-key",
"model_name": "textembedding-gecko"
}
}
)
import os
from crewai import Crew
# Store sensitive data in environment variables
crew = Crew(
memory=True,
embedder={
"provider": "openai",
"config": {
"api_key": os.getenv("OPENAI_API_KEY"),
"model": "text-embedding-3-small"
}
}
)
import os
from crewai import Crew
from crewai.memory import LongTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
# Use secure storage paths
storage_path = os.getenv("CREWAI_STORAGE_DIR", "./storage")
os.makedirs(storage_path, mode=0o700, exist_ok=True) # Restricted permissions
crew = Crew(
memory=True,
long_term_memory=LongTermMemory(
storage=LTMSQLiteStorage(
db_path=f"{storage_path}/memory.db"
)
)
)
CREWAI_STORAGE_DIR environment variable
memory=True
MEM0_API_KEY environment variable is set
mem0ai package is installed
memory=True for most use cases (simplest and fastest)
|Event
|Description
|Key Properties
MemoryQueryStartedEvent |Emitted when a memory query begins
query,
limit,
score_threshold
MemoryQueryCompletedEvent |Emitted when a memory query completes successfully
query,
results,
limit,
score_threshold,
query_time_ms
MemoryQueryFailedEvent |Emitted when a memory query fails
query,
limit,
score_threshold,
error
MemorySaveStartedEvent |Emitted when a memory save operation begins
value,
metadata,
agent_role
MemorySaveCompletedEvent |Emitted when a memory save operation completes successfully
value,
metadata,
agent_role,
save_time_ms
MemorySaveFailedEvent |Emitted when a memory save operation fails
value,
metadata,
agent_role,
error
MemoryRetrievalStartedEvent |Emitted when memory retrieval for a task prompt starts
task_id
MemoryRetrievalCompletedEvent |Emitted when memory retrieval completes successfully
task_id,
memory_content,
retrieval_time_ms
from crewai.utilities.events.base_event_listener import BaseEventListener
from crewai.utilities.events import (
MemoryQueryCompletedEvent,
MemorySaveCompletedEvent
)
import time
class MemoryPerformanceMonitor(BaseEventListener):
def __init__(self):
super().__init__()
self.query_times = []
self.save_times = []
def setup_listeners(self, crewai_event_bus):
@crewai_event_bus.on(MemoryQueryCompletedEvent)
def on_memory_query_completed(source, event: MemoryQueryCompletedEvent):
self.query_times.append(event.query_time_ms)
print(f"Memory query completed in {event.query_time_ms:.2f}ms. Query: '{event.query}'")
print(f"Average query time: {sum(self.query_times)/len(self.query_times):.2f}ms")
@crewai_event_bus.on(MemorySaveCompletedEvent)
def on_memory_save_completed(source, event: MemorySaveCompletedEvent):
self.save_times.append(event.save_time_ms)
print(f"Memory save completed in {event.save_time_ms:.2f}ms")
print(f"Average save time: {sum(self.save_times)/len(self.save_times):.2f}ms")
# Create an instance of your listener
memory_monitor = MemoryPerformanceMonitor()
from crewai.utilities.events.base_event_listener import BaseEventListener
from crewai.utilities.events import (
MemorySaveStartedEvent,
MemoryQueryStartedEvent,
MemoryRetrievalCompletedEvent
)
import logging
# Configure logging
logger = logging.getLogger('memory_events')
class MemoryLogger(BaseEventListener):
def setup_listeners(self, crewai_event_bus):
@crewai_event_bus.on(MemorySaveStartedEvent)
def on_memory_save_started(source, event: MemorySaveStartedEvent):
if event.agent_role:
logger.info(f"Agent '{event.agent_role}' saving memory: {event.value[:50]}...")
else:
logger.info(f"Saving memory: {event.value[:50]}...")
@crewai_event_bus.on(MemoryQueryStartedEvent)
def on_memory_query_started(source, event: MemoryQueryStartedEvent):
logger.info(f"Memory query started: '{event.query}' (limit: {event.limit})")
@crewai_event_bus.on(MemoryRetrievalCompletedEvent)
def on_memory_retrieval_completed(source, event: MemoryRetrievalCompletedEvent):
if event.task_id:
logger.info(f"Memory retrieved for task {event.task_id} in {event.retrieval_time_ms:.2f}ms")
else:
logger.info(f"Memory retrieved in {event.retrieval_time_ms:.2f}ms")
logger.debug(f"Memory content: {event.memory_content}")
# Create an instance of your listener
memory_logger = MemoryLogger()
from crewai.utilities.events.base_event_listener import BaseEventListener
from crewai.utilities.events import (
MemorySaveFailedEvent,
MemoryQueryFailedEvent
)
import logging
from typing import Optional
# Configure logging
logger = logging.getLogger('memory_errors')
class MemoryErrorTracker(BaseEventListener):
def __init__(self, notify_email: Optional[str] = None):
super().__init__()
self.notify_email = notify_email
self.error_count = 0
def setup_listeners(self, crewai_event_bus):
@crewai_event_bus.on(MemorySaveFailedEvent)
def on_memory_save_failed(source, event: MemorySaveFailedEvent):
self.error_count += 1
agent_info = f"Agent '{event.agent_role}'" if event.agent_role else "Unknown agent"
error_message = f"Memory save failed: {event.error}. {agent_info}"
logger.error(error_message)
if self.notify_email and self.error_count % 5 == 0:
self._send_notification(error_message)
@crewai_event_bus.on(MemoryQueryFailedEvent)
def on_memory_query_failed(source, event: MemoryQueryFailedEvent):
self.error_count += 1
error_message = f"Memory query failed: {event.error}. Query: '{event.query}'"
logger.error(error_message)
if self.notify_email and self.error_count % 5 == 0:
self._send_notification(error_message)
def _send_notification(self, message):
# Implement your notification system (email, Slack, etc.)
print(f"[NOTIFICATION] Would send to {self.notify_email}: {message}")
# Create an instance of your listener
error_tracker = MemoryErrorTracker(notify_email="admin@example.com")
from crewai.utilities.events.base_event_listener import BaseEventListener
from crewai.utilities.events import (
MemoryQueryCompletedEvent,
MemorySaveCompletedEvent
)
class MemoryAnalyticsForwarder(BaseEventListener):
def __init__(self, analytics_client):
super().__init__()
self.client = analytics_client
def setup_listeners(self, crewai_event_bus):
@crewai_event_bus.on(MemoryQueryCompletedEvent)
def on_memory_query_completed(source, event: MemoryQueryCompletedEvent):
# Forward query metrics to analytics platform
self.client.track_metric({
"event_type": "memory_query",
"query": event.query,
"duration_ms": event.query_time_ms,
"result_count": len(event.results) if hasattr(event.results, "__len__") else 0,
"timestamp": event.timestamp
})
@crewai_event_bus.on(MemorySaveCompletedEvent)
def on_memory_save_completed(source, event: MemorySaveCompletedEvent):
# Forward save metrics to analytics platform
self.client.track_metric({
"event_type": "memory_save",
"agent_role": event.agent_role,
"duration_ms": event.save_time_ms,
"timestamp": event.timestamp
})

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-memory/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-memory/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
