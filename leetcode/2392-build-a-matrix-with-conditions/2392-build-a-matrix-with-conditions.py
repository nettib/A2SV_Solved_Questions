class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def get_position(k, conditions):
            graph = defaultdict(list)
            degree = [0] * (k + 1)

            for num1, num2 in conditions:
                graph[num1].append(num2)
                degree[num2] += 1

            q = deque([])

            for num in range(1, k + 1):
                if degree[num] == 0:
                    q.append(num)
            
            ans = []

            while q:
                num = q.popleft()
                ans.append(num)

                for nei in graph[num]:
                    degree[nei] -= 1

                    if degree[nei] == 0:
                        q.append(nei)
            
            if len(ans) < len(graph):
                return []
            return ans
        
        row = get_position(k, rowConditions)
        col = get_position(k, colConditions)
        
        if not row or not col:
            return []
        
        ans = [[0 for _ in range(k)] for _ in range(k)]

        ansg = defaultdict(list)

        for i in range(len(row)):
            ansg[row[i]].append(i)
        
        for i in range(len(col)):
            ansg[col[i]].append(i)
        
        for num in ansg:
            ans[ansg[num][0]][ansg[num][-1]] = num
        
        return ans




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna