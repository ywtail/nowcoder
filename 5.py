# -*- coding:utf-8 -*-
# 血型遗传检测

class ChkBloodType:
    def chkBlood(self, father, mother):
        if 'AB' in [father, mother]:
            ans = ['A', 'AB', 'B']
            if 'O' in [father, mother]:
                ans.remove('AB')
        elif 'A' in [father, mother] and 'B' in [father, mother]:
            ans = ['A', 'AB', 'B', 'O']
        else:
            ans = list({father, mother, 'O'})
        return ans


chkbloodtype = ChkBloodType()
print chkbloodtype.chkBlood('A', 'A')

'''
## 血型遗传检测
[题目链接](https://www.nowcoder.com/practice/5541c433dee04c17ba7774c4a20430de?tpId=49&tqId=29303&tPage=3&rp=3&ru=/ta/2016test&qru=/ta/2016test/question-ranking)

血型遗传对照表如下

| 父母血型  | 子女会出现的血型 | 子女不会出现的血型 |
| ----- | -------- | --------- |
| O与O   | O        | A,B,AB    |
| A与O   | A,O      | B,AB      |
| A与A   | A,O      | B,AB      |
| A与B   | A,B,AB,O | ——        |
| A与AB  | A,B,AB   | O         |
| B与O   | B,O      | A,AB      |
| B与B   | B,O      | A,AB      |
| B与AB  | A,B,AB   | O         |
| AB与O  | A,B      | O,AB      |
| AB与AB | A,B,AB   | O         |

请实现一个程序，输入父母血型，判断孩子可能的血型。
给定两个字符串father和mother，代表父母的血型,请返回一个字符串数组，代表孩子的可能血型(按照字典序排列)。

**测试样例**

>”A”,”A”
>返回：[”A”,“O”]

- chkBlood(self, father, mother):
总结了一下，一共就三种情况：（*注意题目中说了要按字典序排序*）
  - 含AB（AB与O是特例），则孩子可能血型是['A', 'AB', 'B']，特例（AB与O）则去掉'AB'这种可能
  - A和B，则孩子可能血型是['A','AB', 'B', 'O']
  - 普通，则孩子可能血型是{father, mother, 'O'}，这里注意去重
运行时间：30ms
占用内存：3156k
'''
