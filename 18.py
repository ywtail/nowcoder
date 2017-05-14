# -*- coding:utf-8 -*-
# 最长递增子序列

class AscentSequence:
    def findLongest(self, A, n):
        length = [1 for i in range(n)]
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if A[j] < A[i] and length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
            ans = max(ans, length[i])
        return ans
        # 复杂度为O(n^2)
        # 运行时间：350ms
        # 占用内存：3156k

    def findLongest1(self, A, n):
        B = [0 for i in range(n)]
        b_endindex = 0  # 记录B最后一个元素的下标
        B[0] = A[0]
        for i in range(1, n):
            if A[i] > B[b_endindex]:
                b_endindex += 1
                B[b_endindex] = A[i]
            else:
                temp_index = self.findIndex1(B, A[i], b_endindex)
                B[temp_index] = A[i]
        return b_endindex + 1
        # 复杂度为O(nlogn)
        # 运行时间：130ms
        # 占用内存：3156k

    # 二分法查找B中第一个大于b的元素的坐标
    def findIndex1(self, B, b, b_endindex):
        left = 0
        right = b_endindex
        while (left < right):
            mid = (left + right) / 2
            if b == B[mid]:
                return mid
            elif b < B[mid]:
                right = mid #注意这里不是right=mid-1，因为要寻找的是第一个比b大的元素的下标，可能就是B[mid]，而B[mid-1]可能就小于b了。
            else:
                left = mid + 1
        return left


ascentsequence = AscentSequence()
print ascentsequence.findLongest([2, 1, 4, 3, 1, 5, 6], 7)
print ascentsequence.findLongest1([2, 1, 4, 3, 1, 5, 6], 7)

'''
## 最长递增子序列
[题目链接](https://www.nowcoder.com/practice/585d46a1447b4064b749f08c2ab9ce66?tpId=49&tqId=29347&tPage=2&rp=2&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对于一个数字序列，请设计一个复杂度为O(nlogn)的算法，返回该序列的最长上升子序列的长度，
这里的子序列定义为这样一个序列U1，U2...，其中Ui < Ui+1，且A[Ui] < A[Ui+1]。
给定一个数字序列A及序列的长度n，请返回最长上升子序列的长度。

**测试样例**
>[2,1,4,3,1,5,6],7
返回：4

- findLongest(self, A, n):
复杂度为O(n^2)
使用length[]数组维护以当前元素结尾的递增子序列的长度。
如果`A[j] < A[i]`，则`length[i]=max(length[i],length[j]+1)`，
最后返回`max(length)`就是最长递增子序列长度。

- findLongest1(self, A, n):
复杂度为O(nlogn)
使用数组B[i]来维护长度为i+1的递增子序列的最小末尾：
从左向右遍历数组A，如果A[i]大于B中最后一个元素，则将A[i]加入B中。
如果A[i]小于B中最后一个元素，则在B中找合适的位置j，用A[i]替换B[j]。
这里注意在B中找合适位置使用二分法，以减少复杂度。
'''