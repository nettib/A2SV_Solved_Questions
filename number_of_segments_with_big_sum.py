n, s = map(int, input().split())
nums = list(map(int, input().split()))


def get_no_of_good_segments(nums):
    count = 0
    curr = 0

    l = 0
    for r in range(len(nums)):
        curr += nums[r]

        while curr >= s:
            curr -= nums[l]
            l += 1

        count += l

    return count

print(get_no_of_good_segments(nums))
