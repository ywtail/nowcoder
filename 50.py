# coding:utf-8
# 连续子数组的最大和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        cur = 0
        ans = array[0] # 初始化为array[0]，即使array全为负数，
        n = len(array)
        for i in range(n):
            cur += array[i]
            ans = max(cur, ans)
            if cur < 0:
                cur = 0
        return ans

    #运行时间：36ms
    #占用内存：5768k

solution = Solution()
print solution.FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2])
# 8

print solution.FindGreatestSumOfSubArray([-2,-8,-1,-5,-9])
# -1

'''
使用cur记录当前和，如果为负数则置为0，
使用ans记录当前最大和的值
'''