# -*- coding:utf-8 -*-
# 最大差值

class LongestDistance:
    def getDis(self, A, n):
        ma = 0
        for i in range(n):
            for j in range(i + 1, n):
                ma = max(A[j] - A[i], ma)
        return ma

    def getDis1(self, A, n):
        start = A[0]
        ma = 0
        for i in range(n):
            start = min(start, A[i])
            ma = max(ma, A[i] - start)
        return ma


longestdistance = LongestDistance()
print longestdistance.getDis([10, 5], 2)
print longestdistance.getDis1([10, 5], 2)
'''
## 最大差值
[题目链接](https://www.nowcoder.com/practice/1f7675ae7a9e40e4bd04eb754b62fd00?tpId=49&tqId=29281&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

**题目描述**
有一个长为n的数组A，求满足0≤a≤b<n的A[b]-A[a]的最大值。
给定数组A及它的大小n，请返回最大差值。

**测试样例：**

> [10,5],2
> 返回：0

- getDis(self, A, n):
最简单的思路是遍历两遍，求最大差值。时间复杂度O(n^2)。
运行时间：150ms
占用内存：3156k

- getDis1(self, A, n):
另一种只遍历一遍，使用start来记录起始位置，star始终是遍历过的最小值。时间复杂度O(n)。
运行时间：40ms
占用内存：3156k
'''
