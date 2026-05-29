class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        degree = [0] * len(colors)

        for u, v in edges:
            graph[u].append(v)
            degree[v] += 1
        
        count = [[0] * 26 for _ in range(len(colors))]

        q = deque()

        for node in range(len(degree)):
            if degree[node] == 0:
                q.append(node)
                ci = ord(colors[node]) - ord('a')
                count[node][ci] = 0
        
        visit = res = 0
        while q:
            node = q.popleft()
            visit += 1
            ci = ord(colors[node]) - ord('a')
            count[node][ci] += 1
            res = max(res, count[node][ci])
        
            for nei in graph[node]:
                degree[nei] -= 1
                for c in range(len(count[node])):
                    count[nei][c] = max(count[nei][c], count[node][c])

                if degree[nei] == 0:
                    q.append(nei)
        
        return res if visit == len(colors) else -1
            
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna