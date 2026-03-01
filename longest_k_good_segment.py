from collections import defaultdict
n, k = map(int, input().split())

nums = list(map(int, input().split()))

longest = 0
ans = [-1, -1]
track = defaultdict(int)

l = 0
for r in range(len(nums)):
    track[nums[r]] += 1

    while len(track) > k:
        track[nums[l]] -= 1
        if track[nums[l]] == 0:
            del track[nums[l]]
        l += 1

    if max(longest, r - l + 1) != longest:
        longest = r - l + 1
        ans[0] = l + 1
        ans[-1] = r + 1

print(*ans)
