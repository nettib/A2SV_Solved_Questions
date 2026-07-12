class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        def at_the_edge(r, c):
            return 0 == r or 0 == c or len(board) - 1 == r or len(board[0]) - 1 == c

        def dfs(r, c):
            nonlocal border

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not inbound(nr, nc) or (nr, nc) in visited or board[nr][nc] == 'X':
                    continue
                if at_the_edge(nr, nc):
                    border = 1
                
                visited.add((nr, nc))
                temp.append((nr, nc))
                dfs(nr, nc)
                    
        visited = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in visited and not at_the_edge(r, c):
                    visited.add((r, c))
                    temp = [(r, c)]
                    border = 0
                    dfs(r, c)
                    if not border:
                        for rr, cc in temp:
                            board[rr][cc] = 'X'
                        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna