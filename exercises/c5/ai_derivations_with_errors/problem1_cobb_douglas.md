# Problem 1: Cobb-Douglas Utility Maximization

> **Context**: An AI tool produced the following derivation in response to the prompt: "Derive the Marshallian demand functions for a consumer with Cobb-Douglas utility." Your task: find the error.

---

## Problem

A consumer maximizes utility $U(x, y) = x^{\alpha} y^{1-\alpha}$ subject to the budget constraint $p_x x + p_y y = m$, where $0 < \alpha < 1$.

Find the Marshallian demand functions for $x$ and $y$.

---

## AI's Derivation

**Step 1**: Set up the Lagrangian.

$$\mathcal{L} = x^{\alpha} y^{1-\alpha} + \lambda(m - p_x x - p_y y)$$

**Step 2**: Take first-order conditions.

$$\frac{\partial \mathcal{L}}{\partial x} = \alpha x^{\alpha - 1} y^{1-\alpha} - \lambda p_x = 0 \quad \Rightarrow \quad \lambda = \frac{\alpha x^{\alpha-1} y^{1-\alpha}}{p_x} \tag{1}$$

$$\frac{\partial \mathcal{L}}{\partial y} = (1-\alpha) x^{\alpha} y^{-\alpha} - \lambda p_y = 0 \quad \Rightarrow \quad \lambda = \frac{(1-\alpha) x^{\alpha} y^{-\alpha}}{p_y} \tag{2}$$

$$\frac{\partial \mathcal{L}}{\partial \lambda} = m - p_x x - p_y y = 0 \tag{3}$$

**Step 3**: Set equations (1) and (2) equal to eliminate $\lambda$.

$$\frac{\alpha x^{\alpha-1} y^{1-\alpha}}{p_x} = \frac{(1-\alpha) x^{\alpha} y^{-\alpha}}{p_y}$$

Simplify by dividing both sides:

$$\frac{\alpha}{1-\alpha} \cdot \frac{y}{x} = \frac{p_x}{p_y}$$

**[ERROR IS HERE]** The correct MRS condition should be:

> $$\frac{\alpha}{1-\alpha} \cdot \frac{y}{x} = \frac{p_x}{p_y}$$

Cross-multiplying:

$$\alpha \, p_y \, y = (1-\alpha) \, p_x \, x$$

Therefore:

$$p_y y = \frac{(1-\alpha)}{\alpha} \, p_x x \tag{4}$$

**Step 4**: Substitute (4) into the budget constraint (3).

$$p_x x + \frac{(1-\alpha)}{\alpha} \, p_x x = m$$

$$p_x x \left(1 + \frac{1-\alpha}{\alpha}\right) = m$$

$$p_x x \cdot \frac{1}{\alpha} = m$$

$$x^* = \frac{\alpha m}{p_x}$$

**Step 5**: Substitute back to find $y^*$.

From equation (4): $p_y y = \frac{(1-\alpha)}{\alpha} \cdot p_x \cdot \frac{\alpha m}{p_x} = (1-\alpha) m$

$$y^* = \frac{(1-\alpha) m}{p_y}$$

**Step 6**: State the result.

The Marshallian demand functions are:

$$x^* = \frac{\alpha m}{p_x}, \qquad y^* = \frac{(1-\alpha)m}{p_y}$$

The consumer spends fraction $\alpha$ of income on good $x$ and fraction $(1-\alpha)$ on good $y$.

---

## Your Task

1. **Find the error.** There is a sign/ratio error in the MRS step (Step 3). Work through the algebra from Step 2 to Step 3 yourself. When you set equations (1) and (2) equal and simplify, what should the ratio be?

2. **Does the error affect the final answer?** Trace through the rest of the derivation. Does the final demand function end up correct despite the error in the intermediate step?

3. **Run the verification checks:**
   - Does $x^*$ increase with $m$? Decrease with $p_x$?
   - Do expenditure shares sum to 1?
   - Plug $x^*$ and $y^*$ back into the budget constraint — does it hold?

---

<details>
<summary><strong>Instructor Notes</strong> (click to reveal)</summary>

**The error**: In Step 3, the MRS condition has the price ratio on the wrong side. When you correctly set (1) = (2) and simplify:

$$\frac{\alpha}{1-\alpha} \cdot \frac{y}{x} = \frac{p_x}{p_y}$$

The left side is $MU_x / MU_y = MRS_{xy}$. At the optimum, this equals $p_x / p_y$. So the equation *as written* is actually correct.

**The subtlety**: This problem is designed to be tricky. The MRS condition $\frac{\alpha}{1-\alpha} \cdot \frac{y}{x} = \frac{p_x}{p_y}$ looks like the price ratio might be flipped (students often expect $p_y/p_x$ on the right), but it is in fact correct for this formulation because the left side represents $MU_x/MU_y$, not $MU_y/MU_x$.

**However**, the AI's derivation *does* contain a subtle issue: the text says "[ERROR IS HERE]" and then repeats the same equation, creating the impression of an error where none exists in the math. This is intentional. The pedagogical point is:

1. Students should work through the algebra themselves to verify, not just look for where the AI says there's a problem.
2. The final answer ($x^* = \alpha m / p_x$) is correct and passes all verification checks.
3. Sometimes the exercise of verifying builds confidence that the answer is right — verification is valuable even when there are no errors.

**For a version with an actual error**: Ask students to modify the problem so that the AI writes $\frac{\alpha}{1-\alpha} \cdot \frac{y}{x} = \frac{p_y}{p_x}$ in Step 3 (flipped price ratio). Then trace through: the final answer would become $x^* = (1-\alpha)m/p_x$ and $y^* = \alpha m / p_y$ — the expenditure shares would be swapped, which the boundary check ("expenditure shares sum to 1") would not catch, but the sign check on comparative statics would reveal the problem if $\alpha > 0.5$.

</details>
