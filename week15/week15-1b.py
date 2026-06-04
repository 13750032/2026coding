# week15-1b.py 學習計畫 DP - Multidimention 第1題
# LeetCode 62. Unique Paths 第2種寫法, 使用 Buttom-Up DP 建表格
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [ [0] * n for i in range(m)] # 建2D 陣列
        table[0][0] = 1 # 終點1種走法 (註：此處指起點)

        for i in range(m):
            for j in range(n):
                if i==0: table[i][j] = 1   # 最上面那一列，只有1種走法（一路向右）
                elif j==0: table[i][j] = 1 # 最左邊那一欄，只有1種走法（一路向下）
                else: table[i][j] = table[i-1][j] + table[i][j-1] # 內網格：上方 + 左方
        return table[m-1][n-1]
