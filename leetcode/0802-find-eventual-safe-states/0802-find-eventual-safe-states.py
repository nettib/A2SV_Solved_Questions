class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        _graph = defaultdict(list)
        degree = [0] * len(graph)

        for n1 in range(len(graph)):
            for n2 in graph[n1]:
                _graph[n2].append(n1)
                degree[n1] += 1

        q = deque([])

        for node in range(len(degree)):
            if degree[node] == 0:
                q.append(node)
        
        ans = []

        while q:
            node = q.popleft()
            ans.append(node)

            for nei in _graph[node]:
                degree[nei] -= 1

                if degree[nei] == 0:
                    q.append(nei)
            
        return sorted(ans)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna