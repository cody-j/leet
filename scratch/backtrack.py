from collections import deque
import copy
def nqueens(n):
    """
        if not valid(state):
            return

        choice, new_state = choose(state) # state modification
        mark_used(choice) # tracking

        backtrack(new_state) # recurse


    """
    board = [[0]*n for _ in range(n)]
    queens = 0
    def mark_attacks(row, col, available=False):

        for i in range(row+1, len(board)):
            board[i][col] = board[i][col] - 1 if available else board[i][col] + 1
            rows_ahead = i-row
            if col-rows_ahead >= 0:
                board[i][col-rows_ahead] = max(0, board[i][col-rows_ahead] - 1) if available else board[i][col-rows_ahead] + 1
            if col+rows_ahead < len(board[row]):
                board[i][col+rows_ahead] = board[i][col+rows_ahead] - 1 if available else board[i][col+rows_ahead] + 1

    def is_solution(board):
        return True
    results = []
    def backtrack(board, row):
        nonlocal queens
        if row >= len(board):
            print('n: ', n)
            if queens == n:
                print('solution found!')
                results.append([[ 'Q' if board[row][col] == 'Q' else '.' for col in range(len(board[row])) ] for row in range(len(board))])
            return

        for col in range(len(board[row])):
            if board[row][col] > 0:
                continue

            board[row][col] = 'Q'
            queens += 1
            mark_attacks(row, col)
            backtrack(board, row+1)
            mark_attacks(row, col, available=True)
            board[row][col] = 0
            queens -= 1
        return board



    backtrack(board, 0)
    return len(results), results

def gen_parens(n):
    valid_parens = []

    def backtrack(s='', l=0, r=0):
        nonlocal valid_parens

        if l == r and r == n:
            valid_parens.append(s)
            return

        if l < n:
            backtrack(s+'(', l+1, r)
        if r < l:
            backtrack(s+')', l, r+1)

    backtrack(s='(', l=1)

    return valid_parens

def perms(word):
    if len(word) == 1:
        return 1

    if len(word) == 2:
        return 2
    valid_parens = []
    q = deque([(word[0], word[1:])])

    while q:
        perm, rest = q.popleft()


        print(perm, rest)

    return valid_parens

if __name__=="__main__":


    n = 4

    results = perms('123')
    for s in results:
        print(s)

    # queens, boards = nqueens(n)
    # print(f'n queens for {n}={queens}')
    # for i in range(len(boards)):
    #     print(f'Solution {i+1}:')
    #     for row in boards[i]:
    #         print(row)

