# coding:utf-8
# python3
# 求int型正整数在内存中存储时1的个数(华为)

input_n=int(input())
print(bin(input_n).count('1'))
#运行时间：29ms
#占用内存：4344k

'''
题目地址：
https://www.nowcoder.com/practice/440f16e490a0404786865e99c6ad91c9?tpId=37&tqId=21238&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述:
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
输入描述:
 输入一个整数（int类型）
输出描述:
 这个数转换成2进制后，输出1的个数
示例1
输入
5
输出
2

bin(n)十进制转二进制
'''