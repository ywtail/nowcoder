# -*- coding:utf-8 -*-
# 年终奖

class Bonus:
    def getMost(self, board):
        for i in range(6):
            for j in range(6):
                board[i][j] += max(board[i][j - 1] if j > 0 else 0, board[i - 1][j] if i > 0 else 0)
        return board[5][5]

        # 输出5300
        # 运行时间：30ms
        # 占用内存：3156k

bonus = Bonus()
print bonus.getMost([[200, 700, 300, 100, 100, 400], [200, 700, 300, 100, 100, 400], [200, 700, 300, 100, 100, 400],
                     [200, 700, 300, 100, 100, 400], [200, 700, 300, 100, 100, 400], [200, 700, 300, 100, 100, 400]])

'''
## 年终奖
[题目链接](https://www.nowcoder.com/practice/72a99e28381a407991f2c96d8cb238ab?tpId=49&tqId=29305&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

小东所在公司要发年终奖，而小东恰好获得了最高福利，他要在公司年会上参与一个抽奖游戏，游戏在一个6*6的棋盘上进行，上面放着36个价值不等的礼物，每个小的棋盘上面放置着一个礼物，他需要从左上角开始游戏，每次只能向下或者向右移动一步，到达右下角停止，一路上的格子里的礼物小东都能拿到，请设计一个算法使小东拿到价值最高的礼物。
给定一个6*6的矩阵board，其中每个元素为对应格子的礼物价值,左上角为[0,0],请返回能获得的最大价值，保证每个礼物价值大于100小于1000。

- getMost(self, board):
典型的动态规划算法。
'''