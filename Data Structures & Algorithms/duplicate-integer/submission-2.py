class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev_num = set()
        for num in nums:
            if num in prev_num:
                return True
            
            prev_num.add(num)
        
        return False