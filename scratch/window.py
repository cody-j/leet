from random import randint
arr = [randint(0, 4) for x in range(4)]

def window_sum(arr=[], k=1):
    wind_sum = sum(arr[:k])
    max_sum = wind_sum
    # for "what's left of the array (len - window size, k)"
    for i in range(len(arr) - k):
        wind_sum = wind_sum - arr[i] + arr[k]
        max_sum = max(max_sum, wind_sum)
    return max_sum


def sliding(arr):
    start = 0
    current = {}
    result = 0
    for end in range(len(arr)):
        current[arr[end]] = current.get(arr[end], 0) + 1



if __name__=="__main__":
    print(arr)
    print(window_sum(arr, 2))
