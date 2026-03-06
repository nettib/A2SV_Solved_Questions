class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        L, R = 0, len(matrix[0])
        T, B = 0, len(matrix)

        while L < R and T < B:

            # Going from left to right
            for c in range(L, R):
                res.append(matrix[T][c])
            T += 1
            
            # Going from top to bottom 
            for r in range(T, B):
                res.append(matrix[r][R - 1])
            R -= 1

            if T == B or L == R:
                break

            # Going from right to left
            for c in range(R - 1, L - 1, -1):
                res.append(matrix[B - 1][c])
            B -= 1

            # Going from bottom to top
            for r in range(B - 1, T - 1, -1):
                res.append(matrix[r][L])
            L += 1

        return res
            
