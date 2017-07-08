# -*- coding:utf-8 -*-
# 最长回文子串

class Palindrome:
    def getLongestPalindrome(self, A, n):
        if n < 2:
            return n
        ans = 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if A[i:j + 1] == A[i:j + 1][::-1]:
                    ans = max(ans, j - i + 1)
        return ans
        # 运行时间：441ms
        # 占用内存：5760k


pld = Palindrome()
print pld.getLongestPalindrome("abc1234321ab", 12)
# 7
print pld.getLongestPalindrome("baabccc", 7)
# 4
print pld.getLongestPalindrome("ccbcabaabba", 11)
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

暴力，枚举每个子串，看是否是回文串。
'''