class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findMaxSubarray(nums, left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            left_sum = findMaxSubarray(nums, left, mid)
            right_sum = findMaxSubarray(nums, mid + 1, right)
            cross_sum = findMaxCrossSubarray(nums, left, mid, right)

            return max(left_sum, right_sum, cross_sum)

        def findMaxCrossSubarray(nums, left, mid, right):
            left_sum = float('-inf')
            curr_sum = 0

            for i in range(mid, left - 1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)

            right_sum = float('-inf')
            curr_sum = 0

            for i in range(mid + 1, right + 1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)

            return left_sum + right_sum

        if not nums:
            return 0

        return findMaxSubarray(nums, 0, len(nums) - 1)
