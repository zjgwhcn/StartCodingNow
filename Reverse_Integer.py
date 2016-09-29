#! /usr/bin/env python
#! -*- coding:utf-8 -*-

class Solution(object):
    def reverse(self,x):
        ret = 0
        flag = 1
        if x < 0:
            flag = -1
            x *= -1
        while(x!=0):
            ret = ret*10+x%10
            x = x/10
        return ret*flag
        '''
        if x < 0:
            flag = -1
        else:
            flag = 1
        t = str(abs(x))
        L = []
        for i in t:
            L.append(i)
        b = L[-1]
        for j in range(2,len(t)+1):

            a = L[-j]
            b += a
        b = int(b)

        return b*flag
'''
def main():
    a = int(input('input:'))
    s = Solution()
    a = s.reverse(a)
    print (a)

if __name__ == '__main__':
    main()

'''
fail???????????????????????
'''
