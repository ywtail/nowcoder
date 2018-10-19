// 数字颠倒

#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
//    方法一：
//    string ans = to_string(n);
//    reverse(ans.begin(),ans.end());
//    cout<<ans;
//    方法二：
//    string ans = to_string(n);
//    for (auto i = int(ans.length() - 1); i >= 0; --i) {
//        cout << ans[i];
//    }
//    cout<<ans;
//    方法三：
    if (n == 0) {
        cout << n;
        return 0;
    }
    while (n) {
        cout << n % 10;
        n /= 10;
    }
}

/*
链接：https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607?tpId=37&tqId=21229&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述
描述：
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001

输入描述:
输入一个int整数

输出描述:
将这个整数以字符串的形式逆序输出

示例1
输入
1516000
输出
0006151

方法一：使用reverse函数 (nowcoder上需要#include <algorithm>)
方法二：转为string逆序打印
方法三：从整数数字个位数开始打印。容易漏考虑n=0的情况
 */