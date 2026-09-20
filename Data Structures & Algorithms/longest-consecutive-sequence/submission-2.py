class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        vals = set(nums)

        largest_seq = 1
        for val in vals:
            if val - 1 not in vals:
                
                cur_seq = 1
                while val + 1 in vals:
                    cur_seq += 1
                    val += 1

                
                largest_seq = max(largest_seq, cur_seq)

        return largest_seq