# -*- coding:utf-8 -*-
class Solution:
    def recurs(self,n,i):
        if(i==n):
            return 0
        if(i==n-1):
            return 1
        if(i==n-2):
            return 2

        sum = 0
        j=1
        while(i+j<n):
            sum += self.recurs(n,i+j)
            j+=1
        return sum+1
    def jumpFloorII(self, number):
        # write code here
        return self.recurs(number,0)
