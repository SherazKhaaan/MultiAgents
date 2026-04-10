# Week 7: Fair Division (Part I) -- Divisible Goods and Cake Cutting

## Learning Objectives
By the end of this week, you should be able to:
- [ ] Explain foundational concepts of fair division, including proportionality, envy-freeness, and efficiency.
- [ ] Model resource allocation problems as fair division scenarios using mathematical and algorithmic frameworks.
- [ ] Apply classic algorithms to achieve fair outcomes for divisible goods (cake cutting).
- [ ] Analyse the strengths and limitations of different fair division procedures by evaluating guarantees, complexity, and strategic aspects.
- [ ] Assess allocation solutions for fairness and optimality using formal properties and counterexamples.
- [ ] Solve practical and theoretical problems involving cake-cutting and other fair division contexts.
- [ ] Discuss applications of fair division in economics, computer science, law, and everyday resource-sharing situations.
- [ ] Reflect on ethical, strategic, and computational challenges inherent to achieving fairness among multiple agents.

---

## 1. Introduction to Fair Division

### 1.1 What is Fair Division?

**Fair division** is the problem of dividing one or several goods amongst two or more agents in a way that satisfies a suitable **fairness criterion**. It is a sub-area of the broader field of **multi-agent resource allocation (MARA)**, distinguished by its explicit focus on fairness concerns.

Fair division is central to multi-agent systems for several reasons:
- Much work in MAS is directly about designing mechanisms for resource allocation
- In collaborative problem solving, agents must first agree on a suitable division of available resources
- Typical MAS application areas (e.g., electronic commerce) are closely tied to resource allocation
- Users and platform developers need fairness guarantees to maintain trust and participation

### 1.2 Setting

We consider:
- A **finite set of agents** $N = \{1, \ldots, n\}$ (also called individuals or players)
- A set of **goods** (resources, items, objects, commodities) to be divided among them

### 1.3 Types of Goods

Goods can be classified along several dimensions:

| Dimension | Options |
|---|---|
| **Divisibility** | Divisible (e.g., cake, land, time) vs. Indivisible (e.g., a book, a house) |
| **Temporal nature** | Static vs. Perishable/Consumable |
| **Sharability** | Sharable vs. Non-sharable |
| **Multiplicity** | Single unit vs. Multiple (indistinguishable) units |

**This week focuses on divisible goods** (cake cutting). Next week covers indivisible goods.

We restrict our attention to goods that are **static**, available in **single units**, and **non-sharable**.

---

## 2. Cake Cutting: Mathematical Model

### 2.1 The Model

We model the cake as the **unit interval** $[0, 1]$ and define:

- A set of players $N = \{1, \ldots, n\}$
- **Pieces of cake** $X_1, \ldots, X_m \subseteq [0, 1]$, each a finite union of disjoint subintervals. The pieces are themselves disjoint and their union gives the whole cake:
$$\forall i, j: X_i \cap X_j = \emptyset; \quad \bigcup_{i=1}^{m} X_i = [0, 1]$$

### 2.2 Valuation Functions

Each player $i \in N$ has a **non-negative, absolutely continuous valuation function** $v_i(X)$ over pieces of cake, satisfying:

1. **Additivity**: If $X$ and $Y$ are disjoint, then $v_i(X \cup Y) = v_i(X) + v_i(Y)$
2. **Normalization**: $v_i([0, 1]) = 1$ (the whole cake is worth exactly 1 to every agent)
3. **Divisibility**: Given an interval $I$ and $\lambda \in [0, 1]$, there exists a subinterval $I' \subseteq I$ such that $v_i(I') = \lambda \cdot v_i(I)$

Different players may value different parts of the cake differently (e.g., one player prefers chocolate, another prefers vanilla).

### 2.3 Allocations

**Goal**: Find an allocation $(A_1, \ldots, A_n)$ where:
- $A_i$ is the piece of cake allocated to agent $i$
- Pieces are **disjoint**: $A_i \cap A_j = \emptyset$ for all $i \neq j$
- An allocation is **complete** if $\bigcup_{i=1}^{n} A_i = [0, 1]$

### 2.4 Worked Example

Consider a cake where $[0, 1/4]$ is chocolate and $[1/4, 1]$ is sponge, with two agents:
- **Agent 1** only likes chocolate: $v_1([p, q]) = 4|q - p|$ for $0 \leq p < q \leq 1/4$, and $v_1([1/4, 1]) = 0$
- **Agent 2** likes everything equally: $v_2([p, q]) = |q - p|$ for $0 \leq p < q \leq 1$

Three possible allocations:
| Allocation | $v_1(A_1)$ | $v_2(A_2)$ |
|---|---|---|
| $A_1 = [0, 1/2], A_2 = [1/2, 1]$ | $1$ | $1/2$ |
| $A_1 = [0, 1/4], A_2 = [1/4, 1]$ | $1$ | $3/4$ |
| $A_1 = [0, 1/5], A_2 = [1/5, 1]$ | $4/5$ | $4/5$ |

---

## 3. Solution Concepts (Fairness Criteria)

### 3.1 Proportionality

An allocation $(A_1, \ldots, A_n)$ is **proportional** if each agent values their share at at least $1/n$:

$$v_i(A_i) \geq \frac{1}{n} \quad \text{for all } i \in N$$

**Intuition**: Every agent receives what they consider to be at least their "fair share."

**Example** (from Section 2.4, $n = 2$, so threshold is $1/2$):
- $A_1 = [0, 1/2], A_2 = [1/2, 1]$: $v_1 = 1 \geq 1/2$, $v_2 = 1/2 \geq 1/2$ -- **Proportional**
- $A_1 = [0, 1/4], A_2 = [1/4, 1]$: $v_1 = 1 \geq 1/2$, $v_2 = 3/4 \geq 1/2$ -- **Proportional**
- $A_1 = [0, 1/5], A_2 = [1/5, 1]$: $v_1 = 4/5 \geq 1/2$, $v_2 = 4/5 \geq 1/2$ -- **Proportional**
- $A_1 = [0, 2/3], A_2 = [2/3, 1]$: $v_1 = 1 \geq 1/2$, but $v_2 = 1/3 < 1/2$ -- **NOT Proportional**

### 3.2 Envy-Freeness

An allocation is **envy-free** if no agent envies another:

$$v_i(A_i) \geq v_i(A_j) \quad \text{for all } i, j \in N$$

**Intuition**: Every agent believes they received the best (or tied-for-best) piece.

**Example**:
- $A_1 = [0, 1/2], A_2 = [1/2, 1]$: Agent 1 has $v_1(A_1) = 1$, $v_1(A_2) = 0$. Agent 2 has $v_2(A_1) = 1/2$, $v_2(A_2) = 1/2$. No envy -- **Envy-free**
- $A_2 = [0, 1/2], A_1 = [1/2, 1]$ (swapped): Agent 1 has $v_1(A_1) = 0$, $v_1(A_2) = 1$. Agent 1 envies Agent 2 -- **NOT Envy-free**

### 3.3 Equitability

An allocation is **equitable** if all agents have the **same value** for their allocated piece:

$$v_i(A_i) = v_j(A_j) \quad \text{for all } i, j \in N$$

**Example**:
- $A_1 = [0, 1/2], A_2 = [1/2, 1]$: $v_1 = 1 \neq 1/2 = v_2$ -- **NOT Equitable**
- $A_1 = [0, 1/4], A_2 = [1/4, 1]$: $v_1 = 1 \neq 3/4 = v_2$ -- **NOT Equitable**
- $A_1 = [0, 1/5], A_2 = [1/5, 1]$: $v_1 = 4/5 = 4/5 = v_2$ -- **Equitable**

### 3.4 Pareto-Optimality

An allocation $(A_1, \ldots, A_n)$ is **Pareto-optimal** if there is no other allocation $(B_1, \ldots, B_n)$ such that:
- $v_i(B_i) \geq v_i(A_i)$ for all $i$ (no one is worse off), AND
- $v_i(B_i) > v_i(A_i)$ for some $i$ (at least one agent is strictly better off)

**Example**:
- $A_1 = [0, 1/2], A_2 = [1/2, 1]$: **NOT Pareto-optimal** because $(B_1 = [0, 1/4], B_2 = [1/4, 1])$ gives Agent 1 the same utility ($v_1 = 1$) but increases Agent 2's utility from $1/2$ to $3/4$
- $A_1 = [0, 1/4], A_2 = [1/4, 1]$: **Pareto-optimal** -- cannot improve Agent 2 without taking chocolate from Agent 1

### 3.5 Summary of Solution Concepts

| Allocation | Proportional | Envy-free | Equitable | Pareto-optimal |
|---|---|---|---|---|
| $A_1 = [0, 1/2], A_2 = [1/2, 1]$ | Yes | Yes | No | No |
| $A_1 = [0, 1/4], A_2 = [1/4, 1]$ | Yes | Yes | No | Yes |
| $A_1 = [0, 1/5], A_2 = [1/5, 1]$ | Yes | Yes | Yes | ? |

---

## 4. Relationships Between Solution Concepts

### 4.1 Two Players: Proportionality $\iff$ Envy-Freeness

**Theorem.** *For two players, an allocation is proportional if and only if it is envy-free.*

**Proof.**

$(\Rightarrow)$ **Envy-freeness implies proportionality**: WLOG, if player 1 does not envy player 2, then $v_1(A_1) \geq v_1(A_2)$. Since $v_1(A_1) + v_1(A_2) = 1$, this implies $v_1(A_1) \geq 1/2$, which is proportionality for $n = 2$.

$(\Leftarrow)$ **Proportionality implies envy-freeness**: If the allocation is proportional, then $v_1(A_1) \geq 1/2$. Since $v_1(A_1) + v_1(A_2) = 1$, this implies $v_1(A_1) \geq v_1(A_2)$, so player 1 does not envy player 2. The same argument applies to player 2. $\square$

### 4.2 Three or More Players: Envy-Freeness $\Rightarrow$ Proportionality (but NOT vice versa)

**Theorem.** *For three or more players, envy-freeness implies proportionality, but the converse is not true.*

**Proof (EF $\Rightarrow$ PROP)**: Let $A_i$ be what player $i$ values most among $A_1, \ldots, A_n$. Since $\sum_{j=1}^{n} v_i(A_j) = 1$, it must be that $v_i(A_i) \geq 1/n$ (otherwise the sum could not reach 1). Since the allocation is envy-free, player $i$ must receive $A_i$ (their most-valued piece), so $v_i(A_i) \geq 1/n$. $\square$

**Counterexample (PROP $\not\Rightarrow$ EF)**: Three players. Let $v_1(A_1) = 1/3$, $v_1(A_2) = 1/3 + \varepsilon$, $v_1(A_3) = 1/3 - \varepsilon$ for small $\varepsilon > 0$. The allocation is proportional (player 1 gets exactly $1/3$), but player 1 envies player 2 (whose piece player 1 values at $1/3 + \varepsilon > 1/3$).

### 4.3 Summary of Relationships

```
For n = 2:    Envy-free  <=>  Proportional
For n >= 3:   Envy-free   =>  Proportional  (but NOT the reverse)
```

---

## 5. Computation: Can We Find Fair Allocations Efficiently?

Key questions:
- Do fair solutions always exist?
- Can we find them efficiently?

Summary of answers:
- **Proportionality**: Yes, with a simple algorithm (Cut-and-Choose for 2 players; Dubins-Spanier or Even-Paz for $n$ players)
- **Envy-freeness**: Trivially yes (throw out the cake -- no one envies anyone!), but this is not useful
- **Envy-freeness AND completeness**: Yes, such allocations exist, but the best known algorithm for $n$ agents has runtime $O(n^{n^{n^{n^{n^n}}}})$ -- astronomically high

---

## 6. The Robertson-Webb Query Model

To measure the complexity of cake-cutting algorithms, we use the **Robertson-Webb model**, which defines two types of atomic operations:

### 6.1 Evaluation Query
$$\text{Eval}_i(x, y) \quad \text{returns } v_i([x, y])$$
"How much does player $i$ value the piece $[x, y]$?"

### 6.2 Cut Query
$$\text{Cut}_i(x, \alpha) \quad \text{returns } y \text{ such that } v_i([x, y]) = \alpha$$
"Please cut a piece of cake starting at point $x$ that player $i$ values at exactly $\alpha$."

The **complexity** of a cake-cutting algorithm is measured by the total number of Eval and Cut queries it uses.

---

## 7. Algorithm 1: Cut-and-Choose (2 Players)

### 7.1 Procedure

1. Player 1 cuts the cake into two pieces $X_1$ and $X_2$ that they value equally: $v_1(X_1) = v_1(X_2) = 1/2$
2. Player 2 chooses the piece they prefer; Player 1 receives the other piece

### 7.2 Properties

**Claim**: The Cut-and-Choose allocation is **envy-free** (and hence also **proportional** for $n = 2$).

**Proof**:
- Player 1 cut the cake into two pieces they value equally, so they will not envy Player 2 regardless of which piece Player 2 chooses
- Player 2 chose the piece they value most, so they do not envy Player 1. $\square$

**Not necessarily equitable**: Consider a cake that is half chocolate, half sponge. Agent 1 likes chocolate only, Agent 2 likes everything.
- If Agent 1 cuts first: $A_1 = [0, 1/4], A_2 = [1/4, 1]$ giving utilities $1/2$ and $3/4$ (not equitable)
- If Agent 2 cuts first: $A_1 = [0, 1/2], A_2 = [1/2, 1]$ giving utilities $1$ and $1/2$ (not equitable)

**Complexity**: 2 operations under the Robertson-Webb model (1 Cut query + 1 Eval query).

---

## 8. Algorithm 2: Dubins-Spanier (Moving Knife) -- Proportionality for $n$ Players

### 8.1 Procedure

A "moving-knife" algorithm that ensures proportionality:

1. A referee moves a knife continuously across the cake from left to right
2. When any player finds the segment to the left of the knife worth at least $1/n$, they shout "Stop!". They receive that segment and are removed from the game. Ties are broken arbitrarily
3. The process repeats with the remaining players until one player is left, who receives the remainder

### 8.2 Proportionality Proof

**Theorem.** *The Dubins-Spanier allocation is proportional.*

**Proof.**
- Any player who shouted "Stop" received a piece worth at least $1/n$ to them -- they received their proportional share
- The last player did not shout "Stop" (or shouted simultaneously with another player), so they must have valued each of the previous $n - 1$ pieces at at most $1/n$. Hence the remaining piece is valued at at least $1 - (n-1)/n = 1/n$. $\square$

### 8.3 Limitations

**Not envy-free** for $n > 2$:

*Counterexample*: Cake is half chocolate $[0, 1/2]$, half sponge $[1/2, 1]$. Agent 1 likes everything; Agents 2 and 3 like sponge only.
- Agent 1 shouts "Stop!" at $1/3$ and gets $[0, 1/3]$
- Agents 2 and 3 both shout "Stop!" at $2/3$ (tie broken arbitrarily)
- Say Agent 2 gets $[1/3, 2/3]$ and Agent 3 gets $[2/3, 1]$
- **Agent 2 envies Agent 3**: Agent 3 gets more sponge than Agent 2

Also **not necessarily equitable** and **not necessarily Pareto-optimal**.

### 8.4 Complexity

**Theorem.** *Under the Robertson-Webb model, the Dubins-Spanier algorithm requires $\Theta(n^2)$ operations.*

**Proof.** At each iteration we remove one player. The number of queries is $n + (n-1) + \ldots + 2 = \Theta(n^2)$. $\square$

### 8.5 Worked Example (from LGT)

Cake $[0, 1]$ with three players:
- Player 1: values $[0, 0.6]$ with density $5/3$, zero elsewhere
- Player 2: values $[0.2, 0.9]$ with density $1/0.7$, zero elsewhere
- Player 3: values $[0.5, 1]$ with density $2$, zero elsewhere

Each $v_i([0, 1]) = 1$ (normalization satisfied).

**Round 1** (all 3 players, each wants value $1/3$):
- P1: $(5/3)x = 1/3 \Rightarrow x = 0.2$. **Mark at $x_1 = 0.2$**
- P2: $(1/0.7)(x - 0.2) = 1/3 \Rightarrow x \approx 0.433$. **Mark at $x_2 \approx 0.433$**
- P3: $2(x - 0.5) = 1/3 \Rightarrow x \approx 0.667$. **Mark at $x_3 \approx 0.667$**
- Leftmost mark is P1 at $0.2$, so P1 gets $[0, 0.2]$ and exits. Value to P1: $(5/3)(0.2) = 1/3$.

**Round 2** (players 2, 3 on $[0.2, 1]$, each wants $1/3$):
- P2 marks at $x_2 \approx 0.433$ (same calculation)
- P3 marks at $x_3 \approx 0.667$
- Leftmost is P2. P2 gets $[0.2, 0.433]$. Value to P2: $(0.233)/0.7 = 1/3$.

**Remaining**: P3 gets $[0.433, 1]$. Intersection with $[0.5, 1]$ is $[0.5, 1]$, length $0.5$, value $2 \times 0.5 = 1$.

**Result**: P1 gets $1/3$, P2 gets $1/3$, P3 gets $1$ -- **Proportional** (all $\geq 1/3$).

**Envy analysis**:
- P1 envies P2: P1 values P2's piece $[0.2, 0.433]$ at $(5/3)(0.233) \approx 0.388 > 1/3$. **P1 envies P2.**
- P2 envies P3: P2 values P3's piece -- intersection of $[0.433, 1]$ with $[0.2, 0.9]$ is $[0.433, 0.9]$, length $\approx 0.467$, value $\approx 0.467/0.7 \approx 2/3 > 1/3$. **P2 envies P3.**
- P3 does not envy anyone: P1's and P2's pieces do not intersect $[0.5, 1]$.

The allocation is **proportional but NOT envy-free**.

---

## 9. Algorithm 3: Even-Paz -- Optimal Proportionality for $n$ Players

### 9.1 Procedure (Divide and Conquer)

For ease of exposition, described for $n = 2^k$ players (extendable to any $n$):

1. Denote the remainder of the cake as $[s, t]$. Initially $s = 0, t = 1$
2. If $n = 1$: the player receives $[s, t]$
3. Each player $i$ makes a mark $z_i$ on the cake that divides $[s, t]$ into two pieces they value equally: $\text{Cut}_i(s, \frac{1}{2} v_i) = z_i$
4. Let $z^*$ be the $n/2$-th mark from the left (the median mark)
5. **Recurse**: The $n/2$ players who marked $z_i \leq z^*$ go to the left half $[s, z^*]$; the remaining $n/2$ players go to the right half $(z^*, t]$

### 9.2 Proportionality Proof

**Theorem.** *The Even-Paz allocation is proportional.*

**Proof by induction.** After $k$ steps, the players sharing a piece of cake value it at least $1/2^k$.

- **Base case** ($k = 0$): The piece is the whole cake, valued at $1$.
- **Inductive step**: If at step $k$ a player's shared piece $[x, y]$ is valued at least $1/2^k$, then at step $k+1$ they share a piece valued at least $v_i([x, y])/2 \geq 1/2^{k+1}$.
  - Why? Each player marks where they see half the value. The median cut ensures each player is assigned to the half they value at least as much as half of $[x, y]$.

The process ends after $\log n$ steps, giving each player a piece valued at least $1/2^{\log n} = 1/n$. $\square$

### 9.3 Complexity

**Theorem.** *The Even-Paz algorithm achieves proportionality in $O(n \log n)$ operations in the Robertson-Webb model.*

**Proof.** The recursion depth is $O(\log n)$ (we halve the number of players at each step). Each step requires $O(n)$ operations (one query per player). Total: $O(n \log n)$. $\square$

**Optimality.** It is known that any proportional cake-cutting algorithm requires $\Omega(n \log n)$ operations in the Robertson-Webb model. Hence, **Even-Paz is optimal**.

### 9.4 Worked Example (from LGT)

Same three players as before. Each marks where they see half the value of the cake:

- P1: $(5/3)x = 1/2 \Rightarrow x = 0.3$
- P2: $(1/0.7)(x - 0.2) = 1/2 \Rightarrow x = 0.55$
- P3: $2(x - 0.5) = 1/2 \Rightarrow x = 0.75$

Median of $\{0.3, 0.55, 0.75\}$ is $0.55$. Cut at $0.55$:
- **Left group** $L = \{P1, P2\}$ on $[0, 0.55]$
- **Right group** $R = \{P3\}$ on $[0.55, 1]$ (P3 alone gets this piece)

P3's value: intersection of $[0.55, 1]$ with $[0.5, 1]$ is $[0.55, 1]$, length $0.45$, value $2 \times 0.45 = 0.9 > 1/3$.

Now recursively divide $[0, 0.55]$ between P1 and P2 using cut-and-choose:
- P1 values up to $\min(0.55, 0.6) = 0.55$. Value of $[0, x]$ is $(5/3)x$. Total value of $[0, 0.55]$ for P1 is $(5/3)(0.55) \approx 0.917$. Half is $\approx 0.458$, so cut at $x = 0.275$
- Pieces: $[0, 0.275]$ and $[0.275, 0.55]$
- P2's valued region within $[0, 0.55]$ is $[0.2, 0.55]$
  - $[0, 0.275]$ contributes $[0.2, 0.275]$, length $0.075$, value $\approx 0.075/0.7 \approx 0.107$
  - $[0.275, 0.55]$ contributes $[0.275, 0.55]$, length $0.275$, value $\approx 0.275/0.7 \approx 0.393$
- P2 chooses $[0.275, 0.55]$ (higher value), P1 gets $[0, 0.275]$

---

## 10. Algorithm 4: Selfridge-Conway -- Envy-Freeness for 3 Players

### 10.1 Motivation

Envy-free cake cutting is algorithmically **much more challenging** than proportional cake cutting. The Selfridge-Conway algorithm guarantees envy-freeness for exactly **three players**.

### 10.2 Procedure (Three Stages)

**Stage 0 (Setup):**
1. Player 1 cuts the cake into **three pieces they value equally** (each worth $1/3$ to Player 1)
2. Player 2 **trims** the largest piece (in Player 2's view) so that the two largest pieces are now **equal** in Player 2's eyes
3. This creates **four pieces**: two equally-valued large pieces (one trimmed, one not), the remaining original piece, and the **trimming** (the strip cut off)
4. Let **Cake 2** = the trimming; **Cake 1** = the other three pieces

**Stage 1 (Divide Cake 1):**
1. Player 3 chooses their highest-valued piece from Cake 1
2. If Player 3 did NOT choose the trimmed piece, then Player 2 is allocated the trimmed piece. Otherwise (Player 3 chose the trimmed piece), Player 2 chooses their highest-valued piece from the remaining two
3. The remaining piece goes to Player 1

**Stage 2 (Divide Cake 2 -- the trimming):**
- Among Players 2 and 3, let $T$ = the player who received the trimmed piece, and $T'$ = the other player
1. Player $T'$ divides Cake 2 into **three pieces they value equally**
2. Players $T$, then Player 1, then Player $T'$ choose one piece each (in that order)

### 10.3 Envy-Freeness Proof

Since valuations are additive, we can show envy-freeness on Cake 1 and Cake 2 **separately**.

**Player $T'$:**
- On Cake 2: They divided it equally, so they are envy-free
- On Cake 1:
  - If $T' = $ Player 3: they chose their highest-valued piece from all three original pieces -- envy-free
  - If $T' = $ Player 2: they trimmed the two largest pieces to be equal, so they received one of the two largest pieces -- envy-free

**Player $T$:**
- On Cake 2: They choose their highest-valued piece first -- envy-free
- On Cake 1: Same argument as for Players 2 and 3 above -- envy-free

**Player 1:**
- On Cake 1: They did NOT receive the trimmed piece, so they received a piece worth exactly $1/3$ (since they cut the cake equally). Envy-free on Cake 1
- On Cake 2: Player 1 does not envy $T'$ because Player 1 chooses before $T'$. For Player $T$: notice that $T$ received the trimmed piece from Cake 1, which is worth **at most** $1/3$ to Player 1. Even if $T$ received ALL of Cake 2, their total would be at most $1/3$. Since Player 1 already has $1/3$ from Cake 1, Player 1 has an **irrevocable advantage** over $T$, so Player 1 does not envy $T$. $\square$

### 10.4 Key Properties

| Property | Selfridge-Conway |
|---|---|
| Envy-free | Yes (for 3 players) |
| Proportional | Yes (implied by EF) |
| Connected pieces | No (pieces may be disconnected) |

---

## 11. Complexity of Envy-Free Algorithms (General $n$)

### 11.1 Existence

**Theorem (Brams and Taylor, 1995).** *There exists an envy-free cake-cutting algorithm for any number of players under the Robertson-Webb model.*

However, by changing the valuation functions, the complexity of their algorithm can be made arbitrarily high -- it cannot be bounded as a function of $n$ alone.

### 11.2 Bounded Algorithms

**Theorem (Aziz and Mackenzie, 2016).** *A bounded envy-free algorithm exists for any $n$, but its complexity is extremely high: $O(n^{n^{n^{n^{n^n}}}})$.*

### 11.3 Lower Bound

**Theorem (Procaccia, 2009).** *Any envy-free cake-cutting algorithm requires $\Omega(n^2)$ operations in the Robertson-Webb model.*

There remains a **massive gap** between the upper bound $O(n^{n^{n^{n^{n^n}}}})$ and the lower bound $\Omega(n^2)$.

---

## 12. Strategyproofness

### 12.1 Definition

A cake-cutting algorithm is **strategyproof** if on every instance, no agent can improve their allocation by answering the algorithm's queries **non-truthfully** (i.e., by misrepresenting their valuation function).

### 12.2 Cut-and-Choose is NOT Strategyproof

Consider a cake: half chocolate, half vanilla.
- Agent 1 likes the entire cake uniformly
- Agent 2 likes vanilla only

If Agent 1 **knows** Agent 2 likes vanilla only, Agent 1 can cut the cake at $3/4 - \varepsilon$ instead of $1/2$. Agent 2 will choose the vanilla-heavy right piece, and Agent 1 gets more cake ($3/4 - \varepsilon$ instead of $1/2$).

### 12.3 Impossibility Results

**Theorem.** *There exists no strategyproof algorithm for 2 agents that is both Pareto-optimal and envy-free.*

**Theorem.** *For any $k$, one cannot find an allocation of the cake that maximises the sum of agents' utilities in the Robertson-Webb model using $k$ queries, even for $n = 2$.*

The other algorithms we have seen (Dubins-Spanier, Even-Paz, Selfridge-Conway) are also **not strategyproof**.

---

## 13. Complexity Summary Table

| Algorithm | Players | Guarantees | Complexity (Robertson-Webb) | Optimal? |
|---|---|---|---|---|
| **Cut-and-Choose** | $n = 2$ | Proportional + Envy-free | $O(1)$ (2 queries) | Yes (for 2 players) |
| **Dubins-Spanier** | $n \geq 2$ | Proportional | $\Theta(n^2)$ | No |
| **Even-Paz** | $n \geq 2$ | Proportional | $O(n \log n)$ | Yes (optimal for proportionality) |
| **Selfridge-Conway** | $n = 3$ | Envy-free | $O(1)$ (bounded, constant) | -- |
| **Aziz-Mackenzie** | any $n$ | Envy-free | $O(n^{n^{n^{n^{n^n}}}})$ | No (huge gap with $\Omega(n^2)$ lower bound) |

---

## 14. Tutorial Problems and Solutions

### 14.1 Problem 1: $1/3$-Envy-Freeness of a Moving Knife Variant

**Setup**: A variant of the moving knife where agents shout "Stop!" when the left piece is worth exactly $1/3$ (not $1/n$). Allocated piece goes to the shouter; if knife reaches the end, remaining cake goes to a remaining agent (with contiguity ensured).

**Prove**: The resulting allocation is $1/3$-envy-free, i.e., $v_i(A_i) \geq v_i(A_j) - 1/3$ for all $i, j$.

**Solution**:
- An agent who shouted "Stop!" values their piece at $1/3$ and hence the remaining cake at $2/3$. So any other agent's piece is worth at most $2/3$ to them. Their envy is at most $2/3 - 1/3 = 1/3$.
- An agent who never shouted (or lost a tie-break): they value every piece allocated to another agent at at most $1/3$ (they could have shouted before but did not, or the knife was moving over cake they value less). So their envy is bounded by $1/3 - 0 = 1/3$.
- **The bound is tight**: Four agents with uniform valuations. Three get pieces of length $1/3$, and the remaining agent (who lost all tie-breaks) receives nothing and values each other agent's piece at $1/3$.

### 14.2 Problem 2: Connected Allocations

**Question**: For two agents (Alice and Bob), is there always a connected allocation where Alice gets $\geq 0.6$ and Bob gets $\geq 0.4$?

**Answer**: **No.** Counterexample: Alice values $[0.1, 0.2]$ and $[0.8, 0.9]$ each at $0.5$. Bob values $[0.4, 0.6]$ at $1$. For Alice to get a connected interval worth $0.6$, it must contain points to the left of $0.4$ and to the right of $0.6$, so it necessarily includes all of Bob's valued region.

**Without connectivity constraint?** **Yes.** Create 3 copies of Alice and 2 copies of Bob (5 agents total), run any proportional protocol (e.g., Dubins-Spanier). Each copy gets $\geq 0.2$. Give Alice's copies' pieces to Alice ($\geq 0.6$) and Bob's copies' pieces to Bob ($\geq 0.4$). This works by additivity.

**With connectivity but flexible assignment (either agent can get 0.6)?** **Yes.** Move a knife from left to right. Ask both agents to shout "Stop!" when the left piece is worth exactly $0.6$ to them. Give the left piece to the agent who shouts first (they value it at $0.6$). The other agent values the left piece at $\leq 0.6$, hence the right piece at $\geq 0.4$.

### 14.3 Problem 3: Price of Proportionality

**Setup**: $n = k^2$ agents. For $i = 1, \ldots, k$, agent $i$'s valuation is uniform on $[(i-1)/k, i/k]$ and 0 elsewhere. All other $k^2 - k$ agents value the entire cake uniformly.

- **Maximum social welfare (unconstrained)**: Give each of the first $k$ agents their valuable interval (each gets utility $1$). Total utility $= k = \sqrt{n}$.
- **Maximum social welfare under proportionality**: Must give each of the $k^2 - k$ uniform agents an interval of length $\geq 1/k^2$ (so each gets utility $1/k^2$). This uses up $(k^2 - k)/k^2 = 1 - 1/k$ of the cake. Only $1/k$ remains for the $k$ specialized agents. Each specialized agent gets a $1/k$-fraction of their valuable interval, contributing utility $1/k$. Total $= (k^2 - k)/k^2 + k \cdot (1/k) = (1 - 1/k) + 1 = 2 - 1/k = 2 - 1/\sqrt{n}$.
- **Ratio**: The proportional allocation achieves only $O(1/\sqrt{n})$ of the socially optimal solution, showing that requiring proportionality can cause significant welfare loss.

---

## 15. Key Takeaways

1. **Fair division** is a fundamental problem in multi-agent systems, focusing on allocating resources while satisfying fairness criteria
2. **Cake cutting** models divisible goods as the unit interval $[0, 1]$ with additive, normalized, divisible valuation functions
3. The four main solution concepts are **proportionality**, **envy-freeness**, **equitability**, and **Pareto-optimality**
4. For two players, proportionality and envy-freeness are equivalent; for three or more, envy-freeness is strictly stronger
5. **Cut-and-Choose** gives envy-free allocations for 2 players in just 2 queries
6. **Dubins-Spanier** (moving knife) gives proportional allocations for $n$ players in $\Theta(n^2)$ queries but may fail envy-freeness
7. **Even-Paz** gives proportional allocations optimally in $O(n \log n)$ queries
8. **Selfridge-Conway** achieves envy-freeness for 3 players but produces disconnected pieces
9. Envy-free cake cutting for general $n$ is possible but **astronomically expensive** -- there is a massive gap between the $\Omega(n^2)$ lower bound and the $O(n^{n^{n^{n^{n^n}}}})$ upper bound
10. **No strategyproof algorithm** exists that is simultaneously Pareto-optimal and envy-free, even for 2 agents
