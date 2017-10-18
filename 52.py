# coding:utf-8
# 句子反转

while 1:
    try:
        s = raw_input().split()
    except:
        break
    print ' '.join(s[::-1])

    #运行时间：24ms
    #占用内存：2952k

'''
题目地址
https://www.nowcoder.com/practice/0ae4a12ab0a048ee900d1536a6e98315?tpId=85&&tqId=29896&rp=1&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
给定一个句子（只包含字母和空格）， 将句子中的单词位置反转，单词用空格分割, 单词之间只有一个空格，前后没有空格。 比如： （1） “hello xiao mi”-> “mi xiao hello”
输入描述:
输入数据有多组，每组占一行，包含一个句子(句子长度小于1000个字符)
输出描述:
对于每个测试示例，要求输出句子中单词反转后形成的句子
示例1
输入
hello xiao mi
输出
mi xiao hello

2017年秋招面试题。
'''