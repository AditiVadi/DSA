class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=nums.count(i)
        c=0
        v=0
        ans=[]
        for i,j in d.items():
            if j%2==0:
                c=c+(j//2)
            elif j%2==1:
                if j==1:
                    v=v+1
                else:
                    c=c+(j//2)
                    v=v+1
        ans.append(c)
        ans.append(v)
        return ans
        