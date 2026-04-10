# Week 1: Non-Cooperative Games (Part I)

## Learning Objectives
By the end of this week, you should be able to:
- [ ] Define the core concepts of non-cooperative game theory, including strategy profiles, payoff functions, and the distinction between cooperative and non-cooperative games.
- [ ] Formulate real-world scenarios as strategic-form (normal-form) or extensive-form games involving rational, self-interested agents.
- [ ] Identify and classify various types of strategies (pure, mixed, dominant, and best response strategies) in strategic games.
- [ ] Analyse game-theoretic models to determine the existence and properties of Nash equilibria (in pure and mixed strategies) and other solution concepts.
- [ ] Explain and interpret equilibrium behaviour in classical games such as the Prisoner's Dilemma, Matching Pennies, Battle of the Sexes, and coordination games.
- [ ] Evaluate the potential for and limitations of non-cooperative solutions, including issues of uniqueness, multiplicity, and inefficiency of equilibria.
- [ ] Demonstrate competency in using mathematical notation and reasoning to represent and solve strategic games.

---

## 1. Introduction: Multi-Agent Systems and Game Theory

### 1.1 Algorithmic Game Theory (AGT)

**Algorithmic Game Theory (AGT)** is the study of algorithms in strategic environments where the inputs come from self-interested agents who may manipulate the system to improve their own outcomes. It combines tools from theoretical computer science and economics to both analyze equilibrium behaviour and design mechanisms that are efficient, fair, and computationally tractable.

Key application areas of AGT:
- **Resource Allocation and Scheduling**: Efficiently allocate shared resources (memory, bandwidth, tasks) among competing agents using protocols that account for strategic behavior (e.g., auctions, congestion games). *Example: Cloud compute allocation, energy market bidding by smart devices.*
- **Mechanism Design for Incentives**: Design auction or payment mechanisms that incentivize truthful behavior and maximize system efficiency. *Example: Online advertising bidding, spectrum auctions for wireless networks.*
- **Equilibrium Computation in Networked Agents**: Compute equilibria (Nash, correlated, market equilibria) to predict or guide agent behavior in competition or cooperation. *Example: Routing in communication networks, multiagent negotiation, security games.*
- **Multiagent Reinforcement Learning**: Formulate learning in interactive multiagent environments as a game, analyzing convergence and performance using equilibrium concepts. *Example: AI agents learning to cooperate or compete in simulated/real-world games.*

### 1.2 Computational Social Choice (COMSOC)

**Computational Social Choice (COMSOC)** is an interdisciplinary field that studies collective decision-making and preference aggregation using tools from computer science, economics, and social choice theory. It asks how a group's individual preferences over alternatives can be combined into a collective decision, while explicitly accounting for computational issues.

Key application areas:
- **Collective Decision-Making**: Aggregate preferences and votes of multiple agents for joint decision-making. *Example: Group planning for robot teams, committee selection.*
- **Fair Division**: Design and implement algorithms for fair division of resources among multiple agents, guaranteeing properties like envy-freeness and proportionality. *Example: Allocation of workspace, fair inheritance division.*
- **Ranking and Recommendation**: Use rank aggregation/voting rules to combine agent preferences into a group-level ranking. *Example: AI-based recommender systems, collaborative filtering.*
- **Participatory Budgeting and Resource Assignment**: Agents select among projects/tasks/resources; COMSOC principles ensure fairness, proportionality, and representativeness. *Example: Autonomous vehicles choosing charging stations.*

### 1.3 Multi-Agent Systems (MAS)

A **multi-agent system (MAS)** is composed of multiple interacting software components (agents), which may be:
- **Cooperative**: agents work together towards common goals
- **Competitive** (self-interested): agents strategically optimise their own utility functions

The competitive case is modelled as a **non-cooperative game**, where players strategically optimise their own utility functions and there are no binding contracts among the players.

*Addresses LO1, LO2*

---

## 2. Normal Form Games

### 2.1 Definition and Components

**Games** model **strategic interactions** (or **conflicts**) between **rational** decision makers — **players**.

In a **non-cooperative** (or **competitive**) game, players take actions and enjoy game outcomes individually — i.e., there are no binding contracts among the players.

A game in **strategic (or normal) form** consists of:
1. **At least 2 PLAYERS** — a player is a general entity: individual, company, nation, protocol, animal, artificial agent, etc.
2. **A set of STRATEGIES for each player** — strategies are actions which a player chooses to follow, and an *outcome* is determined by mutual choice of strategies.
3. **A PREFERENCE RELATION for each player** over possible outcomes — modeled as a **utility** (or **payoff**) function over the set of outcomes.

### 2.2 Formal Definition

Formally, a game is a tuple $\Gamma = (\mathbf{N}, (S_i)_{i \in \mathbf{N}}, (U_i)_{i \in \mathbf{N}})$, where:
- $\mathbf{N}$ is a (finite) set of players
- $S_i$ is a set of strategies for each player $i \in \mathbf{N}$
- $U_i : S \to \mathbb{R}$ is a utility function of $i \in \mathbf{N}$, where $S = \times_{i \in \mathbf{N}} S_i$ is the set of strategy combinations (or **profiles**)

### 2.3 Notation

- A **strategy profile** $s = (s_1, s_2, \ldots, s_n)$ is a vector of strategies for all players
- $s_{-i}$ denotes the vector of all players' strategies *except* player $i$
- For a coalition $C \subseteq N$: $s_C$ denotes strategies of players in $C$, and $s_{-C}$ for the complement
- We write a profile as $(s_C, s_{-C})$

*Addresses LO1, LO7*

---

## 3. Classical Games and Examples

### 3.1 The Prisoner's Dilemma

**Setup**: 2 suspects in a crime are interrogated in separate rooms. Each has 2 choices: **Cooperate** (deny the crime) or **Defect** (rat the other out). With no confessions, there is enough evidence to convict on a lesser charge; one confession is enough to establish guilt. Police offers a plea bargain for confessing.

**Payoff matrix**:

|  | C | D |
|---|---|---|
| **C** | $-1, -1$ | $-10, 0$ |
| **D** | $0, -10$ | $-5, -5$ |

The only stable outcome is **(D, D)** — each player is better off defecting no matter what the other does.

**General form** of Prisoner's Dilemma:

|  | C | D |
|---|---|---|
| **C** | $R, R$ | $S, T$ |
| **D** | $T, S$ | $P, P$ |

where $T > R > P > S$ (Temptation > Reward > Punishment > Sucker's payoff).

**Key insight**: The equilibrium (D,D) with payoffs $(P,P)$ is Pareto-dominated by (C,C) with payoffs $(R,R)$. Individual rationality leads to a collectively suboptimal outcome.

### 3.2 The Ice Cream Wars (Hotelling's Model)

Ed and Ted are selling identical ice cream bars on a beach, modelled as the interval $[0,1]$. Customers go to the closest vendor.

- Initially: Ed at $1/4$, Ted at $3/4$ → each gets $1/2$ of customers
- Ted deviates to $1/2$ → Ted gets $5/8$, Ed gets $3/8$

**Formal model**: $N = \{1,2\}$ and $S_1 = S_2 = [0,1]$, where strategy $s_i \in S_i$ represents setting up a cart at position $s_i$.

$$U_i(s_i, s_{-i}) = \begin{cases} \frac{s_i + s_{-i}}{2} & \text{if } s_i < s_{-i} \\ 1 - \frac{s_i + s_{-i}}{2} & \text{if } s_i > s_{-i} \\ \frac{1}{2} & \text{if } s_i = s_{-i} \end{cases}$$

The unique **Nash equilibrium** is $s_1 = s_2 = 1/2$ (both vendors at the centre).

### 3.3 Working on a Joint Project (Professor's Dilemma variant)

2 students work on a joint project. Each either works hard or goofs off.

|  | Work hard | Goof off |
|---|---|---|
| **Work hard** | $2, 2$ | $0, 3$ |
| **Goof off** | $3, 0$ | $1, 1$ |

This is another instance of the Prisoner's Dilemma structure.

### 3.4 Duopoly

2 firms produce the same good. Each charges either a high price or a low price.

|  | High | Low |
|---|---|---|
| **High** | $1000, 1000$ | $-200, 1200$ |
| **Low** | $1200, -200$ | $600, 600$ |

Again, Prisoner's Dilemma structure: (Low, Low) is the equilibrium despite (High, High) being better for both.

### 3.5 The Professor's Dilemma

A game played between a professor and the class:

| PAYOFFS | Listen | Sleep |
|---|---|---|
| **Make effort** | $(10^6, 10^6)$ | $(-10, 0)$ |
| **Slack off** | $(0, -10)$ | $(0, 0)$ |

- No player has a dominant or dominated strategy
- The best strategy depends on what the other player is doing
- Two pure strategy Nash equilibria: (Make effort, Listen) and (Slack off, Sleep)

### 3.6 Tragedy of the Commons

A **social dilemma** where individuals have an incentive to overconsume a common resource and act in their own self-interest at the expense of society.

The phrase comes from Garrett Hardin's 1968 essay in *Science*, drawing on 19th-century writer William Forster Lloyd's description of overgrazing on shared pastureland ("the commons").

**Examples**:
- Overfishing in international waters
- Overgrazing on shared pastureland
- Overuse of groundwater from shared aquifers
- Air pollution and greenhouse gas emissions
- Deforestation of open-access forests

**In MAS & AI**: Tragedy-of-the-commons situations appear whenever many learning or planning agents share a limited resource and optimise only their own reward — e.g., shared communication bandwidth, autonomous vehicles in traffic networks, open multiagent platforms and reputation systems.

### 3.7 Coordination Game

|  | L | R |
|---|---|---|
| **U** | $1, 1$ | $0, 0$ |
| **D** | $0, 0$ | $1, 1$ |

- No player has a dominant or dominated strategy
- Two pure strategy Nash equilibria: (U, L) and (D, R)
- Both are also **strong equilibria**

### 3.8 Battle of the Sexes

A generalisation of a coordination game where both players want to choose the same action, but have different preferences over possible consistent outcomes.

| PAYOFFS | Theater | Football |
|---|---|---|
| **Theater** | $(2, 1)$ | $(0, 0)$ |
| **Football** | $(0, 0)$ | $(1, 2)$ |

- Two pure strategy Nash equilibria: **(Theater, Theater)** and **(Football, Football)**

### 3.9 Matching Pennies

|  | H | T |
|---|---|---|
| **H** | $1, -1$ | $-1, 1$ |
| **T** | $-1, 1$ | $1, -1$ |

- **No pure strategy Nash equilibrium** exists (cycle of profitable deviations)
- This is a **zero-sum game**

### 3.10 Beauty Contest

Each participant $i$ chooses an integer from $S_i = \{0, 1, \ldots, 100\}$. Player $i$ whose strategy $s_i \in S_i$ is **closest to 2/3 of the average of all strategies** wins the contest.

Each player's aim is to minimise:
$$\left| s_i - \frac{2}{3} \cdot \frac{\sum_{j \in \mathbf{N}} s_j}{N} \right|$$

### 3.11 Stag Hunt

|  | Stag | Hare |
|---|---|---|
| **Stag** | $4, 4$ | $1, 3$ |
| **Hare** | $3, 1$ | $3, 3$ |

- Two PSNE: (Stag, Stag) and (Hare, Hare)
- (Stag, Stag) is **payoff-dominant** but risky; (Hare, Hare) is **risk-dominant**

*Addresses LO2, LO5*

---

## 4. Dominance

### 4.1 Strict Dominance

For player $i \in \mathbf{N}$ and any two strategies $s, t \in S_i$:

**Strategy $s$ strictly dominates strategy $t$** if for every possible combination of strategies for other players $s_{-i} \in S_{-i}$:
$$U_i(s, s_{-i}) > U_i(t, s_{-i})$$

### 4.2 Weak Dominance

**Strategy $s$ weakly dominates strategy $t$** if:
- For all $s_{-i} \in S_{-i}$: $U_i(s, s_{-i}) \geq U_i(t, s_{-i})$
- There exists some $s'_{-i} \in S_{-i}$: $U_i(s, s'_{-i}) > U_i(t, s'_{-i})$

### 4.3 Dominant vs Dominated Strategies

- **Strategy $s$ is (strictly/weakly) dominant** for player $i$ if it dominates **all** other strategies $t$
- **Strategy $t$ is (strictly/weakly) dominated** if there exists **some** strategy $s$ that dominates it

**Key properties**:
- A dominant strategy is a very strong solution concept — no assumptions needed about other players
- Dominant strategies do not often exist (they do in Prisoner's Dilemma)
- Rational players will never choose strictly dominated strategies

### 4.4 Iterated Elimination of Dominated Strategies (IEDS)

Solve a game by iteratively eliminating dominated strategies:
- For **strict** dominance: the outcome is **path-independent** (order of elimination doesn't matter)
- For **weak** dominance: the outcome **may depend** on the order of elimination
- The surviving strategy need not be dominant
- We may end up with more than one strategy per player (game not fully solved)
- Some games have no dominated strategies at all

### 4.5 Worked Example: IEDS (Exercise 1 from LGT)

|  | L | C | R |
|---|---|---|---|
| **T** | $73, 25$ | $57, 42$ | $66, 32$ |
| **M** | $80, 26$ | $35, 12$ | $32, 54$ |
| **B** | $28, 27$ | $63, 31$ | $54, 29$ |

**Step 1**: For Player 2, R dominates L (compare column by column: 32>25, 54>26, 29>27). Eliminate L.

|  | C | R |
|---|---|---|
| **T** | $57, 42$ | $66, 32$ |
| **M** | $35, 12$ | $32, 54$ |
| **B** | $63, 31$ | $54, 29$ |

**Step 2**: For Player 1, T and B both dominate M. Eliminate M.

|  | C | R |
|---|---|---|
| **T** | $57, 42$ | $66, 32$ |
| **B** | $63, 31$ | $54, 29$ |

**Step 3**: For Player 2, C dominates R (42>32 and 31>29). Eliminate R.

|  | C |
|---|---|
| **T** | $57, 42$ |
| **B** | $63, 31$ |

**Step 4**: For Player 1, B dominates T (63>57). Solution: **(B, C)** with payoffs $(63, 31)$.

**(B, C) is a Nash equilibrium**: each player is playing their best response to the other player's strategy.

*Addresses LO3*

---

## 5. Nash Equilibrium in Pure Strategies

### 5.1 Unilateral Improving Deviation

For a strategy profile $s$, player $i$ has a **unilateral improving move (deviation)** if there exists some $s'_i \in S_i$ such that:
$$U_i(s'_i, s_{-i}) > U_i(s_i, s_{-i})$$

### 5.2 Pure Strategy Nash Equilibrium (PSNE)

A **pure strategy Nash equilibrium** is a strategy profile $s^*$ where no player has a unilateral improving move. Equivalently, every player plays their **best response** to the strategies of other players:
$$U_i(s^*_i, s^*_{-i}) \geq U_i(s'_i, s^*_{-i}) \quad \forall s'_i \in S_i, \forall i \in \mathbf{N}$$

### 5.3 Properties of PSNE

- **Not necessarily unique**: Coordination game has two PSNE
- **May not exist**: Matching Pennies has no PSNE
- Every dominant strategy equilibrium is a Nash equilibrium
- Nash equilibrium is a stronger requirement than surviving IEDS

### 5.4 Worked Example: Finding Best Responses (Exercise 2 from LGT)

|  | L | C | R |
|---|---|---|---|
| **T** | $2, 2$ | $1, 3$ | $0, 1$ |
| **M** | $3, 1$ | $0, 0$ | $0, 0$ |
| **B** | $1, 0$ | $0, 0$ | $0, 0$ |

Best responses (marked with $*$):

|  | L | C | R |
|---|---|---|---|
| **T** | $2, 2$ | $1^*, 3^*$ | $0^*, 1$ |
| **M** | $3^*, 1^*$ | $0, 0$ | $0^*, 0$ |
| **B** | $1, 0^*$ | $0, 0^*$ | $0^*, 0^*$ |

No cell has both entries starred → **No pure strategy Nash equilibrium** in this game.

*Addresses LO4*

---

## 6. Mixed Strategy Nash Equilibrium

### 6.1 Mixed Strategies

A **mixed strategy** is a probability distribution over the set of pure strategies. Let $\Delta_i$ denote the set of probability distributions over $S_i$ (the set of mixed strategies for player $i$).

- A pure strategy is a special case of a mixed strategy (one action played with probability 1)
- Even with finite pure strategy sets, there are infinitely many mixed strategies
- Let $\Delta = \times_{i \in \mathbf{N}} \Delta_i$ be the set of all mixed strategy profiles

### 6.2 Expected Utility under Mixed Strategies

When a mixed strategy profile $\tilde{s}$ is played, the payoff to each player is the **expected utility**:
$$U_i(\tilde{s}) = \sum_{s \in S} \left(\prod_{j \in \mathbf{N}} \tilde{s}_j(s_j)\right) U_i(s)$$

### 6.3 Mixed Strategy Nash Equilibrium (MSNE)

A **mixed strategy Nash equilibrium** is a mixed strategy profile $\tilde{s}^*$ where each player's mixed strategy is a best response to the others:
$$U_i(\tilde{s}^*_i, \tilde{s}^*_{-i}) \geq U_i(\tilde{s}'_i, \tilde{s}^*_{-i}) \quad \forall \tilde{s}'_i \in \Delta_i, \forall i \in \mathbf{N}$$

### 6.4 Nash's Theorem

> **Theorem (Nash, 1950)**: Every game with a finite set of players and finite sets of actions has at least one Nash equilibrium in mixed strategies.

### 6.5 Computing Mixed Nash Equilibria: The Indifference Principle

A player will randomize between strategies **if and only if** they are **indifferent** between those strategies — i.e., the expected utilities from playing each pure strategy in the support are equal.

**Key insight**: Player $i$'s mixing probabilities are determined by making the **other** player indifferent.

### 6.6 Worked Example: Matching Pennies

|  | H (prob $q$) | T (prob $1-q$) |
|---|---|---|
| **H** (prob $p$) | $1, -1$ | $-1, 1$ |
| **T** (prob $1-p$) | $-1, 1$ | $1, -1$ |

For Player 2 to be indifferent between H and T:
$$U_2(H) = U_2(T)$$
$$-p + (1-p) = p - (1-p)$$
$$1 - 2p = 2p - 1$$
$$p = \frac{1}{2}$$

By symmetry: $q = \frac{1}{2}$

**MSNE**: $\left(\frac{1}{2}H + \frac{1}{2}T, \frac{1}{2}H + \frac{1}{2}T\right)$ with expected utility $0$ for each player.

### 6.7 Worked Example: Stag Hunt

|  | Stag (prob $q$) | Hare (prob $1-q$) |
|---|---|---|
| **Stag** (prob $p$) | $4, 4$ | $1, 3$ |
| **Hare** (prob $1-p$) | $3, 1$ | $3, 3$ |

For Player 2 to be indifferent:
$$U_2(\text{Stag}) = U_2(\text{Hare})$$
$$4p + 1(1-p) = 3p + 3(1-p)$$
$$4p + 1 - p = 3p + 3 - 3p$$
$$3p + 1 = 3$$
$$p = \frac{2}{3}$$

By symmetry: $q = \frac{2}{3}$

**MSNE**: Each player plays Stag with probability $2/3$ and Hare with probability $1/3$.

**Observation on utility changes**: If Player 2's payoff from (Stag, Hare) changes from 1 to 2, it affects **Player 1's** mixing probability (changes to $p = 1/2$), not Player 2's. This is because Player 1's probabilities are what make Player 2 indifferent.

### 6.8 Worked Example: Battle of the Sexes

**Original game:**

|  | Theater (prob $q$) | Football (prob $1-q$) |
|---|---|---|
| **Theater** (prob $p$) | $2, 1$ | $0, 0$ |
| **Football** (prob $1-p$) | $0, 0$ | $1, 2$ |

**PSNE**: (Theater, Theater) and (Football, Football)

**Finding MSNE** — For Player 2 to be indifferent:
$$p \cdot 1 = (1-p) \cdot 2$$
$$p = 2 - 2p$$
$$3p = 2 \implies p = \frac{2}{3}$$

For Player 1 to be indifferent:
$$2q = 1 - q$$
$$3q = 1 \implies q = \frac{1}{3}$$

**MSNE**: Player 1 plays Theater with prob $2/3$, Player 2 plays Theater with prob $1/3$.

**Modified game** (change (1,2) to (1,3)):

|  | Theater (prob $q$) | Football (prob $1-q$) |
|---|---|---|
| **Theater** (prob $p$) | $2, 1$ | $0, 0$ |
| **Football** (prob $1-p$) | $0, 0$ | $1, 3$ |

For Player 2 to be indifferent: $p = 3(1-p)$, so $4p = 3 \implies p = \frac{3}{4}$

For Player 1 to be indifferent: $2q = 1-q$, so $3q = 1 \implies q = \frac{1}{3}$ (unchanged, since Player 1's payoffs didn't change)

*Addresses LO4, LO5*

---

## 7. Maximin and Minimax Strategies

### 7.1 Maximin (Safety Level) Strategy

The **maximin** (or **safety level**) strategy for player $i$ maximises the worst-case payoff — assuming all other players play to cause the greatest harm to player $i$:

$$\max_{s_i \in S_i} \min_{s_{-i} \in S_{-i}} U_i(s_i, s_{-i})$$

The **maximin value** (safety level value) is the guaranteed minimum payoff from playing this strategy.

**Intuition**: Player $i$ commits to a (possibly mixed) strategy, then the remaining agents observe it and choose their strategies to minimise player $i$'s expected payoff. The maximin strategy is the best choice in this worst-case scenario.

### 7.2 Minimax Strategy

The **minimax strategy** for player $i$ against player $j$ keeps the payoff of player $j$ at a minimum:

$$\min_{s_i \in S_i} \max_{s_j \in S_j} U_j(s_i, s_j)$$

**Useful for punishment** — considering how much a player can punish another player without regard to their own payoff (relevant in repeated games where reputation matters).

**In $n$-player games** ($n > 2$): Player $i$ alone cannot usually guarantee player $j$ achieves minimum payoff. We assume all players other than $j$ coordinate ("gang up") to minimise $j$'s payoff:
$$\min_{s_{-j} \in S_{-j}} \max_{s_j \in S_j} U_j(s_j, s_{-j})$$

### 7.3 Relationship Between Maximin and Minimax

- **Two-player games**: A player's minimax value = maximin value (in mixed strategies)
- **$n$-player games** ($n > 2$): maximin value $\leq$ minimax value

### 7.4 Worked Example: Prisoner's Dilemma (Pure Maximin/Minimax)

For the row player:
- Commit to C → opponent minimises by playing D → payoff = $-10$
- Commit to D → opponent minimises by playing D → payoff = $-5$
- **Maximin**: max$\{-10, -5\} = -5$ → play **D** (safety level = $-5$)

By symmetry, D is also the safety level strategy for the column player.

### 7.5 Worked Example: Battle of Sexes (from handwritten notes)

**Modified game** for maximin/minimax:

|  | | |
|---|---|---|
|  | $2, 1$ | $0, 0$ |
|  | $0, 0$ | $1, 3$ |

**Pure maximin/minimax**: Row player minimum payoffs: row 1 → min = 0, row 2 → min = 0. P1 maximin = 0. Column player minimum payoffs: col 1 → min = 0, col 2 → min = 0. P2 maximin = 0. P1 minimax = 1, P2 minimax = 1.

**Mixed maximin** (another worked game from tutorial):

|  | $q$ | $1-q$ |
|---|---|---|
| $p$ | $2, -2$ | $9, 0$ |
| $1-p$ | $0, 0$ | $1, -1$ |

For P1 maximin: $-2p = -(1-p)$, so $-2p = -1+p$, giving $1 = 3p$, thus $p = 1/3$. Safety value $u_1 = 2/3$.

For P2 minimax: $2q = 1-q$, so $3q = 1$, thus $q = 1/3$.

Another game:

|  | $q$ | $1-q$ |
|---|---|---|
| $p$ | $-1, 1$ | $0, 0$ |
| $1-p$ | $0, 0$ | $-3, 3$ |

$p = 3(1-p)$, so $4p = 3$, giving $p = 3/4$. P1 minimax value $u_2 = 3/4$.

$-q = -3(1-q)$, so $-q = -3+3q$, giving $3 = 4q$, thus $q = 3/4$. P2 maximin.

**Conclusion**: Mixed strategies are more effective than pure strategies for maximin/minimax — they generally yield higher safety level values.

### 7.6 Zero-Sum Games and the Minimax Theorem

A two-player normal form game is **constant-sum** if there exists a constant $C$ such that for every strategy profile: $U_1(s) + U_2(s) = C$.

A **zero-sum game** is a constant-sum game with $C = 0$: $U_2(s) = -U_1(s)$. This is a pure conflict game.

> **Minimax Theorem** (von Neumann): For any finite two-player zero-sum game:
> $$\max_{s_1} \min_{s_2} U_1(s_1, s_2) = \min_{s_2} \max_{s_1} U_1(s_1, s_2)$$

**Consequences for zero-sum games**:
- Each player's maximin value = minimax value
- The **value of the game** = maximin value for Player 1
- For both players, the set of maximin strategies = set of minimax strategies
- Any maximin/minimax strategy profile is a Nash equilibrium
- **All Nash equilibria have the same payoff vector**

**Computing maximin/minimax for general-sum games**: Since the maximin strategy for player $i$ depends only on $i$'s utilities, we can create an auxiliary zero-sum game where $U_{-i} = -U_i$ and solve for the Nash equilibrium.

*Addresses LO3, LO4, LO6*

---

## 8. Other Solution Concepts

### 8.1 Rationalizable Strategies

A pure or mixed strategy is **rationalizable** if it is a best response to some belief about opponents' strategies, where those beliefs are consistent with common knowledge of rationality.

- A strategy is rationalizable exactly when it survives iterated elimination of strategies that are never a best response (equivalently, IEDS allowing domination by mixed strategies)
- The set of rationalizable strategies is the largest set consistent with common knowledge of rationality
- Every Nash equilibrium uses only rationalizable strategies, but rationalizable strategies may not be part of any NE

### 8.2 Correlated Equilibrium

In a **correlated equilibrium**, players may condition their actions on a shared random signal. Imagine a trusted mediator who draws an action profile at random from a publicly known distribution and privately recommends to each player their component.

- The distribution is a correlated equilibrium if following the recommendation gives at least as much expected payoff as deviating
- Every mixed NE induces a correlated equilibrium (via the product distribution)
- The set of correlated equilibria is a **superset** of Nash equilibria
- Correlated equilibria always exist and can be computed via **linear programming** (easier than computing NE)

### 8.3 $\varepsilon$-Nash Equilibrium

An **$\varepsilon$-Nash equilibrium** is a strategy profile where no player can gain more than $\varepsilon > 0$ by unilaterally deviating — every player's strategy is an approximately best response.

- Standard Nash equilibrium is the special case $\varepsilon = 0$

### 8.4 Strong Equilibrium

A **strong equilibrium** (Aumann, Nobel Prize 2005) is a strategy profile where no **coalition** of players has an improving move — i.e., there is no subset $C \subseteq N$ with a joint strategy $s'_C$ such that:
$$U_i(s'_C, s_{-C}) > U_i(s) \quad \forall i \in C$$

- Every strong equilibrium is a Nash equilibrium (singleton coalitions)
- Games with strong equilibria are scarce
- **Prisoner's Dilemma**: (D,D) is not a strong equilibrium (both players can jointly deviate to (C,C)); no strong equilibrium exists
- **Coordination Game**: Both PSNE are strong equilibria

*Addresses LO4, LO6*

---

## 9. Tutorial Problems and Solutions

### 9.1 Exercise 1: Firms Alpha and Beta (Prisoner's Dilemma)

**Setup**: Two firms with constant costs of £2/unit, choosing high price (£10) or low price (£5).
- Both high: demand 10,000, split evenly
- Both low: demand 18,000, split evenly
- One low, one high: low firm gets 15,000 units, high firm gets 2,000

**Payoff calculation** (profit = quantity × (price - cost)):
- (High, High): $5000 \times (10-2) = £40,000$ each
- (Low, Low): $9000 \times (5-2) = £27,000$ each
- (High, Low): High firm: $2000 \times 8 = £16,000$; Low firm: $15000 \times 3 = £45,000$

| $\alpha, \beta$ | High | Low |
|---|---|---|
| **High** | £40,000, £40,000 | £16,000, £45,000 |
| **Low** | £45,000, £16,000 | £27,000, £27,000 |

**Equilibrium**: Each player has a dominant strategy: **Low price**. Equilibrium is (Low, Low) with payoffs (£27,000, £27,000).

**Why PD**: Dominant strategy (Low) leads to equilibrium payoffs that are Pareto-dominated by (High, High) at (£40,000, £40,000). The equilibrium gives the lowest joint payoff.

### 9.2 Exercise 2: Three-Firm Oligopoly

Three firms, each choosing $p_i = 2$ (cheap) or $p_i = 3$ (expensive). 12 customers. Profit = price × customers attracted.

**For $p_3 = 2$**:

| Firm 1,2,3 | $p_2 = 2$ | $p_2 = 3$ |
|---|---|---|
| $p_1 = 2$ | 8, 8, 8 | 10, 6, 10 |
| $p_1 = 3$ | 6, 10, 10 | 9, 9, 12 |

**For $p_3 = 3$**:

| Firm 1,2,3 | $p_2 = 2$ | $p_2 = 3$ |
|---|---|---|
| $p_1 = 2$ | 10, 10, 6 | 12, 9, 9 |
| $p_1 = 3$ | 9, 12, 9 | 12, 12, 12 |

**PSNE**: (2, 2, 2) with payoffs (8, 8, 8) and (3, 3, 3) with payoffs (12, 12, 12).

### 9.3 Exercise 3: Weak Dominance and IEDS Order

**(a)** Construct a game where order of weakly dominated elimination matters:

| Player 1,2 | C | D |
|---|---|---|
| **A** | $2, 0$ | $0, 1$ |
| **B** | $0, 0$ | $0, 0$ |

D weakly dominates C; A weakly dominates B. If we remove B first → C is strongly dominated → (A, D) is the only NE. If we remove C first → both (A, D) and (B, D) are NE.

**(b)** Weakly dominated strategy in a Nash equilibrium:

| Player 1,2 | C | D |
|---|---|---|
| **A** | $1, 0$ | $0, 0$ |
| **B** | $0, 0$ | $0, 0$ |

A weakly dominates B, but (B, D) satisfies NE conditions (no player can profitably deviate).

### 9.4 Exercise 4: Number Choice Game

Strategy set $\{2, \ldots, 100\}$. Same number → each gets that amount. One chooses $s < t$ → former gets $s+2$, latter gets $s-2$.

**Only Nash equilibrium**: $(2, 2)$. If one player chooses $n > 2$, the other's best response is $n-1$ (undercut). This continues until both settle at 2. However, in any profile $(a, b)$ where $a, b \geq 4$, both players are weakly better off than at (2,2).

### 9.5 Exercise 5: Support Lemma (Best Response Characterization)

**Theorem**: $x_1 \in B_1(x_2^*)$ if and only if every pure strategy $s \in S$ in the support of $x_1$ (i.e., $x_1(s) > 0$) is itself in $B_1(x_2^*)$ (i.e., $u_1(s, x_2^*) = \alpha$, the maximum achievable utility).

**Proof ($\Rightarrow$)**: If $x_1 \in B_1(x_2^*)$, suppose for contradiction that some $s$ in the support has $u_1(s, x_2^*) < \alpha$. Then:
$$u_1(x_1, x_2^*) = \sum_{s: x_1(s)>0} x_1(s) u_1(s, x_2^*) < \sum_{s: x_1(s)>0} x_1(s) \alpha = \alpha$$
Contradiction with $x_1$ being a best response.

**Proof ($\Leftarrow$)**: If every pure strategy in the support yields $\alpha$:
$$u_1(x_1, x_2^*) = \sum_{s: x_1(s)>0} x_1(s) u_1(s, x_2^*) = \sum_{s: x_1(s)>0} x_1(s) \alpha = \alpha$$
So $x_1 \in B_1(x_2^*)$.

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Multi-agent system (MAS)** | A system composed of multiple interacting software components (agents), which may be cooperative or competitive |
| **Algorithmic Game Theory (AGT)** | Study of algorithms in strategic environments with self-interested agents |
| **Computational Social Choice (COMSOC)** | Study of collective decision-making and preference aggregation using computational tools |
| **Non-cooperative game** | A game where players take actions individually with no binding contracts |
| **Normal (strategic) form game** | A tuple $\Gamma = (\mathbf{N}, (S_i), (U_i))$ specifying players, strategies, and utilities |
| **Strategy profile** | A vector of strategies, one per player: $s = (s_1, \ldots, s_n)$ |
| **Utility (payoff) function** | $U_i : S \to \mathbb{R}$, mapping strategy profiles to real-valued payoffs |
| **Strict dominance** | Strategy $s$ strictly dominates $t$ if $U_i(s, s_{-i}) > U_i(t, s_{-i})$ for all $s_{-i}$ |
| **Weak dominance** | Strategy $s$ weakly dominates $t$ if $\geq$ for all $s_{-i}$ and $>$ for some |
| **Dominant strategy** | A strategy that dominates all other strategies for a player |
| **IEDS** | Iterated Elimination of Dominated Strategies — solving games by removing dominated strategies |
| **Best response** | Strategy $s_i^*$ such that $U_i(s_i^*, s_{-i}) \geq U_i(s_i, s_{-i})$ for all $s_i$ |
| **Nash equilibrium (pure)** | Profile where no player has a unilateral improving deviation |
| **Mixed strategy** | A probability distribution over pure strategies |
| **Nash equilibrium (mixed)** | Mixed strategy profile where each player's mixed strategy is a best response |
| **Nash's Theorem** | Every finite game has at least one mixed strategy Nash equilibrium |
| **Indifference principle** | A player randomizes iff they are indifferent among strategies in their support |
| **Maximin strategy** | Strategy maximising worst-case payoff: $\max_{s_i} \min_{s_{-i}} U_i(s_i, s_{-i})$ |
| **Safety level value** | The guaranteed minimum payoff from playing a maximin strategy |
| **Minimax strategy** | Strategy minimising the opponent's maximum payoff |
| **Zero-sum game** | Two-player game where $U_1(s) + U_2(s) = 0$ for all $s$ |
| **Minimax theorem** | In zero-sum games: maximin = minimax; maximin/minimax profiles = Nash equilibria |
| **Rationalizable strategy** | Best response to some belief consistent with common knowledge of rationality |
| **Correlated equilibrium** | Distribution over profiles where following a mediator's recommendation is optimal; superset of NE |
| **$\varepsilon$-Nash equilibrium** | Profile where no player gains more than $\varepsilon$ from deviating |
| **Strong equilibrium** | Profile where no coalition of players has a joint improving move |
| **Pareto improvement** | An outcome where at least one player is better off and no player is worse off |
| **Prisoner's Dilemma** | Game where dominant strategies lead to a Pareto-suboptimal equilibrium |
| **Coordination game** | Game where players benefit from making consistent/matching decisions |
| **Matching Pennies** | Zero-sum game with no PSNE; MSNE at $(1/2, 1/2)$ |
| **Battle of the Sexes** | Coordination game with different preferences over coordinated outcomes |
| **Stag Hunt** | Coordination game illustrating payoff dominance vs risk dominance |
| **Tragedy of the Commons** | Social dilemma: individual incentives to overconsume a shared resource lead to collective loss |

---

## Summary

- **LO1 (Core concepts)**: Covered the formal definition of normal form games $\Gamma = (\mathbf{N}, (S_i), (U_i))$, strategy profiles, payoff functions, and the distinction between cooperative and non-cooperative games (Sections 1-2).

- **LO2 (Formulation)**: Demonstrated formulation through the Ice Cream Wars (Hotelling model), Prisoner's Dilemma, Duopoly, Professor's Dilemma, Tragedy of the Commons, and other real-world scenarios (Section 3).

- **LO3 (Strategy types)**: Defined and classified pure, mixed, dominant, dominated, and best response strategies. Covered strict and weak dominance, IEDS, and the indifference principle for computing mixed strategies (Sections 4, 6).

- **LO4 (Nash equilibria)**: Defined pure and mixed Nash equilibria, proved existence via Nash's Theorem, computed equilibria in Matching Pennies, Stag Hunt, and Battle of the Sexes. Introduced maximin/minimax strategies and the Minimax Theorem (Sections 5-7).

- **LO5 (Classical games)**: Analysed equilibrium behaviour in Prisoner's Dilemma (dominant strategy equilibrium), Matching Pennies (no PSNE, unique MSNE), Battle of the Sexes (two PSNE, one MSNE), Coordination Game, and Stag Hunt (Sections 3, 5-6).

- **LO6 (Limitations)**: Discussed uniqueness (PD has unique NE), multiplicity (coordination games), non-existence of PSNE (matching pennies), inefficiency (PD equilibrium is Pareto-suboptimal), and strong equilibrium existence issues (Section 8).

- **LO7 (Mathematical reasoning)**: Used formal notation throughout — game tuples, utility functions, dominance inequalities, expected utility calculations, and the support lemma proof (all sections, especially Section 9.5).
