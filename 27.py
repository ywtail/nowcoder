# coding:utf-8
# 最大公约数

while 1:
    try:
        a, b = map(int, raw_input().split())
    except:
        break
    while b:
        a, b = b, a % b
    print a
    # 运行时间：24ms
    # 占用内存：2824k

'''
题目链接
https://www.nowcoder.com/practice/e58c8a55162d49c48115bdfa5da7da56?tpId=40&&tqId=21561&rp=1&ru=/activity/oj&qru=/ta/kaoyan/question-ranking
题目描述
输入两个正整数，求其最大公约数。
输入描述:
测试数据有多组，每组输入两个正整数。
输出描述:
对于每组输入,请输出其最大公约数。
示例1
输入
49 14
输出
7

辗转相除法gcd
'''