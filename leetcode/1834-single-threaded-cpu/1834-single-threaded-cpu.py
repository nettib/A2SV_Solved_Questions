class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort()

        heap = [[tasks[0][1], tasks[0][-1]]]
        t = tasks[0][0]
        idx = 1

        ans = []
        while heap or idx < len(tasks):
            if not heap and t < tasks[idx][0]:
                t = tasks[idx][0]
            while idx < len(tasks) and tasks[idx][0] <= t:
                heappush(heap, [tasks[idx][1], tasks[idx][-1]])
                idx += 1
            if heap:
                p, i = heappop(heap)
                ans.append(i)
                t += p

        return ans






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna