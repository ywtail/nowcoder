# coding:utf-8
# 网格走法数目

def func(x, y):
    n = x + y
    fenzi = 1
    fenmu = 1
    for i in range(x):
        fenzi *= (n - i)
        fenmu *= (i + 1)
    return fenzi / fenmu


x, y = map(int, raw_input().split())
if x > y: #将x设定为更小的数，能够减少循环次数。
    x, y = y, x

print func(x, y)

# 运行时间：24ms
# 占用内存：2948k

'''
题目地址
https://www.nowcoder.com/practice/e27b9fc9c0ec4a17a5064fb6f5ab13e4?tpId=85&&tqId=29883&rp=2&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走。请设计一个算法，计算小团有多少种走法。给定两个正整数int x,int y，请返回小团的走法数目。
输入描述:
输入包括一行，逗号隔开的两个正整数x和y，取值范围[1,10]。
输出描述:
输出包括一行，为走法的数目。
示例1
输入
3 2
输出
10

走法数目是C(x,x+y)或者C(y,x+y)。
看到很多实用动态规划或者递归做，f[m][n]=f[m-1][n]+f[m][n-1]
'''