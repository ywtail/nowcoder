# coding:utf-8
# 计算字符个数

s = raw_input().lower()
c = raw_input().lower()
print s.count(c)
# 运行时间：25ms
# 占用内存：2948k

'''
题目地址：
https://www.nowcoder.com/practice/a35ce98431874e3a820dbe4b2d0508b1?tpId=37&tqId=21225&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述：
写出一个程序，接受一个有字母和数字以及空格组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
输入描述:
输入一个有字母和数字以及空格组成的字符串，和一个字符。
输出描述:
输出输入字符串中含有该字符的个数。
示例1
输入
ABCDEF
A
输出
1
'''