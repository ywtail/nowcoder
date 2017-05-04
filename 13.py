# -*- coding:utf-8 -*-
# 最长公共子序列

class LCS:
    def findLCS(self, A, n, B, m):
        ans = [[0 for i in range(m + 1)] for j in range(n + 1)]  # 这样初始化不用考虑[i-1]和[j-1]是否越界的问题
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    ans[i][j] = ans[i - 1][j - 1] + 1
                else:
                    ans[i][j] = max(ans[i][j - 1], ans[i - 1][j])
        return ans[n][m]

        # 运行时间：240ms
        # 占用内存：3148k


lcs = LCS()
print lcs.findLCS("1A2C3D4B56", 10, "B1D23CA45B6A", 12)

'''
## 最长公共子序列
[题目链接](https://www.nowcoder.com/practice/c996bbb77dd447d681ec6907ccfb488a?tpId=49&tqId=29348&tPage=1&rp=1&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对于两个字符串，请设计一个高效算法，求他们的最长公共子序列的长度，这里的最长公共子序列定义为有两个序列U1,U2,U3...Un和V1,V2,V3...Vn,其中Ui&ltUi+1，Vi&ltVi+1。且A[Ui] == B[Vi]。
给定两个字符串A和B，同时给定两个串的长度n和m，请返回最长公共子序列的长度。保证两串长度均小于等于300。

**测试样例**

>"1A2C3D4B56",10,"B1D23CA45B6A",12
返回：6

- findLCS(self, A, n, B, m):
动态规划，将公共长度存到ans[N+1][M+1]数组中，求ans[i][j]。
'''