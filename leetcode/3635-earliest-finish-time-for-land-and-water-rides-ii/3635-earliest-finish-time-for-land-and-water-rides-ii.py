from bisect import bisect_right
from math import inf

class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):

        def build(starts, durations):
            rides = sorted(zip(starts, durations))

            s = [x for x, _ in rides]
            d = [x for _, x in rides]

            n = len(rides)

            pref = [0] * n
            pref[0] = d[0]

            for i in range(1, n):
                pref[i] = min(pref[i - 1], d[i])

            suff = [0] * n
            suff[-1] = s[-1] + d[-1]

            for i in range(n - 2, -1, -1):
                suff[i] = min(
                    suff[i + 1],
                    s[i] + d[i]
                )

            return s, pref, suff

        waterS, waterPref, waterSuff = build(
            waterStartTime,
            waterDuration
        )

        landS, landPref, landSuff = build(
            landStartTime,
            landDuration
        )

        ans = inf

        # Land -> Water
        for s, d in zip(landStartTime, landDuration):
            t = s + d

            idx = bisect_right(waterS, t) - 1

            best = inf

            if idx >= 0:
                best = min(best, t + waterPref[idx])

            if idx + 1 < len(waterS):
                best = min(best, waterSuff[idx + 1])

            ans = min(ans, best)

        # Water -> Land
        for s, d in zip(waterStartTime, waterDuration):
            t = s + d

            idx = bisect_right(landS, t) - 1

            best = inf

            if idx >= 0:
                best = min(best, t + landPref[idx])

            if idx + 1 < len(landS):
                best = min(best, landSuff[idx + 1])

            ans = min(ans, best)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna