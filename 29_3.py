# coding:utf-8
# 回文串

while 1:
    try:
        s = raw_input()
    except:
        break
    n = len(s)
    if n < 3:
        print 'YES'
    else:
        re = [[0 for i in range(n + 1)] for j in range(n + 1)]
        t = s[::-1]
        ma = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    re[i][j] = re[i - 1][j - 1] + 1
                else:
                    re[i][j] = re[i - 1][j - 1]
                ma = max(ma, re[i][j])
        if n - ma < 2:
            print 'YES'
        else:
            print 'NO'
    # 运行时间：23ms
    #占用内存：2952k

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

求 s 与 s[::-1] 的公共子序列的长度，
如果这个长度等于 n 或者比 n 小 1，则说明可以通过增加一个字符使字符串变成回文串。
'''