# Week 5: Cooperative Games (Part II) — Hedonic Games, Stable Matchings, and House Allocation

## Learning Objectives
By the end of this week, you should be able to:
- [ ] Describe the core concepts of stable matchings, including preference profiles, stability, and blocking pairs
- [ ] Model real-world matching problems (e.g., college admissions, job markets, school choice) using formal mathematical frameworks
- [ ] Apply algorithms such as Gale-Shapley to find stable matchings in bipartite settings
- [ ] Analyse existence, uniqueness, and properties of stable matching solutions under different assumptions and settings
- [ ] Evaluate the fairness and efficiency of matchings, and understand trade-offs between stability and other criteria
- [ ] Identify strategic aspects and vulnerabilities in matching markets, such as incentives to misreport preferences
- [ ] Solve computational and theoretical exercises involving construction and analysis of stable matchings
- [ ] Interpret the applications and impact of stable matching theory in economics, computer science, and societal allocation problems

---

## 1. Beyond Transferable Utility

Previously, we assumed that a coalition's payoff is allocated to the group as a whole and can be shared arbitrarily (transferable utility). This is appropriate when payoffs are purely monetary.

However, many real-world situations involve **non-transferable utility (NTU)**:
- Payoffs accrue to individual coalition members and cannot be transferred
- Benefits may take the form of reputation, access, rights, or institutional rewards that attach directly to individuals

With no transfers, we must reason about **coalitional actions** and the **vector of payoffs** they generate:
- $\{x, y\}$ can perform action $a$, which pays 1 to $x$ and 6 to $y$
- $\{x, y\}$ can perform action $b$, which pays 4 to $x$ and 2 to $y$

### 1.1 NTU Game Example: Academic Collaboration

$n$ researchers at $n$ different universities can form groups to co-author papers:
- The group's composition determines the quality/impact of the paper
- Each author receives a payoff from their **own** university (promotion, bonus, teaching load reduction, parking spot)
- These payoffs are **non-transferable** — a promotion for one researcher cannot be given to a collaborator at another university

---

## 2. Hedonic Games

### 2.1 Intuition and Definition

**Hedonic games** are a significant simplification of the general NTU setting:
- Each coalition has **only one action** available to it (no strategic choice within a coalition)
- Player $i$'s payoff is determined **solely by the coalition** $i$ is in
- Each player **ranks** all coalitions she could possibly join, from best to worst (ties are possible)

**Example preferences** (3 players):
- 1: $\{1,2\} \sim \{1,3\} \succ \{1,2,3\} \succ \{1\}$
- 2: $\{2\} \succ \{1,2,3\} \succ \{1,2\} \succ \{2,3\}$
- 3: $\{1,2,3\} \succ \{3\} \succ \{3,2\} \sim \{1,3\}$

### 2.2 Formal Definition

A **hedonic game** consists of:
- A set of players $N = \{1, 2, \ldots, n\}$
- Players want to split into coalitions forming a **partition** of $N$
- Each player $i$ has preferences $\succeq_i$ over $\{S \subseteq N \mid i \in S\}$ (all coalitions she could be in)
- **Outcome**: a coalition structure (partition) — note: **no payoff distribution phase**

**Numerical encoding**: Without loss of generality, preferences can be encoded by numbers:
- $\{1,2\} \sim \{1,3\} \succ \{1,2,3\} \succ \{1\}$ becomes $v_1(\{1,2\}) = v_1(\{1,3\}) = 2$, $v_1(\{1,2,3\}) = 1$, $v_1(\{1\}) = 0$

*Addresses LO1*

---

## 3. Compactly Representable Hedonic Games

Full representation of hedonic preferences can be **exponential** in the number of agents. Several compact representations exist:

### 3.1 Anonymous Games
Preferences depend on **coalition sizes only**.

### 3.2 Cardinal Utility-Based Representations

Each agent assigns a value $v_i(j) : N \setminus \{i\} \to \mathbb{R}$ to every other agent. Coalition utility is then aggregated:

**Additively Separable Hedonic Games (ASHGs)**:
$$v_i(S) = \sum_{j \in S \setminus \{i\}} v_i(j)$$

**Fractional Hedonic Games**:
$$v_i(S) = \frac{\sum_{j \in S \setminus \{i\}} v_i(j)}{|S|}$$

**B-games** (Best response): $v_i(S) = \max_{j \in S \setminus \{i\}} v_i(j)$ — agent cares only about their most valued coalition member.

**W-games** (Worst response): $v_i(S) = \min_{j \in S \setminus \{i\}} v_i(j)$ — coalition is only as good as its least-valued member.

### 3.3 ASHGs vs. Induced Subgraph Games

Both represent players as vertices of a weighted graph:

| Property | Induced Subgraph Games | ASHGs |
|----------|----------------------|-------|
| Edge type | **Undirected** (symmetric) | **Directed** (potentially asymmetric) |
| Coalition value for $i$ | Total weight of internal edges | Total weight of edges **from $i$** to other members of $T \setminus \{i\}$ |
| Key result | Non-negative weights implies non-empty core | Core may be empty even for symmetric games |

---

## 4. Stability Concepts in Hedonic Games

### 4.1 Individual Rationality

A partition is **individually rational (IR)** if no player strictly prefers being on its own to its current coalition.
- This is the **minimum stability requirement**
- Formally: $v_i(P(i)) \geq v_i(\{i\})$ for all players $i$, where $P(i)$ is $i$'s coalition in partition $P$

### 4.2 Nash Stability

A partition is **Nash stable** if no player can benefit from moving from its coalition $S$ to another coalition $T$ (or to being alone).

**Formally**: Player $i$ has an **NS-deviation** from partition $P$ if there is a coalition $T \in P \cup \{\emptyset\}$ such that $i$ prefers $T \cup \{i\}$ to its current coalition. A partition is Nash stable if **no player has an NS-deviation**.

**Key facts**:
- Nash stability implies individual rationality
- Nash stable outcomes are **not guaranteed to exist** in general

**Counterexample** (two-player game): Player 1 values player 2 positively ($+1$), but player 2 values player 1 negatively ($-1$). If together, player 2 wants to leave. If apart, player 1 wants to join. No Nash stable partition exists.

### 4.3 Nash Stability in Symmetric ASHGs

**Symmetric ASHGs**: $v_i(j) = v_j(i)$ for all $i, j$.

> **Observation**: Every symmetric ASHG admits a Nash stable outcome.

**Proof idea**: Every NS-deviation increases the sum of utilities (social welfare). Since there are finitely many partitions, improvement dynamics must converge.

> **Theorem (Gairing, Savani 2010)**: Finding a Nash stable outcome in symmetric additively separable hedonic games is **PLS-complete**.

### 4.4 Individual Stability

Player $i$ has an **IS-deviation** from partition $P$ if there is a coalition $T \in P \cup \{\emptyset\}$ such that:
1. $i$ prefers $T \cup \{i\}$ to its current coalition, **AND**
2. All players in $T$ **weakly prefer** $T \cup \{i\}$ to $T$

A partition is **individually stable** if no player has an IS-deviation.

### 4.5 Contractual Individual Stability (CIS)

Player $i$ has a **CIS-deviation** from partition $P$ if there is a coalition $T \in P \cup \{\emptyset\}$ such that:
1. $i$ prefers $T \cup \{i\}$ to its current coalition $S$
2. All players in $T$ weakly prefer $T \cup \{i\}$ to $T$
3. All players in $S$ weakly prefer $S \setminus \{i\}$ to $S$

A partition is **contractually individually stable** if no player has a CIS-deviation.

> **Theorem**: Every hedonic game has a CIS outcome.

**Proof**:
1. Assume each player assigns a numerical utility to each coalition (we showed this is equivalent)
2. Each CIS deviation **increases** the sum of utilities (the deviator improves, receiving coalition members weakly approve, leaving coalition members weakly approve)
3. Therefore, a partition that **maximizes** the sum of utilities is CIS

### 4.6 Hierarchy of Stability Concepts

From strongest to weakest:
$$\text{Core stable} \implies \text{Nash stable} \implies \text{Individually stable} \implies \text{CIS} \implies \text{IR}$$

- **Core stable**: may not exist
- **Nash stable**: may not exist (but exists for symmetric ASHGs)
- **Individually stable**: may not exist
- **CIS**: always exists
- **IR**: always exists (trivially, by the all-singletons partition if utilities are non-negative for singletons)

### 4.7 Core Stability

A group of players $C$ **blocks** a partition $P$ if **each player** in $C$ prefers $C$ to its coalition in $P$.

A partition is **core stable** if no group blocks it.

**Empty core example** (3 players):
- 1: $\{1,2\} \succ \{1,3\} \succ \{1\} \succ \{1,2,3\}$
- 2: $\{2,3\} \succ \{2,1\} \succ \{2\} \succ \{1,2,3\}$
- 3: $\{3,1\} \succ \{3,2\} \succ \{3\} \succ \{1,2,3\}$

**Why every partition is blocked**:
- Grand coalition: any singleton agent deviates (all rank it last)
- All singletons: any pair of agents can form a blocking pair
- One pair + one singleton: the "less preferred" member of the pair wants to leave and form a pair with the singleton, creating a cycle ($\{1,2\} \to$ agent 2 leaves for $\{2,3\} \to$ agent 3 leaves for $\{3,1\} \to$ agent 1 leaves for $\{1,2\}$)

### 4.8 Empty Core in ASHGs

The core can be empty even for **additively separable** and **symmetric** ASHGs.

**Example** (5 agents on a cycle): Adjacent agents have weight $+2$ or $+1$, non-adjacent agents have weight $-10$.
1. No coalition of size $\geq 3$ is IR (at least one agent has negative utility due to $-10$ edge)
2. No partition into coalitions of size 1 and 2 can be stable (two adjacent singletons would form a blocking pair)
3. Hence the core is empty

### 4.9 Friends and Enemies Games

**Friends and enemies games**: ASHGs where each player $i$ partitions $N \setminus \{i\}$ into friends and enemies, assigning:
- Positive utility $F$ to friends
- Negative utility $E$ to enemies
- Need **not** be symmetric

**Special cases with non-empty core**:
- **Friend appreciation game**: $F = n$, $E = -1$ (friends are highly valued, enemies are mildly disliked)
- **Enemy aversion game**: $F = 1$, $E = -n$ (enemies are highly disliked, friends are mildly valued)

> **Theorem**: Every friend appreciation game and every enemy aversion game has a non-empty core.

*Addresses LO1, LO4*

---

## 5. Stable Matching Problem

### 5.1 Problem Definition

The stable matching problem is a foundational model that can be viewed as a **hedonic game**.

**Setup**:
- Set $X$ of women and set $Y$ of men, $|X| = |Y| = n$
- Each $x \in X$ has a strict preference order $\succ_x$ over all $y \in Y$
- Each $y \in Y$ has a strict preference order $\succ_y$ over all $x \in X$
- Being unmatched is **least preferred** by every agent

**Example**:
- Anna: Jacob $\succ$ Isaac $\succ$ Ken
- Bella: Isaac $\succ$ Jacob $\succ$ Ken
- Clare: Isaac $\succ$ Jacob $\succ$ Ken
- Isaac: Anna $\succ$ Bella $\succ$ Clare
- Jacob: Bella $\succ$ Anna $\succ$ Clare
- Ken: Anna $\succ$ Bella $\succ$ Clare

### 5.2 Matchings

A **matching** $M$ is a set of ordered pairs $x - y$ with $x \in X$, $y \in Y$ such that:
- Each woman $x \in X$ appears in at most one pair
- Each man $y \in Y$ appears in at most one pair

A matching is **perfect** if $|M| = |X| = |Y| = n$ (everyone is matched).

**Example**: $M = \{A-K, B-J, C-I\}$ is a perfect matching.

### 5.3 Blocking Pairs and Stability

Given a perfect matching $M$, woman $x$ and man $y$ form a **blocking pair** if:
1. $x$ prefers $y$ to her partner in $M$, **AND**
2. $y$ prefers $x$ to his partner in $M$

A **stable matching** is a perfect matching with **no blocking pairs**.

**Example**: In $M = \{A-K, B-J, C-I\}$, Bella and Isaac form a blocking pair (Bella prefers Isaac over Jacob; Isaac prefers Bella over Clare). So this matching is **not stable**.

**Stable matching**: $M = \{A-I, B-J, C-K\}$ is stable because:
- Isaac is matched to his top choice (Anna)
- Jacob is matched to his top choice (Bella)
- Ken is matched to Clare (his last choice), but neither Anna nor Bella prefers Ken over their current partner

### 5.4 Connection to Hedonic Games

A stable matching instance is a hedonic game where:
- Each man $y$ prefers being alone to any coalition that is not a pair $\{x, y\}$ with a woman
- Each pair $\{x, y\}$ is preferred to being alone
- Preferences over pairs follow preferences over the opposite group

**A stable matching corresponds to a core stable outcome in this hedonic game.**

### 5.5 Stable Roommate Problem

**Differs from stable matching**: one population of $2n$ people (not two disjoint sets). Each person ranks all others.

> **Key result**: Stable roommate matchings **need not exist**.

**Counterexample** (4 agents: Adam, Bob, Chris, Dunn):
- Adam-Dunn matched $\Rightarrow$ Adam-Chris is blocking
- Adam-Chris matched $\Rightarrow$ Adam-Bob is blocking
- Adam-Bob matched $\Rightarrow$ Bob-Chris is blocking

No stable outcome exists.

*Addresses LO1, LO2, LO4*

---

## 6. Gale-Shapley Deferred Acceptance Algorithm

### 6.1 The Algorithm

Unlike the stable roommate problem, the stable matching problem **always has a solution**, computed by the **Gale-Shapley Deferred Acceptance (DA) algorithm** (1962):

```
Algorithm: Deferred Acceptance (men proposing)
1. Each man y proposes to his most preferred woman
2. Each woman x who received proposals tentatively accepts
   her most preferred proposer and rejects all others
3. Each rejected man proposes to his next most preferred woman
4. Each woman with a new proposal tentatively accepts
   the best among her current tentative partner and new proposers,
   rejects all others
5. Repeat steps 3-4 until no new proposals are made
6. All tentative acceptances become final
```

### 6.2 Key Properties of DA

**Men propose in decreasing order of preference**: each rejected man moves to the next woman on his list.

**Women only trade up**: once a woman is tentatively matched, she never becomes unmatched — she can only replace her current partner with someone she prefers.

### 6.3 Termination

DA terminates after at most $n^2$ iterations, because each man proposes to each woman at most once, and there are $n \times n = n^2$ possible proposals.

### 6.4 DA Outputs a Perfect Matching

**Proof by contradiction**: Suppose some man $y$ remains unmatched. Then some woman $x$ must also be unmatched (since $|X| = |Y|$). But $y$ has proposed to all women, including $x$. So $x$ was matched at some point. Since women never become unmatched once matched, $x$ is matched — contradiction.

### 6.5 DA Outputs a Stable Matching

**Proof**: Consider any pair $(x, y)$ not in the matching. Two cases:
1. **Man $y$ never proposed to woman $x$**: Then $y$ is matched to someone he prefers over $x$. So $(x, y)$ is not a blocking pair.
2. **Man $y$ proposed to $x$ but was rejected**: Then $x$ rejected $y$ in favour of someone she prefers. Since women only trade up, she is matched to someone she prefers over $y$. So $(x, y)$ is not a blocking pair.

In either case, no blocking pair exists. The matching is stable.

> **Theorem (Gale-Shapley, 1962)**: The DA algorithm terminates after $O(n^2)$ iterations and finds a stable matching for any problem instance.

This result won the **2012 Nobel Prize in Economics** (awarded to Lloyd Shapley and Alvin Roth).

### 6.6 Worked Example (Men Proposing)

Preferences:
- A: J $\succ$ I $\succ$ K; B: I $\succ$ J $\succ$ K; C: I $\succ$ J $\succ$ K
- I: A $\succ$ B $\succ$ C; J: B $\succ$ A $\succ$ C; K: A $\succ$ B $\succ$ C

**Round 1**: I and K propose to A; A tentatively accepts I (prefers I). J proposes to B; B accepts J.

**Round 2**: K proposes to B; B rejects K (prefers J).

**Round 3**: K proposes to C; C accepts K.

**Final matching**: $\{A-I, B-J, C-K\}$ (man-optimal).

### 6.7 Worked Example (Women Proposing)

**Round 1**: A proposes to J; J accepts A. B and C propose to I; I accepts B.

**Round 2**: C proposes to J; J rejects C (prefers A).

**Round 3**: C proposes to K; K accepts C.

**Final matching**: $\{B-I, A-J, C-K\}$ (woman-optimal).

*Addresses LO3, LO7*

---

## 7. Understanding the Solution: Optimality and Pessimality

### 7.1 Valid Partners and Multiple Stable Matchings

A given instance may have **many** stable matchings.

**Definition**: Woman $x$ is a **valid partner** of man $y$ if there exists a stable matching $M$ with $x - y \in M$.

**Example**: Both stable matchings $\{A-I, B-J, C-K\}$ and $\{B-I, A-J, C-K\}$ exist, so both Anna and Bella are valid partners for Isaac and Jacob. Clare is the only valid partner for Ken.

### 7.2 Man-Optimal Matching

In a **man-optimal matching**, each man receives his **best valid partner**.

> **Theorem**: The DA algorithm (with men proposing) outputs the man-optimal matching.

**Proof by contradiction**:
1. Suppose some man is matched with someone who is not his best valid partner
2. Then some man is rejected by a valid partner — consider the **first time** this happens
3. Let $I$ be the man rejected at this point, and $A$ be the woman who rejects him
4. She rejects $I$ in favour of another man $J$
5. Let $M$ be a stable matching with $A - I \in M$, and let $B$ be $J$'s partner in $M$
6. At this point, $J$ has not been rejected by $B$ (since this is the first rejection by a valid partner) — so $J$ has not yet proposed to $B$
7. This means $J$ prefers $A$ to $B$
8. Also, $A$ prefers $J$ to $I$ (she rejected $I$ for $J$)
9. Therefore $(A, J)$ is a blocking pair in $M$ — contradiction with $M$ being stable

### 7.3 Women Pessimality

> **Theorem**: The DA algorithm (with men proposing) outputs the **women-pessimal matching** — each woman gets her **worst valid partner**.

**Proof**: Suppose under DA woman $A$ is matched to man $J$, but $J$ is not her worst valid partner. Let $I$ be her worst valid partner, so $A$ prefers $J$ to $I$. There is a stable matching $M$ with $A - I \in M$. Let $B$ be $J$'s partner in $M$. Since DA outputs the man-optimal matching, $J$ prefers $A$ to $B$. But then $(A, J)$ is a blocking pair in $M$ — contradiction.

**Implication**: The proposing side gets the best possible outcome; the receiving side gets the worst possible outcome among all stable matchings.

*Addresses LO4, LO5*

---

## 8. Strategyproofness

### 8.1 Definition

An algorithm $A$ is **strategyproof** if on every instance, no agent (man or woman) can benefit from misreporting their preferences under $A$.

Formally: man $y$ can benefit from misreporting if there exists a ranking $\succ'$ over $X$ such that if $y$ reports $\succ'$ instead of $\succ_y$ (while others report truthfully), the algorithm matches $y$ to $x'$ such that $x' \succ_y x$ (where $x$ was his match under truthful reporting).

### 8.2 GS is Strategyproof for the Proposing Side

> **Theorem**: On every instance of the stable matching problem, no man can benefit from misreporting their preferences under GS (with men proposing). That is, GS is strategyproof for men.

**Proof**: Follows directly from the fact that GS outputs the man-optimal matching — each man already gets his best valid partner, so no misreport can improve his outcome.

### 8.3 GS is NOT Strategyproof for the Receiving Side

> **Claim**: Under Gale-Shapley, women can benefit from misreporting their preferences.

**Worked example**: With truthful preferences, GS (men proposing) gives $\{A-I, B-J, C-K\}$.

Suppose A misreports as $J \succ K \succ I$ (instead of $J \succ I \succ K$). Then:
- Round 1: I proposes to A (accepted), J to B (accepted), K to A (A rejects I, accepts K based on misreported preferences)
- Round 2: I proposes to B (B rejects J, accepts I). Current: $\{A-K, B-I\}$
- Round 3: J proposes to A (A rejects K, accepts J). Current: $\{A-J, B-I\}$
- Round 4: K proposes to C. Final: $\{A-J, B-I, C-K\}$

Anna gets Jacob (her true top choice) instead of Isaac (her true second choice). She benefits from misreporting.

### 8.4 Impossibility Result

> **Claim**: There is **no algorithm** that always outputs stable matchings such that no agent (man or woman) can benefit from misreporting their preferences. Full strategyproofness for both sides is impossible.

*Addresses LO5, LO6*

---

## 9. Extensions of Stable Matching

### 9.1 Many-to-One Matching (College Admissions)

Institutions (hospitals, schools) have **quotas** — they can accept multiple agents. The DA algorithm extends naturally.

**Stability**: No pair $(x, y)$ where $x$ is a school and $y$ is a student such that:
- $y$ is not admitted to $x$
- $x$ prefers $y$ to one of its current students (or has free slots)
- $y$ prefers $x$ to their current school

### 9.2 Unacceptable Partners

Some agents may find certain potential matches **unacceptable**. Numbers of men and women need not be equal.

**Stability**: No pair $(x, y)$ such that $y$ is not admitted to $x$, $y$ and $x$ find each other acceptable, $x$ has a free slot or prefers $y$ to a current student, and $y$ is unmatched or prefers $x$ to their current school.

DA still works for this setting.

### 9.3 Ties/Indifferences

Preferences may have ties (e.g., a school partitions students into groups by catchment area and siblings, but is indifferent within groups).

**Weak stability**: No pair $x-y$ where $x$ and $y$ **strictly** prefer each other to their current partners.

*Addresses LO2, LO4, LO8*

---

## 10. Applications of Stable Matching

### 10.1 University Admissions
- **UK UCAS**: Processes 600,000+ student applications annually
- **UAC (New South Wales, Australia)**: Allocates 40,000+ graduates to university degrees

### 10.2 School Choice
- **New York City**: DA-based algorithm for high school admissions (students rank up to 12 programs)
- **Boston**: DA replaced the "First Choices First" system, eliminating 30,000 manual administrative assignments

### 10.3 Medical Residency
- **US NRMP**: Matches ~30,000 medical graduates to hospital residency positions annually using a DA variant

### 10.4 Organ Allocation and Kidney Exchange
- **UK NHS**: Living Kidney Sharing Scheme uses matching algorithms for donor-recipient pairing
- Kidney exchange programs address the **double coincidence of wants** problem
- **Roth, Sonmez, and Unver (2004)**: Established the first kidney exchange clearinghouse in New England

### 10.5 Other Applications
- Adoption and foster care matching
- Mentoring programs and professional partnerships
- Content Delivery Networks (CDNs): matching users to edge servers

*Addresses LO2, LO8*

---

## 11. House Allocation Problem

### 11.1 Problem Definition (No Endowments)

- A set of $n$ agents $N$
- A set of $n$ houses $H$
- Each person in $N$ has a ranking over all houses in $H$
- Goal: match agents to houses (1:1)

This is a **one-sided preference** problem: only agents have preferences, houses are indifferent.

### 11.2 Serial Dictatorship (SD)

**Algorithm**:
1. Agents come one by one (in a fixed order)
2. Each agent chooses her most preferred **available** house
3. The agent and house are removed from the market

**Example**: Agents A, B, C, D with houses x, y, z, t.
- A: $x \succ y \succ z \succ t$ — A gets $x$
- B: $x \succ t \succ y \succ z$ — B gets $t$
- C: $t \succ z \succ y \succ x$ — C gets $z$
- D: $z \succ x \succ y \succ t$ — D gets $y$

### 11.3 Properties of Serial Dictatorship

> **Claim**: Serial dictatorship is **strategyproof**.

Each agent gets their most preferred available house — misreporting cannot improve the set of available houses when it is your turn.

> **Claim**: Serial dictatorship is **core stable**.

**Proof**: Suppose there is a deviating coalition $S$. Let $i$ be the first agent (in the SD order) in $S$. Let $h$ be the house $i$ gets under SD. When $i$ chose $h$, agents in $S \setminus \{i\}$ have not yet made their selection, so their houses were still available. Hence, $i$ prefers $h$ to the houses of agents in $S \setminus \{i\}$. So $i$ does not benefit from deviating with $S$. Contradiction.

> **Claim**: The output of SD is **Pareto-optimal**.

**Proof**: Let $A$ be the output of SD, and suppose $B$ Pareto-dominates $A$. Let $i$ be the first agent (in the SD order) who gets different houses in $A$ and $B$, and let $h$ be her house in $A$. Let $T$ be the set of houses allocated to agents $\{1, \ldots, i-1\}$. In $B$, agents $\{1, \ldots, i-1\}$ also get houses in $T$ (since they get the same houses). Hence in $B$, agent $i$ gets a house in $H \setminus T$. But $h$ is her favourite house in $H \setminus T$. Contradiction.

**Serial dictatorship is NOT fair**: Earlier agents get better choices. **Fix**: draw a random order of agents, let them choose in that order (Random Serial Dictatorship).

**Pareto dominance**: Allocation $A$ is **Pareto-dominated** by allocation $B$ if no agent is worse off in $B$ compared to $A$, and some agent is strictly better in $B$. An allocation is **Pareto-optimal** if it is not Pareto-dominated by any other allocation.

### 11.4 House Allocation with Endowments

**Case 2**: Each agent initially **owns** a house (need not rank her house first).

**Naive approach** (evict all agents, run SD): May fail **individual rationality** — an agent may end up with a house she likes less than her original house.

**Pairwise exchanges**: May fail Pareto optimality and core stability.

**Group exchanges**: Expensive to implement.

### 11.5 Top Trading Cycle (TTC) Algorithm

**Algorithm**:
1. Each person points to her **most preferred house**
2. Each house points to **its owner**
3. This creates a directed graph with $2n$ vertices and $2n$ edges, so **at least one cycle** exists
4. Remove all cycles, assigning people to the house they are pointing at
5. Repeat using preference lists where assigned houses have been deleted

**Termination**: Always terminates.
- Initially: $2n$ vertices, $2n$ edges $\Rightarrow$ at least one cycle (possibly of length 2, i.e., someone pointing to their own house)
- Each iteration removes a cycle (at least 2 vertices: one agent + one house)
- By induction: after each cycle removal, #vertices = #edges, hence at least one cycle remains
- Terminates after at most $n$ iterations

**Worked example**: Agents A, B, C, D own houses a, b, c, d respectively.
- A: $d \succ a \succ c \succ b$; B: $d \succ b \succ a \succ c$; C: $b \succ c \succ a \succ d$; D: $c \succ d \succ a \succ b$

Round 1: A $\to$ d, D $\to$ c, C $\to$ b, B $\to$ d. Houses point to owners: a $\to$ A, b $\to$ B, c $\to$ C, d $\to$ D.

Cycle: C $\to$ b $\to$ B $\to$ d $\to$ D $\to$ c $\to$ C. Remove this cycle: B gets d, D gets c, C gets b.

Round 2: Only A remains. A $\to$ a. Self-cycle: A gets a.

**Final allocation**: A: a, B: d, C: b, D: c.

### 11.6 Properties of TTC

> **Theorem**: TTC is **individually rational** — no agent receives a house they like less than their original house.

**Proof**: Consider agent $i$ who originally has house $h$. Suppose TTC allocates $h'$ to $i$ and $i$ prefers $h$ to $h'$. Consider the round in which $i$ receives $h'$. In this round, $h$ is still present (we only remove a house together with its owner, and $i$ is still present). But then $i$ cannot be pointing to $h'$, since $h$ is available and preferred. Contradiction.

> **Theorem**: TTC outputs a **Pareto-optimal** allocation.

**Proof**: Let $X$ be the TTC output. Suppose $Y$ Pareto-dominates $X$. Let $N^*$ be the set of agents who improve in $Y$. Let $k$ be the first round in which some agent $i \in N^*$ gets a house under TTC. Let $H^*$ be the set of houses allocated before round $k$. The houses in $H^*$ are allocated identically in $X$ and $Y$ (since those agents are not in $N^*$). Hence in $Y$, agent $i$ gets a house in $H \setminus H^*$. But in $X$, $i$ gets her most preferred house in $H \setminus H^*$. Contradiction.

> **Theorem**: TTC outputs an allocation **in the core**.

**Proof**: Let $X$ be the TTC output. Suppose coalition $N'$ can beneficially deviate. Let $k$ be the first round in which some agent $i \in N'$ gets a house under TTC, and let $h$ be that house. Let $h'$ be the house $i$ gets when deviating with $N'$. All agents in $N'$ are present in round $k$ (none allocated before). Hence, so are their houses — in particular, $h'$. Since $i$ points to $h$ (not $h'$), she prefers $h$ to $h'$. Contradiction.

> **Theorem**: TTC is **strategyproof**.

**Proof sketch**: Fix agent $i$. Think of $i$ as choosing which house to point to in each round. If truthful, $i$ points to her favourite house. Could $i$ benefit by pointing to a non-favourite house? Only if she could get that house in the current round (by being in a cycle) and worries that her favourite might disappear later. But: let $H(k)$ be $i$'s "choice set" in round $k$. **Lemma**: $H(k) \subseteq H(k+1)$ — every vertex has outdegree 1, and if an agent $j$ has a path to $i$ in round $k$, this remains the case in round $k+1$ (until $i$ is allocated). So the choice set can only grow, and truth-telling is optimal.

### 11.7 Connection to Kidney Exchange

> House allocation with endowments is essentially equivalent to the **kidney exchange** problem.

- Patient-donor pairs = agents with endowed houses
- TTC can be used to efficiently assign kidneys
- **Roth, Sonmez, and Unver (2004)**: Established the first kidney exchange clearinghouse for New England using TTC-based methods

*Addresses LO2, LO3, LO5, LO6, LO8*

---

## 12. Tutorial Problems and Solutions

### 12.1 Exercise 1: Stability Analysis of a Symmetric ASHG

**Problem**: Symmetric ASHG with $N = \{a_1, a_2, a_3, a_4\}$ and edge weights: $v(a_1, a_2) = \alpha$, $v(a_1, a_3) = -1$, $v(a_1, a_4) = 2$, $v(a_2, a_3) = 4$, $v(a_2, a_4) = \alpha$, $v(a_3, a_4) = -3$.

Coalition structure $CS = \{\{a_1, a_2, a_3\}, \{a_4\}\}$.

**Utilities**: $u_{a_1}(CS) = \alpha - 1$, $u_{a_2}(CS) = \alpha + 4$, $u_{a_3}(CS) = -1 + 4 = 3$, $u_{a_4}(CS) = 0$.

**(a) Individually rational for $\alpha \geq 1$**: Each player must prefer their coalition to being alone (utility 0). $a_3$ gets 3 (always IR), $a_4$ gets 0 (always IR), $a_2$ gets $\alpha + 4$ (IR for $\alpha \geq -4$), $a_1$ gets $\alpha - 1$ (IR for $\alpha \geq 1$). Binding constraint: $\alpha \geq 1$.

**(b) Not Nash stable for any $\alpha$**: For Nash stability we need $\alpha \leq 1$ (otherwise $a_4$ has an NS-deviation to join $\{a_1, a_2, a_3\}$). But we also need $\alpha \geq 3$ (otherwise $a_1$ has an NS-deviation to join $\{a_4\}$, getting utility 2 vs. $\alpha - 1$). Since $\alpha \leq 1$ and $\alpha \geq 3$ cannot both hold, $CS$ is **never Nash stable**.

**(c) Core stable iff $3 \leq \alpha \leq 4$**:
- For $\alpha < 3$: $\{a_1, a_4\}$ is a blocking coalition ($a_1$ gets 2 > $\alpha - 1$ for $\alpha < 3$, $a_4$ gets 2 > 0)
- For $\alpha > 4$: $\{a_1, a_2, a_4\}$ is a blocking coalition ($a_1$ gets $\alpha + 2$, $a_2$ gets $2\alpha$, $a_4$ gets $\alpha + 2$; need $2\alpha > \alpha + 4$, i.e., $\alpha > 4$)
- For $3 \leq \alpha \leq 4$: No blocking coalition exists. Single-agent deviations are ruled out by IR. $a_3$ is only better in $\{a_2, a_3\}$ but this is not an improvement for $a_2$. The best coalition for $a_2$ excluding $a_3$ is $\{a_1, a_2, a_4\}$ with utility $2\alpha \leq \alpha + 4$ for $\alpha \leq 4$. $\{a_1, a_4\}$ gives $a_1$ utility 2 $\leq \alpha - 1$ for $\alpha \geq 3$.

### 12.2 Exercise 2: Worst-Case Proposals in GS

**Problem**: Construct an instance where each man makes at least $n - 1$ proposals.

**Solution**: Consider men $m_1, \ldots, m_n$ and women $w_1, \ldots, w_n$ with rankings:
- $m_i$: $w_i \succ w_{i+1} \succ \cdots \succ w_{n-1} \succ w_1 \succ \cdots \succ w_{i-1}$ (for $i = 1, \ldots, n-1$)
- $m_n$: $w_1 \succ \cdots \succ w_n$
- $w_i$: $m_{i+1} \succ \cdots \succ m_n \succ m_1 \succ \cdots \succ m_i$ (for $i = 1, \ldots, n$)

Each man $m_i$ first proposes to $w_i$. Then $m_n$ proposes to $w_1$, displacing $m_1$. Through a cascade of displacements, each man ends up making at least $n - 1$ proposals. The final matching is $m_1 - w_n$, $m_i - w_{i-1}$ for $i = 2, \ldots, n$.

### 12.3 Exercise 3: Identical Preferences

**Problem**: All men rank women in the same order ($w_1 \succ \cdots \succ w_n$), and the $i$-th woman ranks the $i$-th man first.

**Solution**: All men first propose to $w_1$; she accepts $m_1$ and rejects all others. Then remaining men propose to $w_2$; she accepts $m_2$. By induction, the resulting matching is $m_i - w_i$ for all $i = 1, \ldots, n$.

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Non-transferable utility (NTU)** | Setting where payoffs accrue to individuals and cannot be transferred between coalition members |
| **Hedonic game** | Coalition formation game where each player's utility depends only on which coalition she belongs to |
| **Additively separable hedonic game (ASHG)** | Hedonic game where $v_i(S) = \sum_{j \in S \setminus \{i\}} v_i(j)$ |
| **Fractional hedonic game** | Hedonic game where $v_i(S) = \frac{\sum_{j \in S \setminus \{i\}} v_i(j)}{|S|}$ |
| **Individual rationality** | No player prefers being alone to their current coalition |
| **Nash stability** | No player can benefit from moving to another existing coalition or being alone |
| **Individual stability** | No player can benefit from moving to a coalition where all members weakly approve |
| **Contractual individual stability (CIS)** | No player can move such that she benefits, the receiving coalition weakly approves, AND the leaving coalition weakly approves |
| **Core stability (hedonic)** | No group of players $C$ where every member prefers $C$ to their current coalition |
| **Blocking pair** | A man-woman pair who both prefer each other to their current partners |
| **Stable matching** | Perfect matching with no blocking pairs |
| **Valid partner** | Person $x$ is a valid partner of $y$ if they are matched in some stable matching |
| **Man-optimal matching** | Stable matching where each man gets his best valid partner |
| **Women-pessimal matching** | Stable matching where each woman gets her worst valid partner |
| **Strategyproof** | No agent can benefit from misreporting preferences |
| **Deferred Acceptance (DA)** | Gale-Shapley algorithm; men propose in decreasing preference order, women tentatively accept best proposer |
| **Serial Dictatorship (SD)** | Agents choose in fixed order; each picks most preferred available house |
| **Pareto-optimal** | No other allocation makes someone better off without making someone worse off |
| **Top Trading Cycle (TTC)** | Algorithm for house allocation with endowments; agents point to favourite house, houses point to owner, remove cycles |
| **Friends and enemies game** | ASHG where each agent assigns utility $F > 0$ to friends and $E < 0$ to enemies |
| **Friend appreciation game** | Friends and enemies game with $F = n$, $E = -1$; always has non-empty core |
| **Enemy aversion game** | Friends and enemies game with $F = 1$, $E = -n$; always has non-empty core |
| **Stable roommate problem** | One-population matching problem (not bipartite); stable matching may not exist |

---

## Summary

- **LO1 (Core concepts)**: Defined hedonic games formally with players, preferences over coalitions, and partition outcomes. Introduced stability notions including individual rationality, Nash stability, individual stability, CIS, and core stability. Showed the hierarchy of stability concepts and existence/non-existence results (Sections 2, 4).

- **LO2 (Modelling real-world problems)**: Covered applications including university admissions (UCAS), school choice (NYC, Boston), medical residency matching (NRMP), kidney exchange, foster care, and CDNs. Connected house allocation with endowments to kidney exchange (Sections 10, 11).

- **LO3 (Gale-Shapley algorithm)**: Presented the DA algorithm, proved termination in $O(n^2)$, proved it outputs a perfect matching, and proved stability of the output. Also presented Serial Dictatorship and Top Trading Cycle algorithms (Sections 6, 11).

- **LO4 (Existence, uniqueness, properties)**: Proved stable matchings always exist in bipartite settings (GS theorem). Showed stable roommate matchings may not exist. Proved CIS always exists in hedonic games. Showed core may be empty in hedonic games and ASHGs (Sections 4, 5, 6).

- **LO5 (Fairness and efficiency)**: Proved DA outputs man-optimal and women-pessimal matching. Proved SD is Pareto-optimal and core stable but unfair. Proved TTC is individually rational, Pareto-optimal, and core stable (Sections 7, 11).

- **LO6 (Strategic aspects)**: Proved GS is strategyproof for the proposing side but not for the receiving side (with worked counterexample). Proved TTC and SD are strategyproof. Showed impossibility of full strategyproofness for both sides in stable matching (Sections 8, 11).

- **LO7 (Computational exercises)**: Worked through GS algorithm examples (men proposing and women proposing), stability analysis of ASHGs with parameterised weights, and TTC execution (Sections 6.6, 6.7, 11.5, 12).

- **LO8 (Applications and impact)**: Discussed Nobel Prize-winning work of Shapley and Roth, real-world deployment in NRMP, UCAS, NYC schools, kidney exchange clearinghouses, and the transformative impact of matching theory on societal allocation (Sections 10, 11.7).
