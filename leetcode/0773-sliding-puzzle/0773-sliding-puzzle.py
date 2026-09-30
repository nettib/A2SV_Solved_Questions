class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        target = ((1, 2, 3), (4, 5, 0))
        visited = set()
        q = deque([])
        moves = 0


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 0:
                    start = tuple(tuple(nums) for nums in board)
                    q.append((start, r, c))
        

        while q:
            for _ in range(len(q)):
                state, r, c = q.popleft()

                if state == target:
                    return moves

                temp = list(list(nums) for nums in state)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not inbound(nr, nc):
                        continue
                    
                    temp[r][c], temp[nr][nc] = temp[nr][nc], temp[r][c]
                    state = tuple(tuple(nums) for nums in temp)

                    if state not in visited:
                        visited.add(state)
                        q.append((state, nr, nc))

                    temp[r][c], temp[nr][nc] = temp[nr][nc], temp[r][c]
            
            moves += 1
        
        return -1
                





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna