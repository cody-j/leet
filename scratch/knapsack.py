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
    k = [0] * (capacity+1)
    c = [[]] * (capacity+1)
    for i, (value, weight) in enumerate(items):
        for w in range(capacity, weight-1, -1):
            without_item=k[w]
            with_item=(k[w-weight]+value)
            if with_item > without_item:
                k[w] = with_item
                c[w] = c[w-weight] + [(value,weight)]
    return k[capacity], c[capacity]

if __name__=="__main__":
    items, capacity = genitems()
    results = solveknapsack(items, capacity)
    print(f'results: {results}')
