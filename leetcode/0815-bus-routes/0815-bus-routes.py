class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)

        for i in range(len(routes)):
            routes[i] = set(routes[i])
            for j in range(i + 1, len(routes)):
                for num in routes[j]:
                    if num in routes[i]:
                        graph[i].append(j)
                        graph[j].append(i)
                        break
        
        def bfs():
            nonlocal bus

            while q:
                bus += 1
                for _ in range(len(q)):
                    node = q.popleft()

                    if target in routes[node]:
                        return bus

                    for nei in graph[node]:
                        if nei in visited:
                            continue
                        visited.add(nei)
                        q.append(nei)

            return float("inf")


        
        _min = float("inf")
        for i in range(len(routes)):
            if source in routes[i]:
                q = deque([i])
                bus = 0
                visited = {i}
                res = bfs()
                _min = min(_min, res)
        
        if _min == float("inf"):
            return -1
        
        return _min


        
       

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna