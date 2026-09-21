class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        nums_len = len(nums)
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i - 1] == num:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + num
                if total == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                        
                elif total < 0:
                    l += 1
                else:
                    r -= 1
                    

        return res

