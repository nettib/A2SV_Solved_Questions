class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        def check_row(row):
            if row >= 0 and row < len(img):
                return True
            return False

        def check_col(col):
            if col >= 0 and col < len(img[0]):
                return True
            return False
        
        ans = [[0] * len(img[0]) for _ in range(len(img))]

        for r in range(len(img)):
            for c in range(len(img[0])):
                total = 0
                count = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if check_row(i) and check_col(j):
                            total += img[i][j]
                            count += 1
                ans[r][c] = total // count
        
        return ans
                
