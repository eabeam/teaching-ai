# Problem 2: Profit Maximization with Increasing Returns

> **Context**: An AI tool produced the following derivation in response to the prompt: "A firm with production function $f(L) = 10L^{1.5}$ faces output price $p = 2$ and wage $w = 5$. Find the profit-maximizing labor choice." Your task: evaluate whether the AI's answer is actually a profit maximum.

---

## Problem

A firm produces output using labor according to the production function $f(L) = 10L^{1.5}$ and sells its output at price $p = 2$. The wage rate is $w = 5$. The firm chooses labor $L \geq 0$ to maximize profit:

$$\pi(L) = p \cdot f(L) - wL = 2 \cdot 10L^{1.5} - 5L = 20L^{1.5} - 5L$$

Find the profit-maximizing choice of $L$.

---

## AI's Derivation

**Step 1**: Write the profit function.

$$\pi(L) = 20L^{1.5} - 5L$$

**Step 2**: Take the first-order condition.

$$\frac{d\pi}{dL} = 20 \cdot 1.5 \cdot L^{0.5} - 5 = 30L^{0.5} - 5 = 0$$

**Step 3**: Solve for $L^*$.

$$30L^{0.5} = 5$$

$$L^{0.5} = \frac{5}{30} = \frac{1}{6}$$

$$L^* = \frac{1}{36}$$

**Step 4**: Calculate the profit at the optimum.

$$\pi(L^*) = 20 \left(\frac{1}{36}\right)^{1.5} - 5 \cdot \frac{1}{36}$$

$$= 20 \cdot \frac{1}{216} - \frac{5}{36}$$

$$= \frac{20}{216} - \frac{5}{36} = \frac{20}{216} - \frac{30}{216} = -\frac{10}{216} \approx -0.046$$

**Step 5**: State the result.

The profit-maximizing labor choice is $L^* = 1/36 \approx 0.028$, yielding profit of approximately $-0.046$. The firm operates at a small loss at the optimal scale.

---

## Your Task

### 1. Check the second-order condition

The AI found a critical point using the FOC. But is it a maximum?

Compute the second derivative of $\pi(L)$:

$$\frac{d^2\pi}{dL^2} = \text{?}$$

Evaluate it at $L^* = 1/36$. What is its sign? What does this tell you?

### 2. Think about the production function

The production function is $f(L) = 10L^{1.5}$. What are the returns to scale? (Hint: if you double $L$, what happens to output?)

What does this imply about the firm's profit maximization problem?

### 3. Check the boundary

The AI found that $\pi(L^*) < 0$. But what happens to profit as $L$ gets very large?

Compute $\pi(100)$, $\pi(1000)$, and $\pi(10000)$. What is happening?

### 4. What went wrong?

Write a paragraph explaining why the AI's answer is incorrect and what economic principle it violated.

---

<details>
<summary><strong>Answer Key</strong> (click to reveal)</summary>

**The error**: The AI correctly found the critical point of the profit function but failed to check the second-order condition. The critical point is a **minimum**, not a maximum.

**Second-order condition**:

$$\frac{d^2\pi}{dL^2} = 30 \cdot 0.5 \cdot L^{-0.5} = 15L^{-0.5}$$

At $L^* = 1/36$: $\frac{d^2\pi}{dL^2} = 15 \cdot (1/36)^{-0.5} = 15 \cdot 6 = 90 > 0$

The second derivative is **positive**, which means $L^* = 1/36$ is a **local minimum**, not a maximum.

**Why this happens**: The production function $f(L) = 10L^{1.5}$ exhibits **increasing returns to scale** (the exponent 1.5 > 1). When you double labor, output more than doubles: $f(2L) = 10(2L)^{1.5} = 10 \cdot 2^{1.5} \cdot L^{1.5} \approx 2.83 \cdot f(L)$.

With increasing returns, the marginal product of labor is increasing, so the more labor the firm hires, the more productive each additional unit becomes. This means profit increases without bound as $L \to \infty$:

- $\pi(100) = 20(100)^{1.5} - 5(100) = 20{,}000 - 500 = 19{,}500$
- $\pi(1{,}000) = 20(1{,}000)^{1.5} - 5(1{,}000) = 632{,}456 - 5{,}000 = 627{,}456$
- $\pi(10{,}000) = 20(10{,}000)^{1.5} - 5(10{,}000) = 20{,}000{,}000 - 50{,}000 = 19{,}950{,}000$

**No finite profit maximum exists.** The firm would want to hire infinite labor. This is the standard result for a price-taking firm with increasing returns to scale: the profit maximization problem has no interior solution.

**The AI's mistake**: It solved the FOC mechanically and reported the critical point as "the profit-maximizing labor choice" without:
1. Checking the SOC (which reveals it's a minimum)
2. Recognizing that increasing returns means no finite maximum exists
3. Noticing that negative profit at the "optimum" is a red flag (the firm could earn zero profit by choosing $L = 0$, which dominates)

**Economic lesson**: Second-order conditions are not optional. The FOC identifies candidates; the SOC tells you whether they're maxima, minima, or saddle points. With increasing returns, standard profit maximization for a price-taker breaks down entirely.

</details>
