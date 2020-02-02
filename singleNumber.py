# encoding: utf-8
'''
题目：给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
    输入: [2,2,1]
    输出: 1

示例 2:
    输入: [4,1,2,1,2]
    输出: 4
\

解题思路：解法1： 对数组进行排序，从前往后遍历数组，判断相邻的数字是否相同
         解法2： 用抑或：0^a = a; a^a = 0; a^b^a = b
'''

# 解法一
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果存在只出现一次的数字，则数组长度一定是奇数
        result = None

        if len(nums) == 0 or len(nums) % 2 == 0:
            return result

        sort_nums = sorted(nums)
        index = 0
        for index in range(0, len(nums), 2):
            if (index < len(nums) - 2 and sort_nums[index] != sort_nums[index + 1]) or index == len(nums) - 2:
                break

        result = sort_nums[index]
        return result

# 解法二
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a