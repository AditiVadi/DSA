class Solution:
    def maxPower(self, s: str) -> int:
        m=c=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                c=1
            m=max(m,c)
        return m

        