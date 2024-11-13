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

def knapsack(items, capacity):
    # initialize array of best values at each weight
    # Initialize array of best values at each weight
    dp = [0] * (capacity + 1)

    # Track which items we choose (optional but helpful)
    chosen = [[]] * (capacity + 1)

    print(f"Initial dp array: {dp}")

    for index, (value, weight) in enumerate(items):
        print(f"\nProcessing item {index}: value={value}, weight={weight}")

        # Go backwards to avoid overwriting values we still need
        for w in range(capacity, weight-1, -1):
            # Should we take this item at this weight?
            value_without_item = dp[w]
            value_with_item = dp[w-weight] + value

            print(f"  At weight {w}:")
            print(f"    Without item: {value_without_item}")
            print(f"    With item: {value_with_item}")

            if value_with_item > value_without_item:
                dp[w] = value_with_item
                # Track items chosen (optional)
                chosen[w] = chosen[w-weight] + [(value, weight)]
                print(f"    Took item! New value: {dp[w]}")
            else:
                print(f"    Skipped item, keeping: {dp[w]}")

        print(f"DP array after item {index}: {dp}")

    return dp[capacity], chosen[capacity]


def solveknapsack(items, capacity):
    # highest value by weight used
    k = [0] * (capacity+1)

    # chosen items composing highest value
    c = [[]] * (capacity+1)

    for i, (value, weight) in enumerate(items):
        for w in range(weight, capacity+1):
            # At this packed weight, w the value without this item, is the current value recorded
            without_item=k[w]
            with_item=(k[w-weight]+value)
            if with_item > without_item:
                k[w] = with_item
                c[w] = c[w-weight] + [(value,weight)]

    print(k)
    print(c)

if __name__=="__main__":
    items, capacity = genitems()
    results = solveknapsack(items, capacity)
    # print(f'results: {results}')
