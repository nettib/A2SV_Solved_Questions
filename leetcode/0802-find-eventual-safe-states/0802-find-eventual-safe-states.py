class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        _graph = defaultdict(list)
        degree = [0] * len(graph)
        safe = [0] * len(graph)

        for i in range(len(graph)):
            for node in graph[i]:
                _graph[node].append(i)
            degree[i] += len(graph[i])

        
        q = deque()

        for node in range(len(degree)):
            if degree[node] == 0: 
                q.append(node)
        
        while q:
            node = q.popleft()
            safe[node] = 1

            for nei in _graph[node]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)
        
        ans = []

        for node in range(len(safe)):
            if safe[node]:
                ans.append(node)
        
        return ans
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna