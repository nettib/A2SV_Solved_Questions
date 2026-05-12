from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        has_dep = set()

        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            has_dep.add(c1)
        
        
        indegree = defaultdict(int)

        for c1, c2 in prerequisites:
            indegree[c1] += 1


        q = deque([])

        for c in range(numCourses):
            if c not in has_dep:
                q.append(c)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(ans) == numCourses:
            return ans
        return []

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna