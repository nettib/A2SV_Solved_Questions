class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 = "WHITE", 1 = "GRAY", 2 = "BLACK"
        
        courses = defaultdict(list)
        colors = [0] * numCourses

        for c1, c2 in prerequisites:
            courses[c2].append(c1)
        
        visited = set()
        def dfs(course):
            
            for nei in courses[course]:
                if nei in visited:
                    if colors[nei] == 1:
                        return False
                    continue
                colors[nei] = 1
                visited.add(nei)
                if not dfs(nei):
                    return False
            colors[course] = 2
            return True
        
        for course in range(numCourses):
            if course not in visited:
                colors[course] = 1
                visited.add(course)
                if not dfs(course):
                    return False
        
        return True
        





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna