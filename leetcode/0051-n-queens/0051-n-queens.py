class Solution:
    def solveNQueens(self, n):
        ans = []
        trial = []
        template = ['.'] * n

        def backtrack(r, cols, m_diag, o_diag):
            if r >= n:
                ans.append(trial[:])
                return

            for c in range(n):
                if c not in cols and (r + c) not in m_diag and (r - c) not in o_diag:
                    # DO
                    temp = template[:]
                    temp[c] = "Q"
                    trial.append("".join(temp))

                    cols.add(c)
                    m_diag.add(r + c)
                    o_diag.add(r - c)

                    # RECURSE
                    backtrack(r + 1, cols, m_diag, o_diag)

                    # UNDO (this was missing in your code)
                    trial.pop()
                    cols.remove(c)
                    m_diag.remove(r + c)
                    o_diag.remove(r - c)

        backtrack(0, set(), set(), set())
        return ans