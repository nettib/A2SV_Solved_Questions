class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * n

        for c1, c2 in p:
            graph[c2].append(c1)
            degree[c1] += 1
        
        q = deque([])
        ans = []

        for course in range(n):
            if degree[course] == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            ans.append(course)

            for nei in graph[course]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)

        if len(ans) != n:
            return []
        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna