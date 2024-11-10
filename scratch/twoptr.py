import random
arr = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7]
rand_arr = [random.randint(0, 10) for _ in range(10)]

'''
left pointer, l represents the right-most unique number seen so far in the collection.
uniqueness is guaranteed for the first element, after that, we check against r, which
is initialized as l + 1
'''
def remove_duplicates(arr):
    l, r = 0, 1
    while r < len(arr):
        if arr[l] != arr[r]:
            l += 1
            arr[l] = arr[r]
        r += 1
    return l + 1

def two_sum(arr, n):
    a = sorted(arr)
    l, r = 0, len(a)-1
    while l < r:
        s = arr[l] + arr[r]
        print(l,r,s)
        if s == n:
            return [l,r]
        if s > n:
            r -= 1
        else:
            l += 1

def merge_sorted(a1, a2):
    p1 = len(a1) - 1  # Last element of nums1
    p2 = len(a2) - 1  # Last element of nums2
    r = a1 + [0]*len(a2)
    p = len(a1) + len(a2) - 1  # Last position in result

    while p2 >= 0:  # While we have elements in nums2
        if p1 >= 0 and a1[p1] > a2[p2]:
            r[p] = a1[p1]
            p1 -= 1
        else:
            r[p] = a2[p2]
            p2 -= 1
        p -= 1

    return r

if __name__=="__main__":
    print(arr,arr)
    # print(two_sum(arr, 11))
    # k = remove_duplicates(arr)
    print(merge_sorted(arr, arr))
    # print(arr[0:k])
