# coding:utf-8
# python3
# 字符串的连接最长路径查找(华为)

n=int(input())
input_s_list=[]
for i in range(n):
    input_s_list.append(input())
for s in sorted(input_s_list):
    print(s)
#运行时间：31ms
#占用内存：5396k

'''
题目地址：
https://www.nowcoder.com/practice/5af18ba2eb45443aa91a11e848aa6723?tpId=37&tqId=21237&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述:
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
示例1
输入
9
cap
to
cat
card
two
too
up
boat
boot
输出
boat
boot
cap
card
cat
to
too
two
up
'''