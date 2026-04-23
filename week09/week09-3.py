# week09-3.py 學習計畫 Linked List 第3題 Easy 題 (使用「函式呼叫函式」Recursion)
# week09-2.py 學習計畫 Linked List 第3題 Easy 題
# LeetCode 206. Reverse Linked List
# 把它反過來

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # week09-3.py
        if head == None or head.next == None: return head  # 終止條件(最簡單的狀況)
        head2 = head.next
        ans = self.reverseList(head.next)  # 函數呼叫函數
        head2.next, head.next = head, None
        return ans
        # week09-2.py
        a = []  # 容易理解的方法，把 linked list 變成陣列
        while head:  # 只要還有資料
            a.append( head.val )  # 就塞到陣列 a 的後面
            head = head.next  # 換下一筆

        # print(a) 印出來，成功變成我們習慣的陣列 a[i]

        ans = ListNode()  # 答案將串到裡面
        now = ans

        # 既然要反過來，我們就從陣列的最後一項開始往前走
        for i in range(len(a) - 1, -1, -1):
            now.next = ListNode(a[i]) # 建立新節點
            now = now.next # 移動到下一個位置

        return ans.next # 因為 ans 是 ListNode() 預設為 0，所以要從 next 開始回傳
