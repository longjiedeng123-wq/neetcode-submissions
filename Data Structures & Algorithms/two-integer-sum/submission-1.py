class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev_nums:
                return [prev_nums[complement], i]
            prev_nums[num] = i
        