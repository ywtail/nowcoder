# coding:utf-8
# 统计字符

s = raw_input()
n = len(s)
tmp_dict = {}
for i in range(n):
    if s[i].isalpha(): # 需要过滤非英文字符
        tmp_dict[s[i]] = tmp_dict.get(s[i], 0) + 1
        if tmp_dict[s[i]] == 3:
            print s[i]
            break

    # 运行时间：24ms
    # 占用内存：3076k

'''
题目地址
https://www.nowcoder.com/practice/e3f67da21c3f45bfb091cf0cabb9bb0f?tpId=85&&tqId=29889&rp=1&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
给定一个英文字符串,请写一段代码找出这个字符串中首先出现三次的那个英文字符。
输入描述:
输入数据一个字符串，包括字母,数字等。
输出描述:
输出首先出现三次的那个英文字符
示例1
输入
Have you ever gone shopping and
输出
e

这一题的陷阱在于，题目中说给定的是一个"英文字符串"，实际上在测试用例中包含非英文字符例如"%￥#"，
需要在代码中进行处理
'''