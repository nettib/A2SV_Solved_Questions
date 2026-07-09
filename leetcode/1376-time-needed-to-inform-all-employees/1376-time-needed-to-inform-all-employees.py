class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for _id in range(len(manager)):
            if _id == headID:
                continue
            graph[manager[_id]].append(_id)
        
        max_time = 0
        def dfs(manager, time):
            nonlocal max_time
            time += informTime[manager]
            max_time = max(max_time, time)

            for employee in graph[manager]:
                dfs(employee, time)
            
        dfs(headID, 0)
        return max_time
        


    
            





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna