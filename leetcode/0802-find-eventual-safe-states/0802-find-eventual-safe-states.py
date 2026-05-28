class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        _graph = defaultdict(list)
        degree = [0] * len(graph)

        for i in range(len(graph)):
            for node in graph[i]:
                _graph[node].append(i)
            degree[i] += len(graph[i])

        ans = []
        q = deque()

        for node in range(len(degree)):
            if degree[node] == 0: 
                q.append(node)
        
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
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna