// 质数因子(华为)

#include <iostream>
#include <cmath>

long getResult1(long ulDataInput) {
    for (long i = 2; i <= int(sqrt(ulDataInput)); ++i) {
        if (ulDataInput % i == 0) {
            std::cout << i << " ";
            getResult1(ulDataInput / i);
            return 0;
        }
    }
    std::cout << ulDataInput << " ";
    return 0;
}

long getResult2(long ulDataInput) {
    while (ulDataInput != 1) {
        for (long i = 2; i <= ulDataInput; ++i) {
            if (ulDataInput % i == 0) {
                std::cout << i << " ";
                ulDataInput /= i;
                break;
            }
        }
    }
    return 0;
}

int main() {
    long ulDataInput;
    std::cin >> ulDataInput;
    //getResult1(ulDataInput);
    getResult2(ulDataInput);
    return 0;
}

/*
链接：https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607?tpId=37&tqId=21229&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
最后一个数后面也要有空格
详细描述：
函数接口说明：
public String getResult(long ulDataInput)
输入参数：
long ulDataInput：输入的正整数
返回值：
String
输入描述:
输入一个long型整数
输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
180
输出
2 2 3 3 5

题意：
输入：long型整数n
输出：这个整数的所有质因子。要求：1.从小到大排列；2.返回string类型（可以直接cout）
方法一：使用递归，遍历[2,int(sqrt(n))]
方法二：使用循环，遍历[2,n]
 */