# coding:utf-8
# 倒水
from __future__ import division

n = int(raw_input())
t, c = map(int, raw_input().split())
ts = []
cs = []
for i in range(n):
    a, b = map(int, raw_input().split())
    ts.append(a)
    cs.append(b)

up = t * c
d = c
if min(ts) < t < max(ts):
    print "Impossible"
else:
    for i in range(n):  # 将所有水混合在一起
        up += ts[i] * cs[i]
        d += cs[i]
    tt = up / d
    if tt <= min(ts):  # T 比水杯里的水温度都低，最终能达到 tt
        print "Possible"
        print "%.4f" % min(ts)  # 因为要输出最高温度，所有输出 min(ts)
    elif tt >= max(ts):  # T 比水杯里的水温度都高，最终能达到 tt
        print "Possible"
        print "%.4f" % tt
    else:
        print "Impossible"

'''
题目：
有一个大水缸，里面水的温度为T单位，体积为C升。另有n杯水（假设每个杯子的容量是无限的），每杯水的温度为t[i]单位，体积为c[i]升。
现在要把大水缸的水倒入n杯水中，使得n杯水的温度相同，请问这可能吗？并求出可行的最高温度，保留4位小数。
注意：一杯温度为t1单位、体积为c1升的水与另一杯温度为t2单位、体积为c2升的水混合后，温度变为(t1*c1+t2*c2)/(c1+c2)，体积变为c1+c2。

输入描述:
第一行一个整数n, 1 ≤ n ≤ 10^5
第二行两个整数T，C,其中0 ≤ T ≤ 10^4, 0 ≤ C ≤ 10^9
接下来n行每行两个整数t[i]，c[i]
0 ≤ t[i], c[i] ≤ 10^4

输出描述:
如果非法，输出“Impossible”（不带引号)否则第一行输出“Possible"（不带引号），第二行输出一个保留4位小数的实数表示答案。
样例解释：往第二杯水中倒0.5升水
往第三杯水中到1升水
三杯水的温度都变成了20

输入例子:
3
10 2
20 1
25 1
30 1

输出例子:
Possible
20.0000

分析：
两杯水混合只能无限趋近于某杯水的温度，而不能到达这个温度。
所以，如果 n 杯水中有的温度高于 T，有的温度低于 T，是不可能通过混合达到温度 T 的，返回 Impossible

将水缸里的水分别倒入水杯中和，相当于把所有水混合在一起。
所以只需要求把所有水混合后的温度 tt，
如果 tt < min(ts)，说明 T 比水杯里的水温度都低，那么所能达到的最高温度是 min(ts)
如果 tt > max(tx)，说明 T 比水杯里的水温度都高，那么所能达到的最高温度是 tt
否则，说明大缸中水量 C 不足，不能使水杯里的水达到同一温度，返回 Impossible
'''