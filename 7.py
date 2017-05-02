# -*- coding:utf-8 -*-
# 顺时针旋转矩阵

class Rotate:
    def rotateMatrix(self, mat, n):
        rotate_mat = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                rotate_mat[i][j] = mat[n - j - 1][i]
        return rotate_mat

        # 运行时间：400ms
        # 占用内存：3148k

    def rotateMatrix1(self, mat, n):
        return [x[::-1] for x in zip(*mat)]

        # 运行时间：380ms
        # 占用内存：3148k


rotate = Rotate()
print rotate.rotateMatrix([[1,2,3],[4,5,6],[7,8,9]],3)
print rotate.rotateMatrix([[1,2,3],[4,5,6],[7,8,9]],3)

'''
## 顺时针旋转矩阵
[题目链接](https://www.nowcoder.com/practice/2e95333fbdd4451395066957e24909cc?tpId=49&tqId=29373&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

有一个NxN整数矩阵，请编写一个算法，将矩阵顺时针旋转90度。
给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵,保证N小于等于300。

**测试样例**

>[[1,2,3],[4,5,6],[7,8,9]],3
>返回：[[7,4,1],[8,5,2],[9,6,3]]

- rotateMatrix(self, mat, n):
常规思路

- rotateMatrix1(self, mat, n):
使用zip，具体用法参见： http://ywtail.github.io/2017/04/11/nowcoder-3-%E9%A1%BA%E6%97%B6%E9%92%88%E6%97%8B%E8%BD%AC%E7%9F%A9%E9%98%B5-%E6%8A%9B%E5%B0%8F%E7%90%83-%E6%95%B0%E7%BB%84%E5%8D%95%E8%B0%83%E5%92%8C-%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%80%9A%E9%85%8D/
'''