## Markov Chains - Text Generator

### Overview

This project demonstrates the use of Markov Chains for generating text. A Markov Chain is a stochastic model that describes systems where the next state depends only on the current state. In this case, the states are words in a sentence, and the transition probabilities are derived from a given text corpus.

### Files

1. **text_generator.py**: Implements a basic text generator using a Markov Chain.
2. **transition_matrices.py**: Creates and visualizes the transition matrix of the Markov Chain.
3. **requirements.txt**: Lists the dependencies for the project.

# Markov Chains - Detailed Explanation, Formulas, and Project Setup

## What is a Markov Chain?

A **Markov Chain** is a mathematical system that undergoes transitions from one state to another within a finite set of possible states. It has the **Markov property**, which means the future state depends only on the current state and not on the sequence of events that preceded it (i.e., memoryless).

Formally, a Markov Chain consists of:

- **State space**: The set of all possible states.
- **Transition probability matrix**: Defines the probabilities of moving from one state to another.

The state transition follows the rule:

\[
P(X_{n+1} = s_j | X_n = s_i) = P_{ij}
\]

Where \( P_{ij} \) is the probability of moving from state \( s_i \) to state \( s_j \), and \( X_n \) denotes the state at step \( n \).

## Key Concepts

- **States**: The distinct situations or conditions that a system can be in. In the case of a text generator, the "states" can be the individual words in a sentence or sequence.
  
- **Transition Matrix**: A square matrix \( P \) that represents the probability of moving from one state to another. The element \( P_{ij} \) represents the probability of transitioning from state \( s_i \) to state \( s_j \).

\[
P = \begin{pmatrix}
P_{11} & P_{12} & \dots & P_{1n} \\
P_{21} & P_{22} & \dots & P_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
P_{n1} & P_{n2} & \dots & P_{nn}
\end{pmatrix}
\]

Where \( n \) is the number of states in the system.

- **Stationary Distribution**: For some Markov Chains, there exists a distribution of probabilities over the states that remains unchanged as the system evolves over time. This distribution \( \pi \) satisfies:

\[
\pi P = \pi
\]

- **First-Order Markov Chain**: In a first-order Markov Chain, the probability of transitioning to the next state depends only on the current state. This means the state space is discrete, and future states are independent of past ones.

- **Higher-Order Markov Chains**: Higher-order Markov chains take into account multiple past states for predicting the next state.

## Markov Chain Formula (Discrete)

For a Markov Chain with states \( S = \{s_1, s_2, \dots, s_n\} \) and transition matrix \( P \), the probability of being in a particular state \( s_j \) after \( n \) steps (given initial state \( s_i \)) is:

\[
P(X_n = s_j | X_0 = s_i) = P_{ij}(n)
\]

Where \( P_{ij}(n) \) is the \( n \)-step transition probability from state \( s_i \) to state \( s_j \), which can be computed as:

\[
P(n) = P^n
\]

Where \( P^n \) represents the matrix \( P \) raised to the power \( n \), giving the transition probabilities after \( n \) steps.

---

### Requirements

To run this project, you'll need to install the following libraries:

- `numpy`
- `matplotlib`
- `seaborn`

You can install them using:

```bash
pip install -r requirements.txt
