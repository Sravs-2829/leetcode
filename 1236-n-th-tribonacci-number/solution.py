class Solution:
    def tribonacci(self, n: int) -> int:
        f1=0
        f2=1
        f3=1
        i=1
        f=0
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        else:
            for i in range(0,n):
                f=f1+f2+f3
                f1=f2
                f2=f3
                f3=f
            return f1
