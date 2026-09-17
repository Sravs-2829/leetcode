class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = []
        for num in arr:
            distance = abs(num - x)
            distances.append((distance, num))    
        distances.sort()
        result = []
        for i in range(k):
            closest_num = distances[i][1]
            result.append(closest_num)  
        result.sort()
        return result 