# encoding: utf-8
'''
题目：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
      你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
      示例:
        给定 nums = [2, 7, 11, 15], target = 9
        因为 nums[0] + nums[1] = 2 + 7 = 9
        所以返回 [0, 1]



解题思路：从头开始遍历数组，每遍历一个数字就判断哈希表中有没有数字跟他加起来等于sum，不存在将其存进hash表，key是值，value是index
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if isinstance(nums, list) == False or isinstance(target, int) == False:
            return result

        hashmap = {}
        for index in range(0, len(nums)):
            diff = target - nums[index]
            if diff in hashmap:
                result.append(hashmap[diff])
                result.append(index)
                return result
            else:
                hashmap[nums[index]] = index
        return result