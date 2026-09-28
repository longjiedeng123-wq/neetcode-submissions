class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        min_len = len(nums)
        reached = False
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                reached = True
                min_len = min(min_len, r - l + 1)
                total -= nums[l]
                l += 1
        
        return min_len if reached else 0