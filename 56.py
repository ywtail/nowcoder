# coding:utf-8
# filename extension

filepath = raw_input().split('.')
if len(filepath) > 1:
    print filepath[-1]
else:
    print 'null' # y，如果没有后缀输出"null"

# 运行时间：25ms
# 占用内存：2956k

'''
题目地址
https://www.nowcoder.com/practice/7eb53c86e50845f6a2eafe7ea0fe9ef9?tpId=85&&tqId=29886&rp=2&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
Please create a function to extract the filename extension from the given path,return the extracted filename extension or null if none.
输入描述:
输入数据为一个文件路径
输出描述:
对于每个测试实例，要求输出对应的filename extension
示例1
输入
Abc/file.txt
输出
txt

测试用例:
abcd/Abc/file
对应输出应该为:
null
'''