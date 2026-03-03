class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(n1, n2):
            if str(n1) + str(n2) > str(n2) + str(n1):
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(compare))

        return str(int("".join(map(str, nums))))
   

