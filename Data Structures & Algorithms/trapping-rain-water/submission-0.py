class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        length = len(height)
        prefix = [0] * length
        suffix = [0] * length
        prefix[0] = height[0]
        suffix[-1] = height[-1]
        for i in range(1, length):
            prefix[i] = max(prefix[i-1], height[i])
        
        for i in range(length-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        
        for i, h in enumerate(height):
            total_area += min(prefix[i], suffix[i]) - h
        
        return total_area
         
