---
title: "docs.crewai.com-en-concepts-llms"
slug: "docs.crewai.com-en-concepts-llms"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://docs.crewai.com/en/concepts/llms"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: ""
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-llms/71bc45159c09.webp"
caption: "light logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
- path: "../assets/docs.crewai.com/docs.crewai.com-en-concepts-llms/71bc45159c09.webp"
caption: "dark logo"
credit_name: "docs.crewai.com"
credit_url: "https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# docs.crewai.com-en-concepts-llms

> Synthesis: TODO

A comprehensive guide to configuring and using Large Language Models (LLMs) in your CrewAI projects
.env file or in your app code. If you used
crewai create to bootstrap your project, it will be set already.
MODEL=model-id # e.g. gpt-4o, gemini-2.0-flash, claude-3-sonnet-...
# Be sure to set your API keys here too. See the Provider
# section below.
OpenAI
.env file:
# Required
OPENAI_API_KEY=sk-...
# Optional
OPENAI_API_BASE=<custom-base-url>
OPENAI_ORGANIZATION=<your-org-id>
from crewai import LLM
llm = LLM(
model="openai/gpt-4", # call model by provider/model_name
temperature=0.8,
max_tokens=150,
top_p=0.9,
frequency_penalty=0.1,
presence_penalty=0.1,
stop=["END"],
seed=42
)
|Model
|Context Window
|Best For
|GPT-4
|8,192 tokens
|High-accuracy tasks, complex reasoning
|GPT-4 Turbo
|128,000 tokens
|Long-form content, document analysis
|GPT-4o & GPT-4o-mini
|128,000 tokens
|Cost-effective large context processing
|o3-mini
|200,000 tokens
|Fast reasoning, complex reasoning
|o1-mini
|128,000 tokens
|Fast reasoning, complex reasoning
|o1-preview
|128,000 tokens
|Fast reasoning, complex reasoning
|o1
|200,000 tokens
|Fast reasoning, complex reasoning
Meta-Llama
.env file:
# Meta Llama API Key Configuration
LLAMA_API_KEY=LLM|your_api_key_here
from crewai import LLM
# Initialize Meta Llama LLM
llm = LLM(
model="meta_llama/Llama-4-Scout-17B-16E-Instruct-FP8",
temperature=0.8,
stop=["END"],
seed=42
)
|Model ID
|Input context length
|Output context length
|Input Modalities
|Output Modalities
meta_llama/Llama-4-Scout-17B-16E-Instruct-FP8
|128k
|4028
|Text, Image
|Text
meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8
|128k
|4028
|Text, Image
|Text
meta_llama/Llama-3.3-70B-Instruct
|128k
|4028
|Text
|Text
meta_llama/Llama-3.3-8B-Instruct
|128k
|4028
|Text
|Text
Anthropic
# Required
ANTHROPIC_API_KEY=sk-ant-...
# Optional
ANTHROPIC_API_BASE=<custom-base-url>
llm = LLM(
model="anthropic/claude-3-sonnet-20240229-v1:0",
temperature=0.7
)
Google (Gemini API)
.env file. If you need a key, or need to find an
existing key, check AI Studio.
# https://ai.google.dev/gemini-api/docs/api-key
GEMINI_API_KEY=<your-api-key>
from crewai import LLM
llm = LLM(
model="gemini/gemini-2.0-flash",
temperature=0.7,
)
|Model
|Context Window
|Best For
|gemini-2.5-flash-preview-04-17
|1M tokens
|Adaptive thinking, cost efficiency
|gemini-2.5-pro-preview-05-06
|1M tokens
|Enhanced thinking and reasoning, multimodal understanding, advanced coding, and more
|gemini-2.0-flash
|1M tokens
|Next generation features, speed, thinking, and realtime streaming
|gemini-2.0-flash-lite
|1M tokens
|Cost efficiency and low latency
|gemini-1.5-flash
|1M tokens
|Balanced multimodal model, good for most tasks
|gemini-1.5-flash-8B
|1M tokens
|Fastest, most cost-efficient, good for high-frequency tasks
|gemini-1.5-pro
|2M tokens
|Best performing, wide variety of reasoning tasks including logical reasoning, coding, and creative collaboration
|Model
|Context Window
|gemma-3-1b-it
|32k tokens
|gemma-3-4b-it
|32k tokens
|gemma-3-12b-it
|32k tokens
|gemma-3-27b-it
|128k tokens
Google (Vertex AI)
import json
file_path = 'path/to/vertex_ai_service_account.json'
# Load the JSON file
with open(file_path, 'r') as file:
vertex_credentials = json.load(file)
# Convert the credentials to a JSON string
vertex_credentials_json = json.dumps(vertex_credentials)
from crewai import LLM
llm = LLM(
model="gemini-1.5-pro-latest", # or vertex_ai/gemini-1.5-pro-latest
temperature=0.7,
vertex_credentials=vertex_credentials_json
)
|Model
|Context Window
|Best For
|gemini-2.5-flash-preview-04-17
|1M tokens
|Adaptive thinking, cost efficiency
|gemini-2.5-pro-preview-05-06
|1M tokens
|Enhanced thinking and reasoning, multimodal understanding, advanced coding, and more
|gemini-2.0-flash
|1M tokens
|Next generation features, speed, thinking, and realtime streaming
|gemini-2.0-flash-lite
|1M tokens
|Cost efficiency and low latency
|gemini-1.5-flash
|1M tokens
|Balanced multimodal model, good for most tasks
|gemini-1.5-flash-8B
|1M tokens
|Fastest, most cost-efficient, good for high-frequency tasks
|gemini-1.5-pro
|2M tokens
|Best performing, wide variety of reasoning tasks including logical reasoning, coding, and creative collaboration
Azure
# Required
AZURE_API_KEY=<your-api-key>
AZURE_API_BASE=<your-resource-url>
AZURE_API_VERSION=<api-version>
# Optional
AZURE_AD_TOKEN=<your-azure-ad-token>
AZURE_API_TYPE=<your-azure-api-type>
llm = LLM(
model="azure/gpt-4",
api_version="2023-05-15"
)
AWS Bedrock
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_DEFAULT_REGION=<your-region>
llm = LLM(
model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0"
)
|Model
|Context Window
|Best For
|Amazon Nova Pro
|Up to 300k tokens
|High-performance, model balancing accuracy, speed, and cost-effectiveness across diverse tasks.
|Amazon Nova Micro
|Up to 128k tokens
|High-performance, cost-effective text-only model optimized for lowest latency responses.
|Amazon Nova Lite
|Up to 300k tokens
|High-performance, affordable multimodal processing for images, video, and text with real-time capabilities.
|Claude 3.7 Sonnet
|Up to 128k tokens
|High-performance, best for complex reasoning, coding & AI agents
|Claude 3.5 Sonnet v2
|Up to 200k tokens
|State-of-the-art model specialized in software engineering, agentic capabilities, and computer interaction at optimized cost.
|Claude 3.5 Sonnet
|Up to 200k tokens
|High-performance model delivering superior intelligence and reasoning across diverse tasks with optimal speed-cost balance.
|Claude 3.5 Haiku
|Up to 200k tokens
|Fast, compact multimodal model optimized for quick responses and seamless human-like interactions
|Claude 3 Sonnet
|Up to 200k tokens
|Multimodal model balancing intelligence and speed for high-volume deployments.
|Claude 3 Haiku
|Up to 200k tokens
|Compact, high-speed multimodal model optimized for quick responses and natural conversational interactions
|Claude 3 Opus
|Up to 200k tokens
|Most advanced multimodal model exceling at complex tasks with human-like reasoning and superior contextual understanding.
|Claude 2.1
|Up to 200k tokens
|Enhanced version with expanded context window, improved reliability, and reduced hallucinations for long-form and RAG applications
|Claude
|Up to 100k tokens
|Versatile model excelling in sophisticated dialogue, creative content, and precise instruction following.
|Claude Instant
|Up to 100k tokens
|Fast, cost-effective model for everyday tasks like dialogue, analysis, summarization, and document Q&A
|Llama 3.1 405B Instruct
|Up to 128k tokens
|Advanced LLM for synthetic data generation, distillation, and inference for chatbots, coding, and domain-specific tasks.
|Llama 3.1 70B Instruct
|Up to 128k tokens
|Powers complex conversations with superior contextual understanding, reasoning and text generation.
|Llama 3.1 8B Instruct
|Up to 128k tokens
|Advanced state-of-the-art model with language understanding, superior reasoning, and text generation.
|Llama 3 70B Instruct
|Up to 8k tokens
|Powers complex conversations with superior contextual understanding, reasoning and text generation.
|Llama 3 8B Instruct
|Up to 8k tokens
|Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.
|Titan Text G1 - Lite
|Up to 4k tokens
|Lightweight, cost-effective model optimized for English tasks and fine-tuning with focus on summarization and content generation.
|Titan Text G1 - Express
|Up to 8k tokens
|Versatile model for general language tasks, chat, and RAG applications with support for English and 100+ languages.
|Cohere Command
|Up to 4k tokens
|Model specialized in following user commands and delivering practical enterprise solutions.
|Jurassic-2 Mid
|Up to 8,191 tokens
|Cost-effective model balancing quality and affordability for diverse language tasks like Q&A, summarization, and content generation.
|Jurassic-2 Ultra
|Up to 8,191 tokens
|Model for advanced text generation and comprehension, excelling in complex tasks like analysis and content creation.
|Jamba-Instruct
|Up to 256k tokens
|Model with extended context window optimized for cost-effective text generation, summarization, and Q&A.
|Mistral 7B Instruct
|Up to 32k tokens
|This LLM follows instructions, completes requests, and generates creative text.
|Mistral 8x7B Instruct
|Up to 32k tokens
|An MOE LLM that follows instructions, completes requests, and generates creative text.
Amazon SageMaker
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_DEFAULT_REGION=<your-region>
llm = LLM(
model="sagemaker/<my-endpoint>"
)
Mistral
.env file:
MISTRAL_API_KEY=<your-api-key>
llm = LLM(
model="mistral/mistral-large-latest",
temperature=0.7
)
Nvidia NIM
.env file:
NVIDIA_API_KEY=<your-api-key>
llm = LLM(
model="nvidia_nim/meta/llama3-70b-instruct",
temperature=0.7
)
|Model
|Context Window
|Best For
|nvidia/mistral-nemo-minitron-8b-8k-instruct
|8,192 tokens
|State-of-the-art small language model delivering superior accuracy for chatbot, virtual assistants, and content generation.
|nvidia/nemotron-4-mini-hindi-4b-instruct
|4,096 tokens
|A bilingual Hindi-English SLM for on-device inference, tailored specifically for Hindi Language.
|nvidia/llama-3.1-nemotron-70b-instruct
|128k tokens
|Customized for enhanced helpfulness in responses
|nvidia/llama3-chatqa-1.5-8b
|128k tokens
|Advanced LLM to generate high-quality, context-aware responses for chatbots and search engines.
|nvidia/llama3-chatqa-1.5-70b
|128k tokens
|Advanced LLM to generate high-quality, context-aware responses for chatbots and search engines.
|nvidia/vila
|128k tokens
|Multi-modal vision-language model that understands text/img/video and creates informative responses
|nvidia/neva-22
|4,096 tokens
|Multi-modal vision-language model that understands text/images and generates informative responses
|nvidia/nemotron-mini-4b-instruct
|8,192 tokens
|General-purpose tasks
|nvidia/usdcode-llama3-70b-instruct
|128k tokens
|State-of-the-art LLM that answers OpenUSD knowledge queries and generates USD-Python code.
|nvidia/nemotron-4-340b-instruct
|4,096 tokens
|Creates diverse synthetic data that mimics the characteristics of real-world data.
|meta/codellama-70b
|100k tokens
|LLM capable of generating code from natural language and vice versa.
|meta/llama2-70b
|4,096 tokens
|Cutting-edge large language AI model capable of generating text and code in response to prompts.
|meta/llama3-8b-instruct
|8,192 tokens
|Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.
|meta/llama3-70b-instruct
|8,192 tokens
|Powers complex conversations with superior contextual understanding, reasoning and text generation.
|meta/llama-3.1-8b-instruct
|128k tokens
|Advanced state-of-the-art model with language understanding, superior reasoning, and text generation.
|meta/llama-3.1-70b-instruct
|128k tokens
|Powers complex conversations with superior contextual understanding, reasoning and text generation.
|meta/llama-3.1-405b-instruct
|128k tokens
|Advanced LLM for synthetic data generation, distillation, and inference for chatbots, coding, and domain-specific tasks.
|meta/llama-3.2-1b-instruct
|128k tokens
|Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.
|meta/llama-3.2-3b-instruct
|128k tokens
|Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.
|meta/llama-3.2-11b-vision-instruct
|128k tokens
|Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.
|meta/llama-3.2-90b-vision-instruct
|128k tokens
|Advanced state-of-the-art small language model with language understanding, superior reasoning, and text generation.
|google/gemma-7b
|8,192 tokens
|Cutting-edge text generation model text understanding, transformation, and code generation.
|google/gemma-2b
|8,192 tokens
|Cutting-edge text generation model text understanding, transformation, and code generation.
|google/codegemma-7b
|8,192 tokens
|Cutting-edge model built on Google’s Gemma-7B specialized for code generation and code completion.
|google/codegemma-1.1-7b
|8,192 tokens
|Advanced programming model for code generation, completion, reasoning, and instruction following.
|google/recurrentgemma-2b
|8,192 tokens
|Novel recurrent architecture based language model for faster inference when generating long sequences.
|google/gemma-2-9b-it
|8,192 tokens
|Cutting-edge text generation model text understanding, transformation, and code generation.
|google/gemma-2-27b-it
|8,192 tokens
|Cutting-edge text generation model text understanding, transformation, and code generation.
|google/gemma-2-2b-it
|8,192 tokens
|Cutting-edge text generation model text understanding, transformation, and code generation.
|google/deplot
|512 tokens
|One-shot visual language understanding model that translates images of plots into tables.
|google/paligemma
|8,192 tokens
|Vision language model adept at comprehending text and visual inputs to produce informative responses.
|mistralai/mistral-7b-instruct-v0.2
|32k tokens
|This LLM follows instructions, completes requests, and generates creative text.
|mistralai/mixtral-8x7b-instruct-v0.1
|8,192 tokens
|An MOE LLM that follows instructions, completes requests, and generates creative text.
|mistralai/mistral-large
|4,096 tokens
|Creates diverse synthetic data that mimics the characteristics of real-world data.
|mistralai/mixtral-8x22b-instruct-v0.1
|8,192 tokens
|Creates diverse synthetic data that mimics the characteristics of real-world data.
|mistralai/mistral-7b-instruct-v0.3
|32k tokens
|This LLM follows instructions, completes requests, and generates creative text.
|nv-mistralai/mistral-nemo-12b-instruct
|128k tokens
|Most advanced language model for reasoning, code, multilingual tasks; runs on a single GPU.
|mistralai/mamba-codestral-7b-v0.1
|256k tokens
|Model for writing and interacting with code across a wide range of programming languages and tasks.
|microsoft/phi-3-mini-128k-instruct
|128K tokens
|Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.
|microsoft/phi-3-mini-4k-instruct
|4,096 tokens
|Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.
|microsoft/phi-3-small-8k-instruct
|8,192 tokens
|Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.
|microsoft/phi-3-small-128k-instruct
|128K tokens
|Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.
|microsoft/phi-3-medium-4k-instruct
|4,096 tokens
|Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.
|microsoft/phi-3-medium-128k-instruct
|128K tokens
|Lightweight, state-of-the-art open LLM with strong math and logical reasoning skills.
|microsoft/phi-3.5-mini-instruct
|128K tokens
|Lightweight multilingual LLM powering AI applications in latency bound, memory/compute constrained environments
|microsoft/phi-3.5-moe-instruct
|128K tokens
|Advanced LLM based on Mixture of Experts architecture to deliver compute efficient content generation
|microsoft/kosmos-2
|1,024 tokens
|Groundbreaking multimodal model designed to understand and reason about visual elements in images.
|microsoft/phi-3-vision-128k-instruct
|128k tokens
|Cutting-edge open multimodal model exceling in high-quality reasoning from images.
|microsoft/phi-3.5-vision-instruct
|128k tokens
|Cutting-edge open multimodal model exceling in high-quality reasoning from images.
|databricks/dbrx-instruct
|12k tokens
|A general-purpose LLM with state-of-the-art performance in language understanding, coding, and RAG.
|snowflake/arctic
|1,024 tokens
|Delivers high efficiency inference for enterprise applications focused on SQL generation and coding.
|aisingapore/sea-lion-7b-instruct
|4,096 tokens
|LLM to represent and serve the linguistic and cultural diversity of Southeast Asia
|ibm/granite-8b-code-instruct
|4,096 tokens
|Software programming LLM for code generation, completion, explanation, and multi-turn conversion.
|ibm/granite-34b-code-instruct
|8,192 tokens
|Software programming LLM for code generation, completion, explanation, and multi-turn conversion.
|ibm/granite-3.0-8b-instruct
|4,096 tokens
|Advanced Small Language Model supporting RAG, summarization, classification, code, and agentic AI
|ibm/granite-3.0-3b-a800m-instruct
|4,096 tokens
|Highly efficient Mixture of Experts model for RAG, summarization, entity extraction, and classification
|mediatek/breeze-7b-instruct
|4,096 tokens
|Creates diverse synthetic data that mimics the characteristics of real-world data.
|upstage/solar-10.7b-instruct
|4,096 tokens
|Excels in NLP tasks, particularly in instruction-following, reasoning, and mathematics.
|writer/palmyra-med-70b-32k
|32k tokens
|Leading LLM for accurate, contextually relevant responses in the medical domain.
|writer/palmyra-med-70b
|32k tokens
|Leading LLM for accurate, contextually relevant responses in the medical domain.
|writer/palmyra-fin-70b-32k
|32k tokens
|Specialized LLM for financial analysis, reporting, and data processing
|01-ai/yi-large
|32k tokens
|Powerful model trained on English and Chinese for diverse tasks including chatbot and creative writing.
|deepseek-ai/deepseek-coder-6.7b-instruct
|2k tokens
|Powerful coding model offering advanced capabilities in code generation, completion, and infilling
|rakuten/rakutenai-7b-instruct
|1,024 tokens
|Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.
|rakuten/rakutenai-7b-chat
|1,024 tokens
|Advanced state-of-the-art LLM with language understanding, superior reasoning, and text generation.
|baichuan-inc/baichuan2-13b-chat
|4,096 tokens
|Support Chinese and English chat, coding, math, instruction following, solving quizzes
Local NVIDIA NIM Deployed using WSL2
from crewai.llm import LLM
local_nvidia_nim_llm = LLM(
model="openai/meta/llama-3.1-8b-instruct", # it's an openai-api compatible model
base_url="http://localhost:8000/v1",
api_key="<your_api_key|any text if you have not configured it>", # api_key is required, but you can use any text
)
# Then you can use it in your crew:
@CrewBase
class MyCrew():
# ...
@agent
def researcher(self) -> Agent:
return Agent(
config=self.agents_config['researcher'], # type: ignore[index]
llm=local_nvidia_nim_llm
)
# ...
Groq
.env file:
GROQ_API_KEY=<your-api-key>
llm = LLM(
model="groq/llama-3.2-90b-text-preview",
temperature=0.7
)
|Model
|Context Window
|Best For
|Llama 3.1 70B/8B
|131,072 tokens
|High-performance, large context tasks
|Llama 3.2 Series
|8,192 tokens
|General-purpose tasks
|Mixtral 8x7B
|32,768 tokens
|Balanced performance and context
IBM watsonx.ai
.env file:
# Required
WATSONX_URL=<your-url>
WATSONX_APIKEY=<your-apikey>
WATSONX_PROJECT_ID=<your-project-id>
# Optional
WATSONX_TOKEN=<your-token>
WATSONX_DEPLOYMENT_SPACE_ID=<your-space-id>
llm = LLM(
model="watsonx/meta-llama/llama-3-1-70b-instruct",
base_url="https://api.watsonx.ai/v1"
)
Ollama (Local LLMs)
ollama run llama3
llm = LLM(
model="ollama/llama3:70b",
base_url="http://localhost:11434"
)
Fireworks AI
.env file:
FIREWORKS_API_KEY=<your-api-key>
llm = LLM(
model="fireworks_ai/accounts/fireworks/models/llama-v3-70b-instruct",
temperature=0.7
)
Perplexity AI
.env file:
PERPLEXITY_API_KEY=<your-api-key>
llm = LLM(
model="llama-3.1-sonar-large-128k-online",
base_url="https://api.perplexity.ai/"
)
Hugging Face
.env file:
HF_TOKEN=<your-api-key>
llm = LLM(
model="huggingface/meta-llama/Meta-Llama-3.1-8B-Instruct"
)
SambaNova
.env file:
SAMBANOVA_API_KEY=<your-api-key>
llm = LLM(
model="sambanova/Meta-Llama-3.1-8B-Instruct",
temperature=0.7
)
|Model
|Context Window
|Best For
|Llama 3.1 70B/8B
|Up to 131,072 tokens
|High-performance, large context tasks
|Llama 3.1 405B
|8,192 tokens
|High-performance and output quality
|Llama 3.2 Series
|8,192 tokens
|General-purpose, multimodal tasks
|Llama 3.3 70B
|Up to 131,072 tokens
|High-performance and output quality
|Qwen2 familly
|8,192 tokens
|High-performance and output quality
Cerebras
.env file:
# Required
CEREBRAS_API_KEY=<your-api-key>
llm = LLM(
model="cerebras/llama3.1-70b",
temperature=0.7,
max_tokens=8192
)
Open Router
.env file:
OPENROUTER_API_KEY=<your-api-key>
llm = LLM(
model="openrouter/deepseek/deepseek-r1",
base_url="https://openrouter.ai/api/v1",
api_key=OPENROUTER_API_KEY
)
Nebius AI Studio
.env file:
NEBIUS_API_KEY=<your-api-key>
llm = LLM(
model="nebius/Qwen/Qwen3-30B-A3B"
)
stream parameter to
True when initializing your LLM:
from crewai import LLM
# Create an LLM with streaming enabled
llm = LLM(
model="openai/gpt-4o",
stream=True # Enable streaming
)
response_format using a Pydantic model. This enables the framework to automatically parse and validate the output, making it easier to integrate the response into your application without manual post-processing.
For example, you can define a Pydantic model to represent the expected response structure and pass it as the
response_format when instantiating the LLM. The model will then be used to convert the LLM output into a structured Python object.
from crewai import LLM
class Dog(BaseModel):
name: str
age: int
breed: str
llm = LLM(model="gpt-4o", response_format=Dog)
response = llm.call(
"Analyze the following messages and return the name, age, and breed. "
"Meet Kona! She is 3 years old and is a black german shepherd."
)
print(response)
# Output:
# Dog(name='Kona', age=3, breed='black german shepherd')
Context Window Management
from crewai import LLM
# CrewAI automatically handles:
# 1. Token counting and tracking
# 2. Content summarization when needed
# 3. Task splitting for large contexts
llm = LLM(
model="gpt-4",
max_tokens=4000, # Limit response length
)
Performance Optimization
Token Usage Optimization
# Configure model with appropriate settings
llm = LLM(
model="openai/gpt-4-turbo-preview",
temperature=0.7, # Adjust based on task
max_tokens=4096, # Set based on output needs
timeout=300 # Longer timeout for complex tasks
)
Best Practices
Drop Additional Parameters
stop parameter, you can simply omit it from your LLM call:
from crewai import LLM
import os
os.environ["OPENAI_API_KEY"] = "<api-key>"
o3_llm = LLM(
model="o3",
drop_params=True,
additional_drop_params=["stop"]
)
# OpenAI
OPENAI_API_KEY=sk-...
# Anthropic
ANTHROPIC_API_KEY=sk-ant-...

![light logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-llms/71bc45159c09.webp)
<figcaption>Figure 1. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>

![dark logo](../assets/docs.crewai.com/docs.crewai.com-en-concepts-llms/71bc45159c09.webp)
<figcaption>Figure 2. Credit: [docs.crewai.com](https://mintlify.s3.us-west-1.amazonaws.com/crewai/images/crew_only_logo.png), License: internal-copy</figcaption>
