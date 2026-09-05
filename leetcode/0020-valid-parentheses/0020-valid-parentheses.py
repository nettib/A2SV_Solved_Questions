class Solution:
    def isValid(self, s: str) -> bool:
        char_match = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char not in char_match:
                stack.append(char)
            else:
                if not stack or stack[-1] != char_match[char]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna