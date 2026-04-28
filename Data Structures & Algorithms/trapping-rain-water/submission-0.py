class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0
        max_left = 0
        max_right = 0
        water = 0
        while l < r:
                max_left = max(max_left, height[l])
                max_right = max(max_right, height[r])
                if (height[l] >= height[r]):
                    water = max_right - height[r]
                    r-=1
                else:
                    water = max_left - height[l]
                    l+=1
                result += water
            
        return result