from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
            q = deque([0])

            r = 0
            visited = set([0])
            while q:
                room = q.popleft()
                r += 1

                for key in rooms[room]:
                    if key in visited: continue
                    visited.add(key)
                    q.append(key)
            
            return r == len(rooms)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna