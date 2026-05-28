# week14-2a.py 學習計畫 1D DP 第1題 Easy
# LeetCode 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1] + [0] * n
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2] + a[i-3]
        return a[n]

        if n==0: return 0
        if n==1: return 1
        if n==2: return 1
        if n==3: return 4
        if n==4: return 7
        if n==5: return 11
        if n==6: return 18
        if n==7: return 29
        if n==8: return 47
        if n==9: return 76
        if n==10: return 123
        if n==11: return 199

