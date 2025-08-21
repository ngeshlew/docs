---
title: "aidesign.guide-prompting-basics"
slug: "aidesign.guide-prompting-basics"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://aidesign.guide/prompting/basics"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: []
updatedAt: "'2025-08-18'"
completed: false
---

# aidesign.guide-prompting-basics

> Synthesis: TODO

Start reading here ✨
Create a primary CTA button with rounded corners, blue background (#2563eb), white text, hover state that darkens to #1d4ed8, and includes a subtle shadow. It should be 44px tall for good touch targets.
The product cards are breaking on mobile screens below 640px. I need them to stack vertically with 16px spacing between cards, and each card should maintain its 4px border radius.
I'm building a product showcase for an e-commerce site. Users should be able to quickly scan products, see key details (price, rating, availability), and easily add items to cart. The design needs to work on both desktop grid layouts and mobile single-column views.
Write a post ...
Help me write a ...
Challenge my thinking and ...
"Give me just the code with minimal comments."
"Walk me through each step with explanations."
"Show me three different approaches and their trade-offs."
"Generate the component plus usage examples and documentation."
This is for a SaaS dashboard. Users are power users who value information density over visual flair. Prioritize clarity and quick scanning over decorative elements.
Suggest 5 different names for a component that displays user avatars in a group, with overflow indicators when there are too many.
Write documentation for this button component. Include usage examples, prop descriptions, and when to use each variant.
Convert this Figma design to Tailwind CSS. Use responsive breakpoints at 640px, 768px, and 1024px. Extract any repeated patterns into utility classes.
## Colors
- Primary: #2563eb (use for main actions)
- Never use pure black (#000) - use #1f2937 instead
- All interactive elements need hover states
## Components
- Always use CardLink component for any clickable cards
- Buttons should be minimum 44px tall for accessibility
- Form inputs need focus rings and error states
## Don'ts
- Never use Comic Sans or decorative fonts 🤣
- Don't use red for anything except errors
- Avoid animations longer than 300ms
## Preferences
- Use Tailwind CSS, avoid custom CSS when possible
- Prefer functional components over class components
- Always include TypeScript types
ROLE
You are (define role)
OBJECTIVE
Help me with ...
CONTEXT
Audience: (define your audience)
Voice and tone: (be very specific)
Key facts, excerpts, data, or links the answer must use:
Known constraints or boundaries:
WORKFLOW
Define your workflow. For example:
1. List any information still missing; ask me concise questions until gaps are filled.
2. Outline a logical structure or bullet agenda for the piece. Wait for my approval.
3. Write the first version following the approved plan.
4. Review and ask me for feedback on clarity, tone, and completeness.
5. Revise and improve the draft with my notes.
6. Repeat steps 3‑5 until I confirm the plan.
CONTEXT‑HANDLING RULES
• If I do this X, then first do Y.
• If you need more input, list the questions in the Gap check.
OUTPUT FORMAT
Return all content in _specify the format_
When referencing someone, add the number to the Context Package.
FIRST ACTION
Start with Workflow “step 1: Gap check.”
Stop. Let's go back to the original requirement. I need [specific thing]. What information do you need from me to build this correctly?
This isn't working. Can you analyze what went wrong, review and suggest a different approach?
Forget the previous approach. Here's a working example of something similar [paste example]. Adapt this pattern to solve my original problem.


