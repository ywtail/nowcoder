# -*- coding:utf-8 -*-
# 最长公共子串

class LongestSubstring:
    def findLongest(self, A, n, B, m):
        table = [[0 for i in range(m + 1)] for j in range(n + 1)]  # 这样初始化不用考虑[i-1]和[j-1]是否越界的问题
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                    ans = max(ans, table[i][j])
        return ans

        # 运行时间：180ms
        # 占用内存：3156k


longestsubstring = LongestSubstring()
print longestsubstring.findLongest("1AB2345CD", 9, "12345EF", 7)

'''
## 最长公共子串
[题目链接](https://www.nowcoder.com/practice/02e7cc263f8a49e8b1e1dc9c116f7602?tpId=49&tqId=29349&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对于两个字符串，请设计一个时间复杂度为O(m*n)的算法(这里的m和n为两串的长度)，求出两串的最长公共子串的长度。这里的最长公共子串的定义为两个序列U1,U2,..Un和V1,V2,...Vn，其中Ui + 1 == Ui+1,Vi + 1 == Vi+1，同时Ui == Vi。
给定两个字符串A和B，同时给定两串的长度n和m。

**测试样例**

>"1AB2345CD",9,"12345EF",7
返回：4

- findLongest(self, A, n, B, m):
动态规划。
'''