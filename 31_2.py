# -*- coding:utf-8 -*-
# 添加回文串

class Palindrome:
    def addToPalindrome(self, A, n):
        t = 0
        for i in range(n):
            if A[i] == A[-1]:
                if A[i:] == A[i:][::-1]:
                    t = i
                    break
        return A[:t][::-1]
        # 运行时间：38ms
        # 占用内存：5888k


pld = Palindrome()
print pld.addToPalindrome('ab', 2)
# a
print pld.addToPalindrome("bbabbaaabba", 11)
# bb
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

求出从哪个位置开始到结尾是回文串，这个位置之前的字符串的倒序就是需要添加到末尾的
'''