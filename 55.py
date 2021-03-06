# coding:utf-8
# 身份证分组

s = raw_input().replace(' ', '')
n = len(s)
if n <= 6:
    print s
elif n <= 14:
    print s[:6], s[6:]
else:
    print s[:6], s[6:14], s[14:18]

# 运行时间：25ms
# 占用内存：2956k

'''
题目地址
https://www.nowcoder.com/practice/58766632a6cc45c0a1158fea2db91728?tpId=85&&tqId=29888&rp=2&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
18位身份证的编码规则是：
前1、2位数字表示：所在省（直辖市、自治区）的代码
第3、4位数字表示：所在地级市（自治州）的代码
第5、6位数字表示：所在区（县、自治县、县级市）的代码；
第7—14位数字表示：出生年、月、日；
第15、16位数字表示：所在地的派出所的代码；
第17位数字表示性别：奇数表示男性，偶数表示女性；
第18位数字是校检码，用来检验身份证的正确性。
用户在输入身份证的过程中经常会输入错误，为了方便用户正确输入需要在输入过程中对用户的输入按照 6+8+4 的格式进行分组，实现一个方法接收输入过程中的身份证号，返回分组后的字符
输入描述:
输入数据有多行，每一行是一个输入过程中的身份证号
输出描述:
分组后的字符串
示例1
输入
5021
502104 198803
5021041988033084
502104198803308324
输出
5021
502104 198803
502104 19880330 84
502104 19880330 8324

这一题容易出错的地方在于，直接使用`print s[:6], s[6:14], s[14:18]`看起来结果正确，
但是通过率只有40%，报错：格式错误:您的程序输出的格式不符合要求（比如空格和换行与要求不一致）。
这是因为输入`5021`，输出的是`5021  `，长度为6，虽然s[6:14]=''，但是逗号代表的空格还会输出。
所以应该分情况输出，不能直接`print s[:6], s[6:14], s[14:18]`
'''