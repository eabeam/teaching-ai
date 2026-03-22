# C5 Exercise Materials: Math & Derivations

These materials support the exercises in [Module C5: Math & Derivations](../../modules/c5-math-derivations.qmd).

## Contents

### Verification Report Template

- **`verification_report_template.md`** — Structured template for checking AI-generated derivations. Includes sections for the student's own solution, the AI's solution, a discrepancy table, and a checklist of verification methods (boundary cases, dimensions, special cases, working backwards, sign checks).

### AI Derivations with Errors

These present derivations "produced by an AI" that students must evaluate. Each contains a specific type of error commonly made by AI tools.

- **`ai_derivations_with_errors/problem1_cobb_douglas.md`** — A Cobb-Douglas utility maximization where the MRS step looks potentially wrong (price ratio orientation). Tests whether students can verify the intermediate steps algebraically and recognize when something is actually correct.

- **`ai_derivations_with_errors/problem2_profit_max.md`** — A profit maximization problem where the production function has increasing returns ($f(L) = 10L^{1.5}$). The AI finds the critical point but doesn't check the second-order condition. The "maximum" is actually a minimum, and no finite maximum exists. Tests understanding of SOCs and increasing returns.

- **`ai_derivations_with_errors/problem3_elasticity.md`** — An own-price elasticity calculation and Slutsky decomposition where the math is entirely correct but the interpretation paragraph is wrong. The AI claims "the income effect dominates" when the two effects are equal, and mischaracterizes the good as a "necessity." Tests the distinction between correct algebra and correct economic reasoning.

## How to Use

### Verification Report (standalone or paired with module exercise)

Students fill out the template when doing the module's main exercise (Parts 1-4): solve a problem yourself, ask AI to solve it, compare, and verify.

### AI Derivations (in-class or homework, ~15 min each)

Each problem is self-contained. Students read the AI's derivation, find the error, and explain why it matters. The problems are ordered by difficulty:

1. **Problem 1** (Cobb-Douglas) — Tests algebraic verification. Good warm-up.
2. **Problem 2** (Profit maximization) — Tests understanding of second-order conditions. Core intermediate micro concept.
3. **Problem 3** (Elasticity/Slutsky) — Tests whether students can distinguish correct math from incorrect interpretation. Most subtle.

### Prerequisite Math

Students should be comfortable with:
- Constrained optimization (Lagrangian method)
- Partial derivatives and the chain rule
- Second-order conditions for maximization
- The Slutsky equation (for Problem 3)

These exercises are pitched at the intermediate microeconomics level.

## Answer Keys

Each problem file contains an answer key in collapsible `<details>` tags at the bottom. For instructor-only distribution, these can be extracted or the files can be edited to remove the tags.
