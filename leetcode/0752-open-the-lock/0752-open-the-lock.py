class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        target = [int(num) for num in target]

        _deadends = set()

        for deadend in deadends:
            _deadends.add(tuple([int(num) for num in deadend]))

        def modulo(x1, x2, x3, x4):
            return x1 % 10, x2 % 10, x3 % 10, x4 % 10

        directions = [
            (0, 0, 0, 1),
            (0, 0, 1, 0),
            (0, 1, 0, 0),
            (1, 0, 0, 0),
            (-1, 0, 0, 0),
            (0, -1, 0, 0),
            (0, 0, -1, 0),
            (0, 0, 0, -1),
        ]
        visited = {(0, 0, 0, 0)}
        q = deque([(0, 0, 0, 0)])

        d = 0
        while q:
            for _ in range(len(q)):
                x1, x2, x3, x4 = q.popleft()

                if [x1, x2, x3, x4] == target:
                    return d

                for dx1, dx2, dx3, dx4 in directions:
                    nx1, nx2, nx3, nx4 = modulo(x1 + dx1, x2 + dx2, x3 + dx3, x4 + dx4)

                    if (nx1, nx2, nx3, nx4) in visited or (nx1, nx2, nx3, nx4) in _deadends:
                        continue

                    visited.add((nx1, nx2, nx3, nx4))
                    q.append((nx1, nx2, nx3, nx4))

            d += 1

        return -1



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna