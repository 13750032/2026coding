#week01-2.py 學習計畫Array/String 第一題
#LeetCode 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""##答案塞在ans裡
        N1, N2 = len(word1), len(word2)
        i,j=0,0 # word1[i]vs.word2[j]
        while i<N1 or j<N2:#只要任一個還有剩
            if i<N1: ans += word1[i]#没用完
            if j<N2: ans += word2[j]#没用完
            i,j=i+1,j+1#都换下一位

        return ans # 答案在這裡
