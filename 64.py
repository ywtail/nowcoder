# coding:utf-8
# python3
# 字符个数统计(华为)

input_s=set(list(input()))
ans=0
for s in list(input_s):
    if ord(s)<=127:
        ans+=1
print(ans)
#运行时间：32ms
#占用内存：3424k

'''
题目地址：
https://www.nowcoder.com/practice/eb94f6a5b2ba49c6ac72d40b5ce95f50?tpId=37&tqId=21233&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述：
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。
输入描述:
输入N个字符，字符在ACSII码范围内。
输出描述:
输出范围在(0~127)字符的个数。
示例1
输入
abc
输出
3

测试用例:
uqic^g`(s&jnl(m#vt!onwdj(ru+os&wx
对应输出应该为:
24

注意审题，题中两个条件是：1.范围在(0~127); 2.不同字符
因此需要对字符串去重
'''