class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
            def get_next_state(j1, j2):
                return [
                    [x, j2],
                    [j1, y],
                    [0, j2],
                    [j1, 0],
                    [j1 - min(j1, y - j2), j2 + min(j1, y - j2)],
                    [j1 + min(j2, x - j1), j2 - min(j2, x - j1)],
                ]

            def inbound(j1, j2):
                return 0 <= j1 <= x and 0 <= j2 <= y

            visited = set()

            def dfs(j1, j2):

                visited.add((j1, j2))
                if j1 + j2 == target:
                    return True

                next_states = get_next_state(j1, j2)
                for nx, ny in next_states:
                    if (nx, ny) in visited or not inbound(nx, ny):
                        continue
                    if dfs(nx, ny):
                        return True

                return False

            return dfs(0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna