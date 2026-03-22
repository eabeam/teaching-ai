# Problem 3: Price Elasticity and the Slutsky Decomposition

> **Context**: An AI tool produced the following derivation and interpretation in response to the prompt: "For the demand function $x(p, m) = m / (2p)$, compute the own-price elasticity and decompose the total price effect into income and substitution effects using the Slutsky equation." Your task: check the math and the interpretation.

---

## Problem

A consumer has demand function $x(p, m) = \frac{m}{2p}$ for good $x$ (derived from $U(x, y) = x^{0.5} y^{0.5}$ with budget constraint $px + y = m$, where the price of $y$ is normalized to 1).

1. Compute the own-price elasticity of demand.
2. Use the Slutsky equation to decompose the price effect into substitution and income effects.
3. Interpret the results.

---

## AI's Derivation

**Step 1**: Compute the own-price elasticity.

The demand function is $x(p, m) = \frac{m}{2p}$.

$$\frac{\partial x}{\partial p} = -\frac{m}{2p^2}$$

The own-price elasticity is:

$$\varepsilon_{x,p} = \frac{\partial x}{\partial p} \cdot \frac{p}{x} = -\frac{m}{2p^2} \cdot \frac{p}{\frac{m}{2p}} = -\frac{m}{2p^2} \cdot \frac{2p^2}{m} = -1$$

The demand has unit elasticity: a 1% increase in price leads to a 1% decrease in quantity demanded.

**Step 2**: Apply the Slutsky equation.

The Slutsky equation decomposes the total price effect into substitution and income effects:

$$\frac{\partial x}{\partial p} = \frac{\partial h}{\partial p} - x \cdot \frac{\partial x}{\partial m}$$

where $h(p, u)$ is the Hicksian (compensated) demand.

First, compute the income effect component. The income effect is:

$$\frac{\partial x}{\partial m} = \frac{1}{2p}$$

So the income effect term is:

$$-x \cdot \frac{\partial x}{\partial m} = -\frac{m}{2p} \cdot \frac{1}{2p} = -\frac{m}{4p^2}$$

**Step 3**: Find the substitution effect.

From the Slutsky equation:

$$\frac{\partial h}{\partial p} = \frac{\partial x}{\partial p} + x \cdot \frac{\partial x}{\partial m}$$

$$= -\frac{m}{2p^2} + \frac{m}{4p^2} = -\frac{m}{4p^2}$$

**Step 4**: Summarize the decomposition.

| Component | Expression | Value |
|-----------|-----------|-------|
| Total price effect | $\frac{\partial x}{\partial p}$ | $-\frac{m}{2p^2}$ |
| Substitution effect | $\frac{\partial h}{\partial p}$ | $-\frac{m}{4p^2}$ |
| Income effect | $-x \cdot \frac{\partial x}{\partial m}$ | $-\frac{m}{4p^2}$ |

Both effects are negative and equal in magnitude, each accounting for exactly half of the total price effect.

**Step 5**: Interpretation.

When the price of good $x$ increases, two forces reduce demand. The **substitution effect** captures the fact that the consumer switches to the relatively cheaper good $y$ — this is the pure relative price channel holding utility constant. The **income effect** captures the fact that a price increase reduces the consumer's real purchasing power, causing them to buy less of all normal goods.

In this case, the income effect dominates the substitution effect, meaning that the reduction in real income from the price increase is the primary driver of the demand response. This is consistent with good $x$ being a necessity — goods that absorb a large share of the consumer's budget tend to have large income effects.

---

## Your Task

### 1. Check the math (Steps 1-4)

Work through each step of the derivation. Are the partial derivatives correct? Is the Slutsky decomposition applied correctly? Does the table in Step 4 add up?

### 2. Evaluate the interpretation (Step 5)

The AI claims that "the income effect dominates the substitution effect." Look at the magnitudes in the table. Is this claim correct?

### 3. Evaluate the economic reasoning

The AI says this pattern is "consistent with good $x$ being a necessity — goods that absorb a large share of the consumer's budget tend to have large income effects."

- What fraction of income does the consumer spend on good $x$ in this model?
- Is $x$ a "necessity" in the standard economic sense?
- Is the AI's reasoning about budget shares and income effects correct here?

### 4. Write a corrected interpretation

In 2-3 sentences, write an accurate interpretation of the Slutsky decomposition for this demand function.

---

<details>
<summary><strong>Answer Key</strong> (click to reveal)</summary>

**The math (Steps 1-4) is correct.** The elasticity is $-1$. The Slutsky decomposition is properly computed. The substitution and income effects are indeed equal, each contributing $-m/(4p^2)$ to the total effect of $-m/(2p^2)$.

**The interpretation (Step 5) is wrong in two ways.**

**Error 1: "The income effect dominates the substitution effect."**

This is false. The table clearly shows that both effects are equal in magnitude: $-m/(4p^2)$ each. Neither dominates. The AI stated a conclusion that directly contradicts its own math. This is a common AI failure mode: the mathematical derivation is correct, but the verbal interpretation is generated from patterns in training data rather than from the actual numbers on the page.

**Error 2: "This is consistent with good $x$ being a necessity."**

This reasoning is confused. In this model (Cobb-Douglas with $\alpha = 0.5$), the consumer spends exactly 50% of income on good $x$ — this is a constant expenditure share, not a "necessity" pattern. The income elasticity of demand is exactly 1 (homothetic preferences), which means $x$ is neither a necessity nor a luxury in the standard sense. It is a unit-elastic good.

The equal split between substitution and income effects is a consequence of the Cobb-Douglas functional form with equal exponents, not a statement about whether the good is a necessity. With Cobb-Douglas utility $U = x^\alpha y^{1-\alpha}$, the substitution effect always accounts for fraction $(1-\alpha)$ and the income effect for fraction $\alpha$ of the total price effect. When $\alpha = 0.5$, they're equal by construction.

**A correct interpretation**: "The price elasticity of demand is $-1$ (unit elastic), meaning the consumer's total expenditure on good $x$ remains constant as price changes. The Slutsky decomposition shows that the substitution and income effects contribute equally to the total price response, which is a property of Cobb-Douglas preferences with equal exponents ($\alpha = 0.5$). The consumer has homothetic preferences and spends a constant 50% of income on good $x$ regardless of prices or income."

**Pedagogical point**: This problem demonstrates the module's key warning: AI is better at algebra than interpretation. The derivation is flawless, but the concluding paragraph contains claims that contradict the math and reflect generic patterns from training data ("income effect dominates" and "necessity" are common phrases in textbook discussions of the Slutsky equation, but they don't apply here).

</details>
