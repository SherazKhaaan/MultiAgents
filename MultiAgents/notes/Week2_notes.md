# Week 2: Non-Cooperative Games (Part II) — Congestion Games, Potential Games, and Price of Anarchy

## Learning Objectives
By the end of this week, you should be able to:
- [ ] Define congestion games and network congestion (routing) games formally
- [ ] Identify real-world applications of congestion games across diverse domains
- [ ] Explain and apply best response dynamics to find pure strategy Nash equilibria
- [ ] Define potential games and Rosenthal's potential function, and prove convergence of best response dynamics
- [ ] Distinguish between exact, ordinal, and generalized ordinal potential games
- [ ] Identify whether a given game is a potential game using the guess-and-check or cycle-based approaches
- [ ] Define and compute the Price of Anarchy (PoA) and Price of Stability (PoS)
- [ ] Analyse the efficiency of equilibria in congestion games, including bounds for linear congestion games
- [ ] Explain Braess's Paradox and its implications

---

## 1. Motivation: Large Games and Concise Representations

To represent an $n$-player game where each player has $k$ actions, we need $k^n$ numbers just to encode the utility functions. For even moderately large $k$ and $n$, nobody could oversee, let alone play rationally in such a game.

Hence, we study games with substantially more structure despite being large — games with a **concise description** that makes them easy to reason about. **Congestion games** are a prime example.

---

## 2. Congestion Games

### 2.1 Formal Definition

A **congestion game** is defined by:
- A set of $n$ players $N$
- A set of $m$ **facilities** (or **resources**) $R$
- For each player $i$, a set of actions $A_i$ where each action $a_i \in A_i$ represents a **subset** of the facilities: $a_i \subseteq R$
- For each facility $j \in R$, a **cost (or delay) function** $d_j : \{0, \ldots, n\} \to \mathbb{R}_{\geq 0}$ where $d_j(k)$ is the cost of facility $j$ when $k$ players are using it

### 2.2 Player Costs

For action profile $a = (a_1, \ldots, a_n)$, define $n_j(a) = |\{i : j \in a_i\}|$ to be the number of players using facility $j$.

The **cost of agent $i$** is:
$$c_i(a) = \sum_{j \in a_i} d_j(n_j(a))$$

**Key property**: Each player's cost depends only on the **congestion** (number of users) on each resource they use, not on the identities of the other users.

### 2.3 Network Congestion (Routing) Games

In a **network congestion game** (aka **routing game**):
- There is a graph $G = (V, E)$
- The resource set $R$ corresponds to the set of edges $E$
- For each player $i \in N$, there is a dedicated source-target pair $(s_i, t_i)$ such that $A_i$ is the set of paths from $s_i$ to $t_i$

### 2.4 Worked Example: Three-Player Routing Game

A directed graph with edges labeled $(c_1, c_2, c_3)$ indicating cost when 1, 2, or 3 players use that edge.

- $N = \{1, 2, 3\}$, each traveling from $s$ to $t$
- Edge $s_2 t_2$ has identity cost function: $d(x) = x$
- Other edges have constant cost functions

**State A** (Player 1 uses direct link $s_1 \to t_1$):
- Player 1 cost: 4 (alone on direct link)
- Players 2, 3 cost: 2 each (two users on $s_2 t_2$)
- Social cost: $4 + 2 + 2 = 8$

**State B** (Player 1 routes through $s_2 t_2$):
- All three players on $s_2 t_2$: cost 3 each
- Social cost: $3 + 3 + 3 = 9$

Player 1 prefers State B (cost 3 < 4), so **State B is the Nash equilibrium** despite having higher social cost. State A is the **social optimum**.

*Addresses LO1*

---

## 3. Applications of Congestion Games

### 3.1 Traffic Routing and Transportation Networks
Drivers/vehicles choose routes, each aiming to minimise travel time. Classic use-case: analysis of road traffic, navigation apps, and highway network design.

### 3.2 Telecommunication and Communication Networks
Data packets select routes or channels; performance (latency, bandwidth) decreases with congestion. Applications: TCP/IP routing, spectrum allocation, load balancing in cellular networks.

### 3.3 Cloud and Distributed Computing
Tasks/jobs compete for computational resources (CPUs, memory, bandwidth). Congestion games capture resource sharing and system efficiency.

### 3.4 Multi-Agent Systems and Robotics
Multiple robots/agents sharing physical infrastructure (warehouse aisles, sensor networks) use congestion games to coordinate movement and avoid bottlenecks.

### 3.5 Electricity Grids and Smart Energy Systems
Consumers/smart devices choose when to use electricity; costs rise with collective demand. Congestion games help analyse demand response and peak shifting.

### 3.6 IoT and Sensor Networks
Devices compete for transmission time, battery usage, or shared sensors. Congestion games inform protocol design for fairness and efficiency.

### 3.7 Other Applications
- **Crowdsourcing and Shared Economy**: Platforms allocate resources across a city; too many users at one location reduces utility for all
- **Resource Allocation in AI/ML**: Competing AI agents select computing resources; congestion effects arise in federated learning, model ensembling, online ad auctions
- **Cybersecurity**: Attackers and defenders allocate resources across network surfaces
- **Urban Planning and Facility Location**: Citizens choose between public resources; overuse degrades quality

*Addresses LO2*

---

## 4. Braess's Paradox

### 4.1 The Paradox

**Braess's Paradox**: Adding a new road (resource) to a network can **increase** the total travel time at equilibrium. Closing roads can sometimes **speed up** traffic.

**Real-world example**: Seoul, South Korea closed a major highway along the Cheonggyecheon Stream. Counter-intuitively, traffic flow actually improved as drivers redistributed across other routes.

### 4.2 Worked Example

**200 travelers** going from work (A) to home (D). Two routes:
- $A \to B \to D$: edge $A \to B$ costs $K/10$ min (where $K$ = number on this edge), edge $B \to D$ costs 20 min (constant)
- $A \to C \to D$: edge $A \to C$ costs 20 min (constant), edge $C \to D$ costs $K/10$ min

**Without shortcut (B-C road)**:
- Nash equilibrium: 100 travelers on each route
- Each traveler's time: $100/10 + 20 = 30$ min
- This is a NE because deviating gives $20 + 101/10 = 30.1$ min

**With a free shortcut between B and C (0 min)**:
- Nash equilibrium: ALL travelers take $A \to B \to C \to D$
- Each traveler's time: $200/10 + 200/10 = 40$ min
- This is a NE because any alternative (A→B→D, A→C→D, A→C→B→D) also gives 40 min

**Result**: Adding the free road **increased** everyone's travel time from 30 to 40 minutes!

*Addresses LO9*

---

## 5. Best Response Dynamics

### 5.1 The Algorithm

**Best response dynamics** is both an algorithm and a natural model of agent behavior:

```
Algorithm: Best Response Dynamics
Initialize a = (a₁, ..., aₙ) to be an arbitrary action profile
while There exists i such that aᵢ ∉ argmin_{a'∈Aᵢ} cᵢ(a', a₋ᵢ) do
    Set aᵢ = argmin_{a'∈Aᵢ} cᵢ(a, a₋ᵢ)
end while
Halt and return a
```

**Key observation**: If best response dynamics halts, it returns a **pure Nash equilibrium** (by definition, all players are playing best responses).

**Question**: Does it always halt? In general, **no** (e.g., Matching Pennies has a cycle of profitable deviations and no PSNE). But for congestion games, **yes**.

### 5.2 Rosenthal's Theorem (1973)

> **Theorem (Rosenthal, 1973)**: For every congestion game, every sequence of improvement steps is finite.

This is called the **Finite Improvement Property (FIP)**.

> **Corollary**: Every congestion game has at least one pure Nash equilibrium.

Note: FIP is **stronger** than just existence of PSNE — it means agents can reach equilibrium through natural decentralized dynamics from any starting profile.

*Addresses LO3*

---

## 6. Potential Games and Rosenthal's Potential Function

### 6.1 Rosenthal's Potential Function

The proof of Rosenthal's theorem uses a **potential function**. For every state $a$:

$$\Phi(a) = \sum_{j=1}^{m} \sum_{k=1}^{n_j(a)} d_j(k)$$

This is called **Rosenthal's potential function** — the sum of cumulative delays across all resources.

**Key property**: When player $i$ switches from action $a_i$ to $b_i$, the change in the potential function **exactly equals** the change in player $i$'s cost:

$$\Phi(b_i, a_{-i}) - \Phi(a) = c_i(b_i, a_{-i}) - c_i(a)$$

Since each improvement step decreases the player's cost, it also decreases $\Phi$. Since $\Phi$ takes finitely many values (finite strategy profiles), the process must terminate.

### 6.2 Exact Potential Games

A game is an **exact potential game** if there exists a function $\Phi: \prod_{i=1}^{n} S_i \to \mathbb{R}$ such that for all $i \in N$, for all $s \in \prod S_i$, and for all $s'_i \in S_i$:

$$\text{cost}_i(s'_i, s_{-i}) - \text{cost}_i(s) = \Phi(s'_i, s_{-i}) - \Phi(s)$$

In other words, for any strategy profile, when player $i$ unilaterally deviates, the change in $\Phi$ equals the change in player $i$'s cost. **Congestion games are exact potential games.**

### 6.3 Weaker Notions of Potential

- **Ordinal potential**: $\text{cost}_i(s'_i, s_{-i}) - \text{cost}_i(s) < 0 \iff \Phi(s'_i, s_{-i}) - \Phi(s) < 0$
  (Sign of change matches, but magnitudes need not be equal)

- **Generalized ordinal potential**: $\text{cost}_i(s'_i, s_{-i}) - \text{cost}_i(s) < 0 \implies \Phi(s'_i, s_{-i}) - \Phi(s) < 0$
  (Every improvement in cost implies improvement in $\Phi$, but not vice versa)
  - Generalized ordinal potential ≡ **Finite Improvement Property (FIP)**

### 6.4 Identifying Potential Games

**The potential function is never unique** — adding any constant to a potential function gives another valid potential function.

#### Approach 1: Guess and Check

1. "Seed" the potential function at some profile with an arbitrary value (e.g., $\Phi(C,C) = 0$)
2. Iteratively derive values for other profiles using the potential property
3. If consistent values are obtained, the game is a potential game
4. If inconsistency arises, it is not a potential game

**Worked Example: Prisoner's Dilemma** (with payoffs C/C=3,3; C/D=0,4; D/C=4,0; D/D=1,1):

Set $\Phi(C,C) = 0$.

- $\Phi(D,C) - \Phi(C,C) = U_1(D,C) - U_1(C,C) = 4 - 3 = 1 \Rightarrow \Phi(D,C) = 1$
- $\Phi(C,D) - \Phi(C,C) = U_2(C,D) - U_2(C,C) = 4 - 3 = 1 \Rightarrow \Phi(C,D) = 1$
- $\Phi(D,D) - \Phi(C,D) = U_1(D,D) - U_1(C,D) = 1 - 0 = 1 \Rightarrow \Phi(D,D) = 2$
- Check: $\Phi(D,D) - \Phi(D,C) = U_2(D,D) - U_2(D,C) = 1 - 0 = 1$, and $2 - 1 = 1$ ✓

Potential function: $\Phi = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}$. Prisoner's Dilemma **is** a potential game.

#### Approach 2: Inspect Unilateral Deviation Cycles

Consider cycles of action profiles of the form:
$$(a_i, a_j, \cdot) \to (a'_i, a_j, \cdot) \to (a'_i, a'_j, \cdot) \to (a_i, a'_j, \cdot) \to (a_i, a_j, \cdot)$$

For each transition, compute the change in utility $\Delta_k$ of the deviating player. If the game is a potential game, then $\Delta_1 + \Delta_2 + \Delta_3 + \Delta_4 = 0$ for **any** cycle of length 4.

**Checking all cycles of length 4 proves the result** (for 2-player games with 2 strategies each).

**Example** (game with payoffs T/L=1,1; T/R=3,0; B/L=0,0; B/R=0,1):

Cycle: $(0-1) + (1-0) + (3-0) + (1-0) = 4 \neq 0$

Hence, this game is **not** a potential game.

**Examples of potential games**: Battle of the Sexes ($\Phi$: 2,1,0,2), Stag Hunt ($\Phi$: 2,1,1,2), Prisoner's Dilemma ($\Phi$: 0,1,1,2), Typewriter game ($\Phi$: 3,0,0,1).

### 6.5 Connection: PSNE and Potential Games

Having a PSNE does **not** imply the game is a potential game. A game can have PSNE but fail the cycle test (as shown with the example above where cycle sum $\neq 0$).

### 6.6 Computing PSNE of Congestion Games

Computing a PSNE of a congestion game is equivalent to computing a **local minimum** of Rosenthal's potential function. Hence, complexity theory for **local search problems** is immediately relevant.

*Addresses LO4, LO5, LO6*

---

## 7. Maximum Cut Problem and Local Search

### 7.1 The Max-Cut Problem

A canonical problem for studying local search and its connection to potential games.

**Input**: An undirected graph $G = (V, E)$ with non-negative weight $w_e \geq 0$ for each edge.

**Feasible solutions**: Cuts $(S, \bar{S})$, where $(S, \bar{S})$ is a partition of $V$ into two non-empty sets.

**Objective**: Maximize the total weight of cut edges (edges with one endpoint in each of $S, \bar{S}$).

Unlike minimum cut, **maximum cut is NP-hard**.

### 7.2 Local Search Algorithm

```
1. Start with an arbitrary cut (S, S̄)
2. While there is an improving local move, make one
```

A **local move** = moving a vertex $v$ from one side of the cut to the other (keeping both sides non-empty).

When moving vertex $v$ from $S$ to $\bar{S}$, the change in objective is:
$$\sum_{u \in S} w_{uv} - \sum_{u \in \bar{S}} w_{uv}$$
$$\text{(newly cut)} \quad \text{(newly uncut)}$$

If this difference is positive → **improving local move**.

Local search terminates at a **local optimum** — a solution with no improving move. A local optimum **need not be a global optimum**.

### 7.3 Convergence Properties

- For **unit weight** graphs: objective takes values in $\{0, 1, \ldots, |E|\}$, so local search terminates in at most $|E|$ iterations
- For **general weights**: no known polynomial-time algorithm for computing local optima
- Finding local maxima of max-cut instances is **PLS-complete** (Polynomial Local Search)

### 7.4 PLS: Abstract Local Search Problems

An abstract local search problem is specified by 3 poly-time algorithms:
1. Takes an instance → outputs an arbitrary feasible solution
2. Takes an instance + feasible solution → returns the objective function value
3. Takes an instance + feasible solution → either reports "locally optimal" or produces a better solution

PLS-completeness is the local search analogue of NP-completeness — for PLS-complete problems, we don't expect there to be any clever algorithm that significantly improves over brute-force local search.

**Exponential lower bounds** exist on the number of iterations required by local search to reach a local optimum.

---

## 8. Price of Anarchy and Price of Stability

### 8.1 Definitions

Given an optimization goal (minimization or maximization), we define efficiency measures:

**Price of Anarchy (PoA)** — measures the worst-case equilibrium:
$$\text{PoA} = \frac{\text{value of worst Nash equilibrium}}{\text{value of optimal solution}} \geq 1 \quad \text{(for minimization)}$$

**Price of Stability (PoS)** — measures the best-case equilibrium:
$$\text{PoS} = \frac{\text{value of best Nash equilibrium}}{\text{value of optimal solution}} \geq 1 \quad \text{(for minimization)}$$

For maximization, invert the fractions so that PoA, PoS $\geq 1$.

Always: $\text{PoS} \leq \text{PoA}$.

### 8.2 Examples

**Prisoner's Dilemma** (maximization, social welfare):
- Unique NE: (D,D) with social welfare = 2
- Optimal: (C,C) with social welfare = 20
- PoA = PoS = 20/2 = **10**

**Battle of the Sexes** (maximization):
- Two NE: (Theater,Theater) with welfare 3, (Football,Football) with welfare 4
- Optimal = (Football,Football) with welfare 4
- PoS = 4/4 = **1** (best NE is optimal)
- PoA = 4/3 ≈ **1.33**

**Routing game example** (minimization, social cost):
- Unique NE: State B, social cost = 9
- Optimal: State A, social cost = 8
- PoA = PoS = 9/8 = **1.125**

### 8.3 Simple Two-Link Example

Two parallel links from source to destination, $n$ players:
- Upper link: cost = $x$ (identity function)
- Lower link: cost = $n$ (constant)

**Equilibrium**: All $n$ players take upper link → social cost = $n \cdot n = n^2$

**Better split**: $n/2$ on each → social cost = $\frac{n}{2} \cdot \frac{n}{2} + \frac{n}{2} \cdot n = \frac{3n^2}{4}$

### 8.4 Price of Anarchy for Linear Congestion Games

> **Theorem**: For linear congestion games (all resource cost functions are linear), the **Price of Anarchy is at most 5/2** (two and a half). This bound is **tight**.

**Tight example**: A directed graph with 4 players where:
- Optimal solution: each player takes direct path with cost $K$, total cost = 4
- Worst NE: players take longer paths, total cost = 10
- PoA = 10/4 = **5/2**

### 8.5 Bounding PoS via Potential Function (for Linear Congestion Games)

> **Theorem**: For linear congestion games, $\frac{1}{2}\text{SC}(s) \leq \Phi(s) \leq \text{SC}(s)$

**Proof of upper bound** ($\Phi(s) \leq \text{SC}(s)$):
Since cost functions are nondecreasing: $\Phi(s) = \sum_{r \in R} \sum_{j=1}^{n_r} c_r(j) \leq \sum_{r \in R} \sum_{j=1}^{n_r} c_r(n_r) = \sum_{r \in R} n_r c_r(n_r) = \text{SC}(s)$

**Proof of lower bound** ($\frac{1}{2}\text{SC}(s) \leq \Phi(s)$):
Uses the inequality $\frac{n^{k+1}}{k+1} \leq \sum_{j=1}^{n} j^k$ for $k = 0, 1$, and the linearity of cost functions $c_r(x) = a_r \cdot x + b_r$.

### 8.6 Price of Stability with Bounded Congestion

> **Theorem**: For a congestion game where no resource is ever used by more than $\lambda$ players, the **Price of Stability is at most $\lambda$**.

**Proof**: Start from optimal profile $s^*$. If it's a NE, PoS = 1. Otherwise, apply best response dynamics to reach NE $s$. Since $\Phi$ decreases at each step:
$$\text{SC}(s) \leq \lambda \Phi(s) \leq \lambda \Phi(s^*) \leq \lambda \cdot \text{SC}(s^*)$$

*Addresses LO7, LO8*

---

## 9. Tutorial Problems and Solutions

### 9.1 Exercise 1: Network Congestion Game PSNE

Three players in a directed graph with vertices $\{s, v_1, v_2, v_3, t\}$. Find PSNE by best response dynamics.

**Solution**: Start with all players on route $s \to v_3 \to t$. Apply iterative improvements:
- (a) Player 1 switches to $s \to v_2 \to v_1 \to t$
- (b) Player 2 switches to $s \to v_2 \to v_1 \to t$
- (c) Player 3 switches to $s \to v_1 \to t$
- (d) Player 2 switches to $s \to v_1 \to t$

**PSNE reached**:
- Player 1: $s \to v_2 \to v_1 \to t$
- Player 2: $s \to v_1 \to t$
- Player 3: $s \to v_1 \to t$

All PSNE in this game send two players via $s \to v_1 \to t$ and one via $s \to v_2 \to v_1 \to t$.

### 9.2 Exercise 2: Potential vs Social Cost in Linear Games

**Result**: $\frac{1}{2}\text{SC}(s) \leq \Phi(s) \leq \text{SC}(s)$ for linear congestion games.

### 9.3 Exercise 3: PoS with Bounded Congestion

If no resource is used by more than $\lambda$ players, PoS $\leq \lambda$.

### 9.4 Exercise 4: Cut Games

**Cut games**: Undirected graph $G = (V,E)$, each player $i$ controls vertex $v_i$. Strategy: LEFT or RIGHT. Cut = partition into two sets. Player $i$'s utility = total weight of cut edges adjacent to $v_i$:
$$u_i(s) = \sum_{e \in \text{CUT}(s) \cap E_i} w_e$$

**(a) PoA = 2 example**: Graph with 4 vertices $a,b,c,d$ and edges $(a,b), (c,d), (a,c), (b,d)$ with unit weights. NE: $\{a,b\}$ LEFT, $\{c,d\}$ RIGHT → payoff 4. Optimal: $\{a,d\}$ LEFT, $\{b,c\}$ RIGHT → payoff 8. PoA = 8/4 = 2.

**(b) PoA ≤ 2 proof**: In any PSNE, each player's cut edges are at least half the total weight of their adjacent edges (otherwise they'd deviate). Summing over all players:
$$\sum_i u_i(s_{eq}) \geq \frac{1}{2} \sum_i \sum_{e \in E_i} w_e = \sum_{e \in E} w_e$$
The optimal can't exceed $2 \sum_{e \in E} w_e$ (each edge counted twice), so PoA ≤ 2.

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Congestion game** | Game where player costs depend on congestion (number of users) on shared resources |
| **Network congestion (routing) game** | Congestion game on a graph where resources are edges and strategies are source-to-target paths |
| **Delay/cost function** | $d_j(k)$: cost of resource $j$ when $k$ players use it |
| **Best response dynamics** | Iterative process where players take turns switching to their best response |
| **Finite Improvement Property (FIP)** | Every sequence of improvement steps terminates (congestion games have FIP) |
| **Rosenthal's potential function** | $\Phi(a) = \sum_{j=1}^{m} \sum_{k=1}^{n_j(a)} d_j(k)$; change in $\Phi$ equals change in deviating player's cost |
| **Exact potential game** | Game with a function $\Phi$ where $\Delta\text{cost}_i = \Delta\Phi$ for every unilateral deviation |
| **Ordinal potential game** | $\Delta\text{cost}_i < 0 \iff \Delta\Phi < 0$ |
| **Generalized ordinal potential** | $\Delta\text{cost}_i < 0 \implies \Delta\Phi < 0$ (equivalent to FIP) |
| **Price of Anarchy (PoA)** | Ratio of worst equilibrium value to optimal value (≥ 1) |
| **Price of Stability (PoS)** | Ratio of best equilibrium value to optimal value (≥ 1) |
| **Social cost/welfare** | Sum of all players' costs/utilities |
| **Braess's Paradox** | Adding a resource to a network can worsen equilibrium outcomes |
| **Linear congestion game** | Congestion game where all cost functions are linear: $c_r(x) = a_r x + b_r$ |
| **Cut game** | Game on a graph where players partition vertices into LEFT/RIGHT; utility = weight of adjacent cut edges |
| **Maximum cut problem** | NP-hard optimization: partition graph vertices to maximize cut edge weight |
| **Local search** | Heuristic: start with feasible solution, repeatedly make improving local moves until local optimum |
| **PLS (Polynomial Local Search)** | Complexity class for local search problems; PLS-complete = hardest local search problems |
| **Local optimum** | Solution with no improving local move; need not be global optimum |

---

## Summary

- **LO1 (Congestion games)**: Defined congestion games formally with players, resources, actions (subsets of resources), and congestion-dependent cost functions. Specialised to network/routing games on graphs (Section 2).

- **LO2 (Applications)**: Covered applications in traffic routing, telecom networks, cloud computing, robotics, smart grids, IoT, crowdsourcing, AI/ML, cybersecurity, and urban planning (Section 3).

- **LO3 (Best response dynamics)**: Presented the algorithm, proved it returns PSNE when it halts, and showed convergence for congestion games via Rosenthal's theorem (Section 5).

- **LO4 (Potential games)**: Defined Rosenthal's potential function, proved the exact potential property for congestion games, and showed this implies FIP and PSNE existence (Section 6).

- **LO5 (Potential game variants)**: Distinguished exact, ordinal, and generalized ordinal potential games (Section 6.3).

- **LO6 (Identifying potential games)**: Demonstrated guess-and-check (seeding + iterative derivation) and cycle-based approaches with worked examples including Prisoner's Dilemma, Battle of Sexes, and non-potential games (Section 6.4).

- **LO7 (PoA and PoS)**: Defined both measures, computed them for Prisoner's Dilemma (PoA=10), Battle of Sexes (PoA=4/3, PoS=1), and routing game examples (Section 8).

- **LO8 (Efficiency bounds)**: Proved PoA ≤ 5/2 for linear congestion games (tight), showed $\frac{1}{2}\text{SC} \leq \Phi \leq \text{SC}$, and proved PoS ≤ $\lambda$ for bounded congestion (Section 8.4–8.6).

- **LO9 (Braess's Paradox)**: Demonstrated how adding a free road increased equilibrium travel time from 30 to 40 minutes for all 200 travelers (Section 4).
