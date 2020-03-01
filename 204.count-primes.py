#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (30.51%)
# Total Accepted:    311.5K
# Total Submissions: 1M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        cnt = 0
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, n):
            if is_prime[i]:
                cnt += 1
                for j in range(i * 2, n, i):
                    is_prime[j] = False
        return cnt
