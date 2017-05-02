# -*- coding:utf-8 -*-
# 抛小球

class Balls:
    def calcDistance(self, A, B, C, D):
        return 3*(A+B+C+D)

        # 运行时间：20ms
        # 占用内存：3156k

balls = Balls()
print balls.calcDistance(100,90,80,70)

'''
## 抛小球
[题目链接](https://www.nowcoder.com/practice/ae45a1d8bc1d43858c83762fe8c2802c?tpId=49&tqId=29306&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

小东和三个朋友一起在楼上抛小球，他们站在楼房的不同层，假设小东站的楼层距离地面N米，球从他手里自由落下，每次落地后反跳回上次下落高度的一半，并以此类推知道全部落到地面不跳，求4个小球一共经过了多少米？(数字都为整数)
给定四个整数A,B,C,D，请返回所求结果。

**测试样例**

>100,90,80,70
>返回：1020

- calcDistance(self, A, B, C, D):
求极限
'''