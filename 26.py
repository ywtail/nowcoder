# coding:utf-8
# 阶乘

while 1:
    try:
        n = int(raw_input())
    except:
        break
    odd = 0
    even = 0
    t = 1
    for i in range(1, n + 1):
        t *= i
        if i % 2 == 1:
            odd += t
        else:
            even += t
    print odd, even
    #运行时间：16ms
    #占用内存：2944k

'''
题目链接
https://www.nowcoder.com/practice/e58c8a55162d49c48115bdfa5da7da56?tpId=40&&tqId=21561&rp=1&ru=/activity/oj&qru=/ta/kaoyan/question-ranking
题目描述
输入n， 求y1=1!+3!+...m!(m是小于等于n的最大奇数） y2=2!+4!+...p!(p是小于等于n的最大偶数)。
输入描述:
每组输入包括1个整数：n
输出描述:
可能有多组测试数据，对于每组数据，
输出题目要求的y1和y2
示例1
输入
4
输出
7 26

n!=(n-1)!*n，如果是奇数就加入到odd中，偶数就加入到even中。
'''