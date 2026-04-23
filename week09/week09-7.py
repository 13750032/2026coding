# week09-7 學習計畫 Linked List 第4題
# LeetCode 2130. Maximum Twin Sum of a Linked List
# 頭尾「兩兩配在一起」希望加起來最大
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        while head:
            a.append( head.val )
            head = head.next

        N = len(a)
        ans = 0
        # 遍歷陣列，計算頭尾對稱位置的和，並找出最大值
        for i in range(N):
            ans = max(ans, a[i] + a[N-1-i])

        return ans
