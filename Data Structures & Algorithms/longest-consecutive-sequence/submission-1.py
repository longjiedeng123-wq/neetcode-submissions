class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        vals = set()    
        for num in nums:
            vals.add(num)

        largest_seq = 1
        for val in vals:
            if val - 1 not in vals:
                is_next = True
                cur_seq = 1
                while is_next:
                    if val + 1 in vals:
                        cur_seq += 1
                        val += 1
                    else:
                        is_next = False
                        if cur_seq > largest_seq:
                            largest_seq = cur_seq

        return largest_seq