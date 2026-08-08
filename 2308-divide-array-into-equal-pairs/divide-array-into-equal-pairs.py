class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        else:
            d={}
            for i in range(len((nums))):
                d[nums[i]]=nums.count(nums[i])
            for v in d.values():
                if v%2!=0:
                    return False
            return True
            

        