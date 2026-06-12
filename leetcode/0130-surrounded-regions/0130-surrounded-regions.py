class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def board_edge(r, c, board):
            return (
                (0 == r)
                or (r == (len(board) - 1))
                or (0 == c)
                or (c == (len(board[0]) - 1))
            )

        def dfs(r, c):

            board[r][c] = "U"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not inbound(nr, nc) or board[nr][nc] != "O":
                    continue

                dfs(nr, nc)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board_edge(r, c, board) and board[r][c] == "O":
                    dfs(r, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "U":
                    board[r][c] = "O"


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna