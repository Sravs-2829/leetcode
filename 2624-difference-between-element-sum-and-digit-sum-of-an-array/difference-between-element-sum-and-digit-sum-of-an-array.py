class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            s=0
            while n>0:
                digit=n%10
                s=s+digit
                n=n//10
            return s
        ele_sum=0
        d_sum=0
        for num in nums:
            ele_sum+=num
            d_sum+=digit_sum(num)
        return abs(ele_sum-d_sum)    