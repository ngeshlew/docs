---
title: "www.promptingguide.ai-research-infini-attention"
slug: "www.promptingguide.ai-research-infini-attention"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://www.promptingguide.ai/research/infini-attention"
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

# www.promptingguide.ai-research-infini-attention

> Synthesis: TODO

# Efficient Infinite Context Transformers
A new paper (opens in a new tab) by Google integrates compressive memory into a vanilla dot-product attention layer.
The goal is to enable Transformer LLMs to effectively process infinitely long inputs with bounded memory footprint and computation.
They propose a new attention technique called Infini-attention which incorporates a compressive memory module into a vanilla attention mechanism.
It builds in both masked local attention and long-term linear attention into a single Transformer block. This allows the Infini-Transformer model to efficiently handle both long and short-range contextual dependencies.
This approach outperforms baseline models on long-context language modeling with a 114x compression ratio of memory!
They also show that a 1B LLM can naturally scale to a 1M sequence length and a 8B model achieves a new SoTA result on a 500K length book summarization task.
Given how important long-context LLMs are becoming having an effective memory system could unlock powerful reasoning, planning, continual adaption, and capabilities not seen before in LLMs.

!["Infini-Attention"](../assets/www.promptingguide.ai/www.promptingguide.ai-research-infini-attention/fc26951380ae.webp)
<figcaption>Figure 1. Credit: [www.promptingguide.ai](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finfini-attention.8330113a.png&w=1920&q=75), License: internal-copy</figcaption>
