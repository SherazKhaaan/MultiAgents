# Week 11: Voting Theory (Part II) -- Multiwinner Elections

## Learning Objectives

- [ ] Explain the principles and objectives of multi-winner voting systems, such as committee selection and proportional representation
- [ ] Describe and distinguish key multi-winner voting rules (e.g., Bloc, Chamberlin-Courant, Proportional Approval Voting)
- [ ] Model group selection and resource allocation problems where more than one winner is needed
- [ ] Analyse the fairness, proportionality, and strategic properties of various multi-winner voting rules
- [ ] Apply algorithms to determine committee or allocation outcomes under different multi-winner rules
- [ ] Evaluate multi-winner systems using criteria like justified representation and its variants
- [ ] Solve theoretical and computational problems related to committee selection, participatory budgeting, or group assignments
- [ ] Discuss real-world applications of multi-winner voting in AI and multi-agent systems

---

## 11.1 Multiwinner Elections

### Three Types of Multiwinner Elections

| Type | Goal | Example |
|------|------|---------|
| **Excellence-based** | Select the $k$ best individuals independently | Shortlisting job candidates, award finalists |
| **Diversity-based** | Select a diverse committee covering different perspectives | Fire station placement, homepage product selection |
| **Proportional representation** | Reflect voter groups proportionally | Parliamentary elections |

### Key Differences from Single-Winner

- Two similar candidates: in excellence-based, select both (or neither); in diversity-based, select at most one
- Rules for shortlisting would produce poor parliaments and vice versa

### Challenges

1. **Axiomatic properties:** How to predict if a rule suits a particular application?
2. **Computational complexity:** Many interesting multiwinner rules are **NP-hard** (unlike most single-winner rules)

### Formal Model

- Election: $(C, R)$ where $C$ = candidates, $R$ = preference profile
- **Ordinal model:** each voter $i$ has a strict linear order $R_i$ over all candidates
- **Approval (dichotomous) model:** each voter $i$ has an approval set $A_i \subseteq C$
- A **multiwinner voting rule** $F$ takes election $(C, R)$ and committee size $k$ ($1 \leq k \leq |C|$), returns nonempty family of size-$k$ subsets of $C$ (winning committees)

### Running Example

| Voter | Ordinal ballot | Approval ballot |
|-------|---------------|-----------------|
| 1 | $a \succ b \succ c \succ d \succ e$ | $\{a, b, c\}$ |
| 2 | $e \succ a \succ b \succ d \succ c$ | $\{a, e\}$ |
| 3 | $d \succ a \succ b \succ c \succ e$ | $\{d\}$ |
| 4 | $c \succ b \succ d \succ e \succ a$ | $\{b, c, d\}$ |
| 5 | $c \succ b \succ e \succ a \succ d$ | $\{b, c\}$ |
| 6 | $b \succ c \succ d \succ e \succ a$ | $\{b\}$ |

### Single Transferable Vote (STV)

Generalises single-winner IRV to committee selection:

1. Compute **quota** $q = \lfloor n/(k+1) \rfloor + 1$
2. Each round:
   - If a candidate is ranked first by $\geq q$ voters: **elect** them, remove $q$ of their supporters, remove candidate from remaining ballots
   - Otherwise: **eliminate** the candidate with fewest first-place votes
3. Repeat until $k$ candidates elected

For $k=1$: $q = \lfloor n/2 \rfloor + 1$ (majority) -- this is exactly IRV.

**STV Example** ($k=2$, $n=6$): $q = \lfloor 6/3 \rfloor + 1 = 3$

- Round 1: a=1, e=1, d=1, c=2, b=1. No quota met. Eliminate a (tie-break).
- Round 2: b=2, c=2, e=1, d=1. No quota. Eliminate d.
- Round 3: b=3 (voters 1,3,6). **B elected.** Remove voters 1,3,6.
- Remaining: voter 2 (top: e), voters 4,5 (top: c). No quota. Eliminate e.
- C gets 3 votes (voters 2,4,5). **C elected.**
- **Winning committee: $\{B, C\}$**

---

## 11.2 Committee Scoring Rules

### Committee Positions

For a size-$k$ committee $S$ and preference order $\succ$:
- **Position** of $S$ in $\succ$ = sorted list of positions of $S$'s members: $\text{pos}_\succ(S) = (i_1, \ldots, i_k)$ with $i_1 \leq \ldots \leq i_k$
- $[m]_k$ = set of all increasing sequences of length $k$ from $\{1, \ldots, m\}$
- Position $I$ **dominates** $J$ if $i_t \leq j_t$ for every $t$

### Committee Scoring Functions

A **committee scoring function** $\gamma_{m,k}: [m]_k \to \mathbb{R}$ assigns scores to committee positions such that if $I$ dominates $J$, then $\gamma_{m,k}(I) \geq \gamma_{m,k}(J)$.

**Committee scoring rule** $F_\gamma$: for election $(C, R)$ and size $k$, output committees $W$ maximising:

$$\text{score}(W, E) = \sum_{i=1}^{n} \gamma_{|C|,k}(\text{pos}_{\succ_i}(W))$$

### Four Key Committee Scoring Rules

**1. Single Non-Transferable Vote (SNTV):**

$$\gamma^{\text{SNTV}}_{m,k}(i_1, \ldots, i_k) = \alpha_1(i_1)$$

Committee gets a point from voter if it contains their **most preferred** candidate. (Only first position matters.)

**2. Bloc:**

$$\gamma^{\text{Bloc}}_{m,k}(i_1, \ldots, i_k) = \sum_{t=1}^{k} \alpha_k(i_t)$$

Each voter names their $k$ favourite candidates; winning committee = those mentioned most. (Top-$k$ positions matter.)

**3. $k$-Borda:**

$$\gamma^{k\text{-Borda}}_{m,k}(i_1, \ldots, i_k) = \sum_{t=1}^{k} \beta_m(i_t)$$

Select $k$ candidates with highest individual Borda scores. (Sum of all individual Borda scores.)

**4. Chamberlin-Courant ($\beta$-CC):**

$$\gamma^{\beta\text{-CC}}_{m,k}(i_1, \ldots, i_k) = \beta_m(i_1)$$

Score from a voter = Borda score of the **highest-ranked** committee member. (Only best representative matters.)

### Worked Example ($k=2$)

**SNTV:** C ranked first by 2 voters (most). Winning committee: $\{C, x\}$ where $x \in \{A, B, D, E\}$.

**Bloc:** Count appearances in top-2 positions: A=3, B=4, C=3, D=1, E=1. Winning committees: $\{A,B\}$ or $\{B,C\}$.

**$k$-Borda:** Borda scores: A=11, B=17, C=14, D=10, E=8. **Winner: $\{B, C\}$**.

**Chamberlin-Courant:** $\{B,C\}$ scores 19. But $\{A,C\}$ scores 21. **Winner: $\{A, C\}$** (each voter's best representative is higher-ranked).

---

## 11.3 Condorcet Committees and Stable Rules

### Condorcet Committee (Fishburn, 1981)

Committee $C$ is a **Condorcet committee** if for every other committee $D$ of the same size, a majority of voters prefer $C$ to $D$. (Requires preferences over committees.)

### Weak Condorcet Set (Gehrlein 1985, Ratliff 2003)

Committee $S$ is a **(weak) Condorcet set** if for every $c \in S$ and every $d \in C \setminus S$: more than half the voters prefer $c$ to $d$.

A multiwinner rule is **stable** if it outputs a weak Condorcet set whenever one exists.

### Stable Multiwinner Rules

**Number of External Defeats (NED):**
- Score of committee $S$ = number of pairs $(c, d)$ with $c \in S$, $d \in C \setminus S$, where at least half the voters prefer $c$ to $d$
- Highest score wins

**Minimum Size of External Opposition (SEO):**

$$\text{score}(S) = \min_{c \in S, d \in C \setminus S} |\{i \in N : c \succ_i d\}|$$

- Score = smallest number of voters preferring any committee member to any non-member
- Highest score wins

---

## 11.4 Approval-Based Rules (Thiele Methods)

### Setting

- Each voter $i$ has approval ballot $A_i \subseteq C$
- **Utility** of voter $i$ for committee $W$: $u_i(W) = |A_i \cap W|$

### $w$-AV Rules (Thiele, 1895)

Given weight vector $w^{(k)} = (w_1^{(k)}, \ldots, w_k^{(k)})$:

$$\text{score}_i^{w^{(k)}}(S) = \sum_{j=1}^{|S \cap A_i|} w_j^{(k)}$$

The $w$-AV rule outputs committees maximising $\sum_{i \in N} \text{score}_i^{w^{(k)}}(S)$.

### Three Key Thiele Methods

| Rule | Weight Vector | Score Formula | Goal |
|------|--------------|---------------|------|
| **Approval Voting (AV)** | $(1, 1, \ldots, 1)$ | $\sum_{i \in N} |A_i \cap W|$ | Excellence/total approvals |
| **Approval-based CC ($\alpha$-CC)** | $(1, 0, \ldots, 0)$ | $\sum_{i \in N} \mathbb{1}_{A_i \cap W \neq \emptyset}$ | Diversity/coverage |
| **Proportional Approval Voting (PAV)** | $(1, 1/2, 1/3, \ldots, 1/k)$ | $\sum_{i \in N} H(|A_i \cap W|)$ | Proportional representation |

Where $H(x) = 1 + 1/2 + 1/3 + \ldots + 1/x$ is the $x$-th harmonic number.

**Intuition:**
- **AV:** each additional representative gives equal marginal utility
- **CC:** only the first representative matters (coverage)
- **PAV:** diminishing returns -- first representative worth 1, second worth 1/2, third 1/3, etc.

---

## 11.5 Proportional Representation

### What is Proportionality?

The winning committee should reflect different voter groups in rough proportion to their size. If a **cohesive group** of $\geq \ell \cdot n/k$ voters agrees on $\geq \ell$ candidates, they deserve $\geq \ell$ seats.

### Justified Representation (JR)

**Definition:** A rule satisfies **JR** if: whenever there exists $S \subseteq N$ with $|S| \geq n/k$ and $|\bigcap_{i \in S} A_i| \geq 1$, then $\exists i \in S$ such that $u_i(W) \geq 1$.

*Meaning:* If a group of $\geq n/k$ voters unanimously approves at least one common candidate, at least one member of this group must have a representative in the committee.

### Extended Justified Representation (EJR)

**Definition:** A rule satisfies **EJR** if: for each $\ell \in [k]$, whenever there exists $S \subseteq N$ with $|S| \geq \ell \cdot n/k$ and $|\bigcap_{i \in S} A_i| \geq \ell$, then $\exists i \in S$ such that $u_i(W) \geq \ell$.

EJR is **strictly stronger** than JR (JR = EJR with $\ell = 1$).

### Which Rules Satisfy JR/EJR?

| Rule | JR? | EJR? |
|------|-----|------|
| **Approval Voting (AV)** | **No** | **No** |
| **Chamberlin-Courant (CC)** | **Yes** | **No** |
| **Proportional Approval Voting (PAV)** | **Yes** | **Yes** |

**Theorem: CC satisfies JR.** *Proof:* Suppose CC committee $W$ violates JR via group $S$. Then $W$ covers fewer than $n$ voters, so some $c \in W$ covers $< n/k$ voters. Replace $c$ with the commonly approved candidate of $S$ -- this gives a higher CC score, contradicting optimality. $\square$

**Theorem: PAV satisfies EJR.** *Proof sketch:* Suppose PAV committee $W$ violates EJR via group $S$ ($|S| \geq \ell \cdot n/k$, all approving $\ell$ common candidates, but $u_i(W) < \ell$ for all $i \in S$). Pick $c^* \in \bigcap_{i \in S} A_i \setminus W$. Adding $c^*$ increases PAV score by $\geq |S| \cdot 1/\ell \geq n/k$. The average loss from removing one of the $k+1$ candidates in $W \cup \{c^*\}$ is $< n/k$ (since total score contribution $\leq n$). By pigeonhole, some $c'$ can be removed with loss $< n/k$, giving $(W \cup \{c^*\}) \setminus \{c'\}$ a higher PAV score -- contradicting optimality of $W$. $\square$

### Party-List Example

4 parties ($P_1, P_2, P_3, P_4$) with 12 candidates each ($m=48$), $n=22$ voters, $k=11$.

Supporters: $P_1$: 6, $P_2$: 4, $P_3$: 10, $P_4$: 2.

With PAV (harmonic weights), seats allocated greedily by marginal contribution:
- $P_3$ gets first seat (+10), then $P_1$ (+6), then $P_3$ (+5), then $P_2$ (+4), ...
- Final allocation: $P_1$: 3 seats, $P_2$: 2, $P_3$: 5, $P_4$: 1

**Proportionality check:** If party has $x$ supporters, it deserves $\ell$ seats when $x \geq \ell \cdot n/k = 2\ell$.

---

## Participatory Budgeting (from LGT)

### Model

- Set $C$ of **projects**, each with cost $\text{cost}(c) \geq 0$
- Set $N$ of $n$ voters, each approving $A_i \subseteq C$
- Total budget $B$
- Outcome: $W \subseteq C$ with $\sum_{c \in W} \text{cost}(c) \leq B$
- If all costs = 1 and $B$ is integer, this reduces to committee election

### Greedy Method

1. $R \leftarrow C$, $W \leftarrow \emptyset$
2. While $R \neq \emptyset$:
   - Pick $c^* = \arg\max_{c \in R} |\{i \in N : c \in A_i\}|$ (most-approved project)
   - If affordable: $W \leftarrow W \cup \{c^*\}$
   - $R \leftarrow R \setminus \{c^*\}$
3. Return $W$

The greedy method orders by **vote count** (= bang-per-buck since $v_c \cdot \text{cost}(c) / \text{cost}(c) = v_c$), approximately solving a **knapsack** problem with payoffs $v_c \cdot \text{cost}(c)$.

This implies cities implicitly assume **cost utilities**: $u_i(W) = \text{cost}(A_i \cap W)$.

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Multiwinner rule** | Maps election + committee size $k$ to set of size-$k$ committees |
| **STV** | Iterative: elect candidates meeting quota $q = \lfloor n/(k+1) \rfloor + 1$; eliminate weakest |
| **SNTV** | Score = voters whose top choice is in committee |
| **Bloc** | Score = total top-$k$ mentions |
| **$k$-Borda** | $k$ candidates with highest individual Borda scores |
| **Chamberlin-Courant** | Score = sum of each voter's best representative's Borda score |
| **Condorcet set** | Every member beats every non-member pairwise by majority |
| **NED / SEO** | Condorcet-consistent multiwinner rules |
| **AV** | Thiele weights $(1,1,\ldots)$; maximise total approvals |
| **$\alpha$-CC** | Thiele weights $(1,0,\ldots)$; maximise covered voters |
| **PAV** | Thiele weights $(1, 1/2, 1/3, \ldots)$; proportional representation |
| **JR** | Group of $\geq n/k$ with common candidate must have a represented member |
| **EJR** | Group of $\geq \ell \cdot n/k$ with $\ell$ common candidates needs member with $\geq \ell$ reps |
| **Participatory budgeting** | Select projects under budget constraint |

---

## Summary

- **Multiwinner elections** select committees and arise in parliaments, recommendations, shortlisting, and resource allocation
- Three goals: **excellence**, **diversity**, **proportional representation** -- different rules suit different goals
- **STV** generalises IRV using quota $q = \lfloor n/(k+1) \rfloor + 1$
- **Committee scoring rules** (SNTV, Bloc, $k$-Borda, CC) extend PSRs; CC captures diversity, $k$-Borda captures excellence
- **Condorcet sets** and **stable rules** (NED, SEO) extend Condorcet consistency
- **Thiele methods** for approval elections: AV (excellence), $\alpha$-CC (diversity), **PAV** (proportionality)
- **PAV** with harmonic weights $(1, 1/2, 1/3, \ldots)$ is the unique sequence achieving proportional representation; it satisfies **EJR**
- CC satisfies JR but not EJR; AV fails both
- **Participatory budgeting** generalises committee elections to projects with costs; the greedy method approximately maximises utilitarian cost-weighted welfare
