from collections import defaultdict, deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque()

        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
        
        ancestors = [set() for _ in range(n)]

        while q:
            node = q.popleft()

            for nei in graph[node]:
                ancestors[nei] |= ancestors[node] | {node}

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        
        ans = [sorted(s) for s in ancestors]
        return ans