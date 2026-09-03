class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m=len(mat)
        r=sorted(range(m),key=lambda i:(mat[i],i))
        del r[k:]
        return r

        