class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        a=set(nums)
        ni=list(a)
        n=sorted(ni)
        m=max(n)
        if len(n)<3:
            return m
        else:
            return n[-3]
        