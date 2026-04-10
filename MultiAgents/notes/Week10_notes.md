# Week 10: Voting Theory (Part I)

## Learning Objectives

- [ ] Explain fundamental concepts of voting theory, including preference aggregation, voting rules, and social choice functions
- [ ] Describe and compare classical voting systems (e.g., plurality, Borda, approval, STV), identifying their properties and susceptibilities
- [ ] Model group decision problems using formal voting frameworks, translating real-world scenarios into mathematical terms
- [ ] Analyse the strengths, limitations, and vulnerabilities of various voting rules, such as susceptibility to strategic voting or manipulation
- [ ] Apply mathematical methods and algorithms to solve voting problems and determine election winners for different rules
- [ ] Solve theoretical and computational problems involving collective decision making and social choice
- [ ] Discuss the role and impact of voting theory in societal, organisational, and computational contexts

---

## 10.1 Voting Theory: Introduction

### Computational Social Choice

- Field at the intersection of **algorithms, game theory, and social choice**
- Studies how groups of agents make **collective decisions** in a principled way
- Analyses how **voting rules** aggregate individual preferences into a single outcome
- Explores **paradoxes** and **impossibility results** (e.g., Arrow, Gibbard-Satterthwaite)
- Investigates how **computational complexity** affects feasibility
- Shows how complexity can **protect systems from strategic manipulation**

### Applications Beyond Political Elections

**Recommender systems:** aggregate user ratings via voting rules to represent diverse tastes.

**Resource allocation:** choose subsets of projects in participatory budgeting; allocate resources fairly.

**Multi-agent AI:** multiple agents/models "vote" over actions/plans; coordinate swarms, robot teams, distributed AI.

### Setting

- **Set of alternatives** (candidates): $C = \{c_1, \ldots, c_m\}$
- **Set of voters** (agents): $N = \{1, \ldots, n\}$
- **Voter preferences:** ranking, approval set, or scores over alternatives
- **Preference profile** $R$: collection of all voters' preferences
- **Aggregation:** voting rule takes $R$ and returns a collective decision

### Preference Formats

| Format | Description |
|--------|-------------|
| **Rankings** | Full ordering from most to least preferred |
| **Approval sets** | Subset of "approved" candidates |
| **Scores/stars** | Numerical rating per candidate (e.g., 1-5) |

### Outcome Formats

| Type | Output |
|------|--------|
| **Single-winner rules** (social choice functions) | One winning alternative |
| **Multi-winner rules** | Committee or set of $k$ winners |
| **Social welfare functions** | Complete ranking of all alternatives |

---

## 10.2 Single-Winner Voting Rules

### Formal Model

- Finite set $C = \{c_1, \ldots, c_m\}$, $m \geq 2$
- $\mathcal{L}(C)$: set of all **strict linear orders** on $C$
- Each voter $i$ supplies ballot $R_i$, giving profile $R = (R_1, \ldots, R_n) \in \mathcal{L}(C)^n$
- **Voting rule:** $F: \mathcal{L}(C)^n \to 2^C \setminus \{\emptyset\}$
- **Resolute** if $|F(R)| = 1$ for all $R$; most rules are **irresolute** (need tie-breaking)

### Plurality

**Definition:** Elect the alternative ranked first most often. Scoring vector $(1, 0, \ldots, 0)$.

- **Anonymous** and **neutral**
- For 2 candidates: selects majority winner
- For 3+ candidates: winner may lack majority support; can elect a Condorcet loser

**Worked Example:**

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| a | a | b | c | d |
| b | b | c | b | b |
| c | c | d | d | c |
| d | d | a | a | a |

Plurality: a=2, b=1, c=1, d=1. **Winner: a**. But voters 3,4,5 rank a last. B is ranked 1st or 2nd by everyone and beats a head-to-head 3-2.

### Borda Count

**Definition:** $m-1$ points for 1st, $m-2$ for 2nd, ..., 0 for last. Scoring vector $(m-1, m-2, \ldots, 0)$.

**Same example:** a=6, b=11, c=8, d=5. **Borda winner: b**.

### Positional Scoring Rules (PSR)

**Definition:** Defined by scoring vector $s = (s_1, \ldots, s_m)$ with $s_1 \geq s_2 \geq \ldots \geq s_m$ and $s_1 > s_m$.

| Rule | Scoring Vector |
|------|---------------|
| **Borda** | $(m-1, m-2, \ldots, 0)$ |
| **Plurality** | $(1, 0, \ldots, 0)$ |
| **Veto** | $(1, 1, \ldots, 1, 0)$ |
| **$k$-approval** | $(\underbrace{1,\ldots,1}_{k}, 0, \ldots, 0)$ |

### Elimination-Based Methods

**Plurality with runoff:** Top two from plurality go to a majority runoff.

**Instant-Runoff Voting (IRV):** Repeatedly eliminate the candidate with fewest first-place votes; last standing wins. Used in Ireland, Australia, Maine, Alaska, NYC.

**IRV Worked Example** (same profile):

- Round 1: a=2, b=1, c=1, d=1. Eliminate b (alphabetical tie-break)
- Round 2 (without b): a=2, c=2, d=1. Eliminate d
- Round 3: a=2, c=3. **Winner: c**

IRV eliminated b, who was the **Condorcet winner**.

---

## 10.3 Condorcet Principle

### Condorcet's Paradox

Majority preferences can be **cyclical**: $a \succ b \succ c \succ a$ (each by a different majority). No clear winner.

Example: 3 voters, 3 alternatives with cyclically shifted rankings.

### Condorcet Winner

A **Condorcet winner** defeats every other candidate in pairwise majority comparison.

The **Condorcet criterion** requires electing the Condorcet winner whenever one exists.

### Condorcet Consistency of Common Rules

**No PSR is Condorcet-consistent** (for $m \geq 3$): proven for any scoring vector.

- **Plurality, Borda, IRV** all fail Condorcet consistency (examples shown above)

### Condorcet-Consistent Methods

**Copeland's rule (Llull's rule):**
- +1 per pairwise win, +0.5 per tie
- **Condorcet-consistent:** Condorcet winner scores $m-1$ (uniquely maximal)

**Copeland Example:** A=0, B=3, C=2, D=1. **Winner: B** (Condorcet winner).

**Maximin rule:**
- For each candidate, find minimum pairwise support
- Elect candidate with highest minimum
- **Condorcet-consistent:** Condorcet winner's minimum $> n/2$

**Dodgson's rule:**
- Score = minimum adjacent swaps to become Condorcet winner
- Condorcet winner has score 0
- **NP-hard** to compute

**Dodgson Example:** B needs 3 swaps (swap B-C in voter 4, B-D in voter 4, A-B in voter 1). Dodgson score of B = 3.

---

## Strategic Manipulation (from LGT)

### Definitions

- **Ballot** $\neq$ **true preference**: voter may misreport
- $F$ is **strategyproof** if no voter $i$, profile $R$ (with $i$'s truthful ranking), and untruthful ballot $R'_i$ exist such that $R_i$ ranks $F(R'_i, R_{-i})$ above $F(R)$

### Manipulation Examples

**Borda manipulation:** Voter 3 (true: $a \succ b \succ c \succ d$) changes to $a \succ c \succ d \succ b$, dropping b from 8 to 6 points, making a win instead.

**Plurality:** Strategyproof for 2 alternatives, not for 3+ (vote for second choice to prevent third choice winning).

### Gibbard-Satterthwaite Theorem

**Definitions:**
- **Onto (surjective):** every candidate can win under some profile
- **Dictatorial:** one voter's top choice always wins

**Theorem:** Let $m \geq 3$. A resolute SCF $F$ is strategyproof and onto $C$ **if and only if** $F$ is a dictatorship.

**Implication:** Any non-dictatorial, onto voting rule with $m \geq 3$ is **manipulable**.

**Proof sketch** (with neutrality, $m \geq n$):
1. **Strong monotonicity:** If $F$ is SP and $F(R)=a$, then $F(R')=a$ for all $R'$ preserving $a$'s relative position above others
2. **Unanimity:** If all voters rank $a$ above $b$ and $F$ is SP+onto, then $F(R) \neq b$
3. Construct symmetric cyclic profile; by WLOG, $F(R) = a$; use strong monotonicity to push all other voters' $a$ to last; show voter 1 must be a dictator via neutrality

### Barriers to Manipulation

**1. Domain restriction -- Single-peaked preferences:**

Profile is **single-peaked** w.r.t. ordering $\gg$ if each voter's preference decreases monotonically away from their peak on the line.

- Condorcet cycles **cannot** occur
- Condorcet winner always exists (odd $n$) = candidate at **median peak**
- **Median-voter rule** is **strategyproof**

**Black's Median Voter Theorem:** Under single-peaked preferences (odd $n$), Condorcet winner exists and equals the median peak.

**2. Computational barriers:**

If the **$F$-manipulation problem** (given non-manipulators' votes, can a manipulator make preferred candidate $p$ win?) is **NP-hard**, then $F$ is **resistant** to manipulation.

---

## Exercises (SGT10)

### Exercise 1: 100-Voter Profile

| 33 | 16 | 3 | 8 | 18 | 22 |
|----|-----|---|---|-----|-----|
| a | b | c | c | d | e |
| b | d | d | e | e | c |
| c | c | b | b | c | b |
| d | e | a | d | b | d |
| e | a | e | a | a | a |

Compute winners under plurality, Borda, Llull's, Dodgson's, maximin, and IRV.

### Exercise 2: Impossibility of Anonymous + Neutral (2 voters, 2 alternatives)

With voter 1: $a \succ b$, voter 2: $b \succ a$. Anonymity: swapping voters doesn't change outcome. Neutrality: swapping $a \leftrightarrow b$ in all rankings should swap the winner. But the profile is symmetric under both operations -- contradiction.

### Exercise 3: No PSR is Condorcet-Consistent ($m \geq 3$)

Case $s_2 = 0$: this is plurality, already shown. Case $s_2 > 0$: modify the Borda counterexample.

### Exercise 4: Approval Voting is Non-Manipulable

Voter's only deviation: approve different subset. But approving a less-preferred candidate only helps that candidate; removing approval from a preferred candidate only hurts them. No beneficial manipulation exists.

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Plurality** | PSR $(1,0,\ldots,0)$; top-choice count |
| **Borda count** | PSR $(m-1, m-2, \ldots, 0)$ |
| **Veto** | PSR $(1,1,\ldots,1,0)$ |
| **IRV/STV** | Iteratively eliminate lowest-plurality candidate |
| **Condorcet winner** | Beats every other candidate head-to-head |
| **Condorcet cycle** | Cyclical majority preferences |
| **Copeland** | +1 per pairwise win; Condorcet-consistent |
| **Maximin** | Best worst-case pairwise support; Condorcet-consistent |
| **Dodgson** | Min swaps to become Condorcet winner; NP-hard |
| **Strategyproof** | No voter benefits from misreporting |
| **Gibbard-Satterthwaite** | SP + onto $\iff$ dictatorship (for $m \geq 3$) |
| **Single-peaked** | Preferences decrease away from peak on a line |
| **Median-voter rule** | Elect median peak; SP for single-peaked prefs |

---

## Summary

- **Voting theory** aggregates individual preferences into collective decisions
- **PSRs** (plurality, Borda, veto, $k$-approval) assign points by rank; none is Condorcet-consistent for $m \geq 3$
- **IRV** eliminates candidates iteratively but can eliminate the Condorcet winner
- **Condorcet methods** (Copeland, Maximin, Dodgson) elect the pairwise majority champion when one exists
- **Condorcet's paradox:** majority preferences can cycle
- **Gibbard-Satterthwaite:** any non-dictatorial onto rule with $\geq 3$ candidates is manipulable
- **Single-peaked preferences** allow strategyproof rules (median-voter)
- **Computational complexity** can serve as a barrier to manipulation
