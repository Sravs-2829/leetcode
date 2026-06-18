class Solution:
    def removeStars(self, s: str) -> str:
        k=[]
        for num in s:
            if num=='*':
                k.pop()
            else:
                k.append(num)
            
        return"".join(k)
