# coding:utf-8
# N的阶乘

while 1:
    try:
        n = int(raw_input())
    except:
        break
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    print ans
    #运行时间：27ms
    #占用内存：2820k

'''
题目链接
 https://www.nowcoder.com/practice/f54d8e6de61e4efb8cce3eebfd0e0daa?tpId=40&&tqId=21355&rp=1&ru=/activity/oj&qru=/ta/kaoyan/question-ranking
题目描述
 输入一个正整数N，输出N的阶乘。
输入描述:
 正整数N(0<=N<=1000)
输出描述:
 输入可能包括多组数据，对于每一组输入数据，输出N的阶乘
示例1
输入
4
5
15
输出
24
120
1307674368000

题目给定n的范围是[1,1000]，不涉及大数，对python来说也不用考虑是不是长整型，因此直接求就可以了。
这一题比上一题表达的明确，要求输入多组数据(循环读入while( scanf("%d",&n)!=EOF))。
'''