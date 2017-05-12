# -*- coding:utf-8 -*-
# 相邻最大差值

class MaxDivision:
    def findMaxDivision(self, A, n):
        bucket = [0 for i in range(max(A) - min(A) + 1)]
        for i in range(n):
            bucket[A[i] - min(A)] = 1
        count = 1
        ans = 0
        for i in range(len(bucket)):
            if bucket[i] == 0:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        return ans

        # 运行时间：100ms
        # 占用内存：3156k

maxdivision = MaxDivision()
print maxdivision.findMaxDivision([208, 254, 473, 153, 389, 579, 398], 7) # 返回135

'''
## 相邻最大差值
[题目链接](https://www.nowcoder.com/practice/376ede61d9654bc09dd7d9fa9a4b0bcd?tpId=49&tqId=29366&tPage=2&rp=2&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

请设计一个复杂度为O(n)的算法，计算一个未排序数组中排序后相邻元素的最大差值。
给定一个整数数组A和数组的大小n，请返回最大差值。保证数组元素个数大于等于2小于等于500。

**测试样例**
>[9,3,1,10],4
返回：6

- findMaxDivision(self, A, n):
由于题中数组元素>=2且<=500（数组长度并不大），并且要求复杂度为O(n)，可以考虑桶排序。
申请长度为`max(A) - min(A) + 1`的bucket数组作为桶，遍历A，令`bucket[A[i] - min(A)] = 1`。
最后遍历bucket，连续0的长度的最大值+1即为最大差值。
'''