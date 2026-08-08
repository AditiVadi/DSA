class Solution:
    def countKeyChanges(self, s: str) -> int:
        si=s.lower()
        c=0
        for i in range(len(si)-1):
            if si[i]!=si[i+1]:
                c+=1
        return c
        