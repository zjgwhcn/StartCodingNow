#! /usr/bin/env python
#! -*- coding:utf-8 -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow.


if __name__ == "__main__":
    print Solution().reverse(123)
    print Solution().reverse(-321)
