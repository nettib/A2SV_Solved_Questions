def solve(s1, s2):
    destination = 0

    for cmd in s1:
        if cmd == '+':
            destination += 1
        elif cmd == '-':
            destination -= 1

    possibilities = []

    def backtrack(i, curr):
        if i == len(s2):
            possibilities.append(curr)
            return

        if s2[i] == "+":
            backtrack(i + 1, curr + 1)
        elif s2[i] == "-":
            backtrack(i + 1, curr - 1)
        else:
            backtrack(i + 1, curr + 1)
            backtrack(i + 1, curr - 1)

    backtrack(0, 0)

    correct = 0

    for possibility in possibilities:
        if possibility == destination:
            correct += 1

    print(correct / len(possibilities))

solve(s1, s2)