# coding:utf-8
# 求数列的和
from __future__ import division

while 1:
    try:
        n, m = map(int, raw_input().split())
    except:
        break
    ans = 0
    for i in range(m):
        ans += n
        n = n ** 0.5
    print '%.2f' % ans

    # 运行时间：29ms
    # 占用内存：3076k

'''
题目地址
https://www.nowcoder.com/practice/02f23a209c0c4d2484e29b560c174de1?tpId=85&&tqId=29893&rp=1&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
输入描述:
输入数据有多组，每组占一行，由两个整数n（n < 10000）和m(m < 1000)组成，n和m的含义如前所述。
输出描述:
对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。
示例1
输入
81 4
2 2
输出
94.73
3.41
'''