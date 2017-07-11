# coding:utf-8
# 杨辉三角形

while 1:
    try:
        n = int(raw_input())
    except:
        break
    re = [[1, 1]]
    for i in range(1, n - 1):
        t = [1 for j in range(i + 2)]
        for j in range(1, i + 1):
            t[j] = re[-1][j - 1] + re[-1][j]
        re.append(t)
    for x in re:
        for y in x:
            print y,
        print
    # 运行时间：20ms
    # 占用内存：3072k

'''
题目地址
https://www.nowcoder.com/practice/ef7f264886a14fdf8a6ed3ac008a23c8?tpId=68&&tqId=29650&rp=1&ru=/activity/oj&qru=/ta/nwpu-kaoyan/question-ranking
题目描述
输入n值，使用递归函数，求杨辉三角形中各个位置上的值。
输入描述:
一个大于等于2的整型数n
输出描述:
题目可能有多组不同的测试数据，对于每组输入数据，
按题目的要求输出相应输入n的杨辉三角形。
示例1
输入
6
输出
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
'''