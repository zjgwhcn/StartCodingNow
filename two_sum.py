#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Time:16/9/2016


# 1

class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i] + nums[j]:
                    return [i,j] 

#2
'''
num = [1,5,8,2,7]
target = 13

dict = {}
print dict
for i in xrange(len(num)):
    x = num[i]
    if target-x in dict:
        print [dict[target-x], i]
    dict[x] = i
    print dict[x]

print dict
print dict[8]
'''
class Solution(object):

    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i
