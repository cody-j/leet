"""
Knapsack Problem (DP)

    Considered "Dynamic Programming" because it requires:

        1. Overlapping SUB-problems (repeated work/lookup previously calculated)
        2. Optimal SUB-structure


    for each item, for each w (potential remaining capacity) calculate best possible outcome:
        if doesn't fit, lookback and find the previous value if it was included
        max(
            k[]
        )

"""
def genitems():
    # v, w
    items = [
        (10, 3),
        (3, 1),
        (6, 2),
    ]
    capacity = 5
    return items, capacity


def solveknapsack(items, capacity):
    t=[0]*(capacity+1) # highest value seen
    p=[[]]*(capacity+1) # path items for highest value

    for value, weight in items:
        for i in range(capacity, weight-1, -1):
            value_with = t[i-weight]+value
            value_without = t[i]
            if value_with > value_without:
                t[i] = value_with
                p[i] = p[i-weight] + [(value, weight)]
    return t[capacity], p[capacity]


if __name__=="__main__":
    items, capacity = genitems()
    results = solveknapsack(items, capacity)
    print(f'results: {results}')
