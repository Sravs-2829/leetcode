class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d=dict()
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        heap=[]
        for key,val in d.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [key for(val,key) in heap]    