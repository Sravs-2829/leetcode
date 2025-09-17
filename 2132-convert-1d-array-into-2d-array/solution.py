class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l=len(original)
        k=0
        m1=[]
        if l!=m*n:
            return m1
        for i in range (m):
            row=[]
            for j in range(n):
                row.append(original[k])
                k+=1
            m1.append(row)
        return m1
