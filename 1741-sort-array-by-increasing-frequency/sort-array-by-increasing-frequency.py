class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=nums.count(i)
        ans=[]
        I=sorted(d.items(), key=lambda item: (item[1],-item[0]))
        for i, j in I:    
            ans.extend([i] * j)
        return ans
        