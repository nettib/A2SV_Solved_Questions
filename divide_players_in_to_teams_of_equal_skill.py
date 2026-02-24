class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chem = 0
        curr = 0

        skill.sort()
        l, r = 0, len(skill) - 1

        while l < r:
            total_skill = skill[l] + skill[r]

            if not curr:
                curr = total_skill
            elif total_skill != curr:
                return -1
            chem += (skill[l] * skill[r])
            l += 1
            r -= 1
    
        return chem
            
