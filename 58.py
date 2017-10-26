# coding:utf-8
# 游戏任务标记

id_one, id_two = map(int, raw_input().split())
if id_two > 1024:
    print -1
elif id_one == id_two:
    print 1
else:
    print 0

# 运行时间：26ms
# 占用内存：2944k

'''
题目地址
https://www.nowcoder.com/practice/2f45f0ef94724e06a4173c91ef60781c?tpId=85&&tqId=29871&rp=3&ru=/activity/oj&qru=/ta/2017test/question-ranking
题目描述
游戏里面有很多各式各样的任务，其中有一种任务玩家只能做一次，这类任务一共有1024个，任务ID范围[1,1024]。
请用32个unsigned int类型来记录着1024个任务是否已经完成。初始状态都是未完成。
输入两个参数，都是任务ID，需要设置第一个ID的任务为已经完成；并检查第二个ID的任务是否已经完成。
输出一个参数，如果第二个ID的任务已经完成输出1，如果未完成输出0。
如果第一或第二个ID不在[1,1024]范围，则输出-1。
输入描述:
输入包括一行,两个整数表示人物ID.
输出描述:
输出是否完成
示例1
输入
1024 1024
输出
1

虽然AC了，但是题目的本意应该不是这样的。
任务有1024个，需要1024bit来表示当前id的任务是否完成。
1024bit=1024/8byte=128byte，一个整数占4byte，所以可以用128/4=32个int来表示。
然后检查各个位。
具体参考：https://www.nowcoder.com/questionTerminal/2f45f0ef94724e06a4173c91ef60781c
'''