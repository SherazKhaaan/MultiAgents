# Week 4: Cooperative Game Theory

## Learning Objectives
By the end of this week, you should be able to:
- [ ] Explain the fundamental concepts of cooperative game theory, including coalitions, transferable utility, and the difference from non-cooperative settings.
- [ ] Model real-world scenarios as cooperative games, identifying possible coalitions and collective payoff structures.
- [ ] Analyse solution concepts such as the core, Shapley value, and bargaining set, including their properties and interpretation.
- [ ] Determine when stable and fair coalition structures exist, and evaluate conditions for allocations to be in the core.
- [ ] Apply cooperative game theory to problems in resource sharing, joint ventures, collaborative projects, and fair division.
- [ ] Calculate the Shapley value and other cooperative solution concepts using mathematical reasoning or algorithmic methods.
- [ ] Assess the fairness, efficiency, and stability of division outcomes in cooperative environments.
- [ ] Communicate insights about coalition formation, payoff allocation, and strategic collaboration in team-based or group settings.

---

## 1. Introduction to Cooperative Game Theory

### 1.1 Motivation: From Non-Cooperative to Cooperative Settings

In the standard Prisoner's Dilemma, mutual cooperation would make both players better off, yet it fails to arise because each player can unilaterally deviate and there is no way to enforce promises. The key missing ingredient is the ability to **commit credibly** to a joint course of action.

If players could write and enforce **binding contracts** specifying what each will do and how payoffs are shared, they could rule out the non-cooperative outcome and implement mutually beneficial agreements.

**Cooperative game theory** abstracts away from the strategic details of how agreements are reached and instead asks:
1. Which **coalitions** can form?
2. What total **value** can they generate?
3. How should this value be **divided** among participants under various fairness and stability concepts (e.g., the core, the Shapley value)?

### 1.2 Cooperative vs. Non-Cooperative Games

| Aspect | Non-Cooperative | Cooperative |
|---|---|---|
| **Focus** | Individual strategic interactions | Collective actions and agreements of groups |
| **Binding agreements** | Not possible | Feasible and enforceable |
| **Central question** | What will each agent do independently? | Which coalitions form, what value do they achieve, and how is it divided? |
| **Defection** | Always a concern | Eliminated by binding commitment |

The central premise is that agents often have incentives to pool efforts and resources: a merger may reduce costs, a joint venture may unlock new markets, or a coalition in a voting body may secure a legislative majority.

*Addresses LO1*

---

## 2. Transferable vs. Non-Transferable Utility

### 2.1 Transferable Utility (TU) Games

In **TU games**, a coalition first generates a total pot of payoff (joint profit or collective surplus), and then its members negotiate and agree on how to divide it among themselves.

This divisibility assumption is natural in **monetary contexts** where side payments are feasible:
- A firm sharing dividends
- Partners splitting revenue
- A coalition redistributing gains via cash transfers

**Example (Farmers' Cooperative)**: A group of farmers forms a cooperative to grow and sell fruit. The total profit is a single monetary amount that can be freely divided among members using side payments, bonuses, or share agreements.

### 2.2 Non-Transferable Utility (NTU) Games

In **NTU games**, individual payoffs are determined directly by the coalition's actions and **cannot be freely redistributed**.

**Example (Academic Collaboration)**: Researchers across universities form collaboration groups. Each author is rewarded by their home institution (promotion, salary bonuses, teaching load reductions). These rewards are institution-specific and non-transferable -- a researcher cannot convert their university's promotion offer into a cash payment to a collaborator at another institution.

### 2.3 Phases of a Coalitional Game

Coalitional games unfold in distinct phases:

1. **Coalition Formation Stage**: Agents decide which coalitions to form (partition of the player set into groups)
2. **Action Stage**: Each coalition independently chooses an action or strategy
3. **Value Generation** (TU games): Actions determine the total payoff each coalition generates
4. **Payoff Division** (TU games): Members negotiate and agree on a payoff division -- this is where questions of fairness, stability, and individual incentives become acute

In **NTU games**, the actions taken by all coalitions jointly determine each player's payoff directly with no further redistribution. In **TU games**, generating value and receiving utility are two different things -- the division stage is required.

*Addresses LO1, LO2*

---

## 3. Formal Definition of TU Games

### 3.1 Characteristic Function Games

A **transferable utility game** is a pair $(N, v)$, where:
- $N$ is a (finite) set of players
- $v: 2^N \to \mathbb{R}$ is the **characteristic function** that assigns to each coalition $C \subseteq N$ a real value $v(C)$

For each subset of players $C$, $v(C)$ is the amount that the members of $C$ can earn by working together (taking their best possible action).

**Standard assumptions**:
- **Normalized**: $v(\emptyset) = 0$
- **Non-negative**: $v(C) \geq 0$ for all $C \subseteq N$
- **Monotone**: If $S \subseteq T$, then $v(S) \leq v(T)$

A **coalition** is any subset of players. The set $N$ of all players is called the **grand coalition**.

### 3.2 Partition Function Games vs. Characteristic Function Games

| Type | Payoff depends on... | Example |
|---|---|---|
| **Partition Function Game (PFG)** | The coalition's own composition AND the partition of remaining players and their actions | Farmers' game (market prices respond to total supply from all coalitions) |
| **Characteristic Function Game (CFG)** | Only the coalition's own composition and choice (independent of outsiders) | Ice cream game |

Most classical cooperative game theory (including the core and Shapley value) was developed for **CFGs** because the simpler payoff structure makes analysis tractable. Extending to partition functions is an active research frontier.

### 3.3 The Ice Cream Game (Running Example)

**Setup**: Three children -- Charlie (4 pounds), Marcy (3 pounds), Patty (2 pounds). Three ice cream tubs: 1kg for 9 pounds, 750g for 7 pounds, 500g for 5 pounds. Children have utility for ice cream and do not care about money. The payoff of each group is the maximum quantity of ice cream they can buy by pooling their money.

**Characteristic function**:

| Coalition | Money | Can buy | $v(C)$ |
|---|---|---|---|
| $\emptyset$ | 0 | Nothing | 0 |
| $\{C\}$ | 4 | Nothing (cheapest is 5) | 0 |
| $\{M\}$ | 3 | Nothing | 0 |
| $\{P\}$ | 2 | Nothing | 0 |
| $\{C, P\}$ | 6 | 500g tub | 500 |
| $\{M, P\}$ | 5 | 500g tub | 500 |
| $\{C, M\}$ | 7 | 750g tub | 750 |
| $\{C, M, P\}$ | 9 | 1kg tub | 1000 |

### 3.4 Outcomes of a TU Game

An **outcome** of a TU game is a pair $(CS, \mathbf{x})$, where:
- $CS = \{C_1, C_2, \ldots, C_k\}$ is a **coalition structure** -- a partition of $N$ into disjoint coalitions whose union is $N$
- $\mathbf{x} = (x_1, x_2, \ldots, x_n)$ is a **payoff vector** such that:
  - $x_i \geq 0$ for each player $i$
  - For each coalition $C_j \in CS$: $\sum_{i \in C_j} x_i = v(C_j)$ (the coalition distributes exactly its value)

We write $x(C) = \sum_{i \in C} x_i$ for convenience.

**Ice cream game examples**:
- All singletons: $CS = \{\{C\}, \{M\}, \{P\}\}$, $\mathbf{x} = (0, 0, 0)$
- $CS = \{\{M, P\}, \{C\}\}$, $\mathbf{x} = (0, 150, 350)$
- Grand coalition: $CS = \{\{C, M, P\}\}$, $\mathbf{x} = (334, 333, 333)$
- Grand coalition (unfair): $CS = \{\{C, M, P\}\}$, $\mathbf{x} = (0, 800, 200)$

### 3.5 Imputations

An outcome $(CS, \mathbf{x})$ is called an **imputation** if it satisfies **individual rationality**:

$$x_i \geq v(\{i\}) \quad \text{for all } i \in N$$

Each agent receives at least as much as they would earn by forming a singleton coalition.

*Addresses LO1, LO2, LO7*

---

## 4. Examples of TU Games

### 4.1 Weighted Voting Games

A **weighted voting game** consists of:
- $N$ players, each with a weight $w_i$
- A **quota** $q$

The weight of a coalition is $w(C) = \sum_{i \in C} w_i$, and:

$$v(C) = \begin{cases} 1 & \text{if } w(C) \geq q \text{ (winning coalition)} \\ 0 & \text{if } w(C) < q \text{ (losing coalition)} \end{cases}$$

**Example (UK General Election 2010)**: 650 seats, quota = 326 (majority).
- Conservative: 306, Labour: 258, Lib Dem: 57, SNP: 6, DUP: 8, Others: 15
- $v(\{Con, Lab\}) = 1$ (564 seats), $v(\{Con, LD\}) = 1$ (363 seats)
- $v(\{Lab, LD\}) = 0$ (315 seats < 326)
- $v(\{Lab, LD, SNP, DUP\}) = 1$ (329 seats)

### 4.2 Network Flow Games

- **Network** $G = (V, E)$ with source $s$, sink $t$, and edge capacities $c_1, \ldots, c_{|E|}$
- **Players** are the edges
- $v(C)$ = maximum flow from $s$ to $t$ using only the edges in coalition $C$

### 4.3 Graph-Induced Games

- Players are **vertices** of a weighted graph
- $v(C)$ = total weight of edges internal to the subgraph induced by $C$
- Models social networks; edge weights can be **negative** (negative relationships)
- Example outcome: grand coalition where each player receives half the weight of their adjacent edges

*Addresses LO2, LO5*

---

## 5. Special Classes of TU Games

### 5.1 Simple Games

A game is **simple** if:
- $v(C) \in \{0, 1\}$ for all $C \subseteq N$
- The characteristic function is monotone

A coalition is **winning** if $v(C) = 1$ and **losing** if $v(C) = 0$. Weighted voting games with non-negative weights are simple games.

In simple games, due to monotonicity, we typically assume players form the **grand coalition** (unless specified otherwise).

**Key player types in simple games**:

| Type | Definition | Equivalent condition |
|---|---|---|
| **Null player** | $v(C \cup \{i\}) = v(C)$ for all $C$ | Adding player $i$ to any coalition does not change its value |
| **Veto player** | $v(C) = 0$ whenever $i \notin C$ | No coalition can win without player $i$ |

**UK Elections examples**:
- **2010**: No null players, no veto players
- **2017** (Con: 317): Conservative was not a veto player (others together could still win without them: $v(N \setminus \{Con\}) = 1$), but Conservative paired with any other party formed a winning coalition
- **2019** (Con: 365): Conservative alone was a winning coalition ($365 \geq 326$), making it a **veto player** and all other players **null players**

### 5.2 Superadditivity

A game is **superadditive** if two disjoint coalitions can always merge without losing money:

$$v(S \cup T) \geq v(S) + v(T) \quad \text{for all disjoint } S, T \subseteq N$$

**Implication**: Players always have incentives to merge, so we can assume they form the **grand coalition**. In superadditive games, outcomes can be identified with just the payoff vector $\mathbf{x}$ (no need to specify coalition structure).

**Example**: Network flow games are superadditive.

### 5.3 Convexity and Supermodularity

A function $f: 2^N \to \mathbb{R}$ is **supermodular** if:
- $f(\emptyset) = 0$
- For any $A, B \subseteq N$ (not necessarily disjoint): $f(A \cup B) + f(A \cap B) \geq f(A) + f(B)$

A TU game is **convex** if its characteristic function is supermodular.

**Key property of convex games**: A player is **more useful when joining a bigger coalition**. Formally, if $T \subseteq S$ and $i \notin S$, then:

$$v(T \cup \{i\}) - v(T) \leq v(S \cup \{i\}) - v(S)$$

*Proof*: Set $A = S$ and $B = T \cup \{i\}$, then $A \cup B = S \cup \{i\}$ and $A \cap B = T$. Apply supermodularity.

**Relationships**:
- Supermodular $\Rightarrow$ Superadditive (but not conversely)

**Properties of our example games**:

| Game | Superadditive? | Convex? |
|---|---|---|
| Ice cream game | Yes | No |
| Graph-induced game | Iff all edge weights $\geq 0$ | Iff all edge weights $\geq 0$ |
| Weighted voting game | Only if $q > \frac{w(N)}{2}$ | Not even when $q > \frac{w(N)}{2}$ |

**Counterexample for convexity of weighted voting**: Three players with $w_1 = w_2 = w_3 = 1$, $q = 2$. Let $A = \{1,2\}$, $B = \{2,3\}$. Then $v(A \cup B) + v(A \cap B) = v(\{1,2,3\}) + v(\{2\}) = 1 + 0 = 1$, but $v(A) + v(B) = 1 + 1 = 2$. Since $1 < 2$, this is not convex.

*Addresses LO1, LO2*

---

## 6. The Core

### 6.1 Stability vs. Fairness

Outcomes can be evaluated according to two sets of criteria:
1. **Stability**: What incentives do agents have to stay in the coalition structure? (No group should want to deviate.)
2. **Fairness**: How well does each agent's payoff reflect their contribution?

These give rise to two families of solution concepts.

### 6.2 Definition of the Core

The **core** $\mathcal{C}(G)$ of a characteristic function game $G = (N, v)$ is the set of all outcomes $(CS, \mathbf{x})$ such that:

$$x(C) \geq v(C) \quad \text{for all } C \subseteq N$$

where $x(C) = \sum_{i \in C} x_i$.

**Interpretation**: No coalition $C$ can deviate and do better on its own, because the members of $C$ already collectively receive at least $v(C)$ in the current outcome.

### 6.3 Core of the Ice Cream Game

For any outcome in the core, the coalition structure must be the **grand coalition** (because $v(\{C,M,P\}) = 1000$ exceeds the social welfare of any other partition).

The core constraints are:

$$x_C \geq 0, \quad x_M \geq 0, \quad x_P \geq 0$$
$$x_C + x_M + x_P = 1000$$
$$x_C + x_M \geq 750$$
$$x_C + x_P \geq 500$$
$$x_M + x_P \geq 500$$

**Some core outcomes**: $(400, 400, 200)$, $(500, 400, 100)$, $(500, 500, 0)$

**Non-core example**: $(350, 350, 300)$ is NOT in the core because $x_C + x_M = 700 < 750$, so Charlie and Marcy would deviate.

### 6.4 Stability Implies Efficiency

**Theorem**: If an outcome $(CS, \mathbf{x})$ is in the core of a CFG $G$, then $CS$ maximises social welfare (the total payoff to all players) over all possible coalition structures.

**Proof** (by contradiction): Suppose $CS$ is in the core but there exists $CS'$ with $\text{val}(CS') > \text{val}(CS)$. Then:
- $\sum_{C' \in CS'} x(C') = x(N) = \text{val}(CS) < \text{val}(CS') = \sum_{C' \in CS'} v(C')$
- But since $(CS, \mathbf{x})$ is in the core, $x(C') \geq v(C')$ for every $C' \in CS'$
- Summing over $CS'$: $\sum_{C' \in CS'} x(C') \geq \sum_{C' \in CS'} v(C')$

This is a contradiction. Therefore, core outcomes are always efficient.

### 6.5 Empty Cores

Unfortunately, **some games have empty cores** -- no stable outcome exists.

**Example (Three-player majority game)**: $w_1 = w_2 = w_3 = 1$, $q = 2$. Winning coalitions are any pair or the grand coalition ($v(C) = 1$ if $|C| \geq 2$, else $v(C) = 0$).

**Proof that the core is empty** (case analysis on coalition structures):

1. **Three singletons** $\{\{1\},\{2\},\{3\}\}$: All payoffs must be 0, but the grand coalition can deviate and win (getting value 1).
2. **A pair and a singleton**, e.g., $\{\{1,2\},\{3\}\}$: The pair's total payoff is 1, so one member (say player 1) gets $x_1 < 1$. Then $\{1,3\}$ or $\{2,3\}$ can deviate -- the disadvantaged player teams with player 3 to form a winning coalition and both get more.
3. **Grand coalition** $\{1,2,3\}$: Some player $i$ has $x_i > 0$ (since $x_1 + x_2 + x_3 = 1$). The coalition $N \setminus \{i\}$ has $x(N \setminus \{i\}) < 1 = v(N \setminus \{i\})$, so that pair can deviate.

In every case, some coalition has an incentive to deviate, so the core is empty.

*Addresses LO3, LO4, LO7*

---

## 7. The Shapley Value

### 7.1 Motivation: Fairness-Based Payoff Division

The core captures **stability**, but is it **fair**? For instance, $(500, 500, 0)$ is in the core of the ice cream game, but giving Patty nothing seems unfair.

The **Shapley value** is based on the intuition that each agent's payment should be proportional to their **contribution** to the coalitions they participate in.

### 7.2 Why Not Simple Marginal Contribution?

A naive approach: pay each player $i$ their marginal contribution to the grand coalition:

$$x_i = v(N) - v(N \setminus \{i\})$$

**Problem**: The total payoff $\sum_i x_i$ may not equal $v(N)$.

*Example*: In the three-player majority game, $v(N) - v(N \setminus \{i\}) = 1 - 1 = 0$ for each player, so $\sum_i x_i = 0 \neq 1 = v(N)$.

### 7.3 Why Not a Fixed Ordering?

Fix an ordering of agents and pay each agent their marginal contribution to the coalition of predecessors:
- Agent 1 gets $v(\{1\})$
- Agent 2 gets $v(\{1,2\}) - v(\{1\})$
- Agent $k$ gets $v(\{1,\ldots,k\}) - v(\{1,\ldots,k-1\})$

This is **efficient** (sums to $v(N)$), but **unfair**: symmetric players may receive very different payoffs depending on the ordering.

*Example*: In the three-player majority game with ordering $(1,2,3)$: agent 1 gets 0, agent 2 gets 1 (becomes a winning pair), agent 3 gets 0. But all three players are identical.

### 7.4 The Shapley Value: Averaging Over All Orderings

The solution: **average marginal contributions over all permutations**.

Let $\Pi(N)$ denote the set of all permutations of $N$. For a permutation $\pi$ and player $i$, let $S^{\pi}(i) = \{j \in N : \pi(j) < \pi(i)\}$ be the set of predecessors of $i$ in $\pi$.

The **marginal contribution** of player $i$ with respect to permutation $\pi$:

$$\Delta_i^{\pi}(v) = v(S^{\pi}(i) \cup \{i\}) - v(S^{\pi}(i))$$

The **Shapley value** of player $i$ in game $G = (N, v)$ with $|N| = n$:

$$\phi_i(v) = \frac{1}{n!} \sum_{\pi \in \Pi(N)} \Delta_i^{\pi}(v)$$

**Probabilistic interpretation**: If we choose a permutation uniformly at random, $\phi_i(v)$ is the **expected marginal contribution** of player $i$ to the coalition of their predecessors.

### 7.5 Computing the Shapley Value: Ice Cream Example (Patty)

| Permutation | Patty's predecessors | $\Delta_P^{\pi}$ |
|---|---|---|
| $(C, M, P)$ | $\{C, M\}$ | $v(\{C,M,P\}) - v(\{C,M\}) = 1000 - 750 = 250$ |
| $(M, C, P)$ | $\{M, C\}$ | $1000 - 750 = 250$ |
| $(C, P, M)$ | $\{C\}$ | $v(\{C,P\}) - v(\{C\}) = 500 - 0 = 500$ |
| $(M, P, C)$ | $\{M\}$ | $v(\{M,P\}) - v(\{M\}) = 500 - 0 = 500$ |
| $(P, C, M)$ | $\emptyset$ | $v(\{P\}) - v(\emptyset) = 0 - 0 = 0$ |
| $(P, M, C)$ | $\emptyset$ | $v(\{P\}) - v(\emptyset) = 0 - 0 = 0$ |

$$\phi_P = \frac{250 + 250 + 500 + 500 + 0 + 0}{6} = \frac{1500}{6} = 250$$

### 7.6 Properties of the Shapley Value

The Shapley value satisfies four desirable properties:

1. **Efficiency**: $\sum_{i \in N} \phi_i(v) = v(N)$. It distributes the full value of the grand coalition.

2. **Null (Dummy) Player**: If $v(C \cup \{i\}) = v(C)$ for all $C \subseteq N \setminus \{i\}$, then $\phi_i(v) = 0$. Players who contribute nothing to any coalition receive nothing.

3. **Symmetry**: If players $i$ and $j$ are symmetric (i.e., $v(C \cup \{i\}) = v(C \cup \{j\})$ for all $C \subseteq N \setminus \{i, j\}$), then $\phi_i(v) = \phi_j(v)$.

4. **Additivity**: If $G^+ = (N, v_1 + v_2)$ is the sum of games $G_1 = (N, v_1)$ and $G_2 = (N, v_2)$, then $\phi_i(v_1 + v_2) = \phi_i(v_1) + \phi_i(v_2)$.

**Uniqueness Theorem**: The Shapley value is the **only** payoff division scheme satisfying all four properties.

### 7.7 Using Properties to Simplify Computation

**Example**: Game with $n$ players where $v(N) = 1$ and $v(C) = 0$ for all $C \subsetneq N$.

**Method 1 (Direct)**: Player $i$'s marginal contribution is 1 only if $i$ is last in the permutation ($(n-1)!$ such permutations out of $n!$). So $\phi_i = \frac{(n-1)!}{n!} = \frac{1}{n}$.

**Method 2 (Using properties)**: All players are symmetric, so by symmetry they all get the same value. By efficiency, $n \cdot \phi_i = 1$, so $\phi_i = \frac{1}{n}$.

*Addresses LO3, LO5, LO6, LO7*

---

## 8. The Banzhaf Index

### 8.1 Definition

Like the Shapley value, the **Banzhaf index** measures agents' expected marginal contributions, but it averages over all **coalitions** rather than all **permutations**.

Given a CFG $G = (N, v)$ with $|N| = n$, the Banzhaf index of player $i$ is:

$$\beta_i(v) = \frac{1}{2^{n-1}} \sum_{C \subseteq N \setminus \{i\}} [v(C \cup \{i\}) - v(C)]$$

The sum is over all $2^{n-1}$ coalitions that do not contain player $i$.

### 8.2 Properties

The Banzhaf index satisfies **three** of the four Shapley value properties:
- **Null (Dummy) Player**: Yes
- **Symmetry**: Yes
- **Additivity**: Yes
- **Efficiency**: **No** -- the Banzhaf index does NOT necessarily distribute $v(N)$

### 8.3 Example: Banzhaf Index Computation

Game with $n$ players, $v(N) = 1$, $v(C) = 0$ for all $C \subsetneq N$.

For player $i$: the marginal contribution is 1 only when $C = N \setminus \{i\}$, and 0 for all other coalitions.

$$\beta_i = \frac{1}{2^{n-1}}$$

Sum over all players: $\sum_{i \in N} \beta_i = \frac{n}{2^{n-1}} \neq 1$ (for $n \geq 3$), confirming the lack of efficiency.

### 8.4 Normalized Banzhaf Index

To ensure efficiency, we can **normalize**:

$$\beta_i^* = \frac{\beta_i}{\sum_{j \in N} \beta_j} \cdot v(N)$$

However, normalization **breaks the additivity property** -- there is a fundamental trade-off.

### 8.5 Power Indices in Simple Games

In **simple games** ($v(C) \in \{0, 1\}$), both the Shapley value and Banzhaf index have a natural interpretation as **power indices** -- they measure the probability that a player can influence the outcome (i.e., is a **swing player** who turns a losing coalition into a winning one).

In this context, the Shapley value is called the **Shapley-Shubik power index**.

*Addresses LO3, LO6, LO7*

---

## 9. Summary and Comparison of Solution Concepts

### 9.1 Stability vs. Fairness

| Concept | Type | Key idea |
|---|---|---|
| **Core** | Stability | No coalition can do better by deviating |
| **Shapley value** | Fairness | Average marginal contribution over all orderings |
| **Banzhaf index** | Fairness | Average marginal contribution over all coalitions |

### 9.2 Core vs. Shapley Value

| Property | Core | Shapley Value |
|---|---|---|
| Always exists? | No (can be empty) | Yes (always unique) |
| Can contain multiple outcomes? | Yes (a set) | No (a single vector) |
| Guarantees stability? | Yes | Not necessarily |
| Guarantees fairness? | Not necessarily | Yes (by axioms) |
| Efficient? | Yes (when non-empty) | Yes (always) |

### 9.3 Shapley Value vs. Banzhaf Index

| Property | Shapley Value | Banzhaf Index |
|---|---|---|
| Averages over | Permutations ($n!$) | Coalitions ($2^{n-1}$) |
| Efficiency | Yes | No (unless normalized) |
| Null player | Yes | Yes |
| Symmetry | Yes | Yes |
| Additivity | Yes | Yes (but lost if normalized) |
| Uniqueness | Only scheme with all 4 properties | -- |

---

## 10. Key Takeaways

1. **Cooperative game theory** assumes binding agreements are possible, shifting focus from individual strategies to coalition formation and payoff division.
2. **TU games** allow free redistribution of value; **NTU games** do not.
3. The **characteristic function** $v(C)$ captures the best payoff a coalition can guarantee itself.
4. **Superadditive** games incentivise forming the grand coalition; **convex** games further ensure increasing marginal returns.
5. The **core** captures stable outcomes where no coalition wants to deviate, but may be **empty**.
6. Core outcomes are always **efficient** (maximise social welfare).
7. The **Shapley value** fairly allocates payoffs based on average marginal contributions and is the unique scheme satisfying efficiency, null player, symmetry, and additivity.
8. The **Banzhaf index** is an alternative fairness measure averaging over coalitions rather than permutations, but sacrifices efficiency.
