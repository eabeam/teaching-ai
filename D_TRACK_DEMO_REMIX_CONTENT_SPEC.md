---
type: spec
project: teaching-ai
status: draft
created: 2026-03-24
---

# Demo Remix Workshop: Content Spec

## Purpose

This document specifies the content model for the `Demo Remix Workshop`, a D-track interactive feature for `D1: Building Interactive Demos with AI`.

The goal is to let an instructor choose:

- a topic
- a teaching goal
- an interaction format

and receive a useful, classroom-oriented output scaffold.

## Product Goal

An instructor should be able to leave the page with:

- one plausible demo concept
- one clear pedagogical rationale
- one short classroom-use plan
- one copy-pasteable AI build prompt

## MVP Decision

Use a **hybrid content model**:

- hand-author the option lists
- hand-author 8-12 strong curated combinations
- use one standard output template
- fall back later to a more combinatorial system only if needed

This is safer than fully dynamic generation because the first version needs to feel pedagogically credible, not mechanically exhaustive.

---

## Input Controls

### Control 1: Topic

Use these 6 options in MVP:

1. Supply and demand
2. Externalities
3. Comparative advantage
4. Game theory
5. Regression intuition
6. Elasticity

### Control 2: Teaching Goal

Use these 5 options in MVP:

1. Concept introduction
2. In-class activity
3. Homework extension
4. Exam review
5. Student self-test

### Control 3: Format

Use these 5 options in MVP:

1. Slider-based visualization
2. Click-through scenario
3. Prediction check
4. Parameter manipulation
5. Mini simulation

---

## Output Template

Each generated result should use the same structure.

### Output block 1: Demo concept

One short paragraph answering:

- what the demo is
- what students can manipulate, observe, or decide
- what economics concept becomes visible

### Output block 2: Teaching rationale

One short paragraph answering:

- why this format fits this concept
- what confusion or misconception it helps address

### Output block 3: Classroom use

Exactly 3 bullets:

- how to introduce it
- what students do
- how to debrief or extend it

### Output block 4: AI build prompt

One copy-pasteable prompt that asks an AI tool to help build the demo.

Prompt structure:

- audience level
- economics topic
- interaction type
- required controls or visual elements
- classroom-use constraints
- simplicity requirement

---

## Standard Output Template Text

Use this template shape for all curated entries.

### Demo concept

"Build a [format] demo for [topic] in an undergraduate economics course. Students should be able to [primary interaction]. As they do, they should see [core concept or outcome] update clearly."

### Teaching rationale

"This demo works because it makes [abstract idea] visible and gives students a direct way to test how [economic relationship] changes when [variable] shifts."

### Classroom use

- "Open with a prediction question before students interact with the demo."
- "Have students manipulate one variable and describe what changed."
- "Close by connecting the observed pattern back to the formal model or graph."

### AI build prompt skeleton

"Create a simple browser-based teaching demo for an undergraduate economics course on [topic]. The interaction format should be [format]. Students should be able to [primary interaction]. The demo should visibly update [key outcomes]. Keep the interface clean enough for classroom projection, avoid unnecessary features, and include one short prediction question for students."

---

## Curated Combination Set

The MVP should not try to cover all 150 theoretical combinations. Start with 10 strong combinations that are obviously useful.

### Case 1

**Topic**: Supply and demand
**Teaching goal**: Concept introduction
**Format**: Slider-based visualization

**Demo concept**:
Build a demo where students move demand and supply sliders and watch equilibrium price and quantity shift in real time. The graph should update immediately so students can see comparative statics rather than just hear about them.

**Teaching rationale**:
This works well for first exposure because it links the familiar graph to a concrete action. Students can test whether they actually understand how curve shifts affect equilibrium.

**Classroom use**:
- Ask students to predict what happens before moving either slider.
- Move one curve at a time, then both, and discuss which changes were easier to interpret.
- Debrief by linking the visual movement back to the underlying cause of each shift.

**AI build prompt**:
Create a simple browser-based teaching demo for an undergraduate economics course on supply and demand. Use a slider-based visualization where students can move the demand curve and the supply curve independently. Update equilibrium price and quantity visually as the sliders move. Keep the interface projection-friendly and include one prediction question before students interact.

### Case 2

**Topic**: Externalities
**Teaching goal**: In-class activity
**Format**: Slider-based visualization

**Demo concept**:
Build a demo where students adjust the size of a per-unit tax in a market with a negative production externality. As the tax changes, show private equilibrium, socially efficient output, and deadweight loss.

**Teaching rationale**:
This makes the welfare logic of corrective taxation visible. Students can see why the policy matters rather than memorizing that taxes can improve efficiency in this case.

**Classroom use**:
- Start with a quick vote on whether a tax always reduces welfare.
- Let students change the tax and describe what happens to the socially relevant outcome.
- End by discussing the difference between raising revenue and correcting an externality.

**AI build prompt**:
Create a simple browser-based teaching demo for an undergraduate economics course on negative production externalities. Use a slider-based visualization where students adjust a per-unit tax. Show private equilibrium, socially efficient quantity, and deadweight loss updating clearly as the tax changes. Keep the interface simple for classroom projection and include one prediction prompt.

### Case 3

**Topic**: Comparative advantage
**Teaching goal**: Concept introduction
**Format**: Click-through scenario

**Demo concept**:
Build a step-by-step scenario where students compare two producers with different opportunity costs and decide who should specialize in which good. Reveal each stage only after a student choice.

**Teaching rationale**:
Comparative advantage is often confused with absolute advantage. A click-through scenario slows the reasoning down and makes students commit before seeing the answer.

**Classroom use**:
- Present the initial productivity table without commentary.
- Have students choose specialization before revealing the opportunity-cost comparison.
- Debrief by asking why the less productive producer can still have comparative advantage.

**AI build prompt**:
Create a simple click-through teaching demo for an undergraduate economics course on comparative advantage. Students should work through a specialization scenario step by step, comparing opportunity costs before seeing the answer. Keep the design clean and classroom-friendly, and include one misconception check about absolute versus comparative advantage.

### Case 4

**Topic**: Game theory
**Teaching goal**: In-class activity
**Format**: Prediction check

**Demo concept**:
Build a prediction-based prisoner's dilemma demo where students choose an action, predict what another player will do, and then see the resulting payoffs. The emphasis should be on strategic reasoning, not animation.

**Teaching rationale**:
Students often understand the payoff matrix mechanically but not strategically. A prediction check makes them articulate beliefs, which is the missing step in many classroom explanations.

**Classroom use**:
- Ask students to commit privately to a strategy before seeing any explanation.
- Run the prediction step and compare expected versus realized outcomes.
- Debrief around dominant strategies and why mutual defection can still emerge.

**AI build prompt**:
Create a simple browser-based prediction-check demo for an undergraduate economics course on the prisoner's dilemma. Students should choose an action, predict the other player's action, and then see payoffs update clearly. Keep the interface minimal and focused on strategic reasoning, with one short debrief question built in.

### Case 5

**Topic**: Regression intuition
**Teaching goal**: Concept introduction
**Format**: Parameter manipulation

**Demo concept**:
Build a demo where students adjust the slope, intercept, and noise in a simple regression and watch the scatterplot and fitted line update. The goal is intuitive understanding of fit and signal versus noise.

**Teaching rationale**:
Regression feels abstract when introduced only through formulas. Letting students manipulate parameters makes model structure visible before formal estimation details arrive.

**Classroom use**:
- Ask what a stronger or weaker relationship should look like before changing settings.
- Let students adjust one parameter at a time and narrate what changed.
- Connect the visual pattern back to the interpretation of coefficients and residual noise.

**AI build prompt**:
Create a simple browser-based teaching demo for an undergraduate economics course on regression intuition. Students should be able to manipulate slope, intercept, and noise and see the scatterplot and fitted line update immediately. Keep the interface uncluttered and include one prediction question about what happens when noise increases.

### Case 6

**Topic**: Elasticity
**Teaching goal**: Exam review
**Format**: Prediction check

**Demo concept**:
Build a review demo where students see different demand curves or scenarios and predict which one is more elastic before revealing the answer and explanation.

**Teaching rationale**:
Elasticity errors often come from pattern recognition failures, not missing formulas. A prediction-check format helps students practice classification and justification quickly.

**Classroom use**:
- Present one scenario at a time and collect predictions.
- Reveal the correct answer with a short explanation of the underlying intuition.
- End with a comparison of what features consistently signaled higher elasticity.

**AI build prompt**:
Create a simple browser-based prediction-check demo for an undergraduate economics course on price elasticity of demand. Show students a series of demand scenarios and ask them to predict which is more elastic before revealing the answer. Keep the design simple and include concise explanations rather than long text.

### Case 7

**Topic**: Supply and demand
**Teaching goal**: Homework extension
**Format**: Parameter manipulation

**Demo concept**:
Build a homework-oriented demo where students can manipulate the slope and intercept of supply and demand curves, then answer short follow-up questions about equilibrium changes.

**Teaching rationale**:
This extends comparative statics practice beyond a static worksheet. Students can generate their own examples and test whether their reasoning transfers.

**Classroom use**:
- Assign students to create one parameter combination and screenshot the result.
- Ask them to explain the equilibrium change in words.
- Use responses to identify whether students are confusing movement along a curve with a curve shift.

**AI build prompt**:
Create a simple browser-based teaching demo for an undergraduate economics homework extension on supply and demand. Students should be able to manipulate slopes and intercepts of both curves and observe equilibrium changes. Include two short follow-up questions and keep the interface lightweight.

### Case 8

**Topic**: Externalities
**Teaching goal**: Student self-test
**Format**: Click-through scenario

**Demo concept**:
Build a self-test scenario where students diagnose whether a market example involves a positive or negative externality, identify the private versus social outcome, and then choose an appropriate intervention.

**Teaching rationale**:
Students often memorize policy tools without understanding when they apply. A click-through diagnostic forces classification before solution.

**Classroom use**:
- Use as optional review before a quiz or exam.
- Ask students to explain why their first answer was correct or incorrect.
- Connect the final intervention choice back to the welfare diagram covered in class.

**AI build prompt**:
Create a simple click-through self-test demo for an undergraduate economics course on externalities. Students should classify each scenario, identify the relevant market failure, and choose a plausible intervention before seeing feedback. Keep the interface straightforward and feedback concise.

### Case 9

**Topic**: Game theory
**Teaching goal**: Exam review
**Format**: Mini simulation

**Demo concept**:
Build a simple repeated-play coordination or prisoner's dilemma simulation where students can run several rounds and observe how outcomes depend on strategy choices.

**Teaching rationale**:
A mini simulation helps students see that equilibrium ideas are about incentives over repeated choices, not just static tables on paper.

**Classroom use**:
- Have students predict what repeated interaction will change.
- Run several rounds under one rule, then compare to a different rule.
- Debrief around equilibrium, incentives, and why repetition sometimes matters.

**AI build prompt**:
Create a simple browser-based mini simulation for an undergraduate economics course on game theory. Let students run repeated rounds of a basic strategic interaction and observe how outcomes change with different strategy choices. Keep the simulation small, visual, and easy to explain in class.

### Case 10

**Topic**: Regression intuition
**Teaching goal**: Student self-test
**Format**: Prediction check

**Demo concept**:
Build a self-test where students inspect small scatterplots and predict the sign and relative strength of a linear relationship before revealing a fitted line and explanation.

**Teaching rationale**:
Students need practice translating visual data patterns into verbal statistical intuition. This format is quick, repeatable, and lower-stakes than full computation.

**Classroom use**:
- Ask students to justify each prediction before revealing the fit.
- Compare cases where visual noise makes the answer less obvious.
- Close by discussing what visual inspection can and cannot tell us.

**AI build prompt**:
Create a simple browser-based prediction-check demo for an undergraduate economics course on regression intuition. Show small scatterplots and ask students to predict the sign and rough strength of the relationship before revealing a fitted line. Keep the interface clean and explanations brief.

---

## Recommended JSON-Like Content Shape

For implementation, structure the content as an array of curated cases.

```js
[
  {
    id: "externalities_inclass_slider",
    topic: "Externalities",
    goal: "In-class activity",
    format: "Slider-based visualization",
    demoConcept: "...",
    teachingRationale: "...",
    classroomUse: ["...", "...", "..."],
    aiBuildPrompt: "..."
  }
]
```

## Matching Logic

### MVP logic

- If user selections match a curated case exactly, display that case.
- If there is no exact match, show:
  - the nearest curated case within the same topic, or
  - a generic fallback template populated with the chosen labels

### Recommendation

For V1, consider limiting visible combinations to curated cases only. That avoids weak fallbacks and keeps quality high.

---

## UI Copy

### Intro copy

"Choose a topic, a teaching goal, and an interaction style. The tool will give you a demo idea you can adapt, plus a prompt to help you build it with AI."

### Button label

`Generate Demo Idea`

### Copy button label

`Copy Build Prompt`

### Reset button label

`Try Another Combination`

---

## Design Constraints

- Keep the interface on one screen if possible
- Outputs should appear immediately below the selectors
- The AI build prompt should be easy to copy
- Avoid decorative complexity; the value is in the scaffold

## Open Decisions

1. Should the first release allow all combinations or only curated combinations?
2. Should the output include a suggested tech stack line such as `plain JS`, `Observable`, or `Shinylive`?
3. Should there be a fourth selector for course level later, or is that unnecessary complexity for MVP?

## Recommended Next Artifact

Create a Quarto implementation brief that maps:

- this content model
- the JavaScript data structure
- the page layout
- the fallback behavior

to one actual `.qmd` page prototype.
