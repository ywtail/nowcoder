# coding:utf-8
# 把字符串转换成整数

class Solution:
    def StrToInt(self, s):
        n = len(s)
        if n == 0 or s == '+' or s == '-':
            return 0
        ans = ''
        for i in range(n):
            if i == 0 and s[i] == '+':
                continue
            if i == 0 and s[i] == '-':
                ans = '-'
                continue
            if s[i].isdigit():
                ans += s[i]
            else:
                return 0
        return eval(ans) - eval('0')
        # 运行时间：36ms
        # 占用内存：5760k


solution = Solution()
print solution.StrToInt('+2147483647')
# 2147483647
print solution.StrToInt('1a33')
# 0

'''
题目地址
https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&&tqId=11202&rp=1&ru=/activity/oj&qru=/ta/coding-interviews/question-ranking
题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
+2147483647
1a33
输出
2147483647
0

使用evel将字符串转为整数。
eval的功能是将字符串str当成有效的表达式来求值并返回计算结果。
在python中，'9'-'0'会报错，但是 evel('9')-evel('0')=9
'''