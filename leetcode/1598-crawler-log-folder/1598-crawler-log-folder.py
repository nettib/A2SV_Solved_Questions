class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if (log == "./" or (log == "../" and not stack)):
                continue
            elif log == "../":
                stack.pop()
            else:
                stack.append(log)
        
        return len(stack)