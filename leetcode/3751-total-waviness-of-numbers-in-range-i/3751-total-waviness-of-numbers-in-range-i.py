class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_waviness(num):
            _num = str(num)
            w = 0

            if len(_num) < 3:
                return w
            
            for i in range(1, len(_num) - 1):
                if ((int(_num[i - 1]) < int(_num[i]) > int(_num[i + 1])) or 
                    (int(_num[i - 1]) > int(_num[i]) < int(_num[i + 1]))):
                    w += 1
            
            return w
        
        waviness = 0
        for num in range(num1, num2 + 1):
            waviness += get_waviness(num)
        
        return waviness


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna