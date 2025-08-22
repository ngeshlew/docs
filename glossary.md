---
title: "Glossary"
description: "Comprehensive glossary of AI, ML, and development terms used throughout the course"
slug: "glossary"
updatedAt: "2025-08-20"
---

# Glossary

Key terms and definitions used across the AI Product Engineer course, with links to relevant modules and detailed explanations.

## A

### **Agent**
An autonomous AI system that can perceive its environment, make decisions, and take actions to achieve specific goals. Agents can be simple (rule-based) or complex (learning-based) and often work in multi-agent systems.

**Related:** [Agents & Orchestration](../modules/agents-orchestration/index.mdx), [CrewAI Class](../crew-ai-class.mdx)

### **API (Application Programming Interface)**
A set of rules and protocols that allows different software applications to communicate with each other. In AI systems, APIs enable integration with language models, databases, and external services.

### **Attention Mechanism**
A neural network component that allows models to focus on specific parts of input data when making predictions. Key to transformer architecture and modern language models.

**Related:** [Transformers](../modules/transformers/index.mdx)

### **Autoregressive Model**
A type of language model that generates text by predicting the next token based on all previous tokens. Examples include GPT models and LLaMA.

## B

### **Batch Processing**
Processing multiple inputs together rather than one at a time. Improves efficiency and throughput in AI systems.

**Related:** [Cost & Latency](../modules/cost-latency/index.mdx)

### **BM25**
A ranking function used in information retrieval that ranks documents based on term frequency and inverse document frequency. Often used in RAG systems.

**Related:** [RAG Systems](../modules/rag/index.mdx)

### **Bias**
Systematic prejudice in AI model outputs, often reflecting biases in training data or model architecture. Can lead to unfair or discriminatory results.

**Related:** [Safety & Security](../modules/safety-security/index.mdx)

## C

### **Chain of Thought (CoT)**
A prompting technique where the model is asked to show its reasoning process step-by-step before providing a final answer. Improves reasoning capabilities and transparency.

**Related:** [Chain of Thought](../modules/prompting-techniques/chain-of-thought.mdx)

### **Context Window**
The maximum number of tokens (words/subwords) that a language model can process in a single input. Larger context windows allow for more comprehensive understanding.

**Related:** [Token & Context](../modules/token-context/index.mdx)

### **CrewAI**
An open-source framework for orchestrating role-playing autonomous AI agents. Enables complex multi-agent workflows and collaborative AI systems.

**Related:** [CrewAI Class](../crew-ai-class.mdx), [Agents & Orchestration](../modules/agents-orchestration/index.mdx)

### **Cross-Encoder**
A model that takes pairs of inputs and outputs a relevance score. Used in RAG systems to rerank retrieved documents for better accuracy.

**Related:** [RAG Systems](../modules/rag/index.mdx)

## D

### **Data Pipeline**
A series of data processing steps that transform raw data into a format suitable for AI model training or inference.

### **Embeddings**
Vector representations of text, images, or other data that capture semantic meaning. Used for similarity search, clustering, and as input to neural networks.

**Related:** [RAG Systems](../modules/rag/index.mdx)

### **Fine-tuning**
The process of adapting a pre-trained model to a specific task or domain by training it on additional data.

## E

### **Evaluation**
The systematic assessment of AI model performance using various metrics and benchmarks to ensure quality and reliability.

**Related:** [Evaluation & Observability](../modules/evaluation-observability/index.mdx)

### **Emergent Behavior**
Capabilities that arise in AI models as they scale up, even though they weren't explicitly trained for those tasks.

## F

### **Few-Shot Learning**
A technique where a model learns to perform a new task with only a few examples, leveraging its pre-trained knowledge.

**Related:** [Few-Shot Learning](../modules/prompting-techniques/few-shot.mdx)

### **Function Calling**
A technique where language models can call external functions or APIs to perform specific tasks, enabling more complex workflows.

**Related:** [Structured Outputs](../modules/structured-outputs/index.mdx)

## G

### **Generative AI**
AI systems that can create new content, including text, images, audio, and video, based on learned patterns from training data.

### **Grounding**
The process of connecting AI model outputs to real-world facts and data sources to improve accuracy and reduce hallucinations.

**Related:** [RAG Systems](../modules/rag/index.mdx)

## H

### **Hallucination**
When an AI model generates false or fabricated information that appears plausible but is not based on factual data.

**Related:** [Safety & Security](../modules/safety-security/index.mdx)

### **Human-in-the-Loop (HITL)**
A system design where human oversight and intervention are integrated into AI workflows for quality control and decision-making.

**Related:** [AI UX Behavior](../modules/ai-ux-behavior/index.mdx)

## I

### **Inference**
The process of using a trained AI model to make predictions or generate outputs on new data.

### **In-Context Learning**
The ability of language models to learn new tasks from examples provided in the prompt without additional training.

## J

### **JSON Schema**
A specification for validating JSON data structures, often used with AI models to ensure structured outputs.

**Related:** [Structured Outputs](../modules/structured-outputs/index.mdx)

## K

### **Knowledge Graph**
A structured representation of knowledge that connects entities and their relationships, often used to enhance AI reasoning.

**Related:** [RAG Systems](../modules/rag/index.mdx)

## L

### **Latency**
The time it takes for an AI system to process a request and return a response. Critical for user experience and system performance.

**Related:** [Cost & Latency](../modules/cost-latency/index.mdx)

### **LLM (Large Language Model)**
A neural network model trained on vast amounts of text data to understand and generate human language. Examples include GPT, Claude, and LLaMA.

**Related:** [Foundations](../modules/foundations/index.mdx)

### **LangChain**
An open-source framework for building applications with language models, providing tools for chains, agents, and memory management.

**Related:** [Agents & Orchestration](../modules/agents-orchestration/index.mdx)

## M

### **Memory**
The ability of AI systems to store and retrieve information from previous interactions, enabling more coherent and contextual conversations.

**Related:** [Memory & State](../modules/memory-state/index.mdx)

### **Model Context Protocol (MCP)**
A standardized protocol for connecting AI models to external tools, data sources, and services in a secure and interoperable way.

**Related:** [MCP](../modules/mcp/index.mdx)

### **Multimodality**
The ability of AI systems to process and understand multiple types of data simultaneously, such as text, images, audio, and video.

**Related:** [Multimodality](../modules/multimodality/index.mdx)

## N

### **Natural Language Processing (NLP)**
A branch of AI focused on enabling computers to understand, interpret, and generate human language.

### **Neural Network**
A computational model inspired by biological neural networks, consisting of interconnected nodes (neurons) that process information.

## O

### **Observability**
The ability to monitor, understand, and debug AI systems in production, including logging, metrics, and tracing.

**Related:** [Evaluation & Observability](../modules/evaluation-observability/index.mdx)

### **OTLP (OpenTelemetry Protocol)**
A standardized protocol for exporting traces, metrics, and logs from applications, enabling comprehensive observability.

**Related:** [Evaluation & Observability](../modules/evaluation-observability/index.mdx)

## P

### **Prompt Engineering**
The practice of designing effective inputs (prompts) for language models to achieve desired outputs and behaviors.

**Related:** [Prompting Techniques](../modules/prompting-techniques/index.mdx)

### **Prompt Chaining**
A technique where multiple prompts are used sequentially, with the output of one prompt serving as input to the next.

**Related:** [Prompt Chaining](../modules/prompting-techniques/prompt-chaining.mdx)

### **Parameter**
A variable in a neural network that gets adjusted during training to optimize performance. The number of parameters often indicates model complexity.

## Q

### **Quantization**
A technique for reducing model size and improving inference speed by using lower precision (e.g., 8-bit instead of 32-bit) for model weights.

**Related:** [Cost & Latency](../modules/cost-latency/index.mdx)

## R

### **RAG (Retrieval-Augmented Generation)**
A technique that combines information retrieval with text generation, allowing AI models to access external knowledge sources.

**Related:** [RAG Systems](../modules/rag/index.mdx)

### **Reasoning**
The ability of AI systems to think logically, solve problems step-by-step, and draw conclusions from available information.

**Related:** [Chain of Thought](../modules/prompting-techniques/chain-of-thought.mdx)

### **ReAct**
A framework that combines reasoning and action, allowing AI agents to think about what actions to take and then execute them.

**Related:** [ReAct](../modules/prompting-techniques/react.mdx)

## S

### **Safety**
Measures and techniques to ensure AI systems behave safely and don't cause harm, including alignment, robustness, and security.

**Related:** [Safety & Security](../modules/safety-security/index.mdx)

### **SLO (Service Level Objective)**
A target for system performance metrics, such as response time or availability, used to ensure quality of service.

**Related:** [Cost & Latency](../modules/cost-latency/index.mdx)

### **SSE (Server-Sent Events)**
A web technology that enables real-time streaming of data from server to client, often used for streaming AI responses.

**Related:** [Streaming UX](../modules/streaming-ux/index.mdx)

### **Structured Outputs**
Techniques for ensuring AI models return data in specific, predictable formats like JSON, XML, or custom schemas.

**Related:** [Structured Outputs](../modules/structured-outputs/index.mdx)

## T

### **Token**
The basic unit of text processing in language models, which can be a word, part of a word, or punctuation mark.

**Related:** [Token & Context](../modules/token-context/index.mdx)

### **Transformer**
A neural network architecture that uses attention mechanisms to process sequential data, forming the foundation of modern language models.

**Related:** [Transformers](../modules/transformers/index.mdx)

### **Temperature**
A parameter that controls randomness in AI model outputs. Lower values produce more focused, deterministic responses; higher values produce more creative, varied responses.

## U

### **User Experience (UX)**
The overall experience of users when interacting with AI systems, including interface design, response quality, and system behavior.

**Related:** [AI UX Behavior](../modules/ai-ux-behavior/index.mdx)

## V

### **Vector Database**
A specialized database designed to store and search high-dimensional vector embeddings efficiently, commonly used in RAG systems.

**Related:** [RAG Systems](../modules/rag/index.mdx)

### **Vision Model**
An AI model capable of understanding and analyzing visual content, such as images, videos, and diagrams.

**Related:** [Multimodality](../modules/multimodality/index.mdx)

## W

### **Workflow**
A sequence of connected steps or processes that define how AI systems accomplish complex tasks, often involving multiple models and tools.

**Related:** [Design Patterns](../modules/design-patterns/index.mdx)

## Z

### **Zero-Shot Learning**
The ability of AI models to perform new tasks without any specific training examples, relying solely on their pre-trained knowledge.

**Related:** [Zero-Shot Learning](../modules/prompting-techniques/zero-shot.mdx)

## Additional Resources

<CardGroup cols={2}>
<Card title="Course Modules" icon="book" href="/modules">
  Explore all course modules for detailed explanations and practical examples.
</Card>

<Card title="Sources & References" icon="link" href="/sources">
  Comprehensive list of sources and references used throughout the course.
</Card>

<Card title="Progress Tracking" icon="activity" href="/progress">
  Track your learning progress through the course materials.
</Card>

<Card title="News & Updates" icon="rss" href="/news">
  Stay updated with the latest developments in AI and related technologies.
</Card>
</CardGroup>

<Info>
This glossary is continuously updated as new terms and concepts are introduced in the course. If you encounter a term not listed here, please check the relevant module pages for detailed explanations.
</Info>