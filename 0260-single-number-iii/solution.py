class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        ans=[]
        for k,v in freq.items():
            if v==1:
                ans.append(k)
        return ans
