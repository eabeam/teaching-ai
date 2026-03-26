---
type: memo
project: teaching-ai
status: draft
created: 2026-03-24
---

# D-Track Interactive Feature Memo

## Feature

**Demo Remix Workshop**

A lightweight interactive builder for instructors who want to create or adapt an economics teaching demo with AI support, without starting from a blank page.

## Why This Feature

The D-track should help faculty do pedagogy work, not just read about it. A remix tool fits that goal because it turns a broad idea like "I want an AI-generated class demo" into a structured design workflow:

- choose a topic
- choose a teaching goal
- choose an interaction style
- get a tailored demo concept plus a strong build prompt

This is more useful than a static gallery alone because it helps instructors map from their own course need to a concrete prototype.

## Core User Story

An instructor teaching economics wants a quick in-class interactive or student-facing demo. They do not want to invent the whole thing from scratch, and they do not want generic ed-tech advice. They want a scaffold they can adapt.

## Proposed Interaction

The page presents three sets of choices:

### 1. Topic
- Supply and demand
- Externalities
- Comparative advantage
- Game theory
- Regression intuition
- Elasticity

### 2. Teaching goal
- Concept introduction
- In-class activity
- Homework extension
- Exam review
- Student self-test

### 3. Format
- Slider-based visualization
- Click-through scenario
- Prediction check
- Parameter manipulation
- Mini simulation

Once the user selects one option from each set, the page generates:

- a demo concept
- a short teaching rationale
- a list of what students would do
- a suggested implementation path
- a prompt for building the demo with AI

## Example Output

**Topic**: Externalities
**Teaching goal**: In-class activity
**Format**: Slider-based visualization

**Generated concept**:
"Build a classroom demo where students adjust the size of a pollution tax and watch the gap between private and social marginal cost shrink. Ask students to predict what happens to equilibrium quantity before they move the slider."

**Teaching rationale**:
"This makes the welfare logic visible and gives students a concrete way to connect the diagram to policy intervention."

**AI build prompt**:
"Create a simple browser-based teaching demo for an undergraduate economics course. The demo should show a market with a negative production externality. Include a slider for the per-unit tax and update the private equilibrium, socially efficient quantity, and deadweight loss visually as the slider changes. Keep the interface simple enough for classroom projection and include one prediction question for students."

## Why It Fits D1

This feature belongs naturally in `D1: Building Interactive Demos with AI` because it:

- gives faculty a structured on-ramp to demo creation
- connects pedagogy choices to technical output
- avoids requiring coding knowledge up front
- produces something reusable: a prompt, a concept, and a build plan

## MVP Scope

The first version can be simple and still useful.

### MVP inputs
- 4-6 topic options
- 4-5 teaching goals
- 3-5 format options

### MVP outputs
- one paragraph demo concept
- one paragraph teaching rationale
- 3 bullet points for classroom use
- one copy-pasteable AI prompt

### MVP technical approach
- Quarto page with client-side JavaScript
- simple selection controls
- prewritten lookup table or structured content object
- no backend required

## Why This Is Better Than a Static Template

A static template says, "Here are some demos."

This feature says, "Here is the demo idea that fits your topic, course use, and classroom format."

That is a much better faculty experience because it starts from instructional intent rather than from a pile of examples.

## Design Guardrails

- Keep the interface fast and plainspoken
- Do not pretend the tool is generating infinite originality; it is a scaffold generator
- Keep outputs specific enough to be useful, but simple enough that faculty can edit them
- Avoid overengineering the first version

## Risks

- If the combinations feel too generic, instructors will not trust it
- If there are too many options, the tool becomes fiddly
- If the output sounds too much like prompt boilerplate, it loses pedagogical value

## Recommendation

Build this as a small MVP first, not as a large demo library.

The right first goal is:
"Can an instructor leave this page with one plausible interactive-demo idea and a prompt they would actually use?"

If yes, the feature is working.

## Next Build Step

If this moves forward, the next artifact should be a content spec with:

- the exact option lists
- 8-12 curated output combinations
- one standard output template
- a decision about whether to generate outputs combinatorially or from hand-authored cases
