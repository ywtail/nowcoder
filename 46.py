# coding:utf-8
# 合并表记录

n = int(raw_input())
re = {}
for i in range(n):
    a, b = map(int, raw_input().split())
    if a in re:
        re[a] += b
    else:
        re[a] = b

for x in sorted(re):
    print x, re[x]

# 运行时间：28ms
# 占用内存：3076k

'''
题目地址：
https://www.nowcoder.com/practice/de044e89123f4a7482bd2b214a685201?tpId=37&tqId=21231&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述：
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开
输出描述:
输出合并后的键值对（多行）
示例1
输入
4
0 1
0 2
1 2
3 4
输出
0 3
1 2
3 4
'''