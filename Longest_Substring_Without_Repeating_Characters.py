#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self,s):

        start = 0
        sub_length = 0
        sub_string = ''

        for end in range(len(s)):
            if s[end] not in sub_string:
                sub_string += s[end]

            else:
                sub_length = max(len(sub_string),sub_length)

                while s[start] != s[end]:
                    start += 1
                start += 1
                sub_string = s[start:end + 1]

        print  max(len(sub_string),sub_length)







def main():
    stri = raw_input("Input String:")
    test = Solution()
    test.lengthOfLongestSubstring(stri)
    #print test 

if __name__ == '__main__':
    main()

