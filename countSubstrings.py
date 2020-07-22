# encoding: utf-8
'''
回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。

链接：https://leetcode-cn.com/problems/palindromic-substrings

解题思路：
        动态规划。从前往后遍历每个元素，每遍历到一个元素，就跟其前面的n个元素做比较
        比较时也是从前往后遍历j
        若两个元素相等，且j~i之间最大的字串dp[j+1][]i-1]==1或者i和j相等或i和j相邻，则dp[j][i]=1
'''

class Solution:
    def countSubstrings(self, s: str) -> int:

        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]  # 初始化动态规划数组
        result = 0
        for i in range(0, length):
            for j in range(0, i + 1):
                if s[i] == s[j] and (i - j <= 1 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    result += 1
        return result