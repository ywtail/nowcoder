# coding:utf-8
# 查找两个字符串a,b中的最长公共子串

while 1:
    try:
        s1 = raw_input()
        s2 = raw_input()
    except:
        break
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    n1 = len(s1)
    n2 = len(s2)

    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]  # 注意行列是n1还是n2
    maxlen = 0  # 记录最长公共子串长度
    maxindex = 0  # 记录截止位置
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > maxlen:
                    maxlen = dp[i][j]
                    maxindex = i

    print s1[maxindex - maxlen:maxindex]

    # 运行时间：43ms
    # 占用内存：3344k

'''
题目地址
https://www.nowcoder.com/practice/181a1a71c7574266ad07f9739f791506?tpId=37&&tqId=21288&rp=1&ru=/activity/oj&qru=/ta/huawei/question-ranking
题目描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
输入描述:
输入两个字符串
输出描述:
返回重复出现的字符
示例1
输入
abcdefghijklmnop
abcsafjklmnopqrstuvw
输出
jklmnop

使用动态规划求解：dp[i][j] = dp[i - 1][j - 1] + 1
'''