n, k = map(int, input().split())

nums = list(map(int, input().split()))

total = nums[-1] - nums[0]

diff = []

for i in range(1, len(nums)):
    diff.append(nums[i] - nums[i - 1])

diff.sort()
diff = diff[::-1]

k = k - 1
max_diff = sum(diff[: k])

print(total - max_diff)
