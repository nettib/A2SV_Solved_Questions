from collections import Counter
T = int(input().strip())

for _ in range(T):
    s = input().strip()
    t = input().strip()

    def get_lexicographically_smaller_t_s_merge(s, t):
        s_count = Counter(s)
        t_count = Counter(t)

        possible = True
        for char in s:
            if s_count[char] > t_count[char]:
                possible = False
                return possible

        rem = []

        for char in t_count.keys():
            for _ in range(t_count[char] - s_count[char]):
                rem.append(char)

        rem = "".join(sorted(rem))


        ans = []

        sp = 0
        tp = 0

        while sp < len(s) and tp < len(rem):
            if s[sp] <= rem[tp]:
                ans.append(s[sp])
                sp += 1
            else:
                ans.append(rem[tp])
                tp += 1

        if sp < len(s):
            ans.extend(s[sp:])
        if tp < len(rem):
            ans.extend(rem[tp:])

        return "".join(ans)

    if get_lexicographically_smaller_t_s_merge(s, t):
        print(get_lexicographically_smaller_t_s_merge(s, t))
    else:
        print("Impossible")
