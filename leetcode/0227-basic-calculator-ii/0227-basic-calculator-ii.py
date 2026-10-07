class Solution:
    def calculate(self, s: str) -> int:
        _exp = s.replace(" ", "")
        exp = []
        operations = ["+", "-", "*", "/"]
        # [3, '+', 5, '/', 2]

        i = 0
        while i < len(_exp):
            if _exp[i] in operations:
                exp.append(_exp[i])
                i += 1
                continue
            temp = ""
            while i < len(_exp) and _exp[i] not in operations:
                temp += _exp[i]
                i += 1
            exp.append(int(temp))

        stack = []

        for i in range(len(exp)):
            if i == 0 or exp[i] in operations[:2]:
                stack.append(exp[i])
            elif exp[i - 1] == "*":
                stack.append(stack.pop() * exp[i])
            elif exp[i - 1] == "/":
                stack.append(stack.pop() // exp[i])
            elif str(exp[i]) not in "*/":
                stack.append(exp[i])

        stack = stack[::-1]
        val = stack.pop()

        while stack:
            operation = stack.pop()
            _val = stack.pop()

            if operation == "+":
                val = val + _val
            else:
                val = val - _val

        return val

                



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna