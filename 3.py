# -*- coding:utf-8 -*-
# 二分查找

class BinarySearch:
    def getPos(self, A, n, val):
        if n == 0:
            return -1
        start = 0
        end = n - 1
        while (start <= end):
            mid = (start + end) / 2
            if val == A[mid]:
                for i in range(1, mid + 1):
                    if A[mid - i] < A[mid]:
                        return mid - i + 1
                return 0
            elif val < A[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def getPos1(self, A, n, val):
        if n == 0:
            return -1
        start = 0
        end = n - 1
        while (start < end):
            mid = (start + end) / 2
            if val == A[mid]:
                end = mid
            elif val < A[mid]:
                end = mid - 1
            else:
                start = mid + 1
        if A[start] == val:
            return start
        return -1


binarysearch = BinarySearch()
print binarysearch.getPos([1,3,5,7,9],5,3)
print binarysearch.getPos1([1,3,5,7,9],5,3)

'''
## 二分查找
[题目链接](https://www.nowcoder.com/practice/28d5a9b7fc0b4a078c9a6d59830fb9b9?tpId=49&tqId=29278&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对于一个有序数组，我们通常采用二分查找的方式来定位某一元素，请编写二分查找的算法，在数组中查找指定元素。
给定一个整数数组A及它的大小n，同时给定要查找的元素val，请返回它在数组中的位置(从0开始)，若不存在该元素，返回-1。若该元素出现多次，请返回第一次出现的位置。

**测试样例**

>[1,3,5,7,9],5,3
>返回：1

- getPos(self, A, n, val):
普通的二分，需要注意的是元素出现多次时返回第一次出现的位置。所以在找到元素后，继续向左查找第一次出现的位置。
运行时间：50ms
占用内存：3148k

- getPos1(self, A, n, val):
在评论中看到另一种：在元素出现多次时，不是继续向左查找，而是end=mid，最后返回start指向的元素。
运行时间：50ms
占用内存：3148k
'''