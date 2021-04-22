import numpy as np


def normalize(x):
    return x / np.sum(x)


def execute_simulation(observations, stations, PAM, verbose=False):
    n = len(stations)
    I = np.eye(n) / n
    ll = np.ndarray((len(observations) + 1, n))

    def update(state, observation, PAM):
        state = PAM @ state
        new_state = np.array([
            stations[i].probability_of_observation(*observation) * state[i]
            for i in range(n)
        ])

        return normalize(new_state)

    def print_beautify(state, n_digits=2):
        state = [round(x, n_digits) for x in state]
        for i in range(len(state)):
            print(stations[i].name, state[i])

    ll[0] = normalize(np.ones((n)))

    for i in range(len(observations)):
        ll[i + 1] = update(ll[i], observations[i], PAM)
    return ll
