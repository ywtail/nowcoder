# coding:utf-8
# 取近似值

print int(float(raw_input())+0.5)

# 运行时间：24ms
# 占用内存：2952k

'''
题目地址
https://www.nowcoder.com/practice/3ab09737afb645cc82c35d56a5ce802a?tpId=37&tqId=21230&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
输入描述:1.4
输入一个正浮点数值
输出描述:
输出该数值的近似整数值
示例1
输入
5.5
输出
6

其实是要实现round的功能。
还可以用 float(a)-int(a) 判断是否小于0.5。
'''