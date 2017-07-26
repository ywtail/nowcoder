# coding:utf-8
# 提取不重复的整数

n = raw_input()[::-1]
print int(''.join(sorted(set(n), key=n.index)))
# 运行时间：20ms
# 占用内存：2948k

'''
题目地址：
https://www.nowcoder.com/practice/253986e66d114d378ae8de2e6c4577c1?tpId=37&tqId=21232&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述：
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
输入描述:
输入一个int型整数
输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
示例1
输入
9876673
输出
37689
'''