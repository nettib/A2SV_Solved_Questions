# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = defaultdict(list)
        degree = defaultdict(int)

        for parent, child, isLeft in descriptions:
            if isLeft:
                graph[parent].append(-child)
            else:
                graph[parent].append(child)
            degree[child] += 1

        q = deque()

        for parent, child, isLeft in descriptions:
            if degree[parent] == 0:
                root = TreeNode(parent)
                q.append(root)
                break
        
        while q:
            parent = q.popleft()

            for child in graph[parent.val]:
                node = TreeNode(abs(child))

                degree[abs(child)] -= 1

                if degree[abs(child)] == 0:
                    q.append(node)

                if child < 0:
                    parent.left = node
                else:
                    parent.right = node
        
        return root

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna