class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        res = []
        for num in nums:
            res.append(prefix_product)
            prefix_product *= num
        
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= nums[i]

        return res
