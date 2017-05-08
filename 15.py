# -*- coding:utf-8 -*-
# 股票交易日

class Stock:
    def maxProfit(self, prices, n):
        leftmin = prices[0]
        rightmax = prices[n - 1]
        leftprof = [0 for i in range(n)]
        rightprof = [0 for i in range(n)]
        sum = 0
        for i in range(1, n):
            leftmin = min(leftmin, prices[i]) # 从左向右找最小price记为leftmin
            leftprof[i] = max(leftprof[i - 1], prices[i] - leftmin)
        for j in range(0, n - 1)[::-1]:
            rightmax = max(rightmax, prices[j]) # 从右向左找最大值记为rightmax
            rightprof[j] = max(rightprof[j + 1], rightmax - prices[j])
        for i in range(n): # 以i为分割点，左半段最大收益为leftprof[i]，右半段最大收益为rightprof[i]
            sum = max(sum, leftprof[i] + rightprof[i])
        return sum


        # 运行时间：50ms
        # 占用内存：3156k

stock = Stock()
print stock.maxProfit([10, 22, 5, 75, 65, 80], 6)

'''
## 股票交易日
[题目链接](https://www.nowcoder.com/practice/3e8c66829a7949d887334edaa5952c28?tpId=49&tqId=29317&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

在股市的交易日中，假设最多可进行两次买卖(即买和卖的次数均小于等于2)，规则是必须一笔成交后进行另一笔(即买-卖-买-卖的顺序进行)。
给出一天中的股票变化序列，请写一个程序计算一天可以获得的最大收益。请采用实践复杂度低的方法实现。
给定价格序列prices及它的长度n，请返回最大收益。保证长度小于等于500。

**测试样例**
>[10,22,5,75,65,80],6
返回：87

- maxProfit(self, prices, n):
求出以i点为分割点，左半段最大收益的数组leftprof，和右半段最大收益的数组rightprof。
然后遍历，找出最大的leftprof[i]+rightprof[i]组合。
'''