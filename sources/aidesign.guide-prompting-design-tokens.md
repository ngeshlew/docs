---
title: "aidesign.guide-prompting-design-tokens"
slug: "aidesign.guide-prompting-design-tokens"
tags: ""
whyForDesigners: "TODO"
botApplication: "TODO"
collaborationPrompts: ""
sources:
- url: "https://aidesign.guide/prompting/design-tokens"
author: "''"
license: "internal-copy"
retrieved_at: "'2025-08-18'"
policy: "copy"
figures: []
updatedAt: "'2025-08-18'"
completed: false
---

# aidesign.guide-prompting-design-tokens

> Synthesis: TODO

Prompts for creating and managing design tokens
Generate a complete design token system for [brand/product] using [token format: CSS custom properties/JSON/YAML]. Include color, typography, spacing, and component tokens with semantic naming.
Create design tokens following the [naming convention: BEM/atomic/tier-based] pattern. Structure them for [use case: design system/component library/multi-brand] with proper hierarchy and inheritance.
Create design tokens using the tier-based naming convention and follow the structure:
component-category-state-role
Component: The UI element (e.g. button, input, card)
Category: The design property (e.g. color, spacing, borderRadius, typography)
State: The UI state (e.g. default, hover, active, disabled)
Role: The semantic intent (e.g. primary, secondary, success, error)
Structure the tokens for a [design system / component library / multi-brand setup].
Ensure:
Clear hierarchy from foundations to component-level tokens
Logical inheritance (semantic tokens referencing foundational values)
Scalability for adding new components, states, or roles
Example tokens for at least 2 components (e.g. button and input)
Output should be in JSON or Tokens Studio-compatible format.
Create typography tokens following this pattern: [font-family/size/weight/line-height]-[scale/variant].
Include responsive scaling and semantic hierarchy (heading, body, caption, etc.).
Create accessibility tokens for: focus indicators, high contrast modes, reduced motion, and screen reader states. Include WCAG compliance markers.
Audit these design tokens for: naming consistency, proper hierarchy, accessibility compliance, and missing variants. Suggest improvements.
Compare the color tokens used in this Figma frame to the tokens in tokens-studio.json. List mismatches and auto-fix the ones that are off by ≤2 %.
Run accessibility checks on the selected frame, annotate WCAG 2.2 violations directly on the layers, and export an .xliff file for localization.
Create a token implementation status table with: Token Name | Design Status | Development Status | Testing Status | Documentation Status | Release Version | Known Issues.
Generate a JSON array of token objects that can be imported into spreadsheet tools: [ { "tokenName": "color-primary-500", "value": "#3B82F6", "category": "Color", "usage": "Primary buttons" } ]
Compare Figma variables with design tokens in code and identify: missing variables, unused tokens, and synchronization issues.
Extract all variables from the Figma file and upsert them into Airtable base Design Tokens v2. If a variable already exists, update its value; if not, create it. Map Figma scopes to Airtable Group field.
Figma MCP: “Use get_variable_defs, then output a Tailwind config that maps them 1-to-1


