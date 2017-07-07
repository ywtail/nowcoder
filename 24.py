# coding:utf-8
# n的阶乘

while 1:
    try:
        n = int(raw_input())
    except:
        break
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    print ans
    #运行时间：24ms
    #占用内存：2948k

'''
题目链接
https://www.nowcoder.com/practice/97be22ee50b14cccad2787998ca628c8?tpId=40&&tqId=21348&rp=1&ru=/activity/oj&qru=/ta/kaoyan/question-ranking
题目描述
输入一个整数n，输出n的阶乘
输入描述:
一个整数n(1<=n<=20)
输出描述:
n的阶乘
示例1
输入
3
输出
6

题目给定n的范围是[1,20]，不涉及大数，因此直接求就可以了。
题目的坑不在算法上，而在循环读入上(while( scanf("%d",&n)!=EOF))，如果不是循环读入，就无法通过。
'''