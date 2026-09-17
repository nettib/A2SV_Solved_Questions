class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        cols = set()
        diag = set()
        anti = set()

        def dfs(row):
            nonlocal ans
            if row == n:
                ans += 1
                return

            for col in range(n):

                if col not in cols and row + col not in diag and row - col not in anti:
                    cols.add(col)
                    diag.add(row + col)
                    anti.add(row - col)

                    dfs(row + 1)

                    cols.remove(col)
                    diag.remove(row + col)
                    anti.remove(row - col)
        
        dfs(0)

        return ans
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna