# week04-2.py 學習計畫 prefix sum 第1題
# LeetCode 1732. Find the Highest Altitude
#找到最高的海拔高度(一直加,就好了!!!)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N=len(gain)#陣列的長度 N
        ans=H=0#一開始的高度是
        #答案一開始是0,因為一開始的高度是0
        for i in range(N): #個加起來
            H+= gain[i]#現在增滅的量 gain[1]加進 H
            ans =max(ans,H)#更新最高的答案
        return ans
