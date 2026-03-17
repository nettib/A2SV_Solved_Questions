class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        l, r = 0, len(nums) - 1

        def get_winner(p1, p2, tera, nums):
            if len(nums) == 0:
                return p1 >= p2

            if tera == 1:
                return (get_winner(p1 + nums[0], p2, 0, nums[1:]) or get_winner(p1 + nums[-1], p2, 0, nums[:-1]))
            elif tera == 0:
                return (get_winner(p1, p2 + nums[0], 1, nums[1:]) and get_winner(p1, p2 + nums[-1], 1, nums[:-1]))

        return get_winner(0, 0, 1, nums)




            
