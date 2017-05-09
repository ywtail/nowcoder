# -*- coding:utf-8 -*-
# 之字形打印矩阵

class Printer:
    def printMatrix(self, mat, n, m):
        ans = []
        for i in range(n):
            if i % 2 == 0:
                ans += mat[i]
            else:
                ans += mat[i][::-1]
        return ans

        # 运行时间：350ms
        # 占用内存：3148k

printer = Printer()
print printer.printMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 4, 3)

'''
之字形打印矩阵
[题目链接](https://www.nowcoder.com/practice/7df39c7556424eada267d8f793961a1e?tpId=49&tqId=29374&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对于一个矩阵，请设计一个算法，将元素按“之”字形打印。具体见样例。
给定一个整数矩阵mat，以及他的维数nxm，请返回一个数组，其中元素依次为打印的数字。

**测试样例**

>[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],4,3
返回：[1,2,3,6,5,4,7,8,9,12,11,10]

- printMatrix(self, mat, n, m):
行是奇数时从左到右，行是偶数时从右到左。
'''