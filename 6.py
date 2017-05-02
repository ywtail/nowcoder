# -*- coding:utf-8 -*-
# 串的模式匹配

class StringPattern:
    def findAppearance(self, A, lena, B, lenb):
        return A.find(B)

    def findAppearance1(self, A, lena, B, lenb):
        if lena < lenb:
            return -1
        for i in range(0, lena - lenb + 1):
            if A[i] == B[0]:
                if A[i:i + lenb] == B:
                    return i
        return -1


stringpattern = StringPattern()
print stringpattern.findAppearance("acbc", 4, "bc", 2)
print stringpattern.findAppearance1("acbc", 4, "bc", 2)

'''
## 串的模式匹配
[题目链接](https://www.nowcoder.com/practice/084b6cb2ca934d7daad55355b4445f8a?tpId=49&tqId=29363&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对于两个字符串A，B。请设计一个高效算法，找到B在A中第一次出现的起始位置。若B未在A中出现，则返回-1。
给定两个字符串A和B，及它们的长度lena和lenb，请返回题目所求的答案。

**测试样例**

>"acbc",4,"bc",2
>返回：2

- findAppearance(self, A, lena, B, lenb):
find实现
运行时间：30ms
占用内存：3156k

- findAppearance1(self, A, lena, B, lenb):
老实写一遍：当B长度小于A时，返回-1；遍历A，如果A[i]与B[0]相等，则截取A[i:i + lenb]与B对比，如果相同就返回当前i
运行时间：10ms
占用内存：3156k
'''