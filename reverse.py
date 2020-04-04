'''

题目：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

解题思路：将整数转换为字符串，遍历字符串然后反转
'''

class Solution(object):   
  def reverse(self, x):
      """
      :type x: int
      :rtype: int
      """
      if isinstance(x, int) == False or x == 0:
          return 0

      str_num = str(x)
      index = 0
      is_minus = False

      if str_num[0] == '-':
          # 处理负数
          index = 1
          is_minus = True

      new_str = ''
      for i in list(range(len(str_num) - 1, index - 1, -1)):
          new_str += str_num[i]

      if is_minus:
          new_str = '-' + new_str

      result = int(new_str)
      if result > 2**31 -1 or result < -2**31:
          result = 0
      return result
