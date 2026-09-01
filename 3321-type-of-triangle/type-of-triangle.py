class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c=nums
        nums=set(nums)
        if not(a+b>c and a+c>b and b+c>a):
            return "none"
        ln=len(nums)
        if ln==2:
            return "isosceles"
        if ln==1:
            return "equilateral"
        if ln==3:
            return "scalene"