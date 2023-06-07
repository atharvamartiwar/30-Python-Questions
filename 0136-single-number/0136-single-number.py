class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(0,n):
            res^=nums[i]
        return res  