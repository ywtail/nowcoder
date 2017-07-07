# coding:utf-8
# 回文串

def judge(s, n):
    if n < 2:
        return 'YES'
    else:
        for i in range(n):
            t = s[:i] + s[i + 1:]
            if t[:(n - 1) / 2] == t[-((n - 1) / 2):][::-1]:
                return 'YES'
        return 'NO'


while 1:
    try:
        s = raw_input()
    except:
        break
    n = len(s)
    print judge(s, n)
    #运行时间：25ms
    #占用内存：3072k

'''
题目链接
https://www.nowcoder.com/practice/655a43d702cd466093022383c24a38bf?tpId=49&&tqId=29295&rp=1&ru=/activity/oj&qru=/ta/2016test/question-ranking
题目描述
给定一个字符串，问是否能通过添加一个字母将其变为回文串。
输入描述:
一行一个由小写字母构成的字符串，字符串长度小于等于10。
输出描述:
输出答案(YES\NO).
示例1
输入
coco
输出
YES

如果能通过增加一个字符变成回文串，那么一定也可以通过删除一个字符变成回文串。
用一个循环，每次循环依次删掉一个字符，然后检查新串是否是回文串。
'''