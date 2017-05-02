# -*- coding:utf-8 -*-
# 左右最值最大差

class MaxGap:
    def findMaxGap(self, A, n):
        maxnum = max(A)
        minnum = min(A[0], A[n - 1])
        return maxnum - minnum

    # 运行时间：40ms
    # 占用内存：3156k

maxgap = MaxGap()
print maxgap.findMaxGap([2, 7, 3, 1, 1], 5)

'''
## 左右最值最大差
[题目链接](https://www.nowcoder.com/practice/f5805cc389394cf69d89b29c0430ff27?tpId=49&tqId=29359&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

给定一个长度为N(N>1)的整型数组A，可以将A划分成左右两个部分，左部分A[0..K]，右部分A[K+1..N-1]，K可以取值的范围是[0,N-2]。求这么多划分方案中，左部分中的最大值减去右部分最大值的绝对值，最大是多少？
给定整数数组A和数组的大小n，请返回题目所求的答案。

**测试样例**

>[2,7,3,1,1],5
返回：6

- findMaxGap(self, A, n):
这一题思路很巧妙：先找最大值maxnum（这个最大值肯定是某一边的最值），再对比两个端点处(A[0]与A[n-1])的数值，数值大的与maxnum在一边，数值小的就是另一边的最值（假设A[n-1]<A[0]，那么A[n-1]就是右边的最值。因为继续往左扩充，如果A[n-2]<A[n-1]，那么右边的最大值依然是A[n-1]，如果A[n-2]>A[n-1]，那么显然右侧只包含A[n-1]一个元素时，左部分中的最大值减去右部分最大值的绝对值最大，最值依然是A[n-1]），求得的这两个值的差值就是答案。
'''