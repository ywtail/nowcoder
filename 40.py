# coding:utf-8
# 基本字符串压缩

class Zipper:
    def zipString(self, iniString):
        n = len(iniString)
        if n < 3:
            return iniString
        s = ''  # 字符串压缩结果
        t = iniString[0]  # 当前字符
        c = 1  # 当前字符计数
        for i in range(1, n):
            if iniString[i] == iniString[i - 1]:
                c += 1
            else:
                s += t + str(c)
                t = iniString[i]
                c = 1
        s += t + str(c)
        if len(s) < n:
            return s
        return iniString
        # 运行时间：63ms
        # 占用内存：5748k


zipper = Zipper()
print zipper.zipString('aabcccccaaa')
# a2b1c5a3
print zipper.zipString('welcometonowcoderrrrr')
# welcometonowcoderrrrr

'''
题目地址
https://www.nowcoder.com/practice/21f3a84300c94db092e0b5a7bf2d0ad1?tpId=8&&tqId=10998&rp=1&ru=/activity/oj&qru=/ta/cracking-the-coding-interview/question-ranking
题目描述
利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。比如，字符串“aabcccccaaa”经压缩会变成“a2b1c5a3”。若压缩后的字符串没有变短，则返回原先的字符串。
给定一个string iniString为待压缩的串(长度小于等于10000)，保证串内字符均由大小写英文字母组成，返回一个string，为所求的压缩后或未变化的串。
测试样例
"aabcccccaaa"
返回："a2b1c5a3"
"welcometonowcoderrrrr"
返回："welcometonowcoderrrrr"
'''