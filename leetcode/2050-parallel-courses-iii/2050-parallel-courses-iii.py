class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        degree = [0] * (n + 1)

        for u, v in relations:
            graph[u].append(v)
            degree[v] += 1
        
        q = deque()

        for c in range(1, n + 1):
            if degree[c] == 0: q.append(c)

        earliest = [0] * (n + 1)
        
        while q:
            c = q.popleft()

            for nei in graph[c]:
                earliest[nei] = max(earliest[nei], earliest[c] + time[c - 1])
                degree[nei] -= 1
                if degree[nei] == 0: q.append(nei)

        for i in range(1, n + 1):
            earliest[i] += time[i - 1]

        return max(earliest)





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna