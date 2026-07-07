class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def inbound(r, c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])

        starting_color = image[sr][sc]

        image[sr][sc] = color

        q = deque([(sr, sc)])
        visited = set([(sr, sc)])

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not inbound(nr, nc) or (nr, nc) in visited or image[nr][nc] != starting_color:
                    continue
                
                visited.add((nr, nc))
                image[nr][nc] = color
                q.append((nr, nc))
        

        return image
                



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna