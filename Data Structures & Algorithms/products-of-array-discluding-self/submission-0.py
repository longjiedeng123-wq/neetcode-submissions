class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        prefix_product = []
        for num in nums:
            prefix_product.append(left_product)
            left_product *= num

        right_product = 1
        suffix_product = []
        for num in reversed(nums):
            suffix_product.append(right_product)
            right_product *= num

        suffix_product.reverse()

        final_product = []
        for i in range(len(nums)):
            final_product.append(prefix_product[i] * suffix_product[i])
        
        return final_product
