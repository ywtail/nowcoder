# -*- coding:utf-8 -*-
# 首个重复字符

class FirstRepeat:
    def findFirstRepeat(self, A, n):
        re = {}
        for k in A:
            if k in re:
                return k
            else:
                re[k] = 0 #只是将k放入字典中，不一定=0（等于多少对答案无影响）

firstrepeat = FirstRepeat()
print firstrepeat.findFirstRepeat("qywyer23tdd",11)

'''
## 首个重复字符
[题目链接](https://www.nowcoder.com/practice/dab59997905b4459a42587fece8a75f4?tpId=49&tqId=29279&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对于一个字符串，请设计一个高效算法，找到第一次重复出现的字符。
给定一个字符串(不一定全为字母)A及它的长度n。请返回第一个重复出现的字符。保证字符串中有重复字符，字符串的长度小于等于500。

**测试样例**

>"qywyer23tdd",11
>返回：y

- findFirstRepeat(self, A, n):
用字典记录，如果出现过就返回。
运行时间：20ms
占用内存：3156k
'''