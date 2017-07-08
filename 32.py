# -*- coding:utf-8 -*-
# 链表的回文结构

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class PalindromeList:
    def chkPalindrome(self, A):
        if not A:
            return True
        re = [A.val]
        A = A.next
        while A:
            if not re:
                return False
            if A.val == re[-1]:
                re.pop()
            else:
                re.append(A.val)
            A = A.next
        if not re:
            return True
        return False

    # 运行时间：113ms
    # 占用内存：5764k


l = [1, 2, 2, 1, 1] #输入
a = ListNode(0)
t = a
for x in l:
    t.next = ListNode(x)
    t = t.next

pl = PalindromeList()
print pl.chkPalindrome(a.next)

'''
题目链接
https://www.nowcoder.com/practice/d281619e4b3e4a60a2cc66ea32855bfa?tpId=49&&tqId=29370&rp=1&ru=/activity/oj&qru=/ta/2016test/question-ranking
题目描述
对于一个链表，请设计一个时间复杂度为O(n),额外空间复杂度为O(1)的算法，判断其是否为回文结构。
给定一个链表的头指针A，请返回一个bool值，代表其是否为回文结构。保证链表长度小于等于900。
测试样例：
1->2->2->1
返回：true

依次读入链表中的数，使用列表模拟栈判断。
'''