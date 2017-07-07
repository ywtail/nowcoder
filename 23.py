# -*- coding:utf-8 -*-
# 阶乘尾零

class Factor:
    def getFactorSuffixZero(self, n):
        if n < 2:
            return 0
        ans = 0
        while n:
            n /= 5
            ans += n
        return ans

    #运行时间：35ms
    #占用内存：5764k


f = Factor()
print f.getFactorSuffixZero(5)
# 1
print f.getFactorSuffixZero(25)
# 6

'''
题目地址
https://www.nowcoder.com/practice/434922f9f4724b97b83c417e884008f1?tpId=8&&tqId=11058&rp=1&ru=/activity/oj&qru=/ta/cracking-the-coding-interview/question-ranking
题目描述
请设计一个算法，计算n的阶乘有多少个尾随零。
给定一个int n，请返回n的阶乘的尾零个数。保证n为正整数。
测试样例：
5
返回：1

每个 0 都由 2*5 获得，所以原题变为求这些数中包含的因子 2 和因子 5 的个数。
显然，2 的个数比 5 大，所以只需要求因子 5 的个数，就能够得到尾 0 的个数。
上述算法时间复杂度 O(logn)，以 5 为底。
'''