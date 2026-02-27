n, k = map(int, input().split())

nums = list(map(int, input().split()))

def get_segments_with_small_set(nums, k):
    track = {}
    count = 0

    l = 0
    for r in range(len(nums)):
        if nums[r] not in track:
            track[nums[r]] = 0

        track[nums[r]] += 1

        while len(track.keys()) > k:
            track[nums[l]] -= 1
            if track[nums[l]] == 0:
                del track[nums[l]]
            l += 1

        count += (r - l + 1)

    return count

print(get_segments_with_small_set(nums, k))
