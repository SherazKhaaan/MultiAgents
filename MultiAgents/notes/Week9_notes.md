# Week 9: Mechanism Design and Auctions

## Learning Objectives

- [ ] Describe core concepts of mechanism design, including social choice functions, incentive compatibility, and strategyproofness
- [ ] Model strategic environments using mechanisms for resource allocation, public goods provision, and collective decision making
- [ ] Analyse key mechanism design theorems (e.g., Revelation Principle) and their implications for designing robust systems
- [ ] Evaluate mechanisms in terms of efficiency, fairness, and susceptibility to manipulation by self-interested agents
- [ ] Apply design principles to construct mechanisms that achieve desired objectives, such as truthful reporting or optimal revenue
- [ ] Assess real-world applications of mechanism design in economics, computer science, and multi-agent environments
- [ ] Reflect on trade-offs between robustness, practicality, and optimality in the design and implementation of mechanisms

---

## 9.1 Auctions and Mechanism Design

### Game Theory in Multi-Agent Systems

Game theory helps three roles in MAS:

1. **The agents** -- to understand what are best/reasonable/safe strategies to take
2. **The system administrator** -- to predict possible system outcomes and make agents achieve stable/optimal ones
3. **The system designer** -- to design systems with desirable outcomes

### What is Mechanism Design?

- Equilibrium outcomes in some games are **undesirable** (e.g., Prisoner's Dilemma, Centipede game)
- **Mechanism design** flips the problem: instead of analysing a given game, we **design the game itself**
- Goal: specify action spaces, information flows, and payoff rules so that certain **objectives are achieved at equilibrium** when each agent maximises their own expected utility
- This framework underpins **auction theory**, **voting systems**, **resource allocation protocols**

### Examples of Mechanism Design Goals

- **Elections:** design voting protocols to minimise unsatisfied voters or ensure a particular candidate wins
- **Marketplaces:** design auctions such that:
  - The outcome is **efficient** (maximises sum of utilities)
  - Or maximises/minimises **seller's profit**

### What is an Auction?

- **Auctions** are protocols for **multi-agent resource allocation**
- A tool for allocating discrete resources/goods among selfish agents
- Formally: any protocol that allows agents to indicate interest in resources and uses these indications to determine both an **allocation** and a set of **payments**

### Why Auctions Matter

1. **Practical importance:**
   - Millions use auctions daily on internet consumer websites
   - Governments use auctions to sell public resources (e.g., electromagnetic spectrum)
   - All **financial markets** are a type of auction (double auctions)
   - Used in computational settings to allocate bandwidth/processing power

2. **Theoretical importance:**
   - Provide a general framework for understanding **resource allocation among self-interested agents**
   - Important even in settings not normally thought of as auctions (e.g., sharing computational power in grid computers)

---

## 9.2 Single-Good Auctions

### Setting

- **One** good for sale, **one** seller, **multiple** potential buyers
- Each buyer has a **private valuation** $\theta_i$ (willingness to pay), known only to themselves
- **Single-sided** auction: competition only among buyers
- These auctions capture essential trade-offs: **efficiency**, **revenue**, **incentive compatibility**

### Four Classic Auction Formats

| Auction | Format | Winner Pays |
|---------|--------|-------------|
| **English** (ascending) | Open-cry; bidding starts low, bidders raise price | Highest bid (own bid) |
| **Dutch** (descending) | Open-cry; price starts high, auctioneer lowers until someone bids | Current price when first bidder calls |
| **First-price sealed-bid** | Sealed envelopes; highest bidder wins | Own bid |
| **Second-price sealed-bid (Vickrey)** | Sealed envelopes; highest bidder wins | Second-highest bid (or reserve price) |

### Formal Model

- Each bidder $i$ has a **private valuation** $\theta_i$ for the item
- **Utility** (quasi-linear):

$$u_i = \begin{cases} \theta_i - p_i & \text{if } i \text{ wins the item and pays } p_i \\ 0 & \text{otherwise} \end{cases}$$

- $\theta_i$ is the price at which bidder $i$ is **indifferent** between winning and losing
- Utility does **not** depend on other agents' values
- Bidders do not know others' valuations but have **beliefs** about their distribution $F$ (with density $f$)
- Bidders maximise **expected utility**
- We assume (initially) **no collusion**

### Bayesian Games

A **Bayesian game** is a tuple $(N, (A_i, \Theta_i, u_i)_{i \in N}, Pr)$ where:

- $N$ = set of $n$ agents
- $A_i$ = set of actions available to player $i$
- $\Theta_i$ = **type space** of player $i$
- $Pr: \Theta_1 \times \ldots \times \Theta_n \to [0,1]$ = **common prior** over types
- $u_i: (\times_{i \in N} A_i) \times \Theta_i \to \mathbb{R}$ = utility function for player $i$

A **strategy** is a mapping $s_i: \Theta_i \to A_i$

**Expected utility** of player $i$:

$$\sum_{\theta_{-i}} Pr(\theta_{-i}) \cdot u_i(\theta_i, s_i(\theta_i), s_{-i}(\theta_{-i}))$$

### Bayes-Nash Equilibrium (BNE)

A strategy profile $s$ is a **Bayes-Nash equilibrium** if for every $i \in N$, $\theta_i \in \Theta_i$, and $a_i \in A_i$:

$$\sum_{\theta_{-i}} Pr(\theta_{-i}) \cdot u_i(\theta_i, s_i(\theta_i), s_{-i}(\theta_{-i})) \geq \sum_{\theta_{-i}} Pr(\theta_{-i}) \cdot u_i(\theta_i, a_i, s_{-i}(\theta_{-i}))$$

### First-Price Sealed-Bid Auction: Worked Example

Two players: $\theta_1 = 4$, $\theta_2 = 2$. Bids $b_1, b_2 \in \{0, 1, 2, 3, 4\}$. Ties broken randomly.

**Payoff matrix** (first-price):

|  | $b_2=0$ | $b_2=1$ | $b_2=2$ | $b_2=3$ | $b_2=4$ |
|--|---------|---------|---------|---------|---------|
| $b_1=0$ | 2, 1 | 0, 1 | 0, 0 | 0, -1 | 0, -2 |
| $b_1=1$ | 3, 0 | 1.5, 0.5 | 0, 0 | 0, -1 | 0, -2 |
| $b_1=2$ | 2, 0 | 2, 0 | 1, 0 | 0, -1 | 0, -2 |
| $b_1=3$ | 1, 0 | 1, 0 | 1, 0 | 0.5, -0.5 | 0, -2 |
| $b_1=4$ | 0, 0 | 0, 0 | 0, 0 | 0, 0 | 0, -1 |

**Missing aspect:** This assumes known valuations, but valuations are **private information**.

### First-Price Sealed-Bid: BNE (Continuous)

With $\Theta = [0, 1]$, i.i.d. uniform prior $U(0,1)$:

**Theorem:** The BNE strategy of player $i$ is to bid:

$$s_i(\theta_i) = \frac{n-1}{n} \cdot \theta_i$$

- Bidders **shade their bid** below their true value
- Shading decreases as $n \to \infty$ (more competition $\implies$ bid closer to true value)
- For $n = 2$: bid $\frac{1}{2}\theta_i$
- Strategy is **monotonically increasing** $\implies$ highest-value bidder always wins $\implies$ auction is **efficient**

### Strategic Equivalences

**Dutch auction $\equiv$ First-price sealed-bid:**
- In both, bidders make trade-offs between probability of winning and payment
- Same strategy sets $\implies$ same BNE bid functions
- Dutch is sometimes called the **open first-price auction**

**English auction $\equiv$ Second-price sealed-bid (Vickrey):**
- In English auction, bidder drops out when price exceeds their valuation
- Winner pays slightly above second-highest valuation
- English is sometimes called the **open second-price auction**

### Vickrey Auction: Truthfulness

**Theorem:** In the second-price sealed-bid auction, bidding your true valuation $\theta_i$ is a **weakly dominant strategy**.

Such an auction is called **truthful** / **strategyproof** / **incentive compatible in dominant strategies**.

**Proof (intuition):**

**Case 1: You win the auction (bidding truthfully)**
- Payment = second-highest bid (does not depend on your bid)
- Bidding **lower**: no change to payment, but risk losing the item
- Bidding **higher**: no change to outcome (you already won)

**Case 2: You lose the auction (bidding truthfully)**
- Bidding **lower**: no change (still lose)
- Bidding **higher**: you might win, but then the second-highest bid exceeds your true valuation $\implies$ **negative utility**

Therefore, there is never an incentive to deviate from truthful bidding. $\square$

### Revenue Equivalence Theorem

Under the following assumptions:
- Valuations are **i.i.d.** drawn from a continuous distribution on $[L, H]$
- Agents are **risk-neutral** (expected utility maximisers)

**Theorem:** Any two auctions that (1) allocate the item in equilibrium to the bidder with the highest valuation, and (2) give utility zero to the agent with the lowest possible valuation, yield the **same expected revenue** to the auctioneer.

$\implies$ All four classic auctions (English, Dutch, first-price, second-price) are **revenue equivalent**.

---

## 9.3 Collusion and Other Issues

### Collusion

- In **second-price** and **English** auctions, agents have no individual incentive to misreport, but they **can benefit by coordinating bids** (collusion)

**English auction collusion:**
- A **bidding ring** agrees not to bid against each other
- Item obtained at artificially low price, then allocated/resold among ring members
- Defection is **visible** and can be punished $\implies$ ring is stable

**Dutch auction is robust to collusion:**
- Nothing stops a member from breaking the agreement (others have no opportunity to respond)

### Collusion in Second-Price Auction: Worked Example

**Two colluding bidders** (bidders 1 and 2), $\theta_1 > \theta_2$, no other bidders:

- **Honest play:** Player 1 wins, pays $\theta_2$. Total surplus = $\theta_1 - \theta_2$
- **Optimal collusion:** Player 2 bids 0, Player 1 bids any positive amount. Player 1 wins, pays 0. Total surplus = $\theta_1$
- **Extra surplus from collusion** = $\theta_2$, split evenly: each gets $\theta_2/2$

**With a third non-colluding player** ($\theta_3 \sim U[0,1]$):

- Optimal: Player 2 bids 0, Player 1 bids $\theta_1$ (truthfully, playing a 2-player game against player 3)
- Honest expected payoff: $\frac{\theta_1^2 - \theta_2^2}{2}$
- Colluding expected payoff: $\frac{\theta_1^2}{2}$
- **Extra surplus** = $\frac{\theta_2^2}{2}$, each colluder gets $\frac{\theta_2^2}{4}$

### Auctioneer Manipulation

- In **second-price auction:** dishonest auctioneer can lie about the second-highest bid (nobody can verify)
- In **English auction:** auctioneer can introduce **shill bids** to inflate prices

### Winner's Curse

Occurs in auctions with **common value** and **incomplete information**:

- All bidders value the item roughly equally, but the true value is **unknown**
- Each bidder independently **estimates** the value
- The **winner** is the bidder with the **highest estimate** -- likely an **overestimate**
- **Formally:** $E[\text{value of item} - \text{price} \mid \text{winning}] < 0$

**Examples:** offshore oil field auctions (1950s), spectrum auctions, IPOs, pay-per-click advertising

**Key insight:** Winning the auction is **bad news** about the item's value -- it means you were the most optimistic.

**Mitigation:** **Bid shading** -- bid below your ex-ante estimate, equal to your ex-post belief about value given that you win.

Winner's curse is **more severe with more bidders** (the maximum of more estimates is further from the mean).

---

## 9.4 VCG and Other Auctions

### Reverse Auctions

- **One buyer** accepts bids from **multiple sellers** (e.g., insurance quotes)
- Same analysis as regular auctions but swap buyer/seller and negate prices

### Auctions with Entry Costs

- Bidders pay a cost to participate (researching, driving, time)
- For **second-price/English:** once you decide to enter, truthful bidding remains optimal
- For **first-price:** equilibrium strategy depends on number of participants -- harder to analyse

### Multi-Unit Auctions

$k$ identical copies of one good, multiple bidders:

**Payment rules:**
- **Discriminatory pricing:** each winning bidder pays their own bid
- **Uniform pricing:** all winners pay the same (highest losing bid or lowest winning bid)

**Bid types:**
- **All-or-nothing:** bidder names a quantity and won't accept fewer
- **Divisible:** bidder names a quantity but accepts any smaller number at same per-unit price

### K+1 Price Auction (Multi-Unit Vickrey)

For $k$ identical goods with **single-unit demand** (each bidder wants at most 1 item):

- Sell $k$ goods to the $k$ highest bidders
- **Price** = $(k+1)$-st highest bid (same for all winners)
- This is a **special case of VCG**

### Combinatorial Auctions

- Multiple **different** goods; bidders value **combinations** of goods
- Valuations depend strongly on which **set of goods** a bidder receives (complementarities)
- Examples: spectrum auctions, energy auctions, procurement, network bandwidth

**Formal model:**
- Set of $n$ bidders, set of $m$ items $G$
- Types $\hat{\theta}_1, \ldots, \hat{\theta}_n$
- Valuation function $v(S, \theta_i)$ for subset $S \subseteq G$ and type $\theta_i$
- A **mechanism** is a pair $(F, T)$:
  - $F$: **allocation function** (maps reported types to feasible allocation)
  - $T$: **transfer/payment function**
- **Utility** (quasi-linear): $u_i(x, t, \theta_i) = v(x_i, \theta_i) + t_i$ (where $t_i < 0$ means agent pays)

### The VCG Mechanism

**Allocation function:** Choose the allocation that **maximises total reported welfare**:

$$F(\hat{\theta}) = \arg\max_{x \in \mathcal{F}} \sum_{i \in N} v(x_i, \hat{\theta}_i)$$

**Transfer function:** Pay each agent the amount by which their presence **affects other participants**:

$$t_i = \sum_{j \neq i} v(x_j, \hat{\theta}_j) - \max_{x' \in \mathcal{F}_{-i}} \sum_{j \neq i} v(x'_j, \hat{\theta}_j)$$

Where:
- First term: total value of **other agents** under allocation with $i$ present
- Second term: maximum total value of other agents **without** $i$

If $t_i < 0$: agent $i$ **pays** to the mechanism (their presence hurts others by displacing them).

### Second-Price Auction as Special Case of VCG

- **Allocation:** give item to highest bidder (efficient)
- **Transfer for winner:** when winner present, others get 0; when winner absent, second-highest bidder gets their value $\theta_{(2)}$
  - $t_{\text{winner}} = 0 - \theta_{(2)} = -\theta_{(2)}$ (pay the second-highest bid)
- **Transfer for losers:** $t_i = 0$ (no effect on allocation)

### Properties of VCG

| Property | Holds? |
|----------|--------|
| **Efficient** | Yes -- maximises total welfare |
| **Dominant-strategy truthful** | Yes -- truthful reporting is weakly dominant |
| **Individually rational** | Yes -- every agent gets non-negative utility |
| **Weakly budget-balanced** | Yes -- never pays more than it collects |
| **Strongly budget-balanced** | No -- may have surplus |

### Double Auctions

- **Many buyers** and **many sellers** -- typical in financial/stock markets
- **Continuous double auction:** buyers and sellers bid at their own pace, continuously
- **Equilibrium price:** where demand curve meets supply curve
- Trades occur for buyer-seller pairs where buyer's bid $\geq$ seller's ask

---

## Exercises and Solutions

### LGT Exercise 1: Second-Price Auction Expected Revenue

**(a) Two bidders**, values $v_i \in \{1, 2\}$ each with probability $1/2$.

Four possible pairs $(v_1, v_2)$ each with probability $1/4$: $(1,1), (1,2), (2,1), (2,2)$.

Revenue (= second-highest bid) is 1 in first three cases, 2 in last case.

$$E[\text{revenue}] = 1 \cdot \frac{3}{4} + 2 \cdot \frac{1}{4} = \frac{5}{4}$$

**(b) Three bidders**, values $v_i \in \{1, 2\}$ each with probability $1/2$.

Eight combinations, each with probability $1/8$. Revenue is 1 in first four cases (at most one bidder has value 2), 2 in last four cases.

$$E[\text{revenue}] = 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{2} = \frac{3}{2}$$

**(c)** As number of bidders increases, expected revenue increases because the expected second-highest bid grows.

**(d) Reserve price** $R$ with $1 < R < 2$, two bidders:

Revenue is 0 when $(1,1)$, $R$ when $(1,2)$ or $(2,1)$, and 2 when $(2,2)$:

$$E[\text{revenue}] = 0 \cdot \frac{1}{4} + R \cdot \frac{2}{4} + 2 \cdot \frac{1}{4} = \frac{R+1}{2}$$

**(e)** Reserve price is beneficial when $\frac{R+1}{2} \geq \frac{5}{4}$, i.e., $R \geq \frac{3}{2}$. So a revenue-maximising seller would never set $R$ between 1 and 1.5.

**(f) Entry fee of 0.5**, two potential bidders, values $\in \{1,2\}$ each with prob $1/2$:

- If only one bidder enters: expected utility = $E[v] - 0.5 = 1.5 - 0.5 = 1$
- If both enter: expected utility from auction = $1/4$ (computed from all cases), minus fee = $1/4 - 1/2 = -1/4$

**Payoff matrix:**

|  | Yes | No |
|--|-----|-----|
| **Yes** | $-1/4, -1/4$ | $1, 0$ |
| **No** | $0, 1$ | $0, 0$ |

Both entering is **not** an equilibrium ($-1/4 < 0$). The equilibria are: one bidder enters and the other stays out.

### LGT Exercise 2: Revenue Equivalence Discussion

Despite revenue equivalence theorem, **truthful auctions are preferred** because:
- Revenue equivalence requires strong assumptions (rationality, BNE play, common knowledge of distributions)
- Dominant-strategy truthful auctions need **fewer assumptions**
- When true valuations are revealed, **efficient allocation** (maximising social welfare) can be implemented

### LGT Exercise 3: Direct vs. Indirect Mechanisms

A mechanism is **direct** if bidders directly report their private valuation ("type") to the mechanism, which then calculates allocation and payments (e.g., sealed-bid Vickrey).

A mechanism is **indirect** if bidders interact by acting on information (like price updates) rather than reporting valuations (e.g., English, Dutch auctions).

### Revelation Principle

**Theorem:** Any social choice function $f: \Theta_1 \times \ldots \times \Theta_n \to O$ that is implementable in (Bayesian Nash) equilibrium by some mechanism is **also implementable by a direct, incentive-compatible mechanism** in which agents optimally reveal their true type.

**Formally:** If there exists some mechanism (possibly indirect) and BNE of that mechanism that implements $f$, then there exists a **direct revelation mechanism** in which:
- Each agent $i$ simply reports a type $\hat{\theta}_i \in \Theta_i$
- Truthful reporting $\hat{\theta}_i = \theta_i$ is a BNE
- The outcome on truthful reports is exactly $f(\theta)$

**Significance:** To study what is implementable, we can focus on **incentive-compatible direct mechanisms** without loss of generality.

### SGT Exercise 1: VCG with Multiple Identical Items

5 identical items, 7 buyers with single-unit demand. Valuations: $v_1=70, v_2=30, v_3=27, v_4=25, v_5=12, v_6=5, v_7=2$.

**(a) Allocation:** Items go to the 5 highest bidders: buyers 1, 2, 3, 4, 5.

**(b) Transfers:** For each winner $i \in \{1,\ldots,5\}$: without $i$, the 5 items go to $\{1,\ldots,5,6\} \setminus \{i\}$.

$$t_i = \left(\sum_{\substack{j=1 \\ j \neq i}}^{5} v_j\right) - \left(\sum_{\substack{j=1 \\ j \neq i}}^{6} v_j\right) = -v_6 = -5$$

Each winner pays **5** (the 6th highest valuation). For $i = 6, 7$: $t_i = 0$.

**(c) General rule:** In $k$-item, single-unit demand auction, VCG allocates to $k$ highest bidders, each paying the $(k+1)$-st highest bid.

### SGT Exercise 2: VCG Combinatorial Auction

Two items $\{A, B\}$, three buyers with valuations:

| | $\emptyset$ | $A$ | $B$ | $\{A,B\}$ |
|--|---|---|---|---|
| Buyer 1 | 0 | 5 | 3 | 23 |
| Buyer 2 | 0 | 3 | 12 | 15 |
| Buyer 3 | 0 | 15 | 5 | 18 |

**(a) Allocation:** Max welfare from giving both to same buyer = 23 (buyer 1 gets $\{A,B\}$). But splitting: buyer 3 gets A (15), buyer 2 gets B (12) = 27. **Efficient allocation: buyer 3 gets A, buyer 2 gets B.** Welfare = 27.

**Transfers:**
- $t_3$: welfare of {1,2} with 3 present = 12; max welfare of {1,2} without 3 = 23 (give both to buyer 1). $t_3 = 12 - 23 = -11$ (buyer 3 pays **11**)
- $t_2$: welfare of {1,3} with 2 present = 15; max welfare of {1,3} without 2 = 23. $t_2 = 15 - 23 = -8$ (buyer 2 pays **8**)
- $t_1 = 0$ (no effect on allocation)

**(b)** Buyer 1 bid 23 for $\{A,B\}$ and lost, but the mechanism sold $\{A,B\}$ for only $11 + 8 = 19 < 23$. Buyer 1 could object that she was willing to pay more.

**(c)** Mechanism collects 19, pays 0. Surplus = 19 > 0. **Weakly budget-balanced** but not strongly.

**(d)** $u_1 = 0 \geq 0$, $u_2 = 12 - 8 = 4 \geq 0$, $u_3 = 15 - 11 = 4 \geq 0$. **Individually rational.**

### SGT Exercise 3: Double Auction

5 buyers (limit prices: 2, 4, 6, 8, 10), 3 sellers (limit prices: 4, 8, 12).

**Equilibrium price:** $\pounds 8$. At this price:
- **Buyers** with limit prices $\geq 8$: buyers at 8 and 10 transact
- **Sellers** with limit prices $\leq 8$: sellers at 4 and 8 transact

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Mechanism design** | Engineering the rules of interaction so self-interested agents produce socially desirable outcomes |
| **Auction** | Protocol that allocates resources based on agents' indications of interest and determines payments |
| **Private valuation** $\theta_i$ | Agent $i$'s willingness to pay, known only to themselves |
| **Quasi-linear utility** | $u_i = v_i(\text{allocation}) - p_i$ |
| **English auction** | Ascending open-cry; highest bidder wins, pays own bid |
| **Dutch auction** | Descending open-cry; first bidder wins at current price |
| **First-price sealed-bid** | Sealed bids; highest bidder wins, pays own bid |
| **Vickrey (second-price)** | Sealed bids; highest bidder wins, pays second-highest bid |
| **Bayesian game** | Game with private types and common prior over type distributions |
| **Bayes-Nash equilibrium** | Strategy profile where no player can improve expected utility by unilateral deviation, given beliefs |
| **Strategyproof / Truthful** | Truthful reporting is a (weakly) dominant strategy |
| **Revenue equivalence** | Under i.i.d. continuous priors and risk neutrality, all efficient auctions yield the same expected revenue |
| **Collusion** | Coordinated bidding among agents to gain surplus |
| **Winner's curse** | Winner tends to be the most optimistic estimator, so overpays in common-value auctions |
| **Bid shading** | Bidding below one's estimate to account for winner's curse |
| **VCG mechanism** | Efficient allocation + transfers equal to externality imposed on other agents |
| **Individually rational** | Every agent gets non-negative utility |
| **Weakly budget-balanced** | Mechanism never runs a deficit |
| **Strongly budget-balanced** | Mechanism collects exactly what it pays out (no surplus, no deficit) |
| **Direct mechanism** | Agents report their types directly; mechanism computes outcome |
| **Indirect mechanism** | Agents interact via actions (e.g., bidding in rounds) rather than reporting types |
| **Revelation principle** | Any implementable social choice function can be implemented by a direct, truthful mechanism |
| **Combinatorial auction** | Multiple different goods; bidders bid on subsets |
| **Double auction** | Both buyers and sellers compete; equilibrium at supply-demand intersection |

---

## Summary

- **Mechanism design** is "reverse game theory": designing rules so that equilibrium outcomes are desirable
- **Four classic single-good auctions**: English, Dutch, first-price sealed-bid, and Vickrey (second-price sealed-bid)
- **Dutch $\equiv$ first-price** (strategically); **English $\equiv$ second-price** (strategically)
- In **first-price auctions**, BNE strategy is to bid $\frac{n-1}{n}\theta_i$ (shade bid)
- **Vickrey auction is truthful** (dominant strategy to bid true value) -- William Vickrey won Nobel Prize for this
- Under standard assumptions, all four auctions are **revenue equivalent**
- Second-price/English auctions are susceptible to **collusion**; Dutch auctions are resistant
- **Winner's curse** afflicts common-value auctions; mitigated by bid shading
- **VCG mechanism** generalises Vickrey to multiple items: efficient allocation, truthful, individually rational, weakly budget-balanced
- In multi-unit single-demand settings, VCG reduces to the **(k+1)-price auction**
- **Revelation principle**: any implementable outcome can be achieved by a direct truthful mechanism
- **Double auctions** model two-sided markets; equilibrium at supply-demand intersection
