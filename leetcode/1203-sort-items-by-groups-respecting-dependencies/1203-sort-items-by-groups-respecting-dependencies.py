class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        ggraph = defaultdict(set)

        c = m
        for i in range(n):
            if group[i] == -1:
                group[i] = c
                c += 1
        
        degreeg = [0] * c
        
        for i in range(len(beforeItems)):
            gi = group[i]
            for j in range(len(beforeItems[i])):
                gj = group[beforeItems[i][j]]
                if gi not in ggraph[gj] and gi != gj:
                    ggraph[gj].add(gi)
                    degreeg[gi] += 1 
        

        res1 = []
        q = deque()

        for i in range(c):
            if degreeg[i] == 0: q.append(i)
        
        while q:
            node = q.popleft()
            res1.append(node)

            for nei in ggraph[node]:
                degreeg[nei] -= 1
                if degreeg[nei] == 0: q.append(nei)
        
        if len(res1) != c:
            return []
        
        g = defaultdict(list)

        for i in range(len(group)):
            g[group[i]].append(i)



        def bfs(graph, degree, n):
            res = []
            q = deque()

            for node in degree:
                if degree[node] == 0:
                    q.append(node)
                
            while q:
                node = q.popleft()
                res.append(node)

                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 0: q.append(nei)
            
            if len(res) != n:
                return []
    
            
            return res
        
        for i in g:

            igraph = defaultdict(list)
            degreei = {}

            for item in g[i]:
                degreei[item] = 0

            for item in g[i]:
                for j in beforeItems[item]:
                    if group[j] == i:
                        igraph[j].append(item)
                        degreei[item] += 1
            
            g[i] = bfs(igraph, degreei, len(g[i]))

            if not g[i]: return []

        
        # g, res1
        ans = []

        for gr in res1:
            ans.extend(g[gr])
        
        return ans


        


        
            








# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna