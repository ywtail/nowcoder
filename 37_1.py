# coding:utf-8
# 字符串分隔

for i in range(2):
    s = raw_input()
    for j in range(0, len(s), 8):
        t = len(s[j:j + 8])
        if t == 8:
            print s[j:j + 8]
        else:
            print s[j:j + 8] + '0' * (8 - t)
# 运行时间：23ms
# 占用内存：2952k

'''
题目地址
https://www.nowcoder.com/practice/d9162298cb5a437aad722fccccaae8a7?tpId=37&&tqId=21227&rp=1&ru=/activity/oj&qru=/ta/huawei/question-ranking
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)
输出描述:
输出到长度为8的新字符串数组
示例1
输入
abc
123456789
输出
abc00000
12345678
90000000
'''