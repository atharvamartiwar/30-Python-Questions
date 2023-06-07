import random

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled_nums = self.nums[:]
        n = len(shuffled_nums)
        for i in range(n):
            j = random.randint(i, n - 1)
            shuffled_nums[i], shuffled_nums[j] = shuffled_nums[j], shuffled_nums[i]
        return shuffled_nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()