"""
    Recursive Patterns
    1. Check-Recurse-Store (Memoization)
        Overlapping subproblems exist
        Need to cache results
        Top-down DP problems

    2. Pre-Post Processing
        Working with trees
        Need to process before/after recursion
        Building results bottom-up

    3. Build up-Tear down
        Generating combinations/permutations
        Need to try all possibilities
        Backtracking problems

    4. Divide-Conquer-Combine
        Problem can be split into similar subproblems
        Sorting/searching large datasets
        Parallel processing possible

    5. Accumulator
        Building a result across recursive calls
        Need to maintain state
        Path-finding problems


"""
# def crs(args, memo=None):
#     if memo is None:
#         memo = {}
#     if args in memo:
#         return memo[args]
#     if base_condition:
#         return base_value
#     result = crs(smaller_args, memo)
#     memo[args] = result
#     return result


# def prepostproc(node):
#     if not node:
#         return
#     # PRE-PROCESSING
#     result = some_operation(node)
#     # RECURSE
#     left = prepostproc(node.left)
#     right = prepostproc(node.right)
#     # POST-PROCESSING
#     return combine(result, left, right)


# def butd(args, current=[]):
#     if solution_found:
#         results.append(current[:])  # Save copy
#         return
#     for choice in choices:
#         # BUILD
#         current.append(choice)
#         # RECURSE
#         butd(new_args, current)
#         # TEAR DOWN
#         current.pop()


# def dcc(data):
#     if base_case:
#         return solve_base(data)

#     # DIVIDE
#     left_half = data[:mid]
#     right_half = data[mid:]

#     # CONQUER (recurse)
#     left_result = dcc(left_half)
#     right_result = dcc(right_half)

#     # COMBINE
#     return merge(left_result, right_result)


# def acc(args):
#     result = []  # or other accumulator

#     def _acc(args, acc):
#         if base_case:
#             result.append(acc)  # or other accumulation
#             return

#         for choice in choices:
#             _acc(new_args, acc + [choice])

#     _acc(args, [])  # Start with empty accumulator
#     return result

def longest_palindrome(s):
    n = len(s)
    # dp[i][j] = longest palindrome from i to j
    dp = [[1 if i == j else 0 for j in range(n)]
          for i in range(n)]

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            dp[length-1][start] += 1

    for row in dp:
        print(row)

if __name__=="__main__":
    longest_palindrome('string')

