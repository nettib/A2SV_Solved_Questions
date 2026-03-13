class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = {5: 0, 10: 0}
        
        for bill in bills:
            if bill == 5:
                fives[bill] += 1
            elif bill == 10:
                if fives[5] <= 0:
                    return False
                fives[5] -= 1
                fives[bill] += 1
            else:
                if fives[10] > 0:
                    fives[10] -= 1
                    fives[5] -= 1
                    if fives[5] < 0:
                        return False
                else:
                    fives[5] -= 3
                    if fives[5] < 0:
                        return False
        
        return True

