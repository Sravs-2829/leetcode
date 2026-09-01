class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        count=0
        while num>0:
            d=num%10
            if temp%d==0:
                count+=1
            num=num//10
        return count    