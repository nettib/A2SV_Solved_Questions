matrix = []
for _ in range(5):
    nums = list(map(int, input().split()))
    matrix.append(nums)

def min_moves(matrix):

    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if matrix[m][n] == 1:
                return abs((m + 1) - 3) + abs((n + 1) - 3)

print(min_moves(matrix))
