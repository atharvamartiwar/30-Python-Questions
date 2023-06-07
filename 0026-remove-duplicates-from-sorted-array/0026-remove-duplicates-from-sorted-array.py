class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k=1
        for i in range(0,n-1):
            if nums[i]!=nums[i+1]:
                nums[k]=nums[i+1]
                k+=1
            else: continue
        print(k)
        return k