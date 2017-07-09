# coding:utf-8
# 三角形的边

while 1:
    a, b, c = map(int, raw_input().split())
    if a == 0:
        break
    print a + b + c - 2 * max(a, b, c)
    # 运行时间：15ms
    # 占用内存：2824k

'''
题目地址
https://www.nowcoder.com/practice/05dbd1cd43b24dbbae567b3e816d4e97?tpId=65&&tqId=29620&rp=1&ru=/activity/oj&qru=/ta/jlu-kaoyan/question-ranking
题目描述
给定三个已知长度的边，确定是否能够构成一个三角形，这是一个简单的几何问题。我们都知道，这要求两边之和大于第三边。实际上，并不需要检验所有三种可能，只需要计算最短的两个边长之和是否大于最大那个就可以了。 这次的问题就是：给出三个正整数，计算最小的数加上次小的数与最大的数之差。
输入描述:
每一行包括三个数据a, b, c，并且都是正整数，均小于10000。当a为0时标志所有输入数据结束。
输出描述:
对于输入的每一行，在单独一行内输出结果s。s=min(a,b,c)+mid(a,b,c)-max(a,b,c)。上式中，min为最小值，mid为中间值，max为最大值。
示例1
输入
1 2 3
6 5 4
10 20 15
1 1 100
0 0 0
输出
0
3
5
-98
'''