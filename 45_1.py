# coding:utf-8
# 取近似值

a = raw_input().split('.')
if int(a[1][0]) < 5:
    print int(a[0])
else:
    print int(a[0]) + 1

# 运行时间：27ms
# 占用内存：2824k

'''
题目地址
https://www.nowcoder.com/practice/3ab09737afb645cc82c35d56a5ce802a?tpId=37&tqId=21230&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
输入描述:
输入一个正浮点数值
输出描述:
输出该数值的近似整数值
示例1
输入
5.5
输出
6
'''