class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[i]-nums[j] in [k]:
                    c+=1
        return c


        