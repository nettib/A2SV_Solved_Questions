class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        def check_edge(r, c):
            return 0 == r or r == len(board) - 1 or 0 == c or c == len(board[0]) - 1 
        
        def dfs(r, c, region):

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                
                if not inbound(nr, nc) or (nr, nc) in visited or board[nr][nc] == "X":
                    continue
                
                if board[nr][nc] == "O" and check_edge(nr, nc): 
                    return False
                
                visited.add((nr, nc))
                region.append((nr, nc))
                if not dfs(nr, nc, region):
                    return False
                
            return True
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and not check_edge(r, c):
                    region = [(r, c)]
                    visited = {(r, c)}

                    if dfs(r, c, region):
                        for pr, pc in region:
                            board[pr][pc] = "X"
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna