class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        graph = defaultdict(list)
        track = set()

        root = None

        for node in range(n):
            if leftChild[node] != -1:
                graph[node].append(leftChild[node])
                track.add(leftChild[node])
            if rightChild[node] != -1:
                graph[node].append(rightChild[node])
                track.add(rightChild[node])
        
        for node in range(n):
            if not root and node not in track:
                root = node
            elif root and node not in track:
                return False
        
        if root == None:
            return False
            
        visited = set([root])

        def dfs(node):


            for nei in graph[node]:
                if nei in visited:
                    return False
                visited.add(nei)
                
                if not dfs(nei):
                    return False
                
            return True
        
        if not dfs(root):
            return False
        
        return len(visited) == n
        



        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna