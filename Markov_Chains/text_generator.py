import random

def build_transition_matrix(corpus, n=1):
    """
    Builds a transition matrix for a Markov Chain.
    :param corpus: List of words in the text.
    :param n: Order of the Markov Chain (default is 1, first-order).
    :return: Transition matrix as a dictionary.
    """
    transitions = {}
    
    for i in range(len(corpus) - n):
        state = tuple(corpus[i:i+n])
        next_word = corpus[i+n]
        
        if state not in transitions:
            transitions[state] = {}
        
        if next_word not in transitions[state]:
            transitions[state][next_word] = 0
        
        transitions[state][next_word] += 1
    
    for state, next_words in transitions.items():
        total = sum(next_words.values())
        transitions[state] = {word: count / total for word, count in next_words.items()}
    
    return transitions

def generate_text(chain, start_state, length=20):
    """
    Generates text using a Markov Chain.
    :param chain: Transition matrix (dictionary).
    :param start_state: Initial state (tuple of words).
    :param length: Number of words to generate.
    :return: Generated text as a string.
    """
    current_state = start_state
    generated_words = list(current_state)  

    for _ in range(length - len(start_state)):
        if current_state in chain:
            next_word = random.choices(
                population=list(chain[current_state].keys()),
                weights=list(chain[current_state].values())
            )[0]
            generated_words.append(next_word)

            current_state = tuple(generated_words[-len(current_state):])
        else:
            current_state = random.choice(list(chain.keys()))
            generated_words.extend(list(current_state))

    return " ".join(generated_words)


if __name__ == "__main__":
    text = "I love programming in Python. Python is a great language for solving problems.".split()
    n = 2  
    transition_matrix = build_transition_matrix(text, n)
    
    start_state = ("I", "love")
    
    generated_text = generate_text(transition_matrix, start_state, length=20)
    print("Generated Text:", generated_text)
