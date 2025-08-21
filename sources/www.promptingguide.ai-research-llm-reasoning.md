---
title: "www.promptingguide.ai-research-llm-reasoning"
slug: "www.promptingguide.ai-research-llm-reasoning"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://www.promptingguide.ai/research/llm-reasoning"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: []
- path: "../assets/www.promptingguide.ai/www.promptingguide.ai-research-llm-reasoning/b151f4378e09.webp"
caption: "'"Reasoning Tasks"'"
credit_name: "www.promptingguide.ai"
credit_url: "https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freasoning-tasks.2ab787ba.png&w=3840&q=75"
license: "internal-copy"
- path: "../assets/www.promptingguide.ai/www.promptingguide.ai-research-llm-reasoning/3deb8491bf18.webp"
caption: "'"Reasoning Taxonomy"'"
credit_name: "www.promptingguide.ai"
credit_url: "https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freasoning-taxonomy.806739b9.png&w=3840&q=75"
license: "internal-copy"
- path: "../assets/www.promptingguide.ai/www.promptingguide.ai-research-llm-reasoning/915d2969bed4.webp"
caption: "'"Reasoning Techniques"'"
credit_name: "www.promptingguide.ai"
credit_url: "https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freasoning-techniques.015aac70.png&w=1920&q=75"
license: "internal-copy"
updatedAt: "'2025-08-18'"
completed: false
---

# www.promptingguide.ai-research-llm-reasoning

> Synthesis: TODO

# LLM Reasoning
Over the last couple of years, large language models (LLMs) have made significant progress in a wide range of tasks. More recently, LLMs have shown the potential to exhibit reasoning abilities when scaled to a large enough size. Different types of reasoning are fundamental to intelligence but it's not fully understood how AI models can learn and harness this capability to solve complex problems. It is an area of huge focus and investment for many research labs.
## Reasoning with Foundation Models
Sun et al. (2023) (opens in a new tab) recently proposed an overview of reasoning with foundation models which focuses on the latest advancements in various reasoning tasks. This work also focuses on a more extensive look at reasoning that spans multimodal models and autonomous language agents.
Reasoning tasks could include tasks such as mathematical reasoning, logical reasoning, causal reasoning, visual reasoning and more. The following figure shows an overview of reasoning tasks discussed in the survey paper, including reasoning techniques for foundation models such as alignment training and in-context learning.
*Figure source: Sun et al., 2023 (opens in a new tab)*
## How Can Reasoning be Elicited in LLMs?
Reasoning in LLMs can be elicited and enhanced using many different prompting approaches. Qiao et al. (2023) (opens in a new tab) categorized reasoning methods research into two different branches, namely reasoning enhanced strategy and knowledge enhancement reasoning. Reasoning strategies include prompt engineering, process optimization, and external engines. For instance, single-stage prompting strategies include Chain-of-Thought (opens in a new tab) and Active-Prompt (opens in a new tab). A full taxonomy of reasoning with language model prompting can be found in the paper and summarized in the figure below:
*Figure source: Qiao et al., 2023 (opens in a new tab)*
Huang et al. (2023) also explain a summary of techniques to improve or elicit reasoning in LLMs such as GPT-3. These techniques range from using fully supervised fine-tuning models trained on explanation datasets to prompting methods such as chain-of-thought, problem decomposition, and in-context learning. Below is a summary of the techniques described in the paper:
*Figure source: Huang et al., 2023 (opens in a new tab)*
## Can LLMs Reason and Plan?
There is a lot of debate about whether LLMs can reason and plan. Both reasoning and planning are important capabilities for unlocking complex applications with LLMs such as in the domains of robotics and autonomous agents. A position paper by Subbarao Kambhampati (2024) (opens in a new tab) discusses the topic of reasoning and planning for LLMs.
Here is a summary of the author's conclusion:
To summarize, nothing that I have read, verified, or done gives me any compelling reason to believe that LLMs do reasoning/planning, as normally understood. What they do instead, armed with web-scale training, is a form of universal approximate retrieval, which, as I have argued, can sometimes be mistaken for reasoning capabilities.
## References
- Reasoning with Language Model Prompting: A Survey (opens in a new tab)
- Towards Reasoning in Large Language Models: A Survey (opens in a new tab)
- Can Large Language Models Reason and Plan? (opens in a new tab)
- Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key? (opens in a new tab)
- Awesome LLM Reasoning (opens in a new tab)

!["Reasoning Tasks"](../assets/www.promptingguide.ai/www.promptingguide.ai-research-llm-reasoning/b151f4378e09.webp)
<figcaption>Figure 1. Credit: [www.promptingguide.ai](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freasoning-tasks.2ab787ba.png&w=3840&q=75), License: internal-copy</figcaption>

!["Reasoning Taxonomy"](../assets/www.promptingguide.ai/www.promptingguide.ai-research-llm-reasoning/3deb8491bf18.webp)
<figcaption>Figure 2. Credit: [www.promptingguide.ai](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freasoning-taxonomy.806739b9.png&w=3840&q=75), License: internal-copy</figcaption>

!["Reasoning Techniques"](../assets/www.promptingguide.ai/www.promptingguide.ai-research-llm-reasoning/915d2969bed4.webp)
<figcaption>Figure 3. Credit: [www.promptingguide.ai](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freasoning-techniques.015aac70.png&w=1920&q=75), License: internal-copy</figcaption>
