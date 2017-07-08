# -*- coding:utf-8 -*-
# 添加回文串

class Palindrome:
    def addToPalindrome(self, A, n):
        t = A[::-1]
        re = [[0 for i in range(n)] for j in range(n)]
        ma = 1
        for i in range(n):
            if t[0] == A[i]:
                re[0][i] = 1
        for i in range(1, n):
            for j in range(i, n):
                if t[i] == A[j] and re[i - 1][j - 1] != 0: # 必须re[i - 1][j - 1] != 0
                    re[i][j] = re[i - 1][j - 1] + 1
            ma = max(ma, re[i][j])
        for i in range(n):
            for j in range(n):
                print re[i][j],
            print
        return A[:n - ma][::-1]
        # 运行时间：60ms
        # 占用内存：5764k


pld = Palindrome()
print pld.addToPalindrome("abab", 4)
# a
print pld.addToPalindrome("baabccc", 7)
# baab

'''
题目链接
https://www.nowcoder.com/practice/cfa3338372964151b19e7716e19987ac?tpId=49&&tqId=29361&rp=1&ru=/activity/oj&qru=/ta/2016test/question-ranking
题目描述
对于一个字符串，我们想通过添加字符的方式使得新的字符串整体变成回文串，但是只能在原串的结尾添加字符，请返回在结尾添加的最短字符串。
给定原字符串A及它的长度n，请返回添加的字符串。保证原串不是回文串。
测试样例：
"ab",2
返回："a"

动态规划，求 A 与 A[::-1] 末尾的公共子串，非公共的部分就是需要添加的字符串。
'''