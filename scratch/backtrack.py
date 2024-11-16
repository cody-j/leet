def nqueens(n):
    """
        if not valid(state):
            return

        choice, new_state = choose(state) # state modification
        mark_used(choice) # tracking

        backtrack(new_state) # recurse


    """
    board = [[0]*n for _ in range(n)]


    def valid(cell):
        return cell == '.'

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

    def backtrack(board, row):
        if row >= len(board):
            if is_solution(board):
                for row in board:
                    print(['Q' if v == 'Q' else '.' for v in row])
                print('')
            return

        for col in range(len(board[row])):
            if board[row][col] > 0:
                continue

            board[row][col] = 'Q'
            mark_attacks(row, col)
            backtrack(board, row+1)
            mark_attacks(row, col, available=True)
            board[row][col] = 0
        return board



    board = backtrack(board, 0)
    return board


if __name__=="__main__":
    board = nqueens(5)
