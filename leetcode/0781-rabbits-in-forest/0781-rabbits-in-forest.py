class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = {}
        up_to_now = {}

        rabbits = 0

        for answer in answers:
            if answer not in total:
                total[answer] = answer + 1
                up_to_now[answer] = 1
            elif up_to_now[answer] == total[answer]:
                total[answer] += (answer + 1)
                up_to_now[answer] += 1
            else:
                up_to_now[answer] += 1
        
        return sum(total.values())