def natural_connections(stations):
    n = len(stations)

    for i in range(1, n - 1):
        prev_station = stations[i - 1]
        curr_station = stations[i]
        next_station = stations[i + 1]

        if len(prev_station) == 1:
            curr_station[0].backward = prev_station[0]
            curr_station[1].forward = prev_station[0]
        else:
            curr_station[0].backward = prev_station[1]
            curr_station[1].forward = prev_station[1]

        curr_station[0].forward = next_station[0]
        curr_station[0].opposite = curr_station[1]
        curr_station[1].backward = next_station[0]
        curr_station[1].opposite = curr_station[0]

        assert (curr_station[0].forward == curr_station[1].backward)
        assert (curr_station[1].forward == curr_station[0].backward)

    stations[0][0].backward = stations[1][0]
    stations[0][0].forward = stations[1][0]
    stations[0][0].opposite = stations[0][0]
    stations[-1][0].backward = stations[-2][1]
    stations[-1][0].forward = stations[-2][1]
    stations[-1][0].opposite = stations[-1][0]

    return stations


def flatten(stations):
    flattened = []
    for s in stations:
        flattened += s

    return flattened
