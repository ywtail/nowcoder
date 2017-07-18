# coding:utf-8
# 字符串最后一个单词的长度

s = raw_input().split()
print len(s[-1])
# 运行时间：21ms
# 占用内存：2824k

'''
题目地址
https://www.nowcoder.com/practice/8c949ea5f36f422594b306a2300315da?tpId=37&&tqId=21224&rp=1&ru=/activity/oj&qru=/ta/huawei/question-ranking
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。
输出描述:
整数N，最后一个单词的长度。
示例1
输入
hello world
输出
5
'''