n, s = map(int, input().split())
nums = list(map(int, input().split()))

def get_no_of_segments_with_small_sum(nums):
    count = 0
    curr = 0

    l = 0
    for r in range(len(nums)):
        curr += nums[r]

        while curr > s:
            curr -= nums[l]
            l += 1

        count += (r - l + 1)

    return count

print(get_no_of_segments_with_small_sum(nums))
