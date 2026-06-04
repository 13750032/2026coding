# week15-2a.py 學習計畫 DP - Multidimention 第2題
# LeetCode 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        @cache
        def helper(i, j):
            if i==M or j==N: return 0
            if text1[i]==text2[j]: return 1 + helper(i+1, j+1)
            else: return max( helper(i, j+1), helper(i+1, j) )
        return helper(0, 0)
