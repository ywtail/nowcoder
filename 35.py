# coding:utf-8
# 判断三角形类型

while 1:
    try:
        a, b, c = sorted(map(int, raw_input().split()))
    except:
        break
    t = a * a + b * b - c * c
    if t < 0:
        print '钝角三角形'
    elif t == 0:
        print '直角三角形'
    else:
        print '锐角三角形'
    # 运行时间：33ms
    # 占用内存：2804k

'''
题目地址
https://www.nowcoder.com/practice/1521dea0744c46ad8c31b0bd860625d0?tpId=64&&tqId=29606&rp=1&ru=/activity/oj&qru=/ta/hit-kaoyan/question-ranking
题目描述
给定三角形的三条边，a,b,c。判断该三角形类型。
输入描述:
测试数据有多组，每组输入三角形的三条边。
输出描述:
对于每组输入,输出直角三角形、锐角三角形、或是钝角三角形。
示例1
输入
3 4 5
输出
直角三角形
'''