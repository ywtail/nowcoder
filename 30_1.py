# -*- coding:utf-8 -*-
# 最长回文子串

class Palindrome:
    def getLongestPalindrome(self, A, n):
        re = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            re[j][j] = 1
            for i in range(0, j)[::-1]:
                if A[i] == A[j] and re[i + 1][j - 1] == j - i - 1: #如果s[i+1...j-1]是回文串
                    re[i][j] = re[i + 1][j - 1] + 2
                else:
                    re[i][j] = max(re[i + 1][j], re[i][j - 1])
        return re[0][n - 1]

    # 运行时间：362ms
    # 占用内存：5760k


pld = Palindrome()
print pld.getLongestPalindrome("abc1234321ab", 12)
# 7
print pld.getLongestPalindrome("baabccc", 7)
# 4

'''
题目链接
https://www.nowcoder.com/practice/b4525d1d84934cf280439aeecc36f4af?tpId=49&&tqId=29360&rp=1&ru=/activity/oj&qru=/ta/2016test/question-ranking
题目描述
对于一个字符串，请设计一个高效算法，计算其中最长回文子串的长度。
给定字符串A以及它的长度n，请返回最长回文子串的长度。
测试样例：
"abc1234321ab",12
返回：7

使用动态规划。
用 re[i][j] 表示子串 s[i...j] 中最长回文子串的长度。
'''
