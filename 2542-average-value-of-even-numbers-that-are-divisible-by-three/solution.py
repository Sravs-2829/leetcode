class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count=0
        sum=0
        for num in nums:
            if (num%6==0):
                sum+=num
                count+=1
        if sum==0:
            return 0
        else:
            return sum//count
