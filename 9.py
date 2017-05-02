# -*- coding:utf-8 -*-
# 数组单调和

class MonoSum:
    def calcMonoSum(self, A, n):
        ans = 0
        for i in range(1, n):
            for j in range(i):
                if A[j] <= A[i]:
                    ans += A[j]
        return ans

        # 运行时间：100ms
        # 占用内存：3156k

monosum = MonoSum()
print monosum.calcMonoSum([1,3,5,2,4,6],6)

'''
## 数组单调和
[题目链接](https://www.nowcoder.com/practice/8397609ba7054da382c4599d42e494f3?tpId=49&tqId=29364&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

现定义数组单调和为所有元素i的f(i)值之和。这里的f(i)函数定义为元素i左边(不包括其自身)小于等于它的数字之和。请设计一个高效算法，计算数组的单调和。
给定一个数组A同时给定数组的大小n，请返回数组的单调和。保证数组大小小于等于500，同时保证单调和不会超过int范围。

**测试样例**

>[1,3,5,2,4,6],6
>返回：27

- calcMonoSum(self, A, n):
题目提示动态规划，暂时没有想到动态规划的解法，所以用常规求解
'''