class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        f1 = [-1, 0]
        f2 = [-1, 0]
        _max = -float("inf")
        idx = 0

        for i in range(len(fruits)):
            if f1[0] != -1 and f2[0] != -1 and fruits[i] != f1[0] and fruits[i] != f2[0]:
                while idx < i and f1[-1] != 0 and f2[-1] != 0:
                    if fruits[idx] == f1[0]:
                        f1[-1] -= 1
                    else:
                        f2[-1] -= 1
                    idx += 1

            if f1[-1] == 0 or fruits[i] == f1[0]:
                f1[0] = fruits[i]
                f1[-1] += 1
            elif f2[-1] == 0 or fruits[i] == f2[0]:
                f2[0] = fruits[i]
                f2[-1] += 1
            
            _max = max(_max, f1[-1] + f2[-1])
        
        return _max
            
            

            
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna