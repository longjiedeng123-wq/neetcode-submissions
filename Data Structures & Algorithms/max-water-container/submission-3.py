class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largest_area = 0
        while l < r:
            l_val = heights[l]
            r_val = heights[r]
            area = (r - l) * min(l_val, r_val)
            largest_area = max(largest_area, area)
            if l_val < r_val:
                l += 1
            else:
                r -= 1
            
        return largest_area