# coding:utf-8
# 回文串

while 1:
    try:
        s = raw_input()
    except:
        break
    n = len(s)
    if n < 2:
        print 'YES'
    else:
        re = [[0 for i in range(n)] for j in range(n)]
        for j in range(1, n):
            if s[j - 1] != s[j]:
                re[j - 1][j] = 1
            for i in range(0, j - 1)[::-1]:
                if s[i] == s[j]:
                    re[i][j] = re[i + 1][j - 1]
                else:
                    re[i][j] = min(re[i + 1][j], re[i][j - 1]) + 1
        if re[0][n - 1] > 1:
            print 'NO'
        else:
            print 'YES'
    # 运行时间：24ms
    # 占用内存：2952k

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

这个问题可以使用动态规划求解。
动态规划表 re 是一个 NxN 的矩阵，
re[i][j] 代表子串 s[i...j] 最少添加几个字符可以使 s[i...j] 是回文串。
因此主要解放方法就是求 re。有以下 3 中情况：
1. 如果 s[i...j] 只有一个字符，则已经是回文串了，re[i][j]=0，不需要添加任何字符；
2. 如果 s[i...j] 有两个字符，那么：如果 s[i] == s[j]，re[i][j]=0；否则 re[i][j]=1；
3. 如果 s[i...j] 多于两个字符，那么：
    (1) s[i]==s[j]，则 re[i][j]=re[i+1][j-1]，即 s[i...j] 需要添加的字符数与 s[i+1...j-1] 相同；
    (2) s[i]!=s[j]，则要让 s[i...j] 变成回文串有两种方案：
        a. 先让 s[i+1...j] 变成回文串，再在末尾加上字符 s[i]
        b. 先让 s[i...j-1] 变成回文串，再在开头加上字符 s[j]
        在这两种方法中选择代价小的，即 re[i][j] = min(re[i + 1][j], re[i][j - 1]) + 1
求得 re 后，re[0][n-1] 表示整个字符串需要添加几个字符使其变成回文串。
'''
