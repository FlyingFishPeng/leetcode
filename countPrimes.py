# encoding: utf-8
'''
题目：统计所有小于非负整数 n 的质数的数量。
      示例：
        输入: 10
        输出: 4
        解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

解题思路：质数的倍数一定不是质数，。将质数x的倍数x*2,x*3...全部标记为质数，没剩下的数即为质数；
          最小的质数是2，因此从2开始标记，利用数组的对称性，遍历时只遍历到根号n处；
          标记时为防止 2*3和3*2的情况发生，只从x*x开始往后标记
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if isinstance(n, int) == False:
            return 0

        if n < 2:
            return 0

        else:
            # 思想：质数的倍数一定不是质数，最小的质数是2
            # num_list = [1 for i in range(n)] # 初始化
            num_list = [1] * n  # 此种初始化方式要比上一行更节约时间
            num_list[0] = num_list[1] = 0
            # i = 2
            # 遍历到根号n处
            # while i * i < n:
            # 用for循环比while循环更节约时间
            for i in range(2, int(n ** 0.5) + 1):
                # 如果第i个数是质数，则将i*2,i*3...全部标记为非质数
                if num_list[i]:
                    # 从j = i*i开始遍历，应对i=5时，5*2已被2*5占用的问题
                    # j = i * i
                    # while j < n:
                    # num_list[j] = 0
                    # j += i
                    num_list[i * i: n: i] = [0] * len(num_list[i * i: n: i])
                # i += 1

            return sum(num_list)




