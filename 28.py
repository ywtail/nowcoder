# coding:utf-8
# 回文字符串

while 1:
    try:
        s = raw_input()
    except:
        break
    n = len(s)
    if n == 1:
        print 'Yes!'
    else:
        if s[:n / 2] == s[-(n / 2):][::-1]:
            print 'Yes!'
        else:
            print 'No!'
    # 运行时间：26ms
    # 占用内存：2708k

'''
题目链接
https://www.nowcoder.com/practice/df00c27320b24278b9c25f6bb1e2f3b8?tpId=69&&tqId=29674&rp=1&ru=/activity/oj&qru=/ta/hust-kaoyan/question-ranking
题目描述
给出一个长度不超过1000的字符串，判断它是不是回文(顺读，逆读均相同)的。
输入描述:
输入包括一行字符串，其长度不超过1000。
输出描述:
可能有多组测试数据，对于每组数据，如果是回文字符串则输出"Yes!”，否则输出"No!"。
示例1
输入
hellolleh
helloworld
输出
Yes!
No!

注意 -n/2 与 -(n/2) 结果不同
'''