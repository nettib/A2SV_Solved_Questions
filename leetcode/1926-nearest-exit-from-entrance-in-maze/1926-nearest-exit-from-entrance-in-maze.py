class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        def inbound(r, c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0])

        def at_border(r, c):
            return 0 == r or r == len(maze) - 1 or 0 == c or c == len(maze[0]) - 1
        
        q = deque([(entrance[0], entrance[-1])])
        maze[entrance[0]][entrance[-1]] = "+"

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if not inbound(nr, nc) or maze[nr][nc] == "+":
                        continue

                    if at_border(nr, nc):
                        return steps

                    maze[nr][nc] = "+"
                    q.append((nr, nc))
        
        return -1
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna