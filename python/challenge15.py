def number(bus_stops):
    # There is a bus moving in the city which takes and drops some people at each bus stop.
    # [1, 2] - 1: Num that get on the bus, 2: off the bus.
    current = 0
    for i in bus_stops:
        for x in i:
            if x == i[0]:
                onbus = x
            else:
                offbus = x
            offbus = x
        current = current + (onbus - offbus)
    return(current)
