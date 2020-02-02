# encoding: utf-8
'''
题目：给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

    你找到的子数组应是最短的，请输出它的长度。

    示例 1:

    输入: [2, 6, 4, 8, 10, 9, 15]
    输出: 5
    解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
    说明 :

    输入的数组长度范围在 [1, 10,000]。
    输入的数组可能包含重复元素 ，所以升序的意思是<=。

解题思路：数组从小到大排序
         从前往后遍历原数组，每个元素和排序后的数组上对应的索引值的数值进行比较，如果该值和排序数组的值不同，说明该元素需要被排序，记为起始点
         从后往前遍历原数组，每个元素和排序后的数组上对应的索引值的数值进行比较，如果该值和排序数组的值不同，说明该元素需要被排序，记为终点
'''


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        start = 0
        end = len(nums) - 1

        while start <= end and sort_nums[start] == nums[start]:
            start += 1

        while start <= end and sort_nums[end] == nums[end]:
            end -= 1

        return end - start + 1