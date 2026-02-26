# week01-4.py 學習計畫 Array/Sring 第3題
# LeetCode 1431. Kids With the Greatest Number of Candies
#
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #(請庫存、救命用)只要 Test Result 有線色 Accept 就好了
        ans=[]#答案的True 和False 將塞在裡面
        best=max(candies) #目前小朋友「最多最多有幾個糖」?
        for candie in candies: #逐一檢查、如果把 extracandies 給小朋友
            if candie + extraCandies >= best: ans.append(True)
            else: ans.append(False) # 它會不會>= 最多的,依序塞人ans
        return ans
