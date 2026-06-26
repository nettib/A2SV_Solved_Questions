class Solution:
    def racecar(self, target: int) -> int:
        def move_A(p, s):
            p += s
            s *= 2
            return p, s
        
        def move_R(p, s):
            if s > 0:
                s = -1
            else:
                s = 1
            
            return p, s
        
        def nei_work(p, s, fun):
            np, ns = fun(p, s)
            if (np, ns) in visited:
                return
            visited.add((np, ns))
            q.append((np, ns))

        
        q = deque([(0, 1)])
        visited = set([(0, 1)])

        steps = 0
        while q:
            for _ in range(len(q)):
                p, s = q.popleft()

                if p == target:
                    return steps

                nei_work(p, s, move_A)
                nei_work(p, s, move_R)

            steps += 1
        
        return steps


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna