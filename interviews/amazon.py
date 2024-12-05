from random import randint

def get_child(i):
    return i-(i&(-i))

def get_parent(i):
    return i+(i&(-i))

def warehouseCapacity(warehouses, distributionCenters=[]):
    fen = [0]*(len(warehouses)+1)
    n = len(warehouses)

    last_dc_location = len(warehouses) # locations are 1-based
    last_dc_cap = warehouses[-1] # capacities come from warehouse list
    print('before')
    for i in range(1, len(warehouses)):
        j = i
        while j < len(warehouses):
            location = j+1
            cap = warehouses[location-1]
            fen[location] += cap
            j = get_parent(j)

    print(warehouses)
    print(fen[1:])

    def query(tree, q):
        # add distribution centers
        treec = tree.copy()
        for location in q:
            c = warehouses[location-1]
            i = location
            while i < n:
                tree[i] += c
                i = get_parent(i)


    results = []
    # loop distributionCenters, collect results
    for hubs in distributionCenters:
        results.append(query(fen, hubs))

    return results





if __name__=="__main__":
    warehouses = [randint(1, 20) for _ in range(10)]
    warehouses.sort()
    distributionCenters = [
        [1, 9],
        [1, 2],
        [3, 5],
        [4, 4],
    ] # 1-based
    result = warehouseCapacity(warehouses, distributionCenters)
