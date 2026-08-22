class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=str(n)
        a=0
        b=1
        for i in s:
            a=a+int(i)
            b=b*int(i)
        if n%(a+b)==0:
            return True
        return False

        