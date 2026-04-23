class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                heights[r][c] = [heights[r][c], -1]

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def inbound(r, c):
            return 0 <= r < len(heights) and 0 <= c < len(heights[0])
        

        # Pacific Ocean
        visited = set()
        def dfs_p(r, c):
            visited.add((r, c))
            heights[r][c][-1] = "P"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and (nr, nc) not in visited:
                    curr = heights[nr][nc][0]
                    prev = heights[r][c][0]
                    if curr >= prev:
                        dfs_p(nr, nc)
                    
        for c in range(len(heights[0])):
            # heights[0][c][-1] = "P"
            if (0, c) not in visited:
                dfs_p(0, c)

        for r in range(len(heights)):
            # heights[r][0][-1] = "P"
            if (r, 0) not in visited:
                dfs_p(r, 0)


        # Atlantic Ocean
        visited = set()
        def dfs_a(r, c):
            visited.add((r, c))
            if heights[r][c][-1] == "P":
                ans.append([r, c])

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and (nr, nc) not in visited:
                    curr = heights[nr][nc][0]
                    prev = heights[r][c][0]
                    if curr >= prev:
                        dfs_a(nr, nc)

        for c in range(len(heights[0])):
            r = len(heights) - 1
            # if heights[r][c][-1] == "P":
            #     ans.append([r, c])
            if (r, c) not in visited:
                dfs_a(r, c)
            
        for r in range(len(heights)):
            c = len(heights[0]) - 1
            # if heights[r][c][-1] == "P":
            #     ans.append([r, c])
            if (r, c) not in visited:
                dfs_a(r, c)
        
        return ans 
        
        

