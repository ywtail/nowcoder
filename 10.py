# -*- coding:utf-8 -*-
# 字符串通配

class WildMatch:
    def chkWildMatch(self, A, lena, B, lenb):
        dotcount = B.count('.')
        starcount = B.count('*')
        if starcount == 0:  # 如果没有*，则.的个数必须和lena相同才返回Ture，否则返回False
            if dotcount == lena:
                return True
            else:
                return False
        else:  # 如果有*，因为*可以匹配0或多个，所以只需要(dotcount - starcount) <= lena 就返回Ture，否则返回False
            if (dotcount - starcount) <= lena:
                return True
            else:
                return False
        
        # 运行时间：20ms
        # 占用内存：3156k


wildmatch = WildMatch()
print wildmatch.chkWildMatch("abcd", 4, ".*", 2)

'''
## 字符串通配
[题目链接](https://www.nowcoder.com/practice/28acd1134e344040ad105b3786a79e7a?tpId=49&tqId=29355&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对对于字符串A，其中绝对不含有字符’.’和’*’。再给定字符串B，其中可以含有’.’或’*’，’*’字符不能是B的首字符，并且任意两个’*’字符不相邻。exp中的’.’代表任何一个字符，B中的’*’表示’*’的前一个字符可以有0个或者多个。请写一个函数，判断A是否能被B匹配。
给定两个字符串A和B,同时给定两个串的长度lena和lenb，请返回一个bool值代表能否匹配。保证两串的长度均小于等于300。

**测试样例**

>"abcd",4,".*",2
>返回：true

- chkWildMatch(self, A, lena, B, lenb):
在这一题中，B仅由.和*组成，所以只需要考虑.和*的个数就能够ac
'''