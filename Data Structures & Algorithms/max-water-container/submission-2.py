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
            elif l_val > r_val:
                r -= 1
            else:
                while l < r and heights[l+1] == heights[r-1]:
                    l += 1
                    r -= 1
                    l_val = heights[l]
                    r_val = heights[r]
                    area = (r - l) * min(l_val, r_val)
                    largest_area = max(largest_area, area)
                if l > r:
                    break
                if heights[l+1] > heights[r-1]:
                    r -= 1
                else:
                    l += 1
        return largest_area