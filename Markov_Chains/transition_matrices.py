import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from text_generator import build_transition_matrix

def visualize_transition_matrix(transition_matrix):
    """
    Visualizes the transition matrix using a heatmap.
    :param transition_matrix: Transition matrix as a dictionary.
    """
    states = list(transition_matrix.keys())
    vocab = sorted(set(word for state in states for word in state))
    
    matrix = np.zeros((len(states), len(vocab)))
    state_index = {state: i for i, state in enumerate(states)}
    word_index = {word: i for i, word in enumerate(vocab)}
    
    for state, transitions in transition_matrix.items():
        for word, prob in transitions.items():
            matrix[state_index[state], word_index[word]] = prob
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, annot=False, xticklabels=vocab, yticklabels=states, cmap="coolwarm")
    plt.xlabel("Next Word")
    plt.ylabel("Current State")
    plt.title("Transition Matrix Heatmap")
    plt.show()

if __name__ == "__main__":
    text = "I love programming in Python. Python is a great language for solving problems.".split()
    n = 2  
    transition_matrix = build_transition_matrix(text, n)
    visualize_transition_matrix(transition_matrix)
