#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes
#
# Easy (26.45%)
# Total Accepted:    113648
# Total Submissions: 429695
# Testcase Example:  '0'
#
# Description:
# Count the number of prime numbers less than a non-negative number, n.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def __init__(self):
        self.primes = [2]

    def is_prime(self, num):
        for i in self.primes:
            if (num % i) == 0:
                return False
        self.primes.append(num)
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n <= 2:
            return count
        count += 1
        if n == 3:
            return count
        i = 3
        while i < n:
            if self.is_prime(i):
                count += 1
                i += 2
            else:
                i += 1
        return count
