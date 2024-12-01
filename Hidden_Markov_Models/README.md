# Hidden Markov Models: Part-of-Speech Tagger

This project demonstrates the use of Hidden Markov Models (HMMs) to create a simple Part-of-Speech (POS) tagger.

## Components
1. `hmm_model.py`: Defines the HMM class with methods for training, evaluation, and decoding.
2. `pos_tagger.py`: Implements a POS tagger using the HMM class.


# Hidden Markov Models (HMMs)

## Definition:
A **Hidden Markov Model (HMM)** is a statistical model that assumes there are hidden (latent) states in a system and that the system produces observable outputs (emissions) based on these hidden states. The model is used to model time series data where the system transitions from one state to another over time, but the states are not directly visible. Instead, you observe the outputs associated with each state.

## Key Components:
- **States**: The hidden states in the model (e.g., POS tags in the POS tagging example).
- **Observations**: The visible outputs, which are observed (e.g., words in the POS tagging example).
- **Transition Probabilities**: The probability of transitioning from one state to another.
- **Emission Probabilities**: The probability of observing a certain output from a given state.
- **Initial Probabilities**: The probability of starting in each state.

## Mathematical Formulation:
The HMM is defined by the following parameters:

- **States** \( S = \{s_1, s_2, ..., s_N\} \): The set of hidden states in the model.
- **Observations** \( O = \{o_1, o_2, ..., o_M\} \): The set of possible observable outputs.
- **Transition Probability Matrix** \( A \): A matrix where \( A[i, j] = P(s_j | s_i) \), the probability of transitioning from state \( s_i \) to state \( s_j \).
- **Emission Probability Matrix** \( B \): A matrix where \( B[j, k] = P(o_k | s_j) \), the probability of observing output \( o_k \) given state \( s_j \).
- **Initial State Distribution** \( \pi \): A vector where \( \pi[i] = P(s_i) \), the probability of starting in state \( s_i \).

## The HMM Process:
1. **Initialization**: Begin in one of the hidden states \( s_i \) according to the initial state distribution \( \pi \).
2. **Transition**: Move from one state to another based on the transition probability matrix \( A \).
3. **Observation**: Upon entering a new state, observe an output based on the emission probability matrix \( B \).
4. **Termination**: Repeat the process for a sequence of observations.

## Key Problems in HMMs:
- **Evaluation**: Given an observed sequence of outputs, calculate the probability of the sequence given the model parameters (using the forward algorithm).
- **Decoding**: Given an observed sequence, find the most probable sequence of hidden states (using the Viterbi algorithm).
- **Learning**: Given an observed sequence of outputs and hidden states, estimate the parameters of the model (using the Baum-Welch algorithm).

## POS Tagging Using HMMs:
In Natural Language Processing (NLP), **POS tagging** refers to the process of assigning each word in a sentence to a corresponding part-of-speech tag, such as noun, verb, adjective, etc. Hidden Markov Models can be used to perform this task by modeling the sequence of tags (states) and the sequence of words (observations).

- **States**: POS tags (e.g., Noun, Verb, Adjective).
- **Observations**: Words in a sentence (e.g., "I", "saw", "the", "cat").
- **Transition Probabilities**: The probability of a tag following another tag (e.g., P(Noun|Verb)).
- **Emission Probabilities**: The probability of a word being associated with a particular tag (e.g., P("cat" | Noun)).

### Formulas:
- **Forward Algorithm** (used for evaluating the probability of a given observation sequence):
  \[
  \alpha_t(i) = P(o_1, o_2, ..., o_t, s_i)
  \]
  where \( \alpha_t(i) \) is the forward variable representing the probability of the partial observation sequence up to time \( t \) and ending in state \( i \).

- **Viterbi Algorithm** (used for decoding the most probable sequence of states):
  \[
  \delta_t(i) = \max_{s_{t-1}} (\delta_{t-1}(s_{t-1}) \cdot A_{s_{t-1},s_i} \cdot B_{s_i, o_t})
  \]
  where \( \delta_t(i) \) is the maximum probability of the state sequence up to time \( t \) and ending in state \( i \).

## Step-by-Step Implementation of the POS Tagger:

### 1. Create the `pos_tagger.py` Script:
In this script, we will implement a simple POS tagger using an HMM. We will use the `hmmlearn` library to define our HMM and train it on a simplified dataset.

#### POS Tagging Example:
We will train a model using a small set of POS-tagged words. For simplicity, we will create a mini dataset where each word is tagged as either a noun or a verb.

#### 1.1 Data Format:
- **Sentences**: Each sentence is a sequence of words.
- **Tags**: Each word in the sentence is tagged with its POS (e.g., Noun or Verb).

Example:

- **Sentence**: `["I", "saw", "the", "cat"]`
- **Tags**: `["NOUN", "VERB", "DET", "NOUN"]`

## How to Run:
1. Install the dependencies:


## Features
- Train an HMM on labeled POS data.
- Decode sequences to predict POS tags for sentences.

## Setup

### Install Requirements
```bash
pip install -r requirements.txt