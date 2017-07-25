# coding:utf-8
# 进制转换

while 1:
    try:
        s = raw_input()
        print int(s, 16)
    except:
        break

# 运行时间：20ms
# 占用内存：2824k

'''
题目地址：
https://www.nowcoder.com/practice/8f3df50d2b9043208c5eed283d1d4da6?tpId=37&tqId=21228&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述：
写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）
输入描述:
输入一个十六进制的数值字符串。
输出描述:
输出该数值的十进制字符串。
示例1
输入
0xA
输出
10
'''