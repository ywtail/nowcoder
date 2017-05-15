# -*- coding:utf-8 -*-
# 字符串的旋转

class StringRotation:
    def rotateString(self, A, n, p):
        return A[p + 1:] + A[:p + 1]
        # 运行时间：40ms
        # 占用内存：3156k

    def rotateString1(self, A, n, p):
        return (A + A)[p + 1:p + 1 + n]
        # 运行时间：30ms
        # 占用内存：3156k

stringrotation = StringRotation()
print stringrotation.rotateString("ABCDEFGH", 8, 4)
print stringrotation.rotateString1("ABCDEFGH", 8, 4)

'''
## 字符串的旋转
[题目链接](https://www.nowcoder.com/practice/85062aa6016640d188a6a0daf9f5da0e?tpId=49&tqId=29375&tPage=2&rp=2&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

对于一个字符串，和字符串中的某一位置，请设计一个算法，将包括i位置在内的左侧部分移动到右边，将右侧部分移动到左边。
给定字符串A和它的长度n以及特定位置p，请返回旋转后的结果。

**测试样例**

>"ABCDEFGH",8,4
返回："FGHABCDE"

- rotateString(self, A, n, p):
找到截断点，用截断点右侧字符串连接左侧字符串。

- findLongest1(self, A, n):
两个A连接，从位置p+1开始，截取长度为n的串即为答案。
'''