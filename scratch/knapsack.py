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
        (3, 1),
        (6, 2),
        (10, 3),
    ]
    capacity = 5
    return items, capacity

def solveknapsack(items, capacity):
    # initialize array of best values at each weight
    k = [0] * (capacity+1)
    pass

if __name__=="__main__":
    items, capacity = genitems()
    results = solveknapsack(items, capacity)
    print(f'results: {results}')
