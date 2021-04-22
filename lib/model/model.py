def normalize(v):
    n = sum(v)
    return [x / n for x in v]


def predict(x, action, line):
    ret = [0 for _ in x]
    for i in range(len(line)):
        transition = state_model(line, i, action)
        for j in range(len(line)):
            ret[j] += x[i] * transition[j]
    assert (abs(sum(ret) - 1) < 1e-5)
    return ret  # should sum to 1 already


def print_beautify(stations, v, n_digits=2):
    v = [round(x, n_digits) for x in v]
    for i in range(len(v)):
        print(stations[i].name, v[i])


state_model_mtx = {
    -1: {
        -1: 0.85,
        0: 0.10,
        1: 0.05
    },
    0: {
        -1: 0.05,
        0: 0.90,
        1: 0.05
    },
    1: {
        -1: 0.05,
        0: 0.10,
        1: 0.85
    }
}


def state_model(line, i, action):
    ret = [0 for _ in range(len(line))]

    for chi in [-1, 0, 1]:
        dest = i + chi
        dest = max(min(dest, len(line) - 1), 0)  #clip to 0 len(line)-1
        ret[dest] += state_model_mtx[action][chi]
    return ret


def update(x, observation, line):
    ret = [0 for _ in x]
    for i in range(len(line)):
        p = line[i].probability_of_observation(*observation)
        ret[i] = p * x[i]
    return normalize(ret)


def execute_simulation(observations, line):

    number_of_states = len(observations) + 1
    actions = [1 for _ in range(number_of_states - 1)]
    assert len(actions) == len(
        observations
    ), f"got {len(actions)} actions and {len(observations)} observations"
    x = normalize([1 for _ in range(len(line))])
    for action, observation in zip(actions, observations):
        # print_beautify(line, x)
        x = predict(x, action, line)
        x = update(x, observation, line)
    print_beautify(line, x)
