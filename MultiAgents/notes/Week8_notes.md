# Week 8: Fair Division (Part II) -- Indivisible Goods

## Learning Objectives

- [ ] Describe the indivisible goods allocation model, its components, and real-world applications
- [ ] Define and compare fairness notions: proportionality, envy-freeness, equitability, Pareto-optimality
- [ ] Explain why exact fairness (EF, proportionality) is generally infeasible for indivisible goods
- [ ] Define and apply relaxed fairness notions: PROP1 and EF1
- [ ] Prove that EF1 implies PROP1 for additive valuations
- [ ] Describe and apply the Round-Robin algorithm; prove it achieves EF1 for additive valuations
- [ ] Explain the Envy-Cycle Elimination (ECE) algorithm and prove it achieves EF1 for monotone valuations
- [ ] Define utilitarian, egalitarian, and Nash welfare; analyse their fairness and efficiency properties
- [ ] Define EFX and discuss its existence as an open problem
- [ ] Compute MMS guarantees and understand their limitations

---

## 8.1 Indivisible Items: Model and Applications

### The Problem

- One or more **indivisible items** to be divided (paintings, jewellery, house, car)
- $n$ agents who want these goods
- **Goal:** divide items among agents as **fairly** or **efficiently** as possible
- Finding an optimal allocation is a **combinatorial optimization problem** because items cannot be divided as fractions

### Real-World Applications

- Dividing **inheritance items** among heirs
- Allocating **tasks** among team members
- Assigning **dormitory rooms** to students
- Distributing **computing resources** in data centres

### Formal Model

An **indivisible goods allocation problem** involves:

- A set $G$ of $m$ **indivisible goods**
- A set of players $N = \{1, \ldots, n\}$
- **Valuations** $v_i : 2^G \to \mathbb{R}$ (or $\mathbb{Z}$ for computational purposes) for each player, where $v_i(\emptyset) = 0$

**Additive valuations:** Valuations are **additive** if for all $S \subseteq G$ and $i \in N$:

$$v_i(S) = \sum_{g \in S} v_i(g)$$

**Allocation:** A partition of the goods $A = (A_1, \ldots, A_n)$ where:
- $A_i \subseteq G$ is the **bundle** allocated to agent $i$
- $A_i \cap A_j = \emptyset$ for $i \neq j$ (bundles are disjoint)
- Allocation is **complete** if $\bigcup_{i \in N} A_i = G$
- Allocation is **partial** otherwise

---

## 8.2 Solution Concepts and Relaxations (PROP1 and EF1)

### Basic Solution Concepts

An allocation $A = (A_1, \ldots, A_n)$ is:

- **Proportional** if $v_i(A_i) \geq v_i(G)/n$ for all $i \in N$
- **Envy-free (EF)** if $v_i(A_i) \geq v_i(A_j)$ for all $i, j \in N$
- **Equitable** if $v_i(A_i) = v_j(A_j)$ for all $i, j \in N$
- **Pareto-optimal (PO)** if there is no other allocation $B = (B_1, \ldots, B_n)$ such that $v_i(B_i) \geq v_i(A_i)$ for all $i \in N$ **and** $v_i(B_i) > v_i(A_i)$ for some $i \in N$

### The Core Challenge

- With indivisible goods, **envy-freeness and proportionality are generally infeasible**
- Unlike divisible settings (cake cutting), we cannot simply divide each good
- **Counterexample:** 2 agents, 1 item, both assign positive value -- no proportional, envy-free, or equitable allocation exists

### Relaxations: PROP1 and EF1

**Definition (PROP1):** An allocation $A = (A_1, \ldots, A_n)$ is **proportional up to 1 good (PROP1)** if for each agent $i$ there is an item $g \in G$ such that:

$$v_i(A_i \cup \{g\}) \geq v_i(G)/n$$

*Intuition:* Each agent could reach their proportional $1/n$-th share by adding at most one extra good to their bundle.

**Definition (EF1):** An allocation $A = (A_1, \ldots, A_n)$ is **envy-free up to 1 good (EF1)** if for each pair of agents $i, j$ there is an item $g \in A_j$ such that:

$$v_i(A_i) \geq v_i(A_j \setminus \{g\})$$

*Intuition:* Any envy an agent has toward another can be eliminated by removing at most one good from the envied agent's bundle.

**Example:** 2 agents, 1 house. Giving the house to one agent is both PROP1 and EF1.

### PROP1 vs. EF1

**Does EF1 + completeness imply PROP1?**

- **NO for general valuations.** Counterexample: $n > 2$ items, $n$ agents, $v_i(G) = 1$, $v_i(T) = 0$ for all $T \neq G$. Giving each agent one item is EF (hence EF1) and complete, but **not** PROP1 because adding one item to any bundle still gives value 0, while proportionality requires $1/n$.

- **YES for additive valuations.** Proof:
  1. Suppose $A = (A_1, \ldots, A_n)$ is EF1 and complete
  2. Consider agent $i$; let $g^*$ be their most valuable item in $G \setminus A_i$
  3. By EF1, for every other agent $j$: $v_i(A_i) \geq v_i(A_j \setminus \{g\}) = v_i(A_j) - v_i(g)$ for some $g \in A_j$
  4. Since $v_i(g) \leq v_i(g^*)$, we get $v_i(A_i) + v_i(g^*) \geq v_i(A_j)$
  5. By additivity: $v_i(A_i \cup \{g^*\}) = v_i(A_i) + v_i(g^*) \geq v_i(A_j)$
  6. Multiplying by $n$: $n \times v_i(A_i \cup \{g^*\}) \geq \sum_{j \in N} v_i(A_j) = v_i(G)$, so PROP1 holds. $\square$

---

## 8.3 Round-Robin Algorithm for Additive Valuations

### The Algorithm

**Round-Robin (RR):**
- Agents take turns choosing their **most preferred item** among the remaining items
- Agent $i$ chooses in rounds $i, n+i, 2n+i, \ldots$

### Worked Example (from slides)

|       | $g_1$ | $g_2$ | $g_3$ | $g_4$ | $g_5$ |
|-------|-------|-------|-------|-------|-------|
| $a_1$ | 20    | **50**| 12    | **45**| 3     |
| $a_2$ | 35    | 22    | **90**| 40    | **4** |
| $a_3$ | **30**| 80    | 7     | 18    | 25    |

Order: $a_1 \to a_2 \to a_3$

- Round 1: $a_1$ picks $g_2$ (value 50), $a_2$ picks $g_3$ (value 90), $a_3$ picks $g_1$ (value 30)
- Round 2: $a_1$ picks $g_4$ (value 45), $a_2$ picks $g_5$ (value 4)

Result: $A_1 = \{g_2, g_4\}$, $A_2 = \{g_3, g_5\}$, $A_3 = \{g_1\}$

### Worked Example (from LGT notes)

|       | A  | B  | C  | D  |
|-------|----|----|----|----|
| $v_1$ | 9  | 5  | 4  | 1  |
| $v_2$ | 6  | 7  | 5  | 2  |
| $v_3$ | 3  | 2  | 8  | 10 |

RR order: $1 \to 2 \to 3 \to 1$

- $a_1$ picks A (value 9), $a_2$ picks B (value 7), $a_3$ picks D (value 10)
- $a_1$ picks C (value 4)

Result: $A_1 = \{A, C\}$ ($v_1 = 13$), $A_2 = \{B\}$ ($v_2 = 7$), $A_3 = \{D\}$ ($v_3 = 10$)

### Theorem: Round-Robin Outputs EF1 (and hence PROP1) for Additive Valuations

**Proof:**
- Consider agents $i$ and $j$ with $i < j$ (i.e., $i$ goes before $j$):
  - $i$'s first item is no worse to $i$ than $j$'s first item (since $i$ picked first)
  - $i$'s second item is no worse to $i$ than $j$'s second item (same reasoning)
  - $\ldots$ and so on
  - Therefore, **$i$ does not envy $j$**
- If $j < i$ (i.e., $j$ goes before $i$), remove $i$'s first item:
  - $j$'s first item is no worse to $j$ than $i$'s second item
  - $j$'s second item is no worse to $j$ than $i$'s third item
  - $\ldots$ so **$j$ does not envy $i$ after removing $i$'s first item**
- Since valuations are additive, these per-round claims extend across rounds. $\square$

### Limitations of Round-Robin

**Not Pareto-optimal**, even for additive valuations:

| Item | Agent 1 | Agent 2 |
|------|---------|---------|
| 1    | 10      | 100     |
| 2    | 9       | 3       |
| 3    | 8       | 2       |
| 4    | 7       | 1       |

- RR gives: items 1, 3 to agent 1 (utility 18); items 2, 4 to agent 2 (utility 4)
- **Improving trade:** agent 1 exchanges item 1 for items 2 and 4 -- agent 1 gets utility 16 (items 2,3,4 = 9+8+7=24... actually agent 1 gets items 2,4 value 16, agent 2 gets item 1 value 100). Both improve.

**Not strategyproof**, even for additive valuations:

| Item | Agent 1 | Agent 2 |
|------|---------|---------|
| 1    | 9       | 1       |
| 2    | 8       | 9       |
| 3    | 2       | 2       |
| 4    | 1       | 3       |

- Truthful RR: agent 1 gets items 1, 3 (utility 11); agent 2 gets items 2, 4
- If agent 1 **picks item 2 first** (misreporting preferences): agent 2 takes item 4, then agent 1 takes item 1. Agent 1 gets items 1, 2 (utility **17** vs. 11)

---

## 8.4 Envy-Cycle Elimination Algorithm for Monotone Valuations

### Motivation

- Round-robin is **not even defined** for non-additive valuations (it relies on evaluating individual items)
- Can we achieve EF1 for **monotone** valuations?

**Monotone valuations:** For all $S \subseteq T \subseteq G$ and every agent $i$:

$$v_i(S) \leq v_i(T)$$

### Key Idea: Extending a Partial EF1 Allocation

- If there is an agent $i$ whom **nobody envies**, we can safely give $i$ an unallocated item and **preserve EF1** (by monotonicity)
- **Problem:** What if every agent is envied by someone?

### The Envy Graph

- **Vertices:** agents
- **Directed edge** from $i$ to $j$ if $i$ envies $j$ (i.e., $v_i(A_i) < v_i(A_j)$)
- Can be constructed in polynomial time

### Worked Example (Envy Graph)

|       | $g_1$ | $g_2$ | $g_3$ | $g_4$ | $g_5$ |
|-------|-------|-------|-------|-------|-------|
| $a_1$ | **20**| 50    | 12    | 45    | **3** |
| $a_2$ | 25    | **22**| **10**| 40    | 4     |
| $a_3$ | 30    | 10    | 7     | **18**| 25    |

Allocation: $A_1 = \{g_1, g_5\}$, $A_2 = \{g_2, g_3\}$, $A_3 = \{g_4\}$

- $a_1$ envies $a_2$ (has the valuable $g_2$)
- $a_2$ envies $a_3$ (has valuable $g_4$)
- $a_3$ envies $a_1$ (has a bundle $a_3$ values highly)
- This forms an **envy cycle**: $a_1 \to a_2 \to a_3 \to a_1$
- The allocation is EF1 (removing one item from each envied bundle eliminates envy)

### Reallocation Along a Cycle (RAC)

If the envy graph contains a cycle $i \to j \to k \to \ldots \to t \to i$:

- Give $A_j$ to $i$, $A_k$ to $j$, ..., $A_i$ to $t$
- **The set of bundles does not change**, so the allocation remains EF1
- Each agent on the cycle receives a **strictly more preferred bundle**
- The cycle is **eliminated** (at least one envy edge is removed)

**Why EF1 is preserved after RAC:** If $i$ now envies $j$ by more than one item, then before RAC $i$ envied the previous holder of $j$'s current bundle at least as much -- contradicting EF1.

### Bounding the Number of RAC Steps

- RAC only **reallocates** bundles but does not change them
- Let all agents rank the $n$ bundles; define **score** of agent for a bundle = $n$ - rank
- **Score of an allocation** = sum of agents' scores for their own bundles
- An RAC step:
  - Makes all agents on the cycle **strictly happier** (higher-ranked bundle)
  - Does not affect other agents' allocations
  - Therefore **strictly increases** the total score
- Total score ranges from $0$ to $n(n-1)$
- **At most $n(n-1)$ consecutive RAC steps** before termination

### The ECE Algorithm

1. Start with an **empty allocation** $A$ (which is trivially EF1)
2. Repeat until all items are allocated:
   - If there is an **unenvied agent**, allocate them an unallocated item ($A$ remains EF1)
   - Otherwise, there must be an **envy cycle** -- perform an RAC step ($A$ remains EF1)
3. If no RAC step can be performed, there is no cycle, hence there is an unenvied agent

**Correctness:** The dichotomy -- either a cycle exists or there is an unenvied agent.

**Polynomial runtime:**
- $m$ item allocation steps
- $\leq n(n-1)$ RAC steps between any two allocation steps
- Total: $O(m \cdot n^2)$ steps

### ECE Is Also Not Pareto-Optimal

Even with additive valuations:

| Item | Agent 1 | Agent 2 |
|------|---------|---------|
| 1    | 100     | 0       |
| 2    | 0       | 100     |
| 3    | 1       | 5       |
| 4    | 5       | 1       |

ECE allocates: item 1 to agent 1, item 2 to agent 2, item 3 to agent 1, item 4 to agent 2.

**Improving trade:** swap items 3 and 4 -- both agents strictly improve.

### ECE Worked Example (from LGT notes)

Using the same table as the RR example:

|       | A  | B  | C  | D  |
|-------|----|----|----|----|
| $v_1$ | 9  | 5  | 4  | 1  |
| $v_2$ | 6  | 7  | 5  | 2  |
| $v_3$ | 3  | 2  | 8  | 10 |

ECE order of item allocation: $D \to C \to B \to A$

Step 1: All agents unenvied (empty bundles). Give $D$ to $a_1$: $A_1 = \{D\}$, $A_2 = \emptyset$, $A_3 = \emptyset$

Step 2: $a_1$ is unenvied. Give $C$ to... Actually let's trace as in the notes: give items one by one, checking envy graph.

After some steps: $A_1 = \{D\}$, $A_2 = \{C\}$, $A_3 = \{B\}$. Envy cycle between $a_2$ and $a_3$ (2 envies 3 for item B? No -- $a_2$ values $\{C\}$ at 5, $\{B\}$ at 7, so $a_2$ envies $a_3$. $a_3$ values $\{B\}$ at 2, $\{C\}$ at 8, so $a_3$ envies $a_2$.) RAC: swap bundles of $a_2$ and $a_3$: $A_2 = \{B\}$, $A_3 = \{C\}$. Now unenvied agent exists; give $A$ to them.

Final: $A_1 = \{A, C\}$, $A_2 = \{B\}$, $A_3 = \{D\}$ (same as RR in this case).

---

## 8.5 Concepts of Welfare

### Fairness vs. Efficiency Summary

- **EF:** Does not always exist for indivisible goods
- **EF1:** Always exists for additive (Round-Robin) and monotone (ECE) valuations
- **EF1 + PO** cannot be simultaneously guaranteed in the general case

### Three Welfare Concepts

**Utilitarian welfare:** Sum of utilities

$$UW(A) = \sum_{i \in N} v_i(A_i)$$

**Egalitarian welfare:** Minimum utility

$$EW(A) = \min_{i \in N} v_i(A_i)$$

**Nash welfare:** Product of utilities

$$NW(A) = \prod_{i \in N} v_i(A_i)$$

### Worked Example

|       | $g_1$ | $g_2$ | $g_3$ | $g_4$ | $g_5$ |
|-------|-------|-------|-------|-------|-------|
| $a_1$ | 10    | 10    | 10    | 10    | 10    |
| $a_2$ | 1     | 1     | 1     | 1     | 1     |
| $a_3$ | 3     | 3     | 3     | 3     | 3     |

- **Max Utilitarian welfare:** Give all 5 items to $a_1$ $\Rightarrow UW = 50$. Highly unfair.
- **Max Egalitarian welfare:** Give 3 items to $a_2$, 1 to $a_1$, 1 to $a_3$ $\Rightarrow EW = 3$
- **Max Nash welfare:** 2 agents get 2 items each, 1 gets 1 item $\Rightarrow NW = 120$

### Worked Example (from LGT notes)

|       | A  | B  | C  | D  |
|-------|----|----|----|----|
| $v_1$ | 9  | 5  | 4  | 1  |
| $v_2$ | 6  | 7  | 5  | 2  |
| $v_3$ | 3  | 2  | 8  | 10 |

**Max Utilitarian welfare:** Allocate each item to the agent who values it most: $A_1 = \{A\}$ (9), $A_2 = \{B\}$ (7), $A_3 = \{C, D\}$ (18). $\sum = 34$.

**Max Egalitarian welfare:** $A_1 = \{A\}$ (9), $A_2 = \{B, C\}$ (12), $A_3 = \{D\}$ (10). $\min = 9$.

**Max Nash welfare:** $A_1 = \{A\}$ (9), $A_2 = \{B\}$ (7), $A_3 = \{C, D\}$ (18). $\prod = 9 \times 7 \times 18 = 1134$.

### Properties of Welfare Maximisers

| Welfare Maximiser | Pareto-Optimal? | EF1? |
|-------------------|----------------|------|
| **Utilitarian**   | Always PO      | May be highly unfair (not EF1) |
| **Egalitarian**   | Not necessarily PO | Not necessarily EF1 |
| **Nash**          | Always PO      | Always EF1 (for additive valuations) |

**Utilitarian welfare maximiser is PO:** Any Pareto improvement would increase the sum, contradicting maximality.

**Egalitarian welfare maximiser is NOT necessarily PO:** Example: 2 agents, 3 items {A, B, C}. Agent 1 values A, B at $x$, C at 0. Agent 2 values A, C at $x$, B at 0. Egalitarian max: $A_1 = \{A\}$, $A_2 = \{B, C\}$ gives $EW = x$. But reallocating C from agent 2 to agent 1 strictly improves agent 1 without hurting agent 2.

**Nash welfare maximiser gives both PO and EF1** (for additive valuations):
- PO: Same argument as utilitarian (any Pareto improvement increases the product)
- EF1: Proof is non-trivial (beyond course scope)

---

## 8.6 Envy-Freeness up to Any Good (EFX)

### Definition

An allocation $A = (A_1, \ldots, A_n)$ is **envy-free up to any good (EFX)** if for each pair of agents $i, j \in N$ and **for each** item $g \in A_j$:

$$v_i(A_i) \geq v_i(A_j \setminus \{g\})$$

### EF1 vs. EFX vs. EF

$$\text{EF} \implies \text{EFX} \implies \text{EF1}$$

- **EF1:** There **exists** some item $g \in A_j$ whose removal eliminates envy
- **EFX:** Removing **any** item $g \in A_j$ eliminates envy
- **EF:** No envy exists at all (no removal needed)

EFX is **strictly stronger** than EF1 and **strictly weaker** than EF.

### Existence of EFX (Open Problem)

| Setting | EFX Exists? |
|---------|------------|
| 2 agents, monotone valuations | **Yes** |
| 3 agents, additive valuations | **Yes** |
| $n \geq 4$ agents, additive valuations | **Open problem** |
| Identical additive valuations (any $n$) | **Yes** |

This is currently **one of the most intriguing open problems** in fair division.

### EFX for Identical Additive Valuations

**Theorem:** EFX allocations are guaranteed to exist (and can be found in polynomial time) if all agents have **identical additive valuations**.

**Algorithm:**
1. Sort items by **decreasing value**
2. Allocate one by one, giving each item to the **currently least satisfied** agent

**Proof of EFX:**
- Suppose at the end agent $i$ envies agent $j$
- Let $g$ be the **last item** received by $j$ (this is $j$'s smallest item)
- When $j$ received $g$, agent $i$ was **at least as satisfied** as agent $j$
- Therefore $i$'s bundle dominates $j$'s bundle even without item $g$
- Hence $v_i(A_i) \geq v_i(A_j \setminus \{g\})$ for any $g \in A_j$ (since $g$ is the smallest). $\square$

---

## Exercises and Solutions (SGT8)

### Exercise 1: Nash Welfare Invariance Under Scaling

**Problem:** Let $(A_1, \ldots, A_n)$ maximise Nash welfare. Modify agent $i$'s valuation by $v'_i(g) = 10 \cdot v_i(g)$. Why does $(A_1, \ldots, A_n)$ still maximise Nash welfare?

**Solution:** For any allocation $(B_1, \ldots, B_n)$, scaling agent $i$'s valuation multiplies the Nash welfare by exactly 10 (by additivity). Since **all** allocations' Nash welfare is scaled by the same factor, the maximiser does not change. $\square$

### Exercise 2: MMS Allocation When $|G| \leq |N| + 1$

**Problem:** Show that an MMS allocation always exists when $|G| \leq n + 1$ and valuations are additive.

**Solution:**
- If $|G| < n$: every partition has an empty bundle, so each agent's MMS = 0. Any allocation works.
- If $|G| = n$: MMS = value of least valuable item. Any allocation giving each agent one item is MMS.
- If $|G| = n + 1$: Agent $i$ ranking items $g_1 > \cdots > g_{n+1}$ has MMS $= \min\{v_i(g_{n-1}), v_i(g_n) + v_i(g_{n+1})\} \leq v_i(g_{n-1})$. Let $n-1$ agents sequentially pick their favourite remaining item (each gets an item not in the bottom 2, so $\geq$ MMS). The last agent gets the remaining 2 items $\geq v_i(g_n) + v_i(g_{n+1}) \geq$ MMS. $\square$

### Exercise 3: Round-Robin Guarantees $\frac{2}{3}$ MMS

**Problem:** All agents have additive valuations, $v_i(G) = 1$, each item worth $\leq 1/(3n)$. Show RR guarantees $\geq 2/3$ of MMS.

**Solution:** RR outputs EF1. For agent $i$ and each $j \neq i$: $v_i(A_i) \geq v_i(A_j) - 1/(3n)$. Summing over all $j$:

$$n \cdot v_i(A_i) \geq \sum_{j=1}^{n} v_i(A_j) - \frac{n}{3n} = v_i(G) - \frac{1}{3} = \frac{2}{3}$$

So $v_i(A_i) \geq \frac{2}{3n}$, while each agent's MMS $\leq 1/n$. Thus $v_i(A_i) \geq \frac{2}{3} \cdot \text{MMS}_i$. $\square$

---

## Additional Concepts from LGT Notes

### Maximin Share (MMS) Guarantee

The **maximin share (MMS)** guarantee of player $i$ is:

$$\text{MMS}_i = \max_{(X_1, \ldots, X_n)} \min_j v_i(X_j)$$

**Intuition:** "What's the best I could do if I had to divide items into $n$ piles, knowing I'll get the least valuable pile?" (You cut, adversary chooses.)

An **MMS allocation** ensures $v_i(A_i) \geq \text{MMS}_i$ for all $i \in N$.

**Existence:**
- For $n = 2$: MMS allocation **always exists**
- For $n \geq 3$: there exist additive valuation functions that do **not** admit an MMS allocation (counterexample is non-trivial; took ~4 years to find for 3 agents)
- In practice, MMS guarantee is usually feasible
- Later work showed: can always find allocations giving each player $\geq 3/4$ of their MMS

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Indivisible goods** | Items that cannot be split; must be allocated whole to one agent |
| **Additive valuations** | $v_i(S) = \sum_{g \in S} v_i(g)$ for all $S \subseteq G$ |
| **Monotone valuations** | $S \subseteq T \implies v_i(S) \leq v_i(T)$ |
| **Proportional** | $v_i(A_i) \geq v_i(G)/n$ for all $i$ |
| **Envy-free (EF)** | $v_i(A_i) \geq v_i(A_j)$ for all $i, j$ |
| **Equitable** | $v_i(A_i) = v_j(A_j)$ for all $i, j$ |
| **Pareto-optimal** | No other allocation makes someone strictly better off without making anyone worse off |
| **PROP1** | Adding one item to $A_i$ makes it proportional |
| **EF1** | Removing one item from $A_j$ eliminates $i$'s envy of $j$ |
| **EFX** | Removing **any** item from $A_j$ eliminates $i$'s envy of $j$ |
| **Utilitarian welfare** | $UW(A) = \sum_{i \in N} v_i(A_i)$ |
| **Egalitarian welfare** | $EW(A) = \min_{i \in N} v_i(A_i)$ |
| **Nash welfare** | $NW(A) = \prod_{i \in N} v_i(A_i)$ |
| **MMS** | $\max_{(X_1,\ldots,X_n)} \min_j v_i(X_j)$ -- best guarantee under adversarial choice |
| **Envy graph** | Directed graph: edge $i \to j$ if $i$ envies $j$ |
| **RAC** | Reallocation along a cycle in the envy graph |
| **Round-Robin** | Agents take turns picking favourite remaining item |
| **ECE** | Envy-Cycle Elimination: iteratively allocate to unenvied agents + RAC steps |

---

## Summary

- **Indivisible goods allocation** is a combinatorial problem where exact fairness (EF, proportionality) is generally **impossible**
- **EF1** is achievable: via **Round-Robin** (additive valuations) or **Envy-Cycle Elimination** (monotone valuations), both in polynomial time
- For additive valuations: EF1 + completeness $\implies$ PROP1
- Neither RR nor ECE guarantees **Pareto-optimality** or **strategyproofness**
- **Utilitarian welfare** maximiser is always PO but can be unfair; **Egalitarian welfare** maximiser is neither PO nor EF1; **Nash welfare** maximiser achieves **both PO and EF1** for additive valuations
- **EFX** (removing **any** item eliminates envy) is strictly stronger than EF1; its existence for $n \geq 4$ agents with additive valuations is a **major open problem**
- **MMS guarantee** (maximin share) does not always exist for $n \geq 3$, but $3/4$-approximations are always achievable
