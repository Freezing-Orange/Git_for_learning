'''
设计一个接收整数流的数据结构，该数据结构支持检查是否存在两数之和等于特定值。

实现 TwoSum 类：

TwoSum() 使用空数组初始化 TwoSum 对象
void add(int number) 向数据结构添加一个数 number
boolean find(int value) 寻找数据结构中是否存在一对整数，使得两数之和与给定的值相等。如果存在，返回 true ；否则，返回 false 。
 

示例：

输入：
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
输出：
[null, null, null, null, true, false]

解释：
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4，返回 true
twoSum.find(7);  // 没有两个整数加起来等于 7 ，返回 false
 

提示：

-105 <= number <= 105
-231 <= value <= 231 - 1
最多调用 5 * 104 次 add 和 find

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iii-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data={}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.data[number]=self.data.get(number,0)+1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in self.data.keys():
            if value-i==i:
                if self.data[i]>1:
                    return True
            else:
                if value-i in self.data.keys():
                    return True
        return False


def testFunc(commandList:List,commandValue:List):
    if len(commandList)!=len(commandValue):
        print("指令数组长度不同")
        return 
    if commandList[0]!="TwoSum":
        print("未初始化对象")
        return
    obj=TwoSum()
    for i in range(1,len(commandList)):
        if commandList[i]=="add":
            obj.add(commandValue[i][0])
        else:
            print(obj.find(commandValue[i][0]))
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
obj=TwoSum()
obj.add(1)
obj.add(3)
obj.add(5)
print(obj.find(4))
print(obj.find(7))
testFunc(["TwoSum","add","add","add","find","find"],[[],[1],[3],[5],[4],[7]])