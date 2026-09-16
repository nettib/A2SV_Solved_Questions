class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        path = [["." for _ in range(n)] for _ in range(n)]
        cols = set()
        diag = set()
        anti = set()

        def backtrack(r):
            if r == n:
                ans.append(["".join(path[r]) for r in range(n)])
                return
            
            for c in range(n):
                if c not in cols and r + c not in diag and r - c not in anti:
                    path[r][c] = "Q"
                    cols.add(c)
                    diag.add(r + c)
                    anti.add(r - c)

                    backtrack(r + 1)

                    path[r][c] = "."
                    cols.remove(c)
                    diag.remove(r + c)
                    anti.remove(r - c)
            
        backtrack(0)

        return ans
            




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna