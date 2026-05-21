# week13-5.py 學習計畫 Heap / Priority Queue 第3題, 超難懂的
# LeetCode 2542. Maximum Subsequence Score
# 挑 k 個 index, 讓 nums1 對應的 k 個數相加, 再乘 min(nums2對應k個數) 希望最大
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 先把 nums1 跟 nums2 合併起來
        # ex. [1,3,3,2]
        #     []
        a = [(n2, n1) for n1, n2 in zip(nums1, nums2)]
        a.sort(reverse=True)  # 先湊 k 組數，把前 k 大的 nums2 取出
        heap = [a[i][1] for i in range(k)]
        heapify(heap)  # 之後將小到大依序吐掉 nums1 的這 k 個數，換加入新的 n1,n2組
        total = sum(heap)
        ans = total * a[k-1][0]  # 前 k 項的 nums1 及對應最小的 nums2 相乘

        for i in range(k, len(nums2)):  # 後面將加入的數
            n2, n1 = a[i]  # 將加入的對應的數
            heappush(heap, n1)  # 加1
            total += n1 - heappop(heap)  # 加1、吐1
            ans = max(ans, total * n2)  # 更新答案
        return ans
