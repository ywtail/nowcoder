# -*- coding:utf-8 -*-

class Printer:
    def arrayPrint1(self, arr, n):
        row = 0
        col = n - 1
        ans = []
        while row < n:
            i = row
            j = col
            while i < n and j < n:
                ans.append(arr[i][j])
                i += 1
                j += 1
            if j == n and col > 0:
                col -= 1
            if i == n:
                row += 1
        return ans
        # 运行时间：10690ms
        # 占用内存：13336k

    def arrayPrint2(self, arr, n):
        index = 0
        ans = [0] * (n * n)
        for col in range(n)[::-1]:
            for row in range(n - col):
                ans[index] = arr[row][col + row]
                ans[n * n - 1 - index] = arr[n - 1 - row][n - 1 - row - col]
                index += 1
        return ans
        # 运行时间：10620ms
        # 占用内存：13176k


p = Printer()
print p.arrayPrint1([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4)
# [4, 3, 8, 2, 7, 12, 1, 6, 11, 16, 5, 10, 15, 9, 14, 13]
print p.arrayPrint2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4)
# [4, 3, 8, 2, 7, 12, 1, 6, 11, 16, 5, 10, 15, 9, 14, 13]

'''
## 二维数组打印
[题目链接](https://www.nowcoder.com/practice/6fadc1dac83a443c9434f350a5803b51?tpId=49&tqId=29316&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

有一个二维数组(n*n),写程序实现从右上角到左下角沿主对角线方向打印。
给定一个二位数组arr及题目中的参数n，请返回结果数组。
测试样例：
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],4
'''