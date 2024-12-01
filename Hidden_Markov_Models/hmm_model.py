import numpy as np
from collections import defaultdict

class HiddenMarkovModel:
    def __init__(self, smoothing_factor=1e-6):
        self.start_probs = defaultdict(float)
        self.trans_probs = defaultdict(lambda: defaultdict(float))
        self.emit_probs = defaultdict(lambda: defaultdict(float))
        self.states = []  
        self.observations = [] 
        self.smoothing_factor = smoothing_factor  

    def train(self, tagged_sentences):
        state_counts = defaultdict(int)
        start_counts = defaultdict(int)
        trans_counts = defaultdict(lambda: defaultdict(int))
        emit_counts = defaultdict(lambda: defaultdict(int))

        for sentence in tagged_sentences:
            prev_state = None
            for word, tag in sentence:
                state_counts[tag] += 1
                emit_counts[tag][word] += 1
                if prev_state is None:
                    start_counts[tag] += 1
                else:
                    trans_counts[prev_state][tag] += 1
                prev_state = tag

        total_starts = sum(start_counts.values())
        for state, count in start_counts.items():
            self.start_probs[state] = (count + self.smoothing_factor) / (total_starts + len(start_counts) * self.smoothing_factor)

        for state, transitions in trans_counts.items():
            total_transitions = sum(transitions.values())
            for next_state, count in transitions.items():
                self.trans_probs[state][next_state] = (count + self.smoothing_factor) / (total_transitions + len(self.states) * self.smoothing_factor)

        for state, emissions in emit_counts.items():
            total_emissions = sum(emissions.values())
            for observation, count in emissions.items():
                self.emit_probs[state][observation] = (count + self.smoothing_factor) / (total_emissions + len(self.observations) * self.smoothing_factor)

        self.states = list(state_counts.keys())
        self.observations = list(
            {word for emissions in emit_counts.values() for word in emissions.keys()}
        )

    def predict(self, observations):

        V = [{}]
        path = {}

        for state in self.states:
            V[0][state] = self.start_probs.get(state, self.smoothing_factor) * self.emit_probs[state].get(observations[0], self.smoothing_factor)
            path[state] = [state]

        for t in range(1, len(observations)):
            V.append({})
            new_path = {}

            for state in self.states:
                (prob, state_max) = max(
                    (V[t - 1][prev_state] * self.trans_probs[prev_state].get(state, self.smoothing_factor) *
                     self.emit_probs[state].get(observations[t], self.smoothing_factor), prev_state)
                    for prev_state in self.states
                )
                V[t][state] = prob
                new_path[state] = path[state_max] + [state]

            path = new_path

        (prob, state_max) = max((V[len(observations) - 1][state], state) for state in self.states)
        return path[state_max]
