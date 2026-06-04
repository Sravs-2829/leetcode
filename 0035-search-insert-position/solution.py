class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        if target < nums[l]:
            return l
        while l<=r:
            mid=(l+(r-l)//2)
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                 r=mid-1
        if nums[mid]<target:
            return mid+1
        else:
            return mid
        
